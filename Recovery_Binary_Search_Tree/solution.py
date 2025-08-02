class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    first = second = prev = None
    curr = root

    while curr:
        if curr.left is None:
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                second = curr
            prev = curr
            curr = curr.right
        else:
            # Find the inorder predecessor of current
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right

            if pre.right is None:
                # Make current as right child of its inorder predecessor
                pre.right = curr
                curr = curr.left
            else:
                # Revert the changes made
                pre.right = None
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right

    return sorted([first.val, second.val])

# Example usage:
# Construct the tree:
#     1
#    / \
#   3   4
#    \
#     2

node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(2)

node1.left = node2
node1.right = node3
node2.right = node4

print(recoverTree(node1))  # Output should be [1, 2] if 1 and 2 were swapped
