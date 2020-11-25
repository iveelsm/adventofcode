package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		fmt.Println("Error reading the file", err)
		panic("Error reading file")
	}

	return string(data)
}

func parseData(data string) []int {
	dataPoints := strings.Split(data, "\n")
	result := make([]int, len(dataPoints))
	for index, element := range dataPoints {
		formatted, _ := strconv.Atoi(element)
		result[index] = formatted
	}
	return result
}

func PartOne() {
	data := parseData(readFile("data.txt"))
	start := 0
	for i := 0; i < len(data); i++ {
		start = start + data[i]
	}
	fmt.Println(start)
}

func PartTwo() {
	data := parseData(readFile("data.txt"))
	frequencyMap := make(map[int]bool)
	start := 0
	dup := false

	for dup == false {
		frequencyMap[start] = true
		for _, el := range data {
			start = start + el
			val := frequencyMap[start]
			if val {
				fmt.Println(start)
				dup = true
				break
			}
			frequencyMap[start] = true
		}
	}
}

func main() {
	fmt.Println("Part 1 Starting...")
	PartOne()

	fmt.Println("Part 2 Starting...")
	PartTwo()
}
