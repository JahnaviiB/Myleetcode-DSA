def sym_bt(root1,root2):
    if root1 is None and root2 is None:
        return False
    elif (root1 is None) != (root2 is None):
        return False
    elif root1.val != root2.val:
        return False
    else:
        return sym_bt(root1.left,root2.right) and sym_bt(root1.right,root2.left)
def is_symmetric(root):
    if root is None:
        return True
    return sym_bt(root.left,root.right)


