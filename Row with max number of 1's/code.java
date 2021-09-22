class Solution {
    int rowWithMax1s(int arr[][], int n, int m) {
        // code here
        int row = 0;
        int a = 0;
        int b = m-1;
        int count = 0;
        while(a<n&&b>=0)
        {
            if(arr[a][b]==1)
            {
                row=a;
                b=b-1;
                count++;
            }
            else
            {
                a++;
            }
        }
        if(count>0)
            return row;
        return -1;
    }
}
