import game_pb2
import go_notify  # 引入 Go 的通知接口模块

def on_user_move(uid, x, y):
    print(f"[PY] User {uid} moved to ({x}, {y})")
    # 创建 UserMove Protobuf 消息并发送
    user_move = game_pb2.UserMove()
    user_move.uid = uid
    user_move.x = x
    user_move.y = y

    # 调用 Go 回调，通知 AOI 广播
    go_notify.notify_aoi(user_move)