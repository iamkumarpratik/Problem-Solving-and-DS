# Queue is a data structure.
# Queue follows FIFO principle. 
# FIFO stands for first in first out.
# Queue supports three operations, Enqueue, Dequeue, and Peek.

# Enqueue adds an element to the queue.
# Dequeue removes the element from the queue.
# Peek returns the last element of the queue.

class Queue:

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
        return f"{element} has been added to the queue."

    def dequeue(self):
        if not len(self.queue) == 0:
            return f"{self.queue.pop(0)} exited the queue."
        else:
            return "Queue is already empty."
    
    def show_queue(self):
        return self.queue


queue_obj = Queue()

print(queue_obj.enqueue(11))
print(queue_obj.enqueue(18))
print("Before popping elements from the queue.", queue_obj.show_queue())
print(queue_obj.dequeue())
print("After popping elements from the queue.", queue_obj.show_queue())