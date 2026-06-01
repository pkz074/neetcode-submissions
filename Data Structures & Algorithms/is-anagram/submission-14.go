func isAnagram(s string, t string) bool {


    if len(s) != len(t) {
        return false
    }

    charMap := make(map[rune]int)
    charMap2 := make(map[rune]int)
    

    for _, chr := range s {

        charMap[chr]++
    }

    for _, chr := range t {
        charMap2[chr]++
    }

    for k, v := range charMap {
        if charMap2[k] != v {
            return false
        }
    }
    return true
}
