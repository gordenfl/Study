import pygame
import socket
import threading
import pickle

# 初始化
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# 网络
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 9999)
player_id = str(input("Enter player ID: "))
position = [100.0, 100.0]   # 本地预测位置
server_position = [100.0, 100.0]  # 服务器同步回来的权威位置
all_players = {}

def receive():
    global all_players, server_position
    while True:
        try:
            data, _ = client_socket.recvfrom(1024)
            players = pickle.loads(data)
            all_players = players
            if player_id in players:
                server_position = players[player_id]
        except:
            continue

threading.Thread(target=receive, daemon=True).start()

while True:
    move = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move[0] -= 5
    if keys[pygame.K_RIGHT]:
        move[0] += 5
    if keys[pygame.K_UP]:
        move[1] -= 5
    if keys[pygame.K_DOWN]:
        move[1] += 5

    # 发送输入到服务器
    input_data = {'id': player_id, 'move': move}
    client_socket.sendto(pickle.dumps(input_data), server_address)

    # 预测本地移动
    position[0] += move[0]
    position[1] += move[1]

    # 平滑插值：让本地预测位置平滑向服务器权威位置靠近
    smoothing_factor = 0.5 # 平滑系数，值越小平滑越慢
    position[0] += (server_position[0] - position[0]) * smoothing_factor
    position[1] += (server_position[1] - position[1]) * smoothing_factor

    # 绘制
    screen.fill((0, 0, 0))
    for pid, pos in all_players.items():
        if pid == player_id:
            draw_pos = (int(position[0]), int(position[1]))
            color = (255, 0, 0)
        else:
            draw_pos = (int(pos[0]), int(pos[1]))
            color = (0, 255, 0)
        pygame.draw.circle(screen, color, draw_pos, 20)
    pygame.display.flip()
    clock.tick(30)
