package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		panic("There was an error reading the file")
	}
	return string(data)
}

func abs(r rune) rune {
	if r < 0 {
		return r * -1
	}
	return r
}

func remove(slice []rune, i int) []rune {
	return append(slice[:i], slice[i+2:]...)
}

func ReactPolymer(polymer string) int {
	split := []rune(polymer)
	for i := 0; i < len(split)-1; i++ {
		diff := abs(split[i] - split[i+1])
		if diff == 32 {
			split = remove(split, i)
			i = -1
		}
	}
	return len(split)
}

func PartOne() {
	data := readFile("inputs/puzzle.txt")
	fmt.Println(ReactPolymer(data))
}

func PartTwo() {
	alphabet := "abcdefghijklmnopqrstuvwxyz"
	data := readFile("inputs/puzzle.txt")
	minLength := math.MaxUint32
	for _, el := range alphabet {
		current := strings.ReplaceAll(data, string(el), "")
		current = strings.ReplaceAll(current, strings.ToUpper(string(el)), "")
		lengthPolymer := ReactPolymer(current)
		if lengthPolymer < minLength {
			minLength = lengthPolymer
		}
	}
	fmt.Println(minLength)
}

func main() {
	fmt.Println("Part One Starting...")
	PartOne()

	fmt.Println("Part Two Starting...")
	PartTwo()
}
