class Map:
    class Node:
        def __init__(self, key, data, prev=None, left=None, right=None):
            self.key = key
            self.data = data
            self.prev = prev
            self.left = left
            self.right = right

    def __init__(self, map=None):
        self.head = None
        self.count = 0

        if map is not None:
            self.head = self.copy_tree(map.head)
            self.count = map.count

    def copy_tree(self, root):
        if root is None:
            return None
        new_node = self.Node(root.key, root.data, root.prev, None, None)
        new_node.left = self.copy_tree(root.left)
        new_node.right = self.copy_tree(root.right)
        return new_node

    def _add_node(self, key, data):
        marker = True
        tmp_node = self.Node(key, data, self.head, None, None)
        if self.head is None:
            self.head = tmp_node
            self.count += 1
        else:
            tmp_node = self.head
            while marker:
                if key < tmp_node.key and tmp_node.left is not None:
                    tmp_node = tmp_node.left
                elif key > tmp_node.key and tmp_node.right is not None:
                    tmp_node = tmp_node.right
                else:
                    marker = False
            new_node = self.Node(key, data, tmp_node, None, None)
            if key < tmp_node.key:
                tmp_node.left = new_node
                self.count += 1
            elif key > tmp_node.key:
                tmp_node.right = new_node
                self.count += 1
            else:
                print(f"Значению '{data}' нужно подобрать другой ключ, т.к. данный - {key} - уже присутствует в дереве!")

    def add_element(self, key, data):
        self._add_node(key, data)

    def clear(self):
        if self.head is None:
            print("Список и так уже пуст!")
        else:
            self._clear_tree(self.head)
            print("Список очищен.")

    def _clear_tree(self, root):
        if root.left is not None:
            self._clear_tree(root.left)
        if root.right is not None:
            self._clear_tree(root.right)
        root.data = None
        root.key = None
        root.prev = None
        root.right = None
        root.left = None
        self.count -= 1

    def get_element_node(self, key):
        tmp_node = self.head
        marker = True
        while marker:
            if key < tmp_node.key and tmp_node.left is not None:
                tmp_node = tmp_node.left
            elif key > tmp_node.key and tmp_node.right is not None:
                tmp_node = tmp_node.right
            else:
                marker = False
        if key == tmp_node.key:
            return tmp_node
        else:
            print(f"Значения с ключом - {key} - нет в дереве!")
            return None

    def change_element(self, key, data):
        tmp_node = self.head
        marker = True
        while marker:
            if key < tmp_node.key and tmp_node.left != None:
                tmp_node = tmp_node.left
            elif key > tmp_node.key and tmp_node.right != None:
                tmp_node = tmp_node.right
            else:
                marker = False
        if key == tmp_node.key:
            tmp_node.data = data
        else:
            print("Значения с ключом -", key, "- нет в дереве!")

    def size(self):
        print("Элементов в дереве:", self.count)

    def less_than(self, other):
        return self.head.key < other.head.key

    def less_than_or_equal_to(self, other):
        return self.head.key <= other.head.key

    def equal_to(self, other):
        return self.head.key == other.head.key

    def not_equal_to(self, other):
        return self.head.key != other.head.key

    def greater_than(self, other):
        return self.head.key > other.head.key

    def  greater_than_or_equal_to(self, other):
        return self.head.key >= other.head.key