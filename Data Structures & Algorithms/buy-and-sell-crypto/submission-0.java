class Solution {
    public int maxProfit(int[] prices) {
       int minPrice = prices[0];
       int maxProfit = 0;

       for(int i = 1; i < prices.length; i++){
        int currentProfit = prices[i] - minPrice;
        if(currentProfit > maxProfit){
            maxProfit = currentProfit;
            }
        if (prices[i] < minPrice){
            minPrice = prices[i];
        }

       }
       return maxProfit;
    }
}
