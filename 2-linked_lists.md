# Linked Lists

One of the biggest concerns that programmers focus on is the efficiency of their code. When it comes to different data structures, sorting through data may be a long, difficult process for a computer.

One data structure that is used to optimize the way we store data is called a **linked list**.

On the outside, a linked list looks pretty much like a regular list. It's an array of data with one value placed after another until the end. However, the linked list has more capabilities when it comes to navegating the data.

## Regular Lists

For comparison, here is what the flow of a regular list looks like.

```
[ A, B, C, D, E, F, G ]

[ A  <-  B  <-  C  <-  D  <-  E  <-  F  <-  G ]  <- 
```

When a value is added to the list, it is placed on the end.

For the computer to be able to find all the values on the list, it needs to connect them by storing a variable that has the last item's value. If we look at the value `"C"` from the above list, the computer also stores the address of `"B"` so that it can remember that `C` is after `B`.

This means, however, that if you want to look at the first item on the list, you can't just tell the computer to see the address of the first value. The only one it stores is the address and value of the end, then works back from there. This means if you want the first value of a list 1000 values long, the computer will have to look through data 1000 times to find the right location and access your data.

## Linked Lists

Linked lists help solve this. Picture two lists, one of them is reversed.

```
   [ A  <-  B  <-  C  <-  D  <-  E  <-  F  <-  G ]  <- 

-> [ A  ->  B  ->  C  ->  D  ->  E  ->  F  ->  G ]
```

You zipper those two lists together, and you have a linked list.

```
-> [ <- A ->  <- B ->  <- C ->  <- D ->  <- E ->  <- F ->  <- G ] <-
```

This type of list can be traversed both forward and backward. Not only does `"C"` store the location of `"B"`, but it also stores where `"D"` is as well. You can also add or remove values from either end of the list without having to traverse the entire list first.

# Insert & Remove

Each "node" in a linked list stores several values: `data`, `prev`, and `next`. The list itself also stores two unique values: `head`, and `tail`.

To append an item to the head or tail, you not only need to modify the attribute `head` or `tail`, you'd also need to modify the addresses of any nodes touching it. For the head, it would be the node at `next`. For the tail, it would be the node at `prev`. Here is what an insert function would look like for the head:

```
def insert_head(self, value):

    new_node = LinkedList.Node(value)

    if self.head is None:
        self.head = new_node
        self.tail = new_node

    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
```

This method has 3 parts. First, it creates a node with the desired value. All that is left now is to place it. If there is no head, that means there is no tail, or list at all. It creates a new head and tail and sets them both to the new node.

If there is already a head, the function changes a few values. It sets the new node's `next` to the current head so that it is sticking out on that end of the list. Then, it sets the current head's `prev` to the new node, finishing the two-way link all the values share. Finally, it sets the `head` to the new node.

Appending to the tail looks about the same, except switching the word "head" with "tail" and reversing the order of the connections made.

The method to remove the head is similar but works in reverse:

```
def remove_head(self):

    if self.head == self.tail:
        self.head = None
        self.tail = None
        
    elif self.head is not None:
        self.head.next.prev = None
        self.head = self.head.next
```

The major difference is that the check in the beginning is if the head is the same as the tail. This covers the chance that the list is only one value long.

# Example

Book and movie series are structured somewhat like a linked list. An author or director can make a sequel, which goes at the end of the order, or a prequel, which goes before the others made at the beginning.

They can also make one that goes in between others, like how the movie *Rogue One* went in between the two major Star Wars series, but that movie was made way after.

This is what the code would look like to create and add to a series.

```
class SeriesLinkedList:
    

    class Node:
        """ Each node is an object storing the value (data),
            the previous object, and the next
        """

        def __init__(self, data):
            """ Initializes node with the attributes data, prev, and next.
                prev and next will be decided in the insert() methods.
            """
            self.data = data
            self.next = None
            self.prev = None


    def __init__(self):
        """ makes an empty instance
        """
        self.head = None
        self.tail = None


    def add_prequel(self, value):
        """ Adds a prequel to the start (head) of the list
        """
        new_node = SeriesLinkedList.Node(value)  
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def add_sequel(self, value):
        """ Adds a sequel to the end (tail) of the list
        """
        new_node = SeriesLinkedList.Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def add_after(self, value, new_value):
        """ Adds an installment after the one specified.
        """
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_tail(new_value)
                else:
                    new_node = SeriesLinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next


    def __iter__(self):
        """ Iterate foward through the Linked List
        """
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next


    def __str__(self):
        """ Return a string representation of the linked list.
        """
        output = "["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
```

Here is what the tests for this will look like:

```
""" ---- Tests ---- """

# TEST 1

lotr = SeriesLinkedList()

lotr.add_sequel("Fellowship of the Ring")
lotr.add_sequel("The Two Towers")
lotr.add_sequel("Return of the King")
print(lotr) # [Fellowship of the Ring, The Two Towers, Return of the King]

lotr.add_prequel("The Hobbit")
print(lotr) # [The Hobbit, Fellowship of the Ring, The Two Towers, Return of the King]

# TEST 2

star_wars = SeriesLinkedList()

star_wars.add_sequel("A New Hope")
star_wars.add_sequel("The Empire Strikes Back")
star_wars.add_sequel("Return of the Jedi")

star_wars.add_prequel("Revenge of the Sith")
star_wars.add_prequel("Attack of the Clones")
star_wars.add_prequel("The Phantom Menace")

print(star_wars) # [The Phantom Menace, Attack of the Clones, Revenge of the Sith,
                 #  A New Hope, The Empire Strikes Back, Return of the Jedi]

star_wars.add_after("Revenge of the Sith", "Rogue One")
star_wars.add_after("Attack of the Clones", "Solo")

print(star_wars) # [The Phantom Menace, Attack of the Clones, Solo, Revenge of the Sith,
                 #  Rogue One, A New Hope, The Empire Strikes Back, Return of the Jedi]
```

# Problem

You are assigned to create the code for a new sleep tracker app that promotes healthier sleep habits. The sleep tracker only stores information for the last 7 nights of sleep.

You create a linked list that has the following properties:

* A list that contains the sleep for the last 7 nights

* A method to add a night of sleep. This method will check if there are 7 days of information. If there is already 7, it will remove the current head when it adds the new value on the tail (to keep the total at 7).

* A method to print a "status update". This will calculate and return the week's **average**, **lowest night of sleep**, and **# of nights under 8 hours**.

Here are tests for you to run.

```
st = SleepTracker()

st.add_night(9)
st.add_night(6)
st.add_night(7)
st.add_night(8)
st.add_night(8)
st.add_night(5)
st.add_night(8)

print(st)                   # [9, 6, 7, 8, 8, 5, 8]
print(st.status_update())   # avg: 7.29, low: 5, nights under 8hrs: 3

st.add_night(4)
st.add_night(4)
st.add_night(5)
st.add_night(3)

print(st)                   # [8, 5, 8, 4, 4, 5, 3]
print(st.status_update())   # avg: 5.29, low: 3, nights under 8hrs: 5
```

# Solution

Please do as much of the problem as you are able before you reference the solution.

It can be found [here](solution-2.py).