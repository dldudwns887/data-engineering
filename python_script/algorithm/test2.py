def create_node(value):
    return {"value": value, "left": None, "right": None}


def insert(root, value):
    if root is None:
        return create_node(value)
    current = root
    while True:
        if value < current["value"]:
            if current["left"] is None:
                current["left"] = create_node(value)
                return root
            current = current["left"]
        elif value > current["value"]:
            if current["right"] is None:
                current["right"] = create_node(value)
                return root
            current = current["right"]
        else:
            return root


def inorder(root):
    result = []

    def walk(node):
        if node is None:
            return
        walk(node["left"])
        result.append(node["value"])
        walk(node["right"])

    walk(root)
    return result


def main():
    values = [7, 3, 9, 1, 5, 8, 10]
    root = None
    for value in values:
        root = insert(root, value)
        
    print("inorder:", inorder(root))


if __name__ == "__main__":
    main()
