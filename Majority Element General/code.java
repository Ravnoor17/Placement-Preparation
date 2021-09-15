import java.util.*;

public class Main {
    
    //~~~~~~~~~~~~~~~~User Section~~~~~~~~~~~~~~~~~
    public static ArrayList<Integer> majorityElement(int[] arr, int k) {
        ArrayList<Integer> ls = new ArrayList<Integer>();
        if(k<2)
            return ls;
        int[] e = new int[k-1];
        int[] c = new int[k-1];

        for (int i = 0; i < k - 1; i++)
        c[i] = 0;
    
        int n = arr.length;
        int i; int j;
        for(i=0; i<n; i++)
        {
            for(j=0;j<k-1;j++)
            {
                if(arr[i]==e[j])
                {
                c[j]++;
                break;
                }
            }
            if(j==k-1)
            {
                int l;
                for(l=0;l<k-1;l++)
                {
                    if(c[l]==0)
                    {
                        e[l]=arr[i];
                        c[l]=1;
                        break;
                    }
                }
                if(l==k-1)
                {
                    for(l=0;l<k-1;l++)
                    {
                        c[l]--;
                    }
                }
            }
        }
        for (i = 0; i < k - 1; i++)
        c[i] = 0;
        for(i=0;i<k-1;i++)
        {
            int ac = 0;
            for(j=0;j<n;j++)
            {
                if(e[i]==arr[j])
                c[i]++;
            }
            if(c[i]>(n/k))
            ls.add(e[i]);
        }
        return ls;
    }
    
    //~~~~~~~~~~~~~~~Input Management~~~~~~~~~~~~~~~
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = scn.nextInt();
        }
        int k = scn.nextInt();
        ArrayList<Integer> res = majorityElement(arr, k);
        System.out.println(res);
    }
}
