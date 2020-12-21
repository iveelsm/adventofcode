package main

import "strings"

type Instruction struct {
	node     string
	nextNode string
}

func ParseFileData(data string) []Instruction {
	result := []Instruction{}
	lines := strings.Split(data, "\n")
	for _, line := range lines {
		lineSep := strings.Split(line, " ")
		result = append(result, Instruction{
			node:     lineSep[1],
			nextNode: lineSep[7],
		})
	}
	return result
}
