public class Solution {
    public static int findMaxValue(int mat[][], int n) {
        // Write your code here.
        int maxValue = Integer.MIN_VALUE;
        int maxArr[][] = new int[n][n];
        maxArr[n-1][n-1] = mat[n-1][n-1];
        int maxv = mat[n-1][n-1];
        for(int i=n-2;i>=0;i--)
        {
            if(mat[n-1][i]>maxv)
                maxv=mat[n-1][i];
            maxArr[n-1][i]=maxv;
        }
        maxv = mat[n-1][n-1];
        for(int i=n-2;i>=0;i--)
        {
            if(mat[i][n-1]>maxv)
                maxv=mat[i][n-1];
            maxArr[i][n-1]=maxv;
        }
        for(int i=n-2;i>=0;i--)
        {
            for(int j=n-2;j>=0;j--)
            {
                maxValue = Math.max(maxValue,maxArr[i+1][j+1]-mat[i][j]);
                maxArr[i][j] = Math.max(mat[i][j],Math.max(maxArr[i+1][j],maxArr[i][j+1]));
			      }
        }
         return maxValue;             
        
    }
}
