class Solution {
    int median(int matrix[][], int r, int c) {
        int min = matrix[0][0];
        int max = matrix[0][c-1];
        for(int i=0;i<r;i++)
        {
            if(matrix[i][0]<min)
                min = matrix[i][0];
            if(matrix[i][c-1]>max)
                max = matrix[i][c-1];
        }
        while(min <= max) {
            int mid = (min + max) >> 1; 
            int cnt = 0;
            for(int i = 0;i<r;i++) {
                cnt += countSmallerThanMid(matrix[i], mid); 
            }
    
            if(cnt <= (r * c) / 2) min = mid + 1; 
            else max = mid - 1; 
        }
        return min; 
        
    }
    private int countSmallerThanMid(int[] matrix, int mid) {
        int l = 0, h = matrix.length - 1; 
        while(l <= h) {
            int md = (l + h) >> 1; 
            if(matrix[md] <= mid) {
                l = md + 1;
            }
            else {
                h = md - 1;
            }
        }
        return l; 
    }
}
