def preorder_traversal(node):
    res = []
    if node:
        res.append(node.val)
        res = res + preorder_traversal(node.left)
        res = res + preorder_traversal(node.right)
    return res

# Пример использования
print("Pre-order traversal:", preorder_traversal(bst.root))  # Вывод: [50, 30, 20, 40, 70, 60, 80]