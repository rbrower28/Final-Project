
class Order_Queue:

    class Node:
        
        def __init__(self, customer, quantity, isPriority):
            """ Initialize a node with the given properties
            """

            self.customer = customer
            self.quantity = quantity
            self.isPriority = isPriority


        def __str__(self):
            """ Formats the node to be viewed as a string
            """

            priorityDict = { True: "Priority", False: "Standard"}

            return f"{self.customer} - {self.quantity} ({priorityDict[self.isPriority]})"


    def __init__(self):
        """ Initialize an empty priority queue
        """

        self.queue = []


    def __str__(self):
        """ Formats the queue to be viewed as a string
        """

        result = "["
        for node in self.queue:
            result += str(node)
            result += ", "
        result += "]"
        return result


    def enqueue(self, customer, quantity, priority):
        """ establish a new node, set priority and place on queue
        """

        priorityDict = { "Priority": True, "Standard": False}

        new_node = Order_Queue.Node(customer, quantity, priorityDict[priority])
        self.queue.append(new_node)


    def dequeue(self):
        """ removes an item from the queue.
        Checks shipping status then quantity to determine which
        """

        # Verify the queue is not empty
        if len(self.queue) == 0:  
            print("The queue is empty.")
            return None

        # Find the index of the item to remove 
        next_index = 0
        highest_quantity = 0
        highest_priority_quantity = 0
        has_priority = False

        for index in range(len(self.queue)):

            if self.queue[index].isPriority == True:
                
                has_priority = True
                if self.queue[index].quantity > highest_priority_quantity:
                    highest_priority_quantity = self.queue[index].quantity
                    next_priority = index

            else:
                if self.queue[index].quantity > highest_quantity:
                    highest_quantity = self.queue[index].quantity
                    next_standard = index

        if has_priority:
            next_index = next_priority
        else:
            next_index = next_standard

        # Remove and return the item with the highest priority
        next = self.queue.pop(next_index)
        return str(next)


"""     Tests     """

queue = Order_Queue()

# Test 1

print("\n ------ Test 1 ------ \n")

queue.enqueue("Susan", 4, "Standard")
queue.enqueue("Tommy", 1, "Priority")
queue.enqueue("Craig", 2, "Standard")
queue.enqueue("Brady", 4, "Standard")
queue.enqueue("Sandy", 2, "Priority")
queue.enqueue("Tammy", 2, "Priority")
queue.enqueue("Jonny", 3, "Standard")

print(queue, "\n")

print(queue.dequeue()) # Sandy - 2 (Priority)
print(queue.dequeue()) # Tammy - 2 (Priority)
print(queue.dequeue()) # Tommy - 1 (Priority)
print(queue.dequeue()) # Susan - 4 (Standard)
print(queue.dequeue()) # Brady - 4 (Standard)
print(queue.dequeue()) # Jonny - 3 (Standard)
print(queue.dequeue()) # Craig - 2 (Standard)

# Test 2

print("\n ------ Test 2 ------ \n")

queue.enqueue("Susan", 4, "Standard")
queue.enqueue("Tommy", 1, "Priority")
queue.enqueue("Craig", 2, "Standard")
queue.enqueue("Brady", 4, "Standard")

print(queue.dequeue()) # Tommy - 1 (Priority)
print(queue.dequeue()) # Susan - 4 (Standard)

queue.enqueue("Sandy", 2, "Priority")

print(queue.dequeue()) # Sandy - 2 (Priority)
print(queue.dequeue()) # Brady - 4 (Standard)

queue.enqueue("Tammy", 2, "Priority")
queue.enqueue("Jonny", 3, "Standard")

print(queue.dequeue()) # Tammy - 2 (Priority)
print(queue.dequeue()) # Jonny - 3 (Standard)
print(queue.dequeue()) # Craig - 2 (Standard)