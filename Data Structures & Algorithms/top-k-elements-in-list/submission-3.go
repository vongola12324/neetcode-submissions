type PQ []int

func (p PQ) Len() int            { return len(p) }
func (p PQ) Less(i, j int) bool  { return p[i] > p[j] } // Max PQ
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x any)         { *p = append(*p, x.(int)) }
func (p *PQ) Pop() any {
    old := *p
    x := old[len(old)-1]
    *p = old[:len(old)-1]
    return x
}

func topKFrequent(nums []int, k int) []int {
    counter := make(map[int]int)
    for _, num := range nums {
        counter[num]++
    }
    reverse_counter := make(map[int][]int)
    seen := make(map[int]bool)
    pq := &PQ{}
    heap.Init(pq)
    for num, freq := range counter {
        reverse_counter[freq] = append(reverse_counter[freq], num)
        if !seen[freq] {
            heap.Push(pq, freq)
            seen[freq] = true
        }
        
    }

    var values []int
    index := 0
    for index < k {
        top := heap.Pop(pq).(int)
        for _, num := range reverse_counter[top] {
            values = append(values, num)
            index++
            if index >= k {
                break
            }
        }
    }

    return values
}
