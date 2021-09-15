class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int count1 = 0,count2 = 0;
        int n = nums.length;
        int first = Integer.MIN_VALUE;
        int second = Integer.MAX_VALUE;
        for(int i=0;i<n;i++)
        {
            if(nums[i]==first)
                count1++;
            else if(nums[i]==second)
                count2++;
            else if(count1==0)
            {
                first = nums[i];
                count1++;
            }
            else if(count2==0)
            {
                second = nums[i];
                count2++;
            }
            else
            {
                count1--;
                count2--;
            }
        }
        count1=0;
        count2=0;
        for(int i=0;i<n;i++)
        {
            if(nums[i]==first)
                count1++;
            else if(nums[i]==second)
                count2++;
        }
        List<Integer> l1 = new ArrayList<Integer>();
        if(count1>(n/3) && count2>(n/3))
        {
            l1.add(first);
            l1.add(second);
        }
        else if(count1>n/3)
        {
            l1.add(first);
        }
        else if(count2>n/3)
        {
            l1.add(second);      
        }
        return l1;
            
    }
}
