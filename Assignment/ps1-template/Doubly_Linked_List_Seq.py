class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new = Doubly_Linked_List_Node(x)
        if self.head != None: 
            new.next = self.head
            self.head.prev = new
            self.head = new
        else:
            self.head = new
            self.tail = new

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new = Doubly_Linked_List_Node(x)
        if self.tail != None:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            self.tail = new
            self.head = new


    def delete_first(self):
        x = self.head.item
        ###########################
        # Part (a): Implement me! #
        ###########################
        self.head = self.head.next
        if self.head is None:
            self.tail = None
            return x
        else:
            self.head.prev = None
            return x

    def delete_last(self):
        x = self.tail.item
        ###########################
        # Part (a): Implement me! #
        ###########################
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
            return x
        else:
            self.tail.next = None
            return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        if x1.prev is not None and x2.next is not None:
            L2.head = x1
            L2.tail = x2
            x1.prev.next = x2.next
            x2.next.prev = x1.prev
            x1.prev = None
            x2.next = None
        elif x1.prev is not None and x2.next is None:
            L2.head = x1
            L2.tail = x2
            self.tail = x1.prev
            self.tail.next = None
            x1.prev = None
        elif x1.prev is None and x2.next is not None:
            L2.head = x1
            L2.tail = x2 
            self.head = x2.next
            self.head.prev = None
            x2.next = None
        elif self.head == x1 and self.tail == x2:
            L2.head = x1
            L2.tail = x2
            self.head = None
            self.tail = None
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        if L2.head is None:
            return
        if self.tail != x:
            L2.tail.next = x.next
            x.next.prev = L2.tail
            L2.tail = None
            L2.head.prev = x
            x.next = L2.head
            L2.head = None
        elif self.tail == x:
            L2.head.prev = x
            x.next = L2.head
            self.tail = L2.tail
            L2.head = None
            L2.tail = None
       
