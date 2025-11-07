#import time


# input equations
eqs: list[tuple] = [() for _ in range(10)]

mapping = {}
used_digits = [False for _ in range(10)]
solutions = []

letters = []


def convert_to_num(substring: str) -> int:
    num: int = 0
    # l -> r
    for char in substring:
        num = num * 10 + mapping[char]
    return num

def check_equations() -> bool:
    for equation in eqs:
        if equation == (): break
        num1 = convert_to_num(equation[0])
        num2 = convert_to_num(equation[1])
        num3 = convert_to_num(equation[2])

        if num1 + num2 != num3:
            return False
    return True

# dont look if not needed
def still_possible() -> bool:
    global mapping, eqs

    for equation in eqs:
        if equation == (): break
        n1, n2, n3 = equation
        eq_letters = set(n1) | set(n2) | set(n3)

        all_mapped = True
        for letter in eq_letters:
            if letter not in mapping:
                all_mapped = False
                break

        if not all_mapped:
            continue

        num1 = convert_to_num(n1)
        num2 = convert_to_num(n2)
        num3 = convert_to_num(n3)

        if num1 + num2 != num3:
            return False
    return True


def solve(letter_index: int) -> None:
    global used_digits, solutions

    # Base case: all letters assigned
    if letter_index == len(letters):
        if check_equations():
            solution = ""
            for letter in letters:
                solution += str(mapping[letter])
            solutions.append(solution)
        return

    curr_letter = letters[letter_index]
    for num in range(1, 10):
        if not used_digits[num]:
            mapping[curr_letter] = num
            used_digits[num] = True

            if still_possible():
                solve(letter_index + 1)

            # backtracking
            used_digits[num] = False
            del mapping[curr_letter]


def main():
    global letters, solutions

    N: int = int(input())
    letters = set()

    for i in range(N):
        line_raw = input()

        line_prep = line_raw.split('+')
        rhs = line_prep[1].split('=')

        lhs = line_prep[0], rhs[0]
        rhs = rhs[1]

        eqs[i] = (*lhs, rhs)
        letters.update(*eqs[i])

    letters = sorted(list(letters))

    solve(0)
    solution = list(set(solutions))
    if len(solution) == 1:
       print(*solution)
    else:
        print("BRAK")
    return

if __name__ == "__main__":
    #t1 = time.time()
    main()
    #t2 = time.time()
    #print("TIME:", f"{t2 - t1}s")





