func topKFrequent(nums []int, k int) []int {
    counter := make(map[int]int)
    for _, num := range nums {
        counter[num]++
    }
    bucket := make([][]int, len(nums)+1)
    for num, freq := range counter {
        bucket[freq] = append(bucket[freq], num)
    }

    var values []int
    for i := len(bucket) - 1; i >= 0 && len(values) < k; i-- {
        values = append(values, bucket[i]...)
    }

    return values[:k]
}
