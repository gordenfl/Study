package aoi

import (
	"fmt"
	"sync"
)

type Position struct {
	X, Y int
}

type AOIManager struct {
	GridSize int
	Grids    map[string]map[string]Position
	Lock     sync.RWMutex
}

func NewAOIManager(gridSize int) *AOIManager {
	return &AOIManager{
		GridSize: gridSize,
		Grids:    make(map[string]map[string]Position),
	}
}

func (a *AOIManager) gridKey(x, y int) string {
	return fmt.Sprintf("%d_%d", x/a.GridSize, y/a.GridSize)
}

func (a *AOIManager) UpdatePosition(uid string, pos Position) []string {
	a.Lock.Lock()
	defer a.Lock.Unlock()

	key := a.gridKey(pos.X, pos.Y)
	if _, ok := a.Grids[key]; !ok {
		a.Grids[key] = make(map[string]Position)
	}
	a.Grids[key][uid] = pos

	neighbors := []string{}
	cx := pos.X / a.GridSize
	cy := pos.Y / a.GridSize
	for dx := -1; dx <= 1; dx++ {
		for dy := -1; dy <= 1; dy++ {
			k := fmt.Sprintf("%d_%d", cx+dx, cy+dy)
			if users, ok := a.Grids[k]; ok {
				for id := range users {
					if id != uid {
						neighbors = append(neighbors, id)
					}
				}
			}
		}
	}
	return neighbors
}
