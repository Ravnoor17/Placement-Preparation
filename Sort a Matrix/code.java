class Solution 
{
    int[][] sortedMatrix(int N, int Mat[][]) 
    {
        // code here
        int c=0;
        int[] M = new int[N*N];
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
                M[c++]=Mat[i][j];
        }
        Arrays.sort(M);
        c=0;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
                Mat[i][j]=M[c++];
        }
        return Mat;
    }
};
