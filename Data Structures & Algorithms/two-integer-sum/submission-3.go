func twoSum(nums []int, target int) []int {
    m := make(map[int]int) // value -> index
    for i, v := range nums {
        complement := target - v
        if j, ok := m[complement]; ok {
            return []int{j, i}
        }
        m[v] = i
    }
    return nil
}