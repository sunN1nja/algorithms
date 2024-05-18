def postorder_traversal(node):
    res = []
    if node:
        res = postorder_traversal(node.left)
        res = res + postorder_traversal(node.right)
        res.append(node.val)
    return res

# Пример использования
print("Post-order traversal:", postorder_traversal(bst.root))  # Вывод: [20, 40, 30, 60, 80, 70, 50]