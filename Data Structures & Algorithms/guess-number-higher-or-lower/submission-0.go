/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {

    l, r := 1, n
    var mid int
    
    for l <= r {
        mid = (l+r) / 2

        switch {
            case guess(mid) == -1:
                r = mid - 1
            case guess(mid) == 1:
                l = mid + 1
            default:
                return mid
        }
    }
    return mid
}
