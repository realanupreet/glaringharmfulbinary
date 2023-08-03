def populate_sibling_pointers(root):
    # TODO: Write - Your - Code
    if root is None:
        return
    q = [root]
    prev = None
    while q:
        l = len(q)
        for _ in range(l):
            ele = q.pop(0)
            if prev:
                prev.next = ele
            prev = ele
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)

    return root
