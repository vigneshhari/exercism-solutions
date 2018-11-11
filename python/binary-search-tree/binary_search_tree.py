class TreeNode(object):
    def __init__(self, data, left , right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):

    head = None

    def __init__(self, tree_data):

        self.head = TreeNode(tree_data[0],None,None )
        for i in tree_data[1:]:
            self.insert(i , self.head)



    def insert(self,value, obj):
        while True:
            if( value > obj.data):
                if(obj.right == None):
                    obj.right = TreeNode(value,None,None)
                    break
                else:
                    obj = obj.right
                    continue
            if(value <= obj.data):
                if(obj.left == None):
                    obj.left = TreeNode(value,None,None)
                    break
                else:
                    obj = obj.left
                    continue


    def data(self):
        return self.head

    datas = []

    def sorted_data(self):
        self.datas = []
        self.printInorder(self.head)
        return self.datas

    def printInorder(self,root):

        if root:

            self.printInorder(root.left)

            self.datas += [root.data]

            self.printInorder(root.right)
