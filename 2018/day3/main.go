package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

type Claim struct {
	claimId  int
	fromLeft int
	fromTop  int
	width    int
	length   int
}

type Point struct {
	x int
	y int
}

func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		fmt.Println("Error reading the file", err)
		panic("Error reading file")
	}

	return string(data)
}

func stringToInt(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return i
}

func parseData(data string, re *regexp.Regexp) []Claim {
	split := strings.Split(data, "\n")
	result := make([]Claim, len(split))

	for i, el := range split {
		obj := re.FindStringSubmatch(el)
		result[i] = Claim{
			claimId:  stringToInt(obj[2]),
			fromTop:  stringToInt(obj[3]),
			fromLeft: stringToInt(obj[4]),
			length:   stringToInt(obj[5]),
			width:    stringToInt(obj[6]),
		}
	}
	return result
}

func PartOne(re *regexp.Regexp) {
	data := parseData(readFile("inputs/puzzle.txt"), re)

	var square [1000][1000]int
	multipleClaimMap := make(map[Point]bool)
	totalCount := 0
	for _, el := range data {
		for i := el.fromLeft; i < (el.fromLeft + el.width); i++ {
			for j := el.fromTop; j < (el.fromTop + el.length); j++ {
				dataPt := Point{
					x: i,
					y: j,
				}

				square[dataPt.x][dataPt.y] = square[dataPt.x][dataPt.y] + 1
				if square[dataPt.x][dataPt.y] > 1 {
					if !multipleClaimMap[dataPt] {
						multipleClaimMap[dataPt] = true
						totalCount = totalCount + 1
					}
				}
			}
		}
	}

	fmt.Println(totalCount)
}

func PartTwo(re *regexp.Regexp) {
	data := parseData(readFile("inputs/puzzle.txt"), re)

	var square [1000][1000]int
	intactClaimMap := make(map[int]bool)
	intactClaim := 0
	for _, el := range data {
		for i := el.fromLeft; i < (el.fromLeft + el.width); i++ {
			for j := el.fromTop; j < (el.fromTop + el.length); j++ {
				dataPt := Point{
					x: i,
					y: j,
				}

				square[dataPt.x][dataPt.y] = square[dataPt.x][dataPt.y] + 1
			}
		}
	}

	for _, el := range data {
		isClaimIntact := true
		for i := el.fromLeft; i < (el.fromLeft + el.width); i++ {
			for j := el.fromTop; j < (el.fromTop + el.length); j++ {
				dataPt := Point{
					x: i,
					y: j,
				}

				if square[dataPt.x][dataPt.y] > 1 {
					isClaimIntact = false
				}
			}
		}
		if isClaimIntact {
			intactClaimMap[el.claimId] = true
			intactClaim = el.claimId
		}
	}

	fmt.Println(intactClaimMap)
	fmt.Println(intactClaim)
}

func main() {
	re := regexp.MustCompile("(^\\#([0-9]*)\\s\\@\\s([0-9]*),([0-9]*):\\s([0-9]*)x([0-9]*))")
	fmt.Println("Part 1 Starting...")
	PartOne(re)

	fmt.Println("Part 2 Starting...")
	PartTwo(re)
}
