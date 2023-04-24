class Node:
    def __init__(self, info): 
        self.info = info  
        self.left: Node | None = None  
        self.right: Node | None = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  pathToV1 = path(root, v1)
  pathToV2 = path(root, v2)
  indexV1 = 0
  indexV2 = 0
  while indexV1 < len(pathToV1) and indexV2 < len(pathToV2) and (pathToV1[indexV1].info == pathToV2[indexV2].info):
    indexV1 += 1
    indexV2 += 1
  return pathToV1[indexV1-1]
  
  
def path(root, info):
    path = []
    while root.info != info:
        if info > root.info:
            path.append(root)
            root = root.right
            break
        path.append(root)
        root = root.left
    return path
        
             

tree = BinarySearchTree()
