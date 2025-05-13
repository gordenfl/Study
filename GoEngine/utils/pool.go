package utils

import (
	"fmt"
	"sync"
)

// Task 任务接口
type Task interface {
	Execute()
}

// WorkerPool 线程池管理
type WorkerPool struct {
	tasks chan Task
	wg    sync.WaitGroup
}

// NewWorkerPool 创建一个新的线程池
func NewWorkerPool(poolSize int) *WorkerPool {
	pool := &WorkerPool{
		tasks: make(chan Task),
	}

	// 启动多个工作线程
	for i := 0; i < poolSize; i++ {
		go pool.worker(i)
	}
	return pool
}

// worker 处理任务的工作线程
func (wp *WorkerPool) worker(id int) {
	for task := range wp.tasks {
		fmt.Printf("Worker %d is processing task\n", id)
		task.Execute()
	}
}

// Submit 提交任务到线程池
func (wp *WorkerPool) Submit(task Task) {
	wp.wg.Add(1)
	wp.tasks <- task
}

// Wait 等待所有任务完成
func (wp *WorkerPool) Wait() {
	wp.wg.Wait()
}
