package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"time"
)

type GuardLog struct {
	guardId       int
	year          int
	month         int
	day           int
	minutesAsleep []int
}

type FrequencyCounter struct {
	minute    int
	frequency int
}

type GuardLogSort []string

func (s GuardLogSort) Len() int {
	return len(s)
}

func (s GuardLogSort) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func convertStringToDate(a string) time.Time {
	return time.Date(stringToInt(a[1:5]), time.Month(stringToInt(a[6:8])), stringToInt(a[9:11]), stringToInt(a[12:14]), stringToInt(a[15:17]), 0, 0, time.UTC)
}

func (s GuardLogSort) Less(i, j int) bool {
	a, b := s[i], s[j]
	aDate := convertStringToDate(a)
	bDate := convertStringToDate(b)
	return aDate.Before(bDate)
}

func readFile(f string) string {
	data, err := ioutil.ReadFile(f)
	if err != nil {
		panic("There was an error reading the file")
	}
	return string(data)
}

func extractGuardId(data string) (int, error) {
	result := ""
	for i := strings.Index(data, "#") + 1; i < len(data); i++ {
		num, err := strconv.Atoi(string(data[i]))
		for err == nil {
			result += fmt.Sprint(num)
			i++
			num, err = strconv.Atoi(string(data[i]))
		}
	}
	return strconv.Atoi(result)
}

func stringToInt(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return i
}

func parseData(data string, re *regexp.Regexp) []GuardLog {
	var result []GuardLog

	var split GuardLogSort = strings.Split(data, "\n")
	sort.Sort(split)

	for i := 0; i < len(split); i++ {
		regexResult := re.FindStringSubmatch(split[i])
		guardId, _ := extractGuardId(regexResult[7])

		log := GuardLog{
			guardId: guardId,
			year:    stringToInt(regexResult[2]),
			month:   stringToInt(regexResult[3]),
			day:     stringToInt(regexResult[4]),
		}

		var j int
		for j = i + 1; j < len(split); j = j + 2 {
			innerRegexResult := re.FindStringSubmatch(split[j])
			if _, err := extractGuardId(innerRegexResult[7]); err == nil {
				break
			}

			lower, upper := convertStringToDate(split[j]).Minute(), convertStringToDate(split[j+1]).Minute()
			for j := lower; j < upper; j++ {
				log.minutesAsleep = append(log.minutesAsleep, j)
			}
		}
		i = j - 1
		result = append(result, log)
	}
	return result
}

func PartOne(re *regexp.Regexp) {
	data := parseData(readFile("data.txt"), re)
	guardMinutesAsleepTotal := make(map[int]int)
	sleepiestGuard, minutesAsleep := 0, 0
	for _, el := range data {
		guardMinutesAsleepTotal[el.guardId] = guardMinutesAsleepTotal[el.guardId] + len(el.minutesAsleep)
		if guardMinutesAsleepTotal[el.guardId] > minutesAsleep {
			sleepiestGuard = el.guardId
			minutesAsleep = guardMinutesAsleepTotal[el.guardId]
		}
	}

	sleepiestGuardMinuteCounts := make(map[int]int)
	highestFrequency, highestMinute := 0, 0
	for _, el := range data {
		if el.guardId != sleepiestGuard {
			continue
		}

		for _, minute := range el.minutesAsleep {
			sleepiestGuardMinuteCounts[minute] = sleepiestGuardMinuteCounts[minute] + 1
			if sleepiestGuardMinuteCounts[minute] > highestFrequency {
				highestMinute = minute
				highestFrequency = sleepiestGuardMinuteCounts[minute]
			}
		}
	}
	fmt.Println(sleepiestGuard * highestMinute)
}

func PartTwo(re *regexp.Regexp) {
	data := parseData(readFile("data.txt"), re)
	guardMinuteAsleepFrequency := make(map[int]map[int]int)
	highestFrequency, highestFrequencyMinute, highestFrequencyGuardId := 0, 0, 0
	for _, el := range data {
		for _, minute := range el.minutesAsleep {
			if guardMinuteAsleepFrequency[el.guardId] == nil {
				guardMinuteAsleepFrequency[el.guardId] = make(map[int]int)
			}
			current := guardMinuteAsleepFrequency[el.guardId]
			current[minute] = current[minute] + 1
			if current[minute] > highestFrequency {
				highestFrequency = current[minute]
				highestFrequencyMinute = minute
				highestFrequencyGuardId = el.guardId
			}
			guardMinuteAsleepFrequency[el.guardId] = current
		}
	}
	fmt.Println(highestFrequencyMinute * highestFrequencyGuardId)
}

func main() {
	re := regexp.MustCompile("(^\\[([0-9]{4})-([0-9]{2})-([0-9]{2})\\s([0-9]{2}):([0-9]{2})\\]\\s([a-zA-Z0-9\\#\\s]*))")
	fmt.Println("Part One starting...")
	PartOne(re)

	fmt.Println("Part Two starting...")
	PartTwo(re)
}
