
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, root, index=0):
        if index >= len(root) or not root[index]:
            return None
        ind = TreeNode()
        ind.val = root[index]
        ind.left = self.buildTree(root, index*2+1)
        ind.right = self.buildTree(root, index*2+2)
        return ind

    def maxDepth(self, root):
        point = 1
        if root:
            point += self.maxDepth(root.left)
            point += self.maxDepth(root.right)
        return point


root = [3,9,20,None,None,15,7]
a = Solution().buildTree(root)
b = Solution().maxDepth(a)
print(b)