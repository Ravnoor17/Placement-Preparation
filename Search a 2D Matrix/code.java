class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = 0;
        int column = matrix[0].length-1;
        boolean mat = false;
        /*if(target<matrix[0][0])
            return false;
        if(target>matrix[matrix.length-1][column])
            return false;
        */
        while(row<matrix.length && column>= 0)
        {
            if(matrix[row][column]==target)
            {
                return true;
            }
            else if(matrix[row][column]>target)
            {
                column--;
            }
            else
            {
                row++;
            }
        }
        return false;
        
    }
}
