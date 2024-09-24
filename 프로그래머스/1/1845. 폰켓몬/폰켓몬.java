import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        
        for (int i=0;i<n;i++) {
            hash.put(nums[i], 0);
        }
    
        
        if (hash.size() >= n/2) {
            answer = n/2;
        }
        else {
            answer = hash.size();
        }
        
        return answer;
    }
}