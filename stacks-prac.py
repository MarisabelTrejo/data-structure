class Simple_Queue_Authors:
    
    #Maintaing a Queue/Stack using a List


    def __init__(self):
        
        # Initialize the empty queue using a Python List. 
        # We will put the authors in this empty list. 
        self.queue = []

    def enqueue(self, value):
    
        #Enqueue the value provided into the queu
        # We will append all the authors using this function
        self.queue.append(value)

    def dequeue(self):
        
        # Dequeue the next value and return it
        # This function will remove the next value and return it 

        if len(self.queue) <= 0:
            raise IndexError()
        value = self.queue[0]
        del self.queue[0]
        return value


# Exepcted Result: It should display 100

queue = Simple_Queue_Authors()
authors = ["Achebe", "Christie", "Dickens", "Dostovesky", "Faulkner"]
queue.enqueue(authors)
value = queue.dequeue()
print(value)

print("=================")

# Scenario: Enqueue multiple values and then Dequeue all of them
# Exepcted Result: It should display Joyce, then Morris, then Shakespere in that order
queue = Simple_Queue_Authors()
queue.enqueue("Joyce")
queue.enqueue("Morrris")
queue.enqueue("Shakespeare")
value = queue.dequeue()
print(value)
value = queue.dequeue()
print(value)
value = queue.dequeue()
print(value)

