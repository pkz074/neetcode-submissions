class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequent = new HashMap<>();

        for (int num : nums){
            frequent.put(num, frequent.getOrDefault(num, 0) + 1);

        }

        PriorityQueue<Map.Entry<Integer, Integer>> miniHeap = new PriorityQueue<>(
            (a, b) -> a.getValue() - b.getValue());
    
        for (Map.Entry<Integer, Integer> entry : frequent.entrySet()){
            miniHeap.offer(entry);

            if (miniHeap.size() > k){
                miniHeap.poll();
            }
        }
        int[] result = new int[k];
        for (int i = 0; i < k; i++){
            result[i] = miniHeap.poll().getKey();
        }
        return result;
    }
}
