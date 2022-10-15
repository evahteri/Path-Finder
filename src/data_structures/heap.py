

class Heap:
    """This is a min heap, and the cost of the nodes is the deciding factor when building it.
    If a node is in position k, it's left child is in position 2k, right child in position 2k+1,
    and parent in position k//2.
    """

    def __init__(self):
        """Constructor that establishes the list that is treated like a heap.
        """
        self._heap = [None]

    def get_heap_len(self):
        """Function to get the size of the heap

        Returns:
            int: heap size
        """
        return len(self._heap) - 1

    def _swap(self, pos1, pos2):
        """Swapping function to change two nodes' positions

        Args:
            pos1 (int): position of the first node
            pos2 (int): position of the second node
        """
        (self._heap[pos1], self._heap[pos2]) = (
            self._heap[pos2], self._heap[pos1])

    def push(self, node):
        """Function to insert nodes to the heap

        Args:
            node (tuple): Tuple that is (cost, (x_coordinate, y_coordinate))
            this way the cost is the decifing factor building the heap.
            Accessing node's cost: node[0]
        """
        # Add new node to the heap list
        self._heap.append(node)
        # Get last position
        position = len(self._heap) - 1
        # Looping until found the right position
        parent_position = position // 2
        if len(self._heap) - 1 > 2:
            while self._heap[position][0] < self._heap[parent_position][0]:
                self._swap(position, parent_position)
                position = position // 2

    def pop_smallest(self):
        """Function to return minimun node from heap. Min node is in position 1.
        It will adjust the binary tree after every pop.
        """
        # If heap is empty, nothing to return
        if self.get_heap_len() == 0:
            return None
        # If heap includes only one object, return that
        if self.get_heap_len() == 1:
            return self._heap.pop()
        # Fetch min and max node
        min_node = self._heap[1]
        max_node = self._heap.pop()
        # Set max node as root node
        self._heap[1] = max_node
        position = 1
        # Adjust binary tree
        left__child_position = position * 2
        while left__child_position <= self.get_heap_len():
            smallest_child_position = left__child_position
            right_child_position = left__child_position + 1
            # Check if right child exists
            if right_child_position <= self.get_heap_len():
                # if yes, check it's size and choose smaller child
                if self._heap[right_child_position][0] < self._heap[left__child_position][0]:
                    smallest_child_position = right_child_position
            # Check if parent is the right size
            if self._heap[position][0] <= self._heap[smallest_child_position][0]:
                # if yes, no need to adjust
                break
            # if no, swap parent and smallest child
            self._swap(position, smallest_child_position)
            position = smallest_child_position
            left__child_position = 2 * smallest_child_position
        # Return the smallest node
        return min_node
