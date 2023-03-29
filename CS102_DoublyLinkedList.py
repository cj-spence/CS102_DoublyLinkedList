#double linked list

class Node:
    
    def __init__(self, x):
        self.value = x
        self.prev = None
        self.next = None


class DLL:

    def __init__(self):
        self.head = None
    

    def add2head(self, x):
        newNode = Node(x)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode


    def add2tail(self, x):
        newNode = Node(x)
        explorer = self.head

        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return

        while explorer.next:
            explorer = explorer.next
        explorer.next = newNode
        newNode.prev = explorer


    def insert_after(self, x, y):
        if self.head is None:
            print("Error: The list is empty, you cannot insert.")
            return

        else:
            explorer = self.head
            while explorer is not None:
                if explorer.value == y:
                    break
                explorer = explorer.next 

            if explorer is None:
                print("The item was not found in the list.") 

            else:
                newNode = Node(x)
                newNode.prev = explorer
                newNode.next = explorer.next
                if explorer.next is not None:
                    explorer.next.prev = newNode
                explorer.next = newNode


    def insert_before(self, x, y):
        if self.head is None:
            print("Error: The list is empty, you cannot insert.")
            return

        else:
            explorer = self.head
            while explorer is not None:
                if explorer.value == y:
                    break
                explorer = explorer.next

            if explorer is None:
                print("The item was not found in the list.")

            else:
                newNode = Node(x)
                newNode.next = explorer
                newNode.prev = explorer.prev

                if explorer.prev is not None:
                    explorer.prev.next = newNode
                explorer.prev = newNode


    def delete(self, x):
        if self.head is None:
            print("Error: The list is empty, there is nothing to delete.")
            return

        if self.head.next is None:
            if self.head.value == x:
                self.head = None
            else:
                print("The item is not in the list.")
            return

        if self.head.value == x:
            self.head = self.head.next
            self.head.prev = None
            return
        
        explorer = self.head
        while explorer is not None:
            if explorer.value == x:
                break
            explorer = explorer.next

        if explorer.next is not None:
            explorer.prev.next = explorer.next
            explorer.next.prev = explorer.prev
        else:
            if explorer.value == x:
                explorer.prev.next = None
            else:
                print("The item is not in the list.")
                return
            

    def display(self):
        explorer = self.head
        print("\nForwards List")
        while explorer:
            print(explorer.value, "-> ", end='')
            last = explorer
            explorer = explorer.next
        print('//')
        print("\nReverse List")
        while last:
            print(last.value, "-> ", end='')    
            last = last.prev
        print('//\n')


d1 = DLL()

d1.add2head(10)
d1.add2head(5)
d1.add2tail(20)
d1.insert_after(105, 20)
d1.insert_before(73, 10)
d1.delete(20)
d1.add2tail(8)

d1.display()