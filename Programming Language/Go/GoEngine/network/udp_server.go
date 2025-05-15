package network

import (
	"GoEngine/aoi"
	"fmt"
	"log"
	"net"
)

// 启动 UDP 服务器
func StartUDPServer(address string, aoiManager *aoi.AOIManager) error {
	// 解析目标地址
	udpAddress, err := net.ResolveUDPAddr("udp", address)
	if err != nil {
		return fmt.Errorf("failed to resolve UDP address: %v", err)
	}

	// 监听 UDP 地址
	conn, err := net.ListenUDP("udp", udpAddress)
	if err != nil {
		return fmt.Errorf("failed to listen on UDP address: %v", err)
	}
	defer conn.Close()

	log.Printf("UDP server listening on %s\n", address)

	// 创建缓冲区
	buffer := make([]byte, 1024)

	// 循环接收数据
	for {
		n, addr, err := conn.ReadFromUDP(buffer)
		if err != nil {
			log.Printf("Error reading from UDP: %v", err)
			continue
		}

		// 解析收到的数据包
		log.Printf("Received %d bytes from %s: %s\n", n, addr.String(), string(buffer[:n]))

		// 在这里，我们可以利用 aoiManager 做一些与 AOI 相关的操作
		// 比如判断用户是否进入/离开某个区域，更新场景中的数据等
		// 这里只是一个例子，具体根据你的业务逻辑来处理

		// 简单的广播响应回客户端
		_, err = conn.WriteToUDP([]byte("UDP message received"), addr)
		if err != nil {
			log.Printf("Error sending response: %v", err)
		}
	}
}