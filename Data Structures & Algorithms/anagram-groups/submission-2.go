func groupAnagrams(strs []string) [][]string {
    m := make(map[string][]string)
    for _, s := range strs {
        counter := make([]int, 26)
        for _, ch := range s {
            counter[int(ch - 'a')]++
        }
        var sb strings.Builder
        for ch, v := range counter {
            if v > 0 {
                fmt.Fprintf(&sb, "%d%c", v, 'a'+ch)
            }
        }
        key := sb.String()
        m[key] = append(m[key], s)
    }
    values := make([][]string, len(m))
    index := 0
    for _, v := range m {
        values[index] = v
        index += 1
    }
    return values
}
