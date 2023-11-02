from adt.trees.binary_tree import BinaryTree
from adt.trees.traversal import *
from adt.trees.binary_search_tree import BinarySearchTree
from adt.trees.exceptions import DuplicateKeyException
from colegio import Estudiante
if __name__ == '__main__':
    """tree = BinaryTree()
    tree.append(5)
    tree.append(7)
    tree.append(3)
    tree.append(2)
    tree.append(1)
    tree.append(4)
    tree.append(6)
    tree.append(8)
    tree.append(9)
    tree.append(10)
    print("search " + str(tree.search(1)))
    print("inodes " + str(tree.inodes()))
    print("height " + str(tree.height()))
    preorder(tree)
    preorder_str(tree)
    print("")
    inorder_str(tree)
    print("")
    postorder_str(tree)
    leaves contar las hojas
    def leaves(self)
    def inodes(self)cuenta nodos internos
    def height(self)
    def preorder_str(tree)generar 5
    5
    7
    3
    2
    def inorder _str
    def postorder _str"""

    tree = BinarySearchTree()
    try:
        """tree.append(10)
        tree.append(5)
        tree.append(15)
        tree.append(12)
        tree.append(5)"""
        tree.append(Estudiante(123, "Juan",4.5))
        tree.append(Estudiante(456, "Pedro",4.5))
        tree.append(Estudiante(789, "Maria",4.5))
        #tree.append(Estudiante(456, "Pedro",5.0))
    except DuplicateKeyException as e:
        print(e.args[0])

    preorder(tree)
    print("search " + str(tree.search(Estudiante(456, "Pedro",4.5))))
