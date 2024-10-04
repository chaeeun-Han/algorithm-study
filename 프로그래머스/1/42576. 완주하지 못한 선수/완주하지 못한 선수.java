import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hash = new HashMap<>();
        
        for (int i=0; i<completion.length; i++) {
            hash.put(completion[i], hash.get(completion[i]) != null?hash.get(completion[i])+1:1);
        }
        
        for (int j=0; j<participant.length; j++) {
            Integer cnt = hash.get(participant[j]);
            
            if (cnt == null || cnt == 0) 
                return participant[j];
            
            hash.put(participant[j], cnt - 1);
        }
        return answer;
    }
}