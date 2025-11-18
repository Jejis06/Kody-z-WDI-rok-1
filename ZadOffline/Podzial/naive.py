import sys
import time

# 1. Helper function to check if a number is prime
def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# 2. Helper function to check if digits are unique
def has_unique_digits(s):
    # A string longer than 10 must have repeating digits (0-9)
    if len(s) > 10: return False
    return len(set(s)) == len(s)

# 3. Recursive function to find minimum pieces for the remaining string
def solve_recursive(s):
    # Base case: If string is empty, we need 0 more pieces
    if not s:
        return 0
    
    # Initialize best result for this substring to Infinity
    min_pieces = float('inf')
    
    # Try cutting chunks of length 1 to 10 (or length of s)
    # We stop at 10 because digits must be unique
    max_len = min(len(s), 10)
    
    for length in range(1, max_len + 1):
        chunk = s[:length]
        
        # Check validity
        if has_unique_digits(chunk):
            number = int(chunk)
            if is_prime(number):
                # Recursive step: solve for the rest of the string
                remaining_result = solve_recursive(s[length:])
                
                # If the rest of the string returned a valid result
                if remaining_result != float('inf'):
                    current_total = 1 + remaining_result
                    if current_total < min_pieces:
                        min_pieces = current_total
                        
    return min_pieces

def main():
    # Read input from standard input
    try:
        # Using sys.stdin.read to safely handle input
        input_str = sys.stdin.read().split()
        if not input_str: return
        s = input_str[0]
    except ValueError:
        return

    n = len(s)
    global_min = float('inf')

    # The problem requires AT LEAST 2 pieces.
    # We cannot just call solve_recursive(s) because it might return 1 
    # (if the whole string is a valid prime).
    # Instead, we manually iterate through the first cut.
    
    first_cut_max_len = min(n, 10)
    
    for length in range(1, first_cut_max_len + 1):
        # This ensures we leave at least 1 character for the second piece
        if length == n: 
            continue
            
        first_chunk = s[:length]
        
        if has_unique_digits(first_chunk):
            if is_prime(int(first_chunk)):
                # Solve for the rest of the string
                rest_of_string = s[length:]
                res = solve_recursive(rest_of_string)
                
                if res != float('inf'):
                    total = 1 + res
                    if total < global_min:
                        global_min = total

    if global_min == float('inf'):
        print("BRAK")
    else:
        print(global_min)

if __name__ == "__main__":
    # Increase recursion depth just in case, though backtracking 
    # on N=99 without memoization is very slow regardless.
    sys.setrecursionlimit(2000)
    main()
