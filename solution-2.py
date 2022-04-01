class SleepTracker:
    

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


    def _insert_tail(self, value):
        """ Adds a night of sleep to the end (tail) of the list
        """
        new_node = SleepTracker.Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def _remove_head(self):
        """ Removes the head of the linked list.
        """
        if self.head == self.tail:
            self.head = None
            self.tail = None
            
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next


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


    def add_night(self, length):
        """ Adds a night of sleep. If there are already 7,
            removes a night from the head to make room.
        """
        sleep_list = list(self)

        if len(sleep_list) >= 7:
            self._remove_head()
            
        self._insert_tail(length)


    def status_update(self):
        
        sleep_list = list(self)

        sleep_avg = round(sum(sleep_list) / len(sleep_list), 2)
        sleep_low = min(sleep_list)
        under_8_hours = 0

        for night in sleep_list:
            if night < 8:
                under_8_hours += 1

        return f"avg: {sleep_avg}, low: {sleep_low}, nights under 8hrs: {under_8_hours}"



""" ---- Tests ---- """

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