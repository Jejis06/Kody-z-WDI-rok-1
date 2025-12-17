import sys
Vowels = set(['A', 'E', 'I', 'O', 'U', 'Y'])

def is_vowel(char):
    return char in Vowels

def add(a, b) -> str:
    type_a = is_vowel(a)
    type_b = is_vowel(b)

    if type_a and type_b:
        return min(a, b)
    elif not type_a and not type_b:
        return max(a, b)
    else:
        return a if type_a else b

def mult(a, b) -> str:
    type_a = is_vowel(a)
    type_b = is_vowel(b)

    if type_a and type_b:
        return max(a, b)
    elif not type_a and not type_b:
        return min(a, b)
    else:
        return a if not type_a else b

def pri(op: str) -> int:
    if op == '+':
        return 1
    elif op == '*':
        return 2
    return 0


def main() -> None:
    rownanie = sys.stdin.readline().strip()

    vals:list[str] = []
    ops:list[str] = []

    i = 0
    while i < len(rownanie):
        znak = rownanie[i]

        if znak.isalpha():
            vals.append(znak);
        elif znak == '(':
            ops.append(znak)
        elif znak == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                v1 = vals.pop()
                v2 = vals.pop()
                res = add(v1, v2) if op == '+' else mult(v1, v2)
                vals.append(res)
            ops.pop()
        elif znak in ['+', '*']:
            while (ops and ops[-1] != '(') and pri(ops[-1]) >= pri(znak):
                op = ops.pop()
                v1 = vals.pop()
                v2 = vals.pop()
                res = add(v1, v2) if op == '+' else mult(v1, v2)
                vals.append(res)
            ops.append(znak)
        i += 1
    while ops:
        op = ops.pop()
        v1 = vals.pop()
        v2 = vals.pop()
        res = add(v1, v2) if op == '+' else mult(v1, v2)
        vals.append(res)
    print(vals[0])
    return
if __name__ == '__main__':
    main()
