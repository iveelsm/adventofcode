package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"sort"
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

func parseData(data string) []string {
	return strings.Split(data, "\n")
}

func countCharacters(data string) (int, int) {
	two := 0
	three := 0

	s := strings.Split(data, "")
	sort.Strings(s)
	for i := 0; i < len(s); {
		el := s[i]
		current := el
		count := 1

		for el == current {
			if i+count > len(s)-1 {
				break
			}

			el = s[i+count]
			if el == current {
				count = count + 1
			}
		}

		if count == 2 {
			two = 1
		} else if count == 3 {
			three = 1
		}

		i = i + count
	}
	return two, three
}

func PartOne() {
	data := parseData(readFile("data.txt"))
	linesTwoChars := 0
	linesThreeChars := 0
	for _, el := range data {
		two, three := countCharacters(el)
		if two > 0 {
			linesTwoChars = linesTwoChars + 1
		}
		if three > 0 {
			linesThreeChars = linesThreeChars + 1
		}
	}
	fmt.Println(linesTwoChars * linesThreeChars)
}

func isWithinOne(a, b string) (bool, string) {
	countDiff := 0
	buff := bytes.NewBufferString("")
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			countDiff = countDiff + 1
		} else {
			buff.WriteByte(a[i])
		}
	}
	return countDiff == 1, buff.String()
}

func PartTwo() {
	data := parseData(readFile("data.txt"))
	for i := 0; i < len(data); i++ {
		for j := i + 1; j < len(data); j++ {
			res, matched := isWithinOne(data[i], data[j])
			if res {
				fmt.Println(matched)
			}
		}
	}
}

func main() {
	fmt.Println("Part 1 Starting...")
	PartOne()

	fmt.Println("Part 2 Starting...")
	PartTwo()
}
