
  public class TreeeNode {
     int val;
      TreeeNode left;
      TreeeNode right;
      TreeeNode() {}
      TreeeNode(int val) { this.val = val; }
      TreeeNode(int val, TreeeNode left, TreeeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
 

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }


        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);

        return 1 + Math.max(leftDepth, rightDepth);
    }
}
