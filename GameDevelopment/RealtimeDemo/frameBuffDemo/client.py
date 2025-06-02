import pygame
import socket
import threading
import pickle
import time

# Pygame 初始化
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# 角色状态
player_pos = [300, 200]
other_players = {}

# 网络部分
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 12345)

# 帧缓冲设置（提前预测3帧）
FRAME_BUFFER_SIZE = 3
frame_buffer = []  # 缓存未来3帧的输入

current_frame = 0

# 发送线程
def send_loop():
    global frame_buffer, current_frame
    while True:
        if len(frame_buffer) < FRAME_BUFFER_SIZE:
            # 预测未来帧的输入（这里我们简单用当前输入预测）
            keys = pygame.key.get_pressed()
            input_data = {
                'frame': current_frame + len(frame_buffer) + 1,
                'input': {
                    'up': keys[pygame.K_UP],
                    'down': keys[pygame.K_DOWN],
                    'left': keys[pygame.K_LEFT],
                    'right': keys[pygame.K_RIGHT]
                }
            }
            frame_buffer.append(input_data)

        # 每帧发一个包
        if frame_buffer:
            package = frame_buffer.pop(0)
            client_socket.sendto(pickle.dumps(package), server_addr)

        time.sleep(1 / 30)  # 30 FPS

# 接收线程
def recv_loop():
    global other_players, current_frame
    while True:
        data, _ = client_socket.recvfrom(4096)
        package = pickle.loads(data)
        # 更新世界状态
        current_frame = package['frame']
        player_pos[:] = package['players'].get('self', player_pos)
        other_players = package['players']
        other_players.pop('self', None)

# 启动线程
threading.Thread(target=send_loop, daemon=True).start()
threading.Thread(target=recv_loop, daemon=True).start()

# 游戏主循环
running = True
while running:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), player_pos, 15)
    for pos in other_players.values():
        pygame.draw.circle(screen, (255, 0, 0), pos, 15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
