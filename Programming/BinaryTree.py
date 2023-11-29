class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


    def buildTree(self, array):
        value = map(int, input("Enter value"))

        if(value != -1):

            root = Node(value)
            root.left = self.buildTree()
            root.right = self.buildTree()


    def levelOrdertraversal(self, root):

        queue = []
        queue.append(root)
        queue.append(None)

        while queue:

            current = queue.pop(0)

            if current == None:
                print()
                queue.append(None)

            else:
                print(current.data)
                queue.append(current.left)
                queue.append(current.right)



if __name__ == "__main__":

    n = Node(1)

    n.buildTree()
