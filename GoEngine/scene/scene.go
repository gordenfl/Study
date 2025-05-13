package scene

import (
	"GoEngine/utils"
	"log"
)

// Scene 场景结构
type Scene struct {
	ID        string
	WorkerPool *utils.WorkerPool
}

// NewScene 创建一个新的场景
func NewScene(id string, poolSize int) *Scene {
	return &Scene{
		ID:        id,
		WorkerPool: utils.NewWorkerPool(poolSize),
	}
}

// SceneTask 场景任务接口
type SceneTask struct {
	UserID string
	X, Y   int
}

// Execute 执行场景任务
func (task *SceneTask) Execute() {
	log.Printf("User %s moved to (%d, %d) in scene\n", task.UserID, task.X, task.Y)
	// 这里可以放置场景更新、AOI 检查等逻辑
}

// AddTask 添加任务到场景任务队列
func (s *Scene) AddTask(userID string, x, y int) {
	task := &SceneTask{
		UserID: userID,
		X:      x,
		Y:      y,
	}
	s.WorkerPool.Submit(task)
}
