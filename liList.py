class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ll:
    def __init__(self, head_node):
        self.head = head_node

    def insert(self, node):
        if self.head == None:
            self.head = node
            return

        next_node = self.head
        while next_node.next != None:
            next_node = next_node.next

        next_node.next = node
    

    def delete(self, data):
        tmp_node = self.head
        if self.head == data:
            self.head = None
            return
        
        while True: 
            if tmp_node == None or tmp_node.next == None:
                print(f"Couldn't find number {data} in list")
                return
            elif tmp_node.next.data == data and tmp_node.next.next != None:
                print(f"number {data} deleted succesfully")
                tmp_node.next = tmp_node.next.next
                return
            elif tmp_node.next.data == data and tmp_node.next.next == None:
                print(f"number {data} deleted succesfully")
                tmp_node.next = None
                return
            else: 
                tmp_node = tmp_node.next

       
    def display(self):
        tmp_node = self.head
        while tmp_node != None:
            print(tmp_node.data)
            tmp_node = tmp_node.next
    

lili = ll(node(50))

lili.insert(node(30))

lili.insert(node(20))

lili.insert(node(100))

lili.delete(100)

lili.delete(15)
lili.display()
