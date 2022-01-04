package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

type Point struct {
	x int
	y int
}

func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		panic("There was an error reading the file")
	}
	return string(data)
}

func stringToInt(s string) int {
	result, err := strconv.Atoi(s)
	if err != nil {
		panic("Not a number")
	}
	return result
}

func parseData(data string) []Point {
	split := strings.Split(data, "\n")
	result := make([]Point, len(split))
	for i, el := range split {
		points := strings.Split(el, ",")
		result[i] = Point{
			x: stringToInt(strings.Trim(points[0], " ")),
			y: stringToInt(strings.Trim(points[1], " ")),
		}
	}
	return result
}

func makeGrid(data []Point) ([][]int, int, int) {
	left, top := math.MaxUint32, math.MaxUint32
	right, bottom := 0, 0
	for _, el := range data {
		if el.x > right {
			right = el.x
		}
		if el.x < left {
			left = el.x
		}
		if el.y > bottom {
			bottom = el.y
		}
		if el.y < top {
			top = el.y
		}
	}

	width := (bottom - top) + 1
	height := (right - left) + 1

	grid := make([][]int, width)
	for i := 0; i < width; i++ {
		grid[i] = make([]int, height)
	}
	return grid, left, top
}

func manhattanDistance(a Point, b Point) int {
	return int(math.Abs(float64(a.x-b.x)) + math.Abs(float64(a.y-b.y)))
}

func nearestPoint(pt Point, data []Point) int {
	var nearestPoints []int
	minimumDistance := math.MaxUint32
	for i, el := range data {
		current := manhattanDistance(pt, el)
		if current < minimumDistance {
			nearestPoints = []int{(i + 1)}
			minimumDistance = current
		} else if current == minimumDistance {
			nearestPoints = append(nearestPoints, (i + 1))
		}
	}
	if len(nearestPoints) > 1 {
		return 0
	}
	return nearestPoints[0]
}

func paintGrid(grid [][]int, data []Point) [][]int {
	for i, el := range grid {
		for j, _ := range el {
			grid[i][j] = nearestPoint(Point{j, i}, data)
		}
	}
	return grid
}

func PartOne() {
	data := parseData(readFile("inputs/puzzle.txt"))
	grid, left, top := makeGrid(data)

	for i, el := range data {
		grid[el.y-top][el.x-left] = i + 1
		data[i] = Point{
			x: el.x - left,
			y: el.y - top,
		}
	}
	grid = paintGrid(grid, data)

	enclosed := make(map[int]bool)
	areas := make(map[int][]Point)
	for i, el := range grid {
		for j, _ := range el {
			coord := grid[i][j] + 1
			if areas[coord] == nil {
				areas[coord] = make([]Point, 0)
				enclosed[coord] = true
			}

			if i == 0 || i == len(grid)-1 || j == 0 || j == len(el)-1 {
				enclosed[coord] = false
			}

			areas[coord] = append(areas[coord], Point{j, i})
		}
	}

	maxArea := 0
	for key, value := range enclosed {
		if value {
			current := len(areas[key])
			if current > maxArea {
				maxArea = current
			}
		}
	}
	fmt.Println(maxArea)
}

func paintGridTwo(grid [][]int, data []Point, tolerance int) [][]int {
	for i, el := range grid {
		for j, _ := range el {
			sum := 0
			for _, el := range data {
				sum = sum + manhattanDistance(Point{j, i}, el)
			}
			if sum < tolerance {
				grid[i][j] = -1
			}
		}
	}
	return grid
}

func PartTwo() {
	data := parseData(readFile("inputs/puzzle.txt"))
	tolerance := 10_000
	grid, left, top := makeGrid(data)

	for i, el := range data {
		grid[el.y-top][el.x-left] = i + 1
		data[i] = Point{
			x: el.x - left,
			y: el.y - top,
		}
	}

	grid = paintGridTwo(grid, data, tolerance)
	paintedRegions := 0
	for i, el := range grid {
		for j, _ := range el {
			if grid[i][j] == -1 {
				paintedRegions++
			}
		}
	}
	fmt.Println(paintedRegions)

}

func main() {
	fmt.Println("Part One Starting...")
	PartOne()

	fmt.Println("Part Two Starting...")
	PartTwo()
}
