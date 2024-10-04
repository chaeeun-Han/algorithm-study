import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hm = new HashMap<>();
        
        // 1. 종류별로 분류하기
        for (int i=0;i<clothes.length;i++) {
            hm.put(clothes[i][1], hm.getOrDefault(clothes[i][1], 0) + 1);
        }
        
        // 2. 조합 answer = (values+1)C1 x ... x (values+1)C1
        // values+1을 하는 이유: 의상의 종류 중 선택 안 하는 경우 추가
        for (Integer cnt : hm.values()) {
            answer *= (cnt+1);

        }
        
        // 3. 모두 선택 안 하는 경우 빼기
        return answer - 1;
    }
}