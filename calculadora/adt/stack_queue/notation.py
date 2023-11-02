from adt.lists.sll import SinglyLinkedList
from adt.stack_queue.stack import Stack


class Prefix:
    def __init__(self, infix_expression):
        self.infix_expression = infix_expression

    def infix(self):
        while " " in self.infix_expression:
            self.infix_expression = self.infix_expression.replace(" ", "")

        string = self.infix_expression
        self.infix_expression = ""
        for i in string:
            self.infix_expression += i + " "
        self.infix_expression = self.infix_expression[
            : len(self.infix_expression) - 1
        ]

        return self.infix_expression

    def prefix(self):
        precedencia = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, ")": 4}
        numeros_pila = Stack()

        infija = self.infix()
        if not infija:
            return

        infija = self.__voltear(infija)
        elementos_infija = self.__separar(infija)
        elementos_prefija = SinglyLinkedList()

        for i in elementos_infija:
            if self.__es_real(i):
                elementos_prefija.append(i)
            elif i == "(":
                top = numeros_pila.pop()
                while top != ")" and not numeros_pila.is_empty():
                    elementos_prefija.append(top)
                    top = numeros_pila.pop()
            elif i in precedencia:
                if numeros_pila.is_empty():
                    numeros_pila.push(i)
                else:
                    cima = numeros_pila.peek()
                    if precedencia[i] >= precedencia[cima] or cima == ")":
                        if i == cima == "^":
                            elementos_prefija.append(i)
                        else:
                            numeros_pila.push(i)
                    else:
                        while not numeros_pila.is_empty():
                            cima = numeros_pila.peek()
                            if precedencia[cima] > precedencia[i] and cima != ")":
                                elementos_prefija.append(numeros_pila.pop())
                            else:
                                break
                        numeros_pila.push(i)

        while not numeros_pila.is_empty():
            elementos_prefija.append(numeros_pila.pop())

        prefija = ""
        for i in elementos_prefija:
            prefija += str(i) + " "

        prefija = prefija[: len(prefija) - 1]
        prefija = self.__voltear(prefija)

        return prefija

    def __es_real(self, string: str) -> bool:
        try:
            float(string)
            return True
        except:
            pass
        return False

    def __voltear(self, expression: str) -> str:
        expression = self.__separar(expression)
        stack = Stack()
        for i in expression:
            stack.push(i)

        expression = ""
        while not stack.is_empty():
            expression += stack.pop() + " "

        return expression[: len(expression) - 1]

    def __separar(self, string):
        splited_list = SinglyLinkedList()
        while " " in string:
            index = string.find(" ")
            splited_list.append(string[:index])
            string = string[index + 1 :]
        splited_list.append(string)
        return splited_list

    def arithmetic_expression_evaluation(self):
        result = None

        prefija = self.prefix()

        if prefija:
            prefija = self.__voltear(prefija)
            elementos_prefija = self.__separar(prefija)
            operands_stack = Stack()

            for i in elementos_prefija:
                if self.__es_real(i):
                    operands_stack.push(i)
                elif i in "+-*/^":
                    a = operands_stack.pop()
                    b = operands_stack.pop()
                    result = self.__calcular(i, float(a), float(b))
                    operands_stack.push(str(result))
            return result

    def __calcular(self, op, a, b):
        if op == '^':
            return a ** b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '+':
            return a + b
        elif op == '-':
            return a - b
        else:
            return None
