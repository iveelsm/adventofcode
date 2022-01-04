package main

import (
	"fmt"
	"strings"
	"io/ioutil"
	"strconv"
)

type TreeNode struct {
	id    int
	children []*TreeNode
	metadata []int
}

func (t *TreeNode) addChild(child *TreeNode) {
	t.children = append(t.children, child)
}

func (t *TreeNode) addMetadata(val int) {
	t.metadata = append(t.metadata, val)
}

type Tree struct {
	head *TreeNode
}

func NewTree() *Tree {
	tree := Tree{
		head: &TreeNode{
			id: 0,
			children: make([]*TreeNode, 0),
			metadata: make([]int, 0),
		},
	}
	return &tree
}


func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		panic("There was an error reading the file")
	}
	return string(data)
}

func parseFileData(data string) []int {
	trimmed := strings.Split(strings.Trim(data, "\n"), " ")
	result := make([]int, len(trimmed))
	for i := 0; i < len(trimmed); i++ {
		val, _ := strconv.Atoi(trimmed[i])
		result[i] = val
	}
	return result
}

func processData(data []int) *Tree {
	tree := NewTree()
	addNode(0, data, tree.head)
	return tree
}

func addNode(index int, data []int, node *TreeNode) int {
	children := data[index]
	metadata := data[index + 1]
	index = index + 2

	for i := 0; i < children; i++ {
		child := &TreeNode{
			id: node.id + (i + 1),
			children: make([]*TreeNode, 0),
			metadata: make([]int, 0),
		}
		node.addChild(child)
		index = addNode(index, data, child)
	}

	for j := 0; j < metadata; j++ {
		meta := data[index]
		node.addMetadata(meta)
		index = index + 1
	}

	return index
}

func parseTree(tree *Tree) int {
	sum := 0
	return processNode(sum, tree.head)
}


func processNode(sum int, node *TreeNode) int {
	for i := 0; i < len(node.metadata); i++ {
		sum = sum + node.metadata[i]
	}

	for j := 0; j < len(node.children); j++ {
		sum = processNode(sum, node.children[j])
	}
	return sum
}

func parseTreeTwo(tree *Tree) int {
	sum := 0
	return processNodeTwo(sum, tree.head)
}

func processNodeTwo(sum int, node *TreeNode) int {
	if (len(node.children) == 0) {
		for i := 0; i < len(node.metadata); i++ {
			sum = sum + node.metadata[i]
		}
		return sum
	} else {
		for j := 0; j < len(node.metadata); j++ {
			if (node.metadata[j] <= len(node.children)) {
				sum = processNodeTwo(sum, node.children[node.metadata[j] - 1])
			}
		}
		return sum
	}
}


func PartOne() {
	data := parseFileData(readFile("inputs/puzzle.txt"))
	tree := processData(data)
	result := parseTree(tree)
	fmt.Println(result)
}


func PartTwo() {
	data := parseFileData(readFile("inputs/puzzle.txt"))
	tree := processData(data)
	result := parseTreeTwo(tree)
	fmt.Println(result)
}


func main() {
	fmt.Println("Part One is starting...")
	PartOne()

	fmt.Println("Part Two is starting...")
	PartTwo()
}
