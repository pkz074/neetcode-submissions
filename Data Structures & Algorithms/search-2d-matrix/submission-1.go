func searchMatrix(matrix [][]int, target int) bool {


    rows, cols := len(matrix), len(matrix[0])
    l, r := 0, rows * cols - 1

    var mid int 

    for l <= r {

        mid = l + (r - l) / 2
        row := mid / cols
        col := mid % cols

        if target > matrix[row][col] {
            l = mid+1
        } else if target < matrix[row][col] {
            r = mid - 1
        } else {
            return true
        }
    }
    return false
}
