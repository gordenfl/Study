# Congestion Control (拥塞控制)

a strategy to keep network stable and high efficient running. 动态感知网络状态，合理调整发送速率，避免网络拥堵，提高传输效率。

## Background

1. Package loss
2. latency increase
3. Decreased throughput of whole network

## Policy (Core Idea)

if in the Background situation, we need some policy to avoid our network broken and keep it stable.

1. Slow Start (慢启动): start with a small window, to see whether it works, if yes, increase the window to send with Exponential(指数级)
2. Avoid Congestion : 一旦到达某个阈值, 就开始线性增长而不是指数级. 这个阈值代表的是操作系统中设定的, 就是一个警戒线.
3. Fast Retransmit: 快速重传, 三个连续的同一个包的ACK就说明可能丢包(解释一下):

* 如果收到一个ACK说明数据可能是因为延迟导致,或者包乱序了, 都是正常现象
* 如果收到两个ACK说明小概率的重复确认, 也不一定是丢包
* 连续3个相同包的ACK是经验上的一个阈值,说明对方正在等待某个数据包,但是一直没有收到, 你需要立即重传不要等到超时,这样可以大幅减少等待时间

4. 快速恢复: 就是重传后不是直接回到慢启动, 而是减少窗口并线性增长,避免性能损失太大.