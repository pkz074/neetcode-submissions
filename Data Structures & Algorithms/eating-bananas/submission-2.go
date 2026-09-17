func minEatingSpeed(piles []int, h int) int {
    // p+k-1 / k
    maxpiles := 0

    for _, p := range piles {

        if p > maxpiles {
            maxpiles = p
        }
    }

    l, r := 1, maxpiles
    res := r

    for l <= r {

        k := (l + r) / 2

        var totaltime int = 0

        for _, p := range piles {
            totaltime += (p + k - 1) / k
        }

        if totaltime <= h {
            res = k
            r = k - 1
        } else {
            l = k + 1
        }
    }
    return res
}
