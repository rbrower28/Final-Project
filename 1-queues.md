# Queues

Imagine you're waiting to be seated at your favorite restaurant. You're first in line (you've been waiting a while), and there are a dozen more hungry people behind you. The host finally comes out from the back and offers to seat the last people in line... before everyone else! Does this seem right?

## Lists

In Python, regular lists are ordered in the same way. They have a **First In Last Out (FILO)** policy, meaning that items are removed opposite the order they were placed. Using `.pop()` to remove the next item on this list:

```
["You", "Tommy", "Stacy", "Amy"]
```

would leave this:

```
["You", "Tommy", "Stacy"]
```

Adding and removing would always happen on one end of the list, like so.

```
                            <-----
["You", "Tommy", "Stacy"]
                            ----->
```

If you're first in line at a restaurant run this way, they would have to serve all the people that got there later than you first! It probably means you won't ever get a table because new people are always coming in.

In a list, looking for something at the beginning means sorting through every item on it, one by one from back to front. While this may be a good way to organize some things, it clearly isn't for everything. A restaurant run in this style would lose all it's customers!

## Queues

A queue, however, solves this problem by ordering the same list in a different way. The Queue's policy is **First In First Out (FIFO)**, meaning that if you've been there the longest, you're next in line. This principle has tons of real-world applications, such as:

* Fast food
* The doctor's office
* Customer support call centers

And many more.

Using a function to take the next item on this queue:

```
["You", "Tommy", "Stacy", "Amy"]
```

Would leave you with this:

```
["Tommy", "Stacy", "Amy"]
```

This is because the flow of a queue is strictly linear. Visually, a queue looks like this:

```
                                     <-----
         ["Tommy", "Stacy", "Amy"]
<-----
```

# Queue Properties and Methods

An item in a queue can have certain properties. Usually it consists of a `Node`, which has the property `value` (`node.value`) and as many other properties as you'd like.

Just like how a list in Python has the methods append and pop to add and remove items, a queue has similar methods: `enqueue` and `dequeue`.

## Enqueue

This is what a basic queue's `enqueue` method looks like.

```
def enqueue(self, value):

    new_node = Queue.Node(value)

    self.queue.append(new_node)
```

It first defines a new node, which holds the value and can store any other properties depending on the use.

## Dequeue

A queue's `dequeue` function looks a bit like this.

```
def dequeue(self):

    if len(self.queue) == 0:
        print("The queue is empty.")
        return None
    
    next = self.queue.pop(0)
    return next.value
```

It first determines if the queue is empty. If it is, that saves us a lot of work. If not, it will take the item at the beginning of the queue and remove it. Here can also be the logic for determining which item is next (based on certain parameters).

# Example

An emergency room relies on queues to know who to attend to. Each patient is given a spot in the queue as well as a level of urgency (between 1 and 5, 1 being low danger and 5 being high danger).

This sample code will enqueue patients with their name and level of urgency, then dequeue them with the following criteria:

* The higher levels of urgency go first
* in each level, the first in the queue is taken

Here is what that code would look like.

```
class Emergency_Queue:

    class Node:
        
        def __init__(self, name, urgency=1):
            """ Initialize a node with the properties
                "name" and "urgency"
            """
            self.name = name
            self.urgency = urgency


        def __str__(self):
            """ Formats the node to be viewed as a string
            """
            return f"{self.name} (urgency: {self.urgency})"


    def __init__(self):
        """ Initialize an empty queue
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


    def enqueue(self, name, urgency):
        """ establish a new node, set name and urgency
        """
        new_node = Emergency_Queue.Node(name, urgency)
        self.queue.append(new_node)


    def dequeue(self):
        """ removes an item from the queue.
            Checks urgency first.
        """
        if len(self.queue) == 0:  
            print("The queue is empty.")
            return None

        highest_urgency = 0

        for index in range(len(self.queue)):
            if self.queue[index].urgency > highest_urgency:
                    next_index = index

        next = self.queue.pop(next_index)
        return str(next)
```

Test cases will be run to verify the code. This is what they would look like:

```
print("\n ------ Tests ------ \n")

queue = Emergency_Queue()

queue.enqueue("Amy", 2)
queue.enqueue("Ken", 1)
queue.enqueue("Joe", 3)
queue.enqueue("Ian", 2)
queue.enqueue("Tim", 1)
queue.enqueue("Mac", 5)
queue.enqueue("Jan", 1)

print(queue, "\n")

print(queue.dequeue())   # Mac (urgency: 5)
print(queue.dequeue())   # Joe (urgency: 3)
print(queue.dequeue())   # Amy (urgency: 2)
print(queue.dequeue())   # Ian (urgency: 2)
print(queue.dequeue())   # Ken (urgency: 1)
print(queue.dequeue())   # Tim (urgency: 1)
print(queue.dequeue())   # Jan (urgency: 1)
```

# Problem

An online shopping company needs a way to keep track of their orders. Each order contains the following information:

* Customer name
* Order quantity
* Shipping option (Standard or Priority)

They need a way to organize their list of orders in the following ways and in this exact order:

* Priority orders before Standard
* Larger orders before smaller
* Earlier orders before later

This means that the item taken with the `dequeue` method will be the priority order that has the largest quantity. If there are multiple priority orders at the highest quantity, the earliest order will be taken. If there are no priority orders, the first standard order with the largest quantity will be next and so on.

The following table shows the correct order of the items dequeued from a sample. Test your program using this information. Enqueue them from top to bottom.

| Product Queue        | Order Shipped  |
| -------------------- | -------------- |
| Susan, 4, Standard   | 4th            |
| Tommy, 1, Priority   | 3rd            |
| Craig, 2, Standard   | 7th            |
| Brady, 4, Standard   | 5th            |
| Sandy, 2, Priority   | 1st            |
| Tammy, 2, Priority   | 2st            |
| Jonny, 3, Standard   | 6th            |

Note: **Do not reorder the items on the queue**. Use this criteria in the dequeue method to determine the next order.

# Solution

Please do as much of the problem as you are able before you reference the solution.

It can be found [here](solution-1.py).