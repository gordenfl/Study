import time
import threading
from queue import Queue

# 模拟服务器
class Server:
    def __init__(self):
        self.frame = 0
        self.inputs = {}  # {player_id: input}
        self.client_queues = {}  # player_id: queue

    def register_client(self, player_id, queue):
        self.client_queues[player_id] = queue

    def receive_input(self, player_id, input_data):
        self.inputs[player_id] = input_data

    def broadcast_frame(self):
        # 打包输入，广播给所有客户端
        frame_data = {pid: self.inputs.get(pid, "NO_INPUT") for pid in self.client_queues}
        for q in self.client_queues.values():
            q.put((self.frame, frame_data))
        print(f"Server: Frame {self.frame}, Data: {frame_data}")
        self.inputs.clear()
        self.frame += 1

# 模拟客户端
class Client(threading.Thread):
    def __init__(self, player_id, server):
        super().__init__()
        self.player_id = player_id
        self.server = server
        self.queue = Queue()
        self.position = [0, 0]  # x, y
        self.running = True
        self.server.register_client(player_id, self.queue)

    def send_input(self, input_data):
        self.server.receive_input(self.player_id, input_data)

    def apply_input(self, input_data):
        if input_data == "UP":
            self.position[1] += 1
        elif input_data == "DOWN":
            self.position[1] -= 1
        elif input_data == "LEFT":
            self.position[0] -= 1
        elif input_data == "RIGHT":
            self.position[0] += 1

    def run(self):
        while self.running:
            # 模拟输入
            input_data = "RIGHT"  # 假设玩家一直按右键
            self.send_input(input_data)

            # 接收服务器广播
            try:
                frame, frame_data = self.queue.get(timeout=0.1)
                my_input = frame_data[self.player_id]
                print(f"Client {self.player_id} Frame {frame}: Input: {my_input}")
                self.apply_input(my_input)
                print(f"Client {self.player_id} Position: {self.position}")
            except:
                pass

            time.sleep(0.1)  # 每100ms处理一帧

    def stop(self):
        self.running = False

# 创建服务器和客户端
server = Server()
client1 = Client("PlayerA", server)
client2 = Client("PlayerB", server)

client1.start()
client2.start()

# 主循环：服务器广播帧
try:
    while True:
        time.sleep(0.1)  # 100ms一帧
        server.broadcast_frame()
except KeyboardInterrupt:
    client1.stop()
    client2.stop()
    client1.join()
    client2.join()
    print("Simulation stopped.")
