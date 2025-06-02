import socket
import threading
import pickle

# 存储所有玩家位置
players = {}

# UDP Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 9999))

def handle():
    while True:
        data, addr = server_socket.recvfrom(1024)
        try:
            input_data = pickle.loads(data)
            player_id = input_data['id']
            move = input_data['move']

            # 更新玩家位置
            if player_id not in players:
                players[player_id] = [100, 100]  # 初始位置

            players[player_id][0] += move[0]
            players[player_id][1] += move[1]

            # 广播所有玩家位置
            sync_data = pickle.dumps(players)
            server_socket.sendto(sync_data, addr)
        except:
            continue

threading.Thread(target=handle).start()
print("Server started")
