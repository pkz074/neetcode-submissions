impl Solution {
    pub fn is_valid(s: String) -> bool {

        let mut stack = Vec::new();

        let close_open: HashMap<char, char> = [(')', '('), (']', '['), ('}', '{')].into();
    
    
        for ch in s.chars() {

            if let Some(&open) = close_open.get(&ch) {
                if !stack.is_empty() && *stack.last().unwrap() == open {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }
        stack.is_empty()
    
    
    }

}
