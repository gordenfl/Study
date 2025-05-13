package main

import (
	"GoEngine/aoi"
	"GoEngine/logic"
	"GoEngine/network"
	"GoEngine/python"
	"GoEngine/scene"
)

func main() {
	python.Initialize()
	defer python.Finalize()

	// 创建场景管理器
	sceneManager := scene.NewSceneManager()

	// 创建场景并设置线程池大小
	sceneManager.CreateScene("scene1", 5)

	// 初始化 AOI 管理器并注册回调
	aoiManager := aoi.NewAOIManager(100)
	python.RegisterAOICallback(aoiManager)

	// 启动网络服务
	go network.StartTCPServer(":9000", aoiManager)
	go network.StartUDPServer(":9001", aoiManager)
	go network.StartWebSocketServer(":9002", aoiManager)


	// 模拟用户移动，添加任务到场景
	sceneManager.AddUserMoveTask("scene1", "user1", 10, 20)
	sceneManager.AddUserMoveTask("scene1", "user2", 30, 40)

	// 加载 Python 模块 & 注册回调
	logic.InitPython()

	select {} // 阻塞主线程
}