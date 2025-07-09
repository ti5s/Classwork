class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("Stack is empty")
        popped = self.top.data
        self.top = self.top.next
        return popped

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            raise Exception("Queue is empty")
        dequeued = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeued

class PalindromeCheckerLL:
    def __init__(self):
        self.stack = StackLL()
        self.queue = QueueLL()

    def pushCharacter(self, ch):
        self.stack.push(ch)

    def enqueueCharacter(self, ch):
        self.queue.enqueue(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.dequeue()

# Main program
if __name__ == '__main__':
    s = input("Enter a word: ").strip()
    checker = PalindromeCheckerLL()

    for ch in s:
        checker.pushCharacter(ch)
        checker.enqueueCharacter(ch)

    is_palindrome = True
    for _ in range(len(s) // 2):
        if checker.popCharacter() != checker.dequeueCharacter():
            is_palindrome = False
            break

    if is_palindrome:
        print(f"The word, {s}, is a palindrome.")
    else:
        print(f"The word, {s}, is not a palindrome.")
