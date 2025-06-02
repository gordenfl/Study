import socket
import threading
import pickle
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))
print("服务器已启动，监听端口 12345")

# 玩家输入缓存：frame_number -> {addr: input}
inputs_per_frame = {}
players_pos = {}
FRAME_DURATION = 1 / 30  # 30 FPS
current_frame = 0

def handle_inputs():
    global current_frame
    while True:
        data, addr = server_socket.recvfrom(4096)
        package = pickle.loads(data)
        frame_number = package['frame']
        input_data = package['input']
        
        # 保存输入
        if frame_number not in inputs_per_frame:
            inputs_per_frame[frame_number] = {}
        inputs_per_frame[frame_number][addr] = input_data

        # 初始化玩家位置
        if addr not in players_pos:
            players_pos[addr] = [300, 200]

def update_and_broadcast():
    global current_frame
    while True:
        time.sleep(FRAME_DURATION)
        frame_inputs = inputs_per_frame.pop(current_frame, {})

        # 处理每个玩家输入
        for addr, input_data in frame_inputs.items():
            pos = players_pos.get(addr, [300, 200])
            if input_data['up']:
                pos[1] -= 5
            if input_data['down']:
                pos[1] += 5
            if input_data['left']:
                pos[0] -= 5
            if input_data['right']:
                pos[0] += 5
            players_pos[addr] = pos

        # 准备广播数据
        for addr in players_pos.keys():
            package = {
                'frame': current_frame,
                'players': { 
                    'self': players_pos[addr],
                    **{f'player_{i}': pos for i, (other_addr, pos) in enumerate(players_pos.items()) if other_addr != addr}
                }
            }
            server_socket.sendto(pickle.dumps(package), addr)

        print(f"帧 {current_frame} 广播完成")
        current_frame += 1

# 启动线程
threading.Thread(target=handle_inputs, daemon=True).start()
threading.Thread(target=update_and_broadcast, daemon=True).start()

# 主线程保持运行
while True:
    time.sleep(1)
