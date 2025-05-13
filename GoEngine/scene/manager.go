package scene

import (
	"log"
)

// SceneManager 场景管理器
type SceneManager struct {
	scenes map[string]*Scene
}

// NewSceneManager 创建一个新的场景管理器
func NewSceneManager() *SceneManager {
	return &SceneManager{
		scenes: make(map[string]*Scene),
	}
}

// CreateScene 创建新的场景
func (mgr *SceneManager) CreateScene(sceneID string, poolSize int) {
	scene := NewScene(sceneID, poolSize)
	mgr.scenes[sceneID] = scene
	log.Printf("Scene %s created", sceneID)
}

// AddUserMoveTask 添加用户移动任务到指定场景
func (mgr *SceneManager) AddUserMoveTask(sceneID, userID string, x, y int) {
	scene, exists := mgr.scenes[sceneID]
	if !exists {
		log.Printf("Scene %s not found", sceneID)
		return
	}
	scene.AddTask(userID, x, y)
}
