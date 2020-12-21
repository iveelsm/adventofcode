package main

import (
	"fmt"
	"io/ioutil"
	"sort"
)

func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		panic("There was an error reading the file")
	}
	return string(data)
}

func InString(s string, c string) bool {
	for _, n := range s {
		if c == string(n) {
			return true
		}
	}
	return false
}

func removeValue(b []*TreeNode, val *TreeNode) []*TreeNode {
	index := -1
	for i, el := range b {
		if el.node == val.node {
			index = i
		}
	}

	if index == -1 {
		return b
	}

	return append(b[:index], b[index+1:]...)
}

func processWaiting(waiting []*TreeNode, available []string, result string) ([]*TreeNode, []string) {
	resultWaiting := make([]*TreeNode, 0)
	for _, el := range waiting {
		if el.IsAvailable(result) {
			available = append(available, el.node)

			for _, next := range el.enables {
				inWaiting := next.InArray(waiting)
				if !inWaiting {
					resultWaiting = append(resultWaiting, next)
				}
			}

		} else {
			resultWaiting = append(resultWaiting, el)
		}
	}
	return resultWaiting, available
}

func traverse(t Tree) string {
	result := ""
	available := make([]string, 0)
	waiting := t.heads
	resultComplete := false

	for !resultComplete {
		waiting, available = processWaiting(waiting, available, result)
		sort.Strings(available)

		if len(available) > 0 {
			next := available[0]
			if !InString(result, next) {
				result += next
			}
			available = available[1:]
		}
		resultComplete = len(waiting) == 0 && len(available) == 0
	}
	return result
}

func PartOne() {
	data := ParseFileData(readFile("data.txt"))
	tree := BuildTree(data)
	result := traverse(tree)
	fmt.Println(result)
}

func process(t Tree) int {
	result := ""
	available := make([]string, 0)
	waiting := t.heads
	workers := BuildWorkers(5)
	resultComplete := false
	count := 0

	for !resultComplete || workers.WorkInProgress() {
		results := workers.Process()
		for _, i := range results {
			if !InString(result, i) {
				result += i
			}
		}

		availableWorkers := workers.GetAvailableWorkers()
		if len(availableWorkers) != 0 {
			waiting, available = processWaiting(waiting, available, result)
			sort.Strings(available)
			for _, el := range availableWorkers {
				if len(available) > 0 {
					next := available[0]
					el.job = next
					el.working = true
					el.timeToFinish = 60 + int([]rune(next)[0]) - (int('A') - 1)
					available = available[1:]
				}
			}
		}

		resultComplete = len(waiting) == 0 && len(available) == 0
		fmt.Println(count)
		fmt.Println(result)
		count++
	}
	return count - 1
}

func PartTwo() {
	data := ParseFileData(readFile("data.txt"))
	tree := BuildTree(data)
	result := process(tree)
	fmt.Println(result)
}

func main() {
	fmt.Println("Part One is starting...")
	PartOne()

	fmt.Println("Part Two is starting...")
	PartTwo()
}
