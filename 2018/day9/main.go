package main

import (
	"fmt"
	"strings"
	"io/ioutil"
	"strconv"
)

type Marble struct {
	previous *Marble
	next *Marble
	value int
}

type MarbleBuffer struct {
	length int
	current *Marble
}

func NewBuffer() *MarbleBuffer {
	b := &MarbleBuffer{
		length: 1,
		current: &Marble{
			previous: nil,
			next: nil,
			value: 0,
		},
	}
	return b
}

func (b* MarbleBuffer) ShiftCurrent(m int) {
	if m >= 0 {
		for i := 0; i < m; i++ {
			b.current = b.current.next
		}
	} else {
		for i := 0; i < (-1 * m); i++ {
			b.current = b.current.previous
		}
	}
}

func (b* MarbleBuffer) IncrementLength(m int) {
	b.length = b.length + m
}

func (b *MarbleBuffer) AddMarble(m int) int {
	if b.current.next == nil || b.current.previous == nil {
		next := &Marble{
			previous: b.current,
			next: b.current,
			value: m,
		}
		b.current.next = next
		b.current.previous = next
		b.ShiftCurrent(1)
		b.IncrementLength(1)
		return 0
	}

	if m % 23 != 0 {
		b.ShiftCurrent(1)

		new := &Marble{
			previous: b.current,
			next: b.current.next,
			value: m,
		}

		b.current.next.previous = new
		b.current.next = new
		b.IncrementLength(1)
		b.ShiftCurrent(1)

		return 0
	}

	
	b.ShiftCurrent(-7)

	next := b.current.next
	previous := b.current.previous
	previous.next = next
	next.previous = previous

	marble := b.current.value
	b.current = next
	b.IncrementLength(-1)

	return marble + m
}


func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		panic("There was an error reading the file")
	}
	return string(data)
}

func parseFileData(data string) []int {
	trimmed := strings.Split(strings.Trim(data, "\n"), ",")
	result := make([]int, len(trimmed))
	for i := 0; i < len(trimmed); i++ {
		val, _ := strconv.Atoi(trimmed[i])
		result[i] = val
	}
	return result
}

func PartOne() {
	data := parseFileData(readFile("inputs/puzzle.txt"))
	players := data[0]
	marbles := data[1]

	game := NewBuffer()
	scores := make(map[int]int)

	for i := 1; i < marbles + 1; i++ {
		value := game.AddMarble(i)
		if (value > 0) {
			player := i % players
			scores[player] += value
		}
	}

	maximumScore := 0
	winningPlayer := 0
	for k, v := range scores {
		if v > maximumScore {
			winningPlayer = k
			maximumScore = v
		}
	}
	fmt.Println(maximumScore)
	fmt.Println(winningPlayer)
}

func main() {
	fmt.Println("Part One is starting...")
	PartOne() //modify puzzle.txt for part 2
}