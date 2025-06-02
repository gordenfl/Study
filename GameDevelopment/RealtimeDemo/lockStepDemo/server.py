import socket
import threading
import json
import time

FRAME_INTERVAL = 0.017 # 60 FPS
PORT = 12345
HOST = '0.0.0.0'

# 玩家状态 {player_id: {"x": int, "y": int, "dir": [dx, dy]}}
players = {}
players_lock = threading.Lock()

def handle_client(conn, addr, player_id):
    global players
    try:
        conn.sendall(json.dumps({"player_id": player_id}).encode() + b'\n')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            for line in data.split(b'\n'):
                if not line:
                    continue
                try:
                    msg = json.loads(line.decode())
                    with players_lock:
                        if player_id in players:
                            # 更新玩家方向
                            players[player_id]['dir'] = msg.get('dir', [0,0])
                except:
                    continue
    except:
        pass
    finally:
        with players_lock:
            if player_id in players:
                del players[player_id]
        conn.close()

def broadcast_positions(conns):
    global players
    while True:
        time.sleep(FRAME_INTERVAL)
        with players_lock:
            # 更新所有玩家位置
            for p in players.values():
                dx, dy = p.get('dir', [0,0])
                p['x'] += dx
                p['y'] += dy
                # 限制边界
                p['x'] = max(0, min(600, p['x']))
                p['y'] = max(0, min(400, p['y']))
            pos_data = json.dumps({"players": players}).encode() + b'\n'
        # 广播给所有客户端
        for c in conns[:]:
            try:
                c.sendall(pos_data)
            except:
                conns.remove(c)

def main():
    global players
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Server listening on", PORT)

    connections = []
    player_id_counter = 1

    threading.Thread(target=broadcast_positions, args=(connections,), daemon=True).start()

    while True:
        conn, addr = server.accept()
        print(f"New connection from {addr}")
        player_id = str(player_id_counter)
        player_id_counter += 1

        with players_lock:
            players[player_id] = {"x": 300, "y": 200, "dir": [0,0]}

        connections.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr, player_id), daemon=True).start()

if __name__ == "__main__":
    main()
