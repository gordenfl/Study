# Game Development Realtime Synchronous

## Frame Synchronous

What is Frame Sync?
All user input will be collected at the same frame, and broadcast.

Frame Sync, means you need separate the time into different pieces. Each of the piece will receive frame package from all the client and sync data to each client and. If there is some client does not send the frame package, the server logic need to wait for all the client's package then distribute to different client. make all client the same status.

There are some point need to be care:

1. Delay of the network. that's may cause user feels bad
2. You can make some way to avoid this, just n+1, n+x etc. the data you broadcasted is x period package not the the right now package.
3. That will not let user fell lag
4. you can promote your client's frame rate more higher, such as from 20 ~ 30.
5. Client will rend with the data received from server, it will keep the game status always keep the same.

Please see the code here: [Client](./RealTimeDemo/lockStepDemo/client.py) [Server](./RealTimeDemo/lockStepDemo/server.py)

for the server.py:

```python
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

```

The code in broadcast_position(conns) function, in the Loop logic will build an 

```py
with players_lock:
```

lock this logic of for loop, it will not cause the other thread create the logic, update the position anytime.

It will make these logic a frame.

during the server receive the next step of client's value, it will include into the next frame of the data send to client with the next step.

Next Steep, let's analysis the more deep of the LockStep:

## Predictive Sync 预测同步原理

1. Client get the status itself
    If Client have itself input, client can get the prediction of the result of the input. Client will rend these result in itself without server's confirmation.
    User can feel better. Because the graphic display does not have lag
2. Get status from server
    Server will send this frame data to client include client itself. After render all other client's status, the client will verify the its status with the status comes from server.
    If two of these status are the same, just skip it. if there are some different, Client need to fix the error. 
3. Client roll back or fix
    How to fix the error? while client received the status does not match with the status of itself. Two way:
    * rollback and replay the data comes from server (it will cause game lag or feels not good). it's called Blink or Stutter
    * Another better way is fix the error with smoothly. avoid the teleportation or stuttering.

## Status Synchronous 状态同步 (RPG, MMO) 

All these method can not used to make a realtime game. because all the status will be different during one time. it will let client lost the dependency of the game object status. But this kind of Sync can be used with Predicative Sync. Some data does not key value of the game such like NPC, Rewards, and user list order etc.


| Action     | State Sync         | Lockstep / Frame Sync |
| ------ | ------------------------ | -------------------------- |
| Content Sync   | send status such like position, HP etc for each Frame | send key_press, direction etc.|
| Decision Logic  | Each client make decision them selfs, Server will correct       | Every client execute the same logic |
| Network   | High (because the data is very big)               | lower（only sync the user behavior）  |
| Sync requirement | Fault Tolerance high    | Fault Tolerance Low，every client must the same data     |
| Usage   | Action、MMO                 | RTS、Fighting、MOBA、Turn_based      |

This methods can only used to the game such as RPG, MMO etc. 

Interpolation Sync 差值同步
压缩同步




