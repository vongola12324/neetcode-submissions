func hasDuplicate(nums []int) bool {
    m := make(map[int]int)
    for _, num := range nums {
        m[num]++
    }
    flag := false
    for _, value := range m {
        if value > 1 {
            flag = true
            break
        }
    }

    return flag
}
