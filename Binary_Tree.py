class Binary_Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Binary_Tree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right=Binary_Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
    
    def inorder(self,node):
        res=[]
        if node:
            res=self.inorder(node.left)
            res.append(node.data)
            res=res+self.inorder(node.right)
        return res
    
    def preorder(self,node):
        res=[]
        if node:
            res.append(node.data)
            res=res+self.preorder(node.left)
            res=res+self.preorder(node.right)
        return res
    
    def postorder(self,node):
        res=[]
        if node:
            res=self.postorder(node.left)
            res=res+self.postorder(node.right)
            res.append(node.data)
        return res
    
    def search(self,node,find):
        if node:
            if node.data==find:
                return True
            elif find<node.data:
                return self.search(node.left,find)
            else:
                return self.search(node.right,find)
        else:
            return False




    
tree=Binary_Tree(5)
tree.insert(2)
tree.insert(1)
tree.insert(6)
tree.insert(8)

print(tree.inorder(tree))
print(tree.preorder(tree))
print(tree.postorder(tree))
tree.print_tree()

print(tree.search(tree,10))