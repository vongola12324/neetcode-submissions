func isAnagram(s string, t string) bool {
    m := make(map[rune]int)
    for _, ch := range s {
        m[ch]++
    }
    for _, ch := range t {
        m[ch]--
    }
    for _, value := range m {
        if value != 0 {
            return false
        }
    }
    return true
}
