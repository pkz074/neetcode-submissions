struct MinStack {
    stack: Vec<i32>,
}

impl MinStack {
    pub fn new() -> Self {
        Self { stack: Vec::new() }
    }

    pub fn push(&mut self, val: i32) {
        self.stack.push(val);
    }

    pub fn pop(&mut self) {
        self.stack.pop();
    }

    pub fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }

    pub fn get_min(&mut self) -> i32 {
        let mut tmp = Vec::new();
        let mut mini = *self.stack.last().unwrap();

        while let Some(val) = self.stack.pop() {
            mini = mini.min(val);
            tmp.push(val);
        }

        while let Some(val) = tmp.pop() {
            self.stack.push(val);
        }

        mini
    }
}
