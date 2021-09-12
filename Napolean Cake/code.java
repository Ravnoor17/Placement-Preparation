import java.util.*;
public class Main
{
    public static void main (String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int[] arr;
        int count = 0;
        int flag;
        for(int i = 1;i<=t;i++)
        {
            count = 0;
            int n = sc.nextInt();
            arr = new int[n];
            for(int j=0;j<n;j++)
                arr[j] = sc.nextInt();
            for(int j=0;j<n;j++)
            {
                count = 0;
                if(arr[j]!=0)
                {
                    flag=j;
                    while(count<=arr[j])
                    {
                        arr[flag--]=1;
                        count++;
                    }
                }
            }
            for(int j=0;j<n;j++)
                System.out.print(arr[j]+" ");
            System.out.println();
        }
        
        
    }
}
