# Trees- Binary Data Storage

When we learned about Big O notation, one of the ways we learned to sort through data efficiently is through the use of trees.

Looping through data one at a time will bring a Big O notation of O(n), and can be done more efficiently.

Creating a binary tree allows you to sort information and retrieve data with a Big O notation of O(log(n)) - also known as O(2^n), which is even more efficient than O(n) and guarantees that it will take less iterations than the whole length of the data.

## This is what a data tree looks like:

**data tree image**

Each node, or spot on the tree can possibly have a left value and a right. Just like your family tree, each will continue branching until all the data is included.

Data on these trees is usually sorted from smallest to largest, but it looks differently than a regular list sorted the same way. Here is what a regular sorted list looks like:

```
[1,2,3,4,5,6,7,8,9]
```

And this is what the same data could look like in the binary tree.

```
           5 
         /   \
       3      8
      / \    / \
     2   4  6   9
    /        \
   1          7
```

Each node is at exactly halfway between each of its child nodes. This means that if you search through a binary tree, you can simply repeatedly ask, "is this value higher or lower than the one I'm looking for?"

## Recursion

To look at a value or sort through a value on the tree, we need to use a coding principle called **recursion**. This means writing a function that calls itself.

Here's what this would look like:

```
def check_tree(self, node):

    print(node.value)

    if node.left:
        check_tree(node.left)

    if node.right:
        check_tree(node.right)
```

Let me translate. First, I wrote the action that was to be performed on each node (in this one it was printing the value of the node- it can be whatever you like). Then, I called the same function to be performed on both the left and right connected nodes on the tree.

When the last node is completed, it will complete the code in the function and return to the previous one, again and again until the functions are all complete.

Most people write recursive functions with a conditional statement in the beginning to break from the function once a certain requirement is met. This will make the code even more efficient.

## Append and Remove methods

This is what the append method looks like for a binary tree:

```
def append(self, data, node)

    if data == node.data:
                return

    elif data < node.data:

        if node.left is None:
            node.left = BST.Node(data)

        else:
            self.append(data, node.left)

    else:
        if node.right is None:
            node.right = BST.Node(data)

        else:
            self.append(data, node.right) 
```

The first thing written was the catch- if the data that you want to insert is already in the tree, it will just stop there. Then, the function checks if the data is less than or greater than the node value. This will decide what side the function searches next.

If there is no value on left or right, the value is placed as a new node. Mission accomplished! If there is a value on either side, the function is reapeated over again, starting on the new node that is found on one side.

Next, we'll look at a search function, that looks for a specific value and returns if it exists in the tree:

```
def search(self, data, node)

    has_node = False

    if node is not None:

        if data == node.data:
            has_node = True

        elif data < node.data:
            has_node = self.search(data, node.left)

        elif data > node.data:
            has_node = self.search(data, node.right)

    return has_node
```

This function loops through every value in the node tree, except this time tries to define the boolean `has_node`. If the value is found, it is caught in the beginning and returned right up until the original funcion, which returns `True`. If the value is never found, the functions all pass down the boolean `False`.

# Example

In this example, I will show you how to make a tree out of a list of student GPAs.

The list looks something like this: 

```
put list here
```

First I will need to sort the list from smallest to largest. This will set us up for an organized tree.

```
code goes here
```

Next, I will need to...

```
example code here...


tests & outputs too
```

# Problem

In this problem you will need to take all the ages from a list and calculate with them the standard deviation of all the data.

The formula to calculate standard deviation is this:

```
big formula here
```

in python, that huge formula will look something like this.

```
python formula here
```

The instructions are as follows:

* First, you will need to create a recursive function that goes through each item on the tree and places it on a list.

* Next, you will need to calculate the mean of the data.

* Finally, you will need to place the standard deviation function from above and run the numbers through it.

The standard deviation will be returned at the end.

Here are some tests for you. Your code should pass them all.

```
Tests go here
```

# Solution

Please do as much of the problem as you are able before you reference the solution.

It can be found [here](solution-3.py).