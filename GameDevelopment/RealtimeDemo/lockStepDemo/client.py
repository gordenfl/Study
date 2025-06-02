import pygame
import socket
import threading
import json

WIDTH, HEIGHT = 640, 480
FPS = 60

HOST = '127.0.0.1'
PORT = 12345

player_id = None
players = {}
players_lock = threading.Lock()

def recv_thread(sock):
    global player_id, players
    buffer = b''
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            buffer += data
            while b'\n' in buffer:
                line, buffer = buffer.split(b'\n', 1)
                msg = json.loads(line.decode())
                if 'player_id' in msg:
                    player_id = msg['player_id']
                if 'players' in msg:
                    with players_lock:
                        players = msg['players']
        except:
            break

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Frame Sync Demo")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    threading.Thread(target=recv_thread, args=(sock,), daemon=True).start()

    clock = pygame.time.Clock()

    while not player_id:
        pygame.time.wait(10)  # 等待服务器返回player_id

    running = True
    while running:
        dir_x, dir_y = 0, 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dir_x = -5
        elif keys[pygame.K_RIGHT]:
            dir_x = 5
        if keys[pygame.K_UP]:
            dir_y = -5
        elif keys[pygame.K_DOWN]:
            dir_y = 5

        # 发送当前帧的操作方向
        try:
            sock.sendall(json.dumps({"dir": [dir_x, dir_y]}).encode() + b'\n')
        except:
            running = False

        screen.fill((30, 30, 30))

        with players_lock:
            for pid, p in players.items():
                color = (0, 255, 0) if pid == player_id else (255, 0, 0)
                pygame.draw.rect(screen, color, pygame.Rect(p['x'], p['y'], 30, 30))

        pygame.display.flip()
        clock.tick(FPS)

    sock.close()
    pygame.quit()

if __name__ == "__main__":
    main()
