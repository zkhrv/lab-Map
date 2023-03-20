# Класс узла
class node:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.height = 0

# Класс Дерева
class Map:
    def __init__(self):
        self.head = None
        self.count = 0

    def updateHeight(self, n):
        n.height = 1 + max(self.height(n.left), self.height(n.right))

    def height(self, n):
        return -1 if n is None else n.height

    # балансировка
    def getBalance(self, n):
        return 0 if n is None else self.height(n.right) - self.height(n.left)

    # поворот направо
    def rotateRight(self, y):
        x = y.left
        z = x.right
        x.right = y
        y.left = z
        self.updateHeight(y)
        self.updateHeight(x)
        return x

    # поворот налево
    def rotateLeft(self, y):
        x = y.right
        z = x.left
        x.left = y
        y.right = z
        self.updateHeight(y)
        self.updateHeight(x)
        return x

    # перебалансировка
    def rebalance(self, z):
        self.updateHeight(z)
        balance = self.getBalance(z)
        if balance > 1:
            if self.height(z.right.right) > self.height(z.right.left):
                z = self.rotateLeft(z)
            else:
                z.right = self.rotateRight(z.right)
                z = self.rotateLeft(z)
        elif balance < -1:
            if self.height(z.left.left) > self.height(z.left.right):
                z = self.rotateRight(z)
            else:
                z.left = self.rotateLeft(z.left)
                z = self.rotateRight(z)
        return z

    # добавление элемента
    def AddEl(self, key, data):
        self.head = self.insert(self.head, key, data)

    def insert(self, root, key, data):
        if root is None:
            return node(key, data, None, None)
        elif key < root.key:
            root.left = self.insert(root.left, key, data)
        elif key > root.key:
            root.right = self.insert(root.right, key, data)
        else:
            raise ValueError("Значению '" + data + "' нужно подобрать другой ключ, т.к. данный - " + str(
                key) + " - уже присутствует в дереве!")
        return self.rebalance(root)

    # удаление всех элементов
    def clear(self):
        if self.head is None:
            print("Сипсок и так уже пуст!")
        else:
            self.ClearTree(self.head)
            print("Список очищен.")

    def ClearTree(self, root):
        if root.left is not None:
            self.ClearTree(root.left)
        if root.right is not None:
            self.ClearTree(root.right)
        root.data = None
        root.key = None
        root.right = None
        root.left = None
        self.count -= 1

    # возвращает элемент по ключу
    def ElemetnPoinet(self, key):
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
            print("Значения с ключом - " + str(key) + " - нет в дереве!")
            return None

    # изменение значения по ключу
    def ChangeEl(self, key, data):
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
            tmp_node.data = data
        else:
            print("Значения с ключом - " + str(key) + " - нет в дереве!")

    # возвращает количество элементов в дереве
    def Size(self):
        print("Элементов в дереве: " + str(self.count))

    