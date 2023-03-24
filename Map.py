# Определение класса узла дерева с атрибутами key (ключ), data (данные),
# left (левый дочерний узел) и right (правый дочерний узел)
class node:
    def __init__(self, key, data, left=None, right=None):
        self.key = key  # установка ключа узла
        self.data = data  # установка данных узла
        self.left = left  # установка левого дочернего узла
        self.right = right  # установка правого дочернего узла
        self.height = 0  # инициализация высоты узла

# Определение класса карты, использующей дерево
class Map:
    def __init__(self):
        # Инициализация пустой карты
        self.head = None  # установка головного узла в None
        self.count = 0  # установка счетчика узлов в 0

    # Обновление высоты узла
    def updateHeight(self, n):
        # Высота узла - это 1 плюс максимальная высота его левого и правого дочерних узлов
        n.height = 1 + max(self.height(n.left), self.height(n.right))

    # Получение высоты узла
    def height(self, n):
        # Высота узла - это 1 плюс максимальная высота его левого и правого дочерних узлов
        return -1 if n is None else n.height

    # Получение баланса узла
    def getBalance(self, n):
        # Баланс узла - это разность высоты его правого и левого дочерних узлов
        return 0 if n is None else self.height(n.right) - self.height(n.left)

    # Поворот вправо
    def rotateRight(self, y):
        x = y.left  # определение левого дочернего узла y
        z = x.right  # определение правого дочернего узла x
        x.right = y  # смена y на x в качестве правого дочернего узла
        y.left = z  # смена z на y в качестве левого дочернего узла
        self.updateHeight(y)  # обновление высоты y
        self.updateHeight(x)  # обновление высоты x
        return x  # возвращение нового корня поддерева
    
    # Поворот влево
    def rotateLeft(self, y):
        x = y.right # определение правого дочернего узла у
        z = x.left # определение левого дочернего узла х
        x.left = y # смена х на у в качестве левого дочернего элемента
        y.right = z # смена у на z в качестве правого дочернего узла
        self.updateHeight(y) # обновление высоты у
        self.updateHeight(x) # обновление высоты х
        return x # возвращение нового корня поддерева
    
    # метод перебалансировки дерева, принимает узел z
    def rebalance(self, z):
        self.updateHeight(z)  # обновление высоты узла
        balance = self.getBalance(z)  # расчет баланса узла
        if balance > 1: # если баланс больше 1
            if self.height(z.right.right) > self.height(z.right.left): # если высота правого поддерева правой ветви больше высоты левого поддерева правой ветви
                z = self.rotateLeft(z)  # поворот влево
            else:
                z.right = self.rotateRight(z.right)  # поворот вправо для правой ветви
                z = self.rotateLeft(z)  # поворот влево
        elif balance < -1: # если баланс меньше -1
            if self.height(z.left.left) > self.height(z.left.right): # если высота левого поддерева левой ветви больше высоты правого поддерева левой ветви
                z = self.rotateRight(z)  # поворот вправо
            else:
                z.left = self.rotateLeft(z.left)  # поворот влево для левой ветви
                z = self.rotateRight(z)  # поворот вправо
        return z


    def AddEl(self, key, data): # метод добавления элемента в дерево, принимает ключ и данные
        self.head = self.insert(self.head, key, data)

    def insert(self, root, key, data): # метод вставки элемента в дерево, принимает узел, ключ и данные
        if root is None: # если корень не существует, создается новый
            return node(key, data, None, None)
            #рекурсивный метод для поиска местарасположения узла в дереве 
        elif key < root.key: # если ключ меньше значения корневого узла
            root.left = self.insert(root.left, key, data) # переход к левому поддереву 
        elif key > root.key: # если ключ больше значения корневого узла 
            root.right = self.insert(root.right, key, data) # переход к правому поддереву 
        else:
            # если ключ уже существует, выбрасывается ошибка
            raise ValueError("Значению '" + data + "' нужно подобрать другой ключ, т.к. данный - " + str(
                key) + " - уже присутствует в дереве!")
        return self.rebalance(root)  # возвращается перебалансированное дерево


    def clear(self):
        # метод очистки дерева
        if self.head is None:
            print("Список и так уже пуст!")
        else:
            self.ClearTree(self.head)  # рекурсивный метод очистки дерева
            print("Список очищен.")

    def ClearTree(self, root):  # объявление метода ClearTree
        if root.left is not None:  # если у узла есть левый потомок, рекурсивно вызываем ClearTree от него
            self.ClearTree(root.left)
        if root.right is not None:  # если у узла есть правый потомок, рекурсивно вызываем ClearTree от него
            self.ClearTree(root.right)
        root.data = None  # очищаем значение данных узла
        root.key = None  # очищаем ключ узла
        root.right = None  # удаляем ссылку на правого потомка
        root.left = None  # удаляем ссылку на левого потомка
        self.count -= 1  # уменьшаем количество элементов в дереве на 1

    def ElementPoinet(self, key):  # объявление метода ElemetnPoinet
        tmp_node = self.head  # начинаем поиск с корня
        marker = True
        while marker:  # пока не найден нужный узел
            if key < tmp_node.key and tmp_node.left is not None:  # если ключ меньше ключа текущего узла и у текущего узла есть левый потомок, переходим к левому потомку
                tmp_node = tmp_node.left
            elif key > tmp_node.key and tmp_node.right is not None:  # если ключ больше ключа текущего узла и у текущего узла есть правый потомок, переходим к правому потомку
                tmp_node = tmp_node.right
            else:  # если у узла нет соответствующего потомка, завершаем цикл
                marker = False
        if key == tmp_node.key:  # если нашли узел с заданным ключом, возвращаем его
            return tmp_node
        else:  # если узел с заданным ключом не найден, выводим сообщение об ошибке и возвращаем None
            print("Значения с ключом - " + str(key) + " - нет в дереве!")
            return None

    def ChangeEl(self, key, data):  # объявление метода изменения значения элемента по ключу
        tmp_node = self.head  # инициализация временной переменной tmp_node, равной корню дерева
        marker = True  # установка маркера в значение True
        while marker:  # цикл, пока маркер равен True
            if key < tmp_node.key and tmp_node.left is not None:  # если ключ меньше ключа текущего узла и у узла есть левый потомок
                tmp_node = tmp_node.left  # переход к левому потомку
            elif key > tmp_node.key and tmp_node.right is not None:  # если ключ больше ключа текущего узла и у узла есть правый потомок
                tmp_node = tmp_node.right  # переход к правому потомку
            else:  # в противном случае
                marker = False  # установка маркера в значение False
        if key == tmp_node.key:  # если ключ совпадает с ключом найденного узла
            tmp_node.data = data  # изменение значения узла на переданное значение data
        else:  # в противном случае
            print("Значения с ключом - " + str(key) + " - нет в дереве!")  # вывод сообщения о том, что узла с переданным ключом в дереве нет

    def Size(self):  # объявление метода подсчета количества элементов в дереве
        print("Элементов в дереве: " + str(self.count))  # вывод количества элементов в дереве

    