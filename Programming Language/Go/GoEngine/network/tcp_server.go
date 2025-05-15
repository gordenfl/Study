package network

import (
	"GoEngine/aoi"
	"log"
	"net"
)

func StartTCPServer(addr string, mgr *aoi.AOIManager) {
	ln, err := net.Listen("tcp", addr)
	if err != nil {
		log.Fatal("TCP Listen error:", err)
	}
	log.Println("TCP server listening on", addr)
	for {
		conn, _ := ln.Accept()
		go handleTCP(conn, mgr)
	}
}

func handleTCP(conn net.Conn, mgr *aoi.AOIManager) {
	defer conn.Close()
	buf := make([]byte, 1024)
	for {
		n, err := conn.Read(buf)
		if err != nil {
			return
		}
		msgID, payload, _ := DecodePacket(buf[:n])
		log.Println("TCP Received:", msgID, payload)
	}
}