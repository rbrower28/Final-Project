class Binary_Tree:
    

    class Node:
        """ Each node on the tree has data and references the 
        left and right branches.
        """

        def __init__(self, data):
            """ Initialize a node with the properties
                "name", "left", and "right".
            """
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        """ Initialize an empty tree.
        """
        self.root = None


    def insert(self, data):
        """ checks if the value of the root is none.
        If not, starts the recursive method _insert() to find a place.
        """
        if self.root is None:
            self.root = Binary_Tree.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root


    def _insert(self, data, node):
        """ This method will look for a place to insert a node.
        """
        if data == node.data:
            return
        elif data < node.data:
            if node.left is None:
                node.left = Binary_Tree.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Binary_Tree.Node(data)
            else:
                self._insert(data, node.right)


    def _generate_sorted_list(self):
        """ This method calls the recursive method _check_branch to gather data from every node,
            then sorts the list and returns it.
        """
        nodes = []
        self._check_branch(self.root, nodes)
        nodes.sort()
        return nodes


    def _check_branch(self, node, nodes):
        """ This function will find the data for each active node and add them to the list.
        """
        if node is None:
            pass
        else:
            nodes.append(node.data)

            self._check_branch(node.right, nodes)
            self._check_branch(node.left, nodes)

    
    def standard_deviation(self):
        """ Calculates and returns the standard deviation of the values on the tree
        """
        import math

        tree_sorted = self._generate_sorted_list()

        # Finding Mean value
        sum = 0

        for i in range(len(tree_sorted)):
            sum += tree_sorted[i]

        mean = sum / len(tree_sorted)

        # Finding square of the difference between mean and each value
        difference_squared = 0

        for i in range(len(tree_sorted)):
            difference_squared += (tree_sorted[i] - mean) ** 2

        # Finding Square Root of the differences and the list length
        standard_deviation = math.sqrt(difference_squared / ((len(tree_sorted)) - 1))

        return standard_deviation


""" ---- non-class methods ---- """

def generate_tree(sorted_list):
    """ Given a sorted list (sorted_list), create a balanced tree.
    This requires that the data is already sorted from smallest to largest.
    """
    tree = Binary_Tree()
    _insert_middle(sorted_list, 0, len(sorted_list)-1, tree)
    return tree


def _insert_middle(sorted_list, first, last, bst):
    """ This method will attempt to insert the item in the middle
    of 'sorted_list' into the tree.
        as the method repeats, the "first" and "last" parameters keep
        the range within the sliced sections of the list.
    """

    if last >= 0:

        middle = int((last - first) / 2) + first
        bst.insert(sorted_list[middle])

        if last - first < 1:
            return
        else:
            _insert_middle(sorted_list, first, middle - 1, bst)
            _insert_middle(sorted_list, middle + 1, last, bst)



""" ---- Tests ---- """

tree1 = generate_tree([10, 20, 30, 40, 50, 60])
print(tree1.standard_deviation())

tree2 = generate_tree([1, 4, 5, 6, 7, 8, 14])
print(tree2.standard_deviation())