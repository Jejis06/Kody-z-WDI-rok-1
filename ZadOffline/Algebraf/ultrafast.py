import sys


class AlgebrafSolver:
    def __init__(self):
        self.coeffs = []
        self.eq_completers = []
        self.num_letters = 0
        self.solution_count = 0
        self.final_solution = None
        self.used_digits = [False] * 10
        self.sorted_letters = []
        self.letter_to_idx = {}
        self.mapping_res = {}

    def run(self):
        try:
            input_data = sys.stdin.read().split()
        except Exception:
            return

        if not input_data:
            return

        iterator = iter(input_data)
        try:
            N = int(next(iterator))
        except StopIteration:
            return

        raw_eqs = []
        for _ in range(N):
            raw_eqs.append(next(iterator))

        unique_chars = set()
        for eq in raw_eqs:
            for char in eq:
                if 'A' <= char <= 'Z':
                    unique_chars.add(char)
        
        self.sorted_letters = sorted(list(unique_chars))
        self.num_letters = len(self.sorted_letters)
        self.letter_to_idx = {char: i for i, char in enumerate(self.sorted_letters)}
        self.mapping_res = [0] * self.num_letters

        self.coeffs = [[0] * self.num_letters for _ in range(N)]
        self.eq_completers = [-1] * N

        for i, eq in enumerate(raw_eqs):
            if '=' in eq:
                lhs_part, rhs_part = eq.split('=')
            else:
                continue

            def add_term(term_str, sign):
                power = 1
                for char in reversed(term_str):
                    idx = self.letter_to_idx[char]
                    self.coeffs[i][idx] += sign * power
                    if idx > self.eq_completers[i]:
                        self.eq_completers[i] = idx
                    power *= 10

            for term in lhs_part.split('+'):
                add_term(term, 1)
            
            for term in rhs_part.split('+'):
                add_term(term, -1)

        self.solve_recursive(0, [0] * N)

        if self.solution_count == 1:
            print(self.final_solution)
        else:
            print("BRAK")

    def solve_recursive(self, idx, current_eq_sums):
        if self.solution_count > 1:
            return

        if idx == self.num_letters:
            if all(s == 0 for s in current_eq_sums):
                self.solution_count += 1
                self.final_solution = "".join(str(x) for x in self.mapping_res)
            return

        for digit in range(1, 10):
            if not self.used_digits[digit]:
                valid_move = True
                next_eq_sums = current_eq_sums[:]
                
                for eq_i in range(len(self.coeffs)):
                    weight = self.coeffs[eq_i][idx]
                    if weight != 0:
                        next_eq_sums[eq_i] += weight * digit
                    
                    if self.eq_completers[eq_i] == idx:
                        if next_eq_sums[eq_i] != 0:
                            valid_move = False
                            break
                
                if not valid_move:
                    continue

                self.used_digits[digit] = True
                self.mapping_res[idx] = digit
                
                self.solve_recursive(idx + 1, next_eq_sums)
                
                self.used_digits[digit] = False
                
                if self.solution_count > 1:
                    return

if __name__ == "__main__":
    solver = AlgebrafSolver()
    solver.run()
