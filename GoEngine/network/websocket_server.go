package network

import (
	"GoEngine/aoi"
	"fmt"
	"log"
	"net/http"
	"sync"

	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{}
var wsConns = make(map[*websocket.Conn]string)
var wsLock sync.Mutex

func StartWebSocketServer(addr string, mgr *aoi.AOIManager) {
	http.HandleFunc("/ws", func(w http.ResponseWriter, r *http.Request) {
		conn, err := upgrader.Upgrade(w, r, nil)
		if err != nil {
			log.Println("WS upgrade error:", err)
			return
		}
		log.Println("WebSocket connected")
		go handleWS(conn, mgr)
	})

	log.Println("WebSocket listening on", addr)
	http.ListenAndServe(addr, nil)
}

func handleWS(conn *websocket.Conn, mgr *aoi.AOIManager) {
	wsLock.Lock()
	wsConns[conn] = ""
	wsLock.Unlock()
	for {
		_, msg, err := conn.ReadMessage()
		if err != nil {
			log.Println("WS read error:", err)
			return
		}
		msgID, payload, _ := DecodePacket(msg)
		fmt.Println("WS Received:", msgID, payload)
	}
}