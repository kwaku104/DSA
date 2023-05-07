class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return "{'value': " + str(self.value) + ", 'left': " + str(self.left) + ", 'right': " + str(self.right) + "}"

    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)
# BreadthFirstSearchR(queue, list) {
#     if (!queue.length) {
#       return list;
#     }
#     const currentNode = queue.shift();
#     list.push(currentNode.value);
    
#     if (currentNode.left) {
#       queue.push(currentNode.left);
#     }
#     if (currentNode.right) {
#       queue.push(currentNode.right);
#     }
    
#     return this.BreadthFirstSearchR(queue, list);
#   }
# }
    def BreadthFirstSearchR(self, queue, array):
        if not len(queue):
            return array
        currentNode = queue.pop()
        array.append(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        return self.BreadthFirstSearchR(queue, array)

    def BreadthFirstSearch(self):
        currentNode = self.root
        array = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop()
            array.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return array

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if not currentNode.left:
                        currentNode.left = newNode
                        return self
                    currentNode = currentNode.left
                else:
                    if not currentNode.right:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right

    def lookup(self, value):
        if not self.root:
            return False
        currentNode = self.root
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif currentNode.value == value:
                return currentNode
        return False

    def DFTPreOrder(self, currentNode, array):
        return traversePreOrder(self.root, [])

    def DFTPostOrder(self):
        return traversePostOrder(self.root, [])

    def DFTInOrder(self):
        traverseInOrder(self.root, [])

    def traversePreOrder(self, node, array):
        array.append(node.value)
        if node.left:
            traversePreOrder(node.left, array)
        if node.right:
            traversePreOrder(node.right, array)
        return array

    def traverseInOrder(self, node, list):
        if node.left:
            traverseInOrder(node.left, array)
        array.push(node.value)
        if node.right:
            traverseInOrder(node.right, array)
        return array

    def traversePostOrder(self, node, array):
        if node.left:
            traversePostOrder(node.left, array)
        if node.right:
            traversePostOrder(node.right, array)
        array.append(node.value)
        return array

    def remove(self,value):
        if not self.root:
            return False
        currentNode = self.root
        parentNode = None
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode.value == value:
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right
                else:
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left is not None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                return True

# let currentNode = this.root;
#     let list = [];
#     let queue = [];
#     queue.push(currentNode);

#     while(queue.length > 0){
#       currentNode = queue.shift();
#       list.push(currentNode.value);
#       if(currentNode.left) {
#         queue.push(currentNode.left);
#       }
#       if(currentNode.right) {
#         queue.push(currentNode.right);
#       }
#     }
#     return list;
#   }
# }



tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# tree.lookup(20)
# tree.remove(9)
print(tree)
print('BFS', tree.BreadthFirstSearch())
print('BFS', tree.BreadthFirstSearchR([tree.root], []))
print('DFSpre', tree.DFTPreOrder())
print('DFSin', tree.DFTInOrder())
print('DFSpost', tree.DFTPostOrder())