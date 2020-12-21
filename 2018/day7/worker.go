package main

type Workers struct {
	workers map[int]*Worker
}

type Worker struct {
	working      bool
	job          string
	timeToFinish int
}

func (w *Workers) WorkInProgress() bool {
	result := false
	for _, v := range w.workers {
		if v.working {
			result = true
		}
	}
	return result
}

func (w *Workers) GetAvailableWorkers() []*Worker {
	result := make([]*Worker, 0)
	for _, v := range w.workers {
		if !v.working {
			result = append(result, v)
		}
	}
	return result
}

func (w *Workers) Process() []string {
	jobsFinished := make([]string, 0)
	for _, v := range w.workers {
		if v.working {
			v.timeToFinish--
		}
		if v.timeToFinish == 0 {
			v.working = false
			jobsFinished = append(jobsFinished, v.job)
		}
	}
	return jobsFinished
}

func BuildWorkers(numWorkers int) Workers {
	result := make(map[int]*Worker)
	for i := 0; i < numWorkers; i++ {
		result[i] = &Worker{
			working: false,
		}
	}
	return Workers{
		workers: result,
	}
}
