from collections import deque

def level_order_traversal(root):
    res = []
    if root is None:
        return res
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        res.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return res

# Пример использования
print("Level-order traversal:", level_order_traversal(bst.root))  # Вывод: [50, 30, 70, 20, 40, 60, 80]