func groupAnagrams(strs []string) [][]string {
    m := make(map[[26]int][]string)
    for _, s := range strs {
        var counter [26]int
        for _, ch := range s {
            counter[ch-'a']++
        }
        m[counter] = append(m[counter], s)
    }
    values := make([][]string, 0, len(m))
    for _, v := range m {
        values = append(values, v)
    }
    return values
}
