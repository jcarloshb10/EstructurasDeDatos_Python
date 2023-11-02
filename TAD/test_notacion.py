#!/usr/bin/env python
from ed.secuenciales.notacionpostfija import Postfija

if __name__ == '__main__':
    exp = "   (   12  -    8 )  +(2^3)^  3 + 7     "
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")  

    exp = "12 + (3 - 1) * 85 / (58 - 9)"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "1 + 2 * 3 + 4"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "(1 + 2) * (3 + 4)"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "(7 + 6) - 2 ^ (3 - 1) + 33"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "0/1"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "1/1"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "(((5   +9)* 2) + (6 *5))"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "(     2 + ( 3 *4))"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")

    exp = "((2+   3)*   4)"
    obj = Postfija(exp)
    print(obj.infija())
    print(obj.postfija())
    print(obj.eval_expr_aritm())
    print("\n")



