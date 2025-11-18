import sys

# Increase recursion depth just in case
sys.setrecursionlimit(3000)

def is_prime(n):
    """Basic trial division to check primality."""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    # Check divisibility up to square root
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def has_unique_digits(s):
    """Checks if digits in the string are unique."""
    # A string longer than 10 MUST have repeating digits (0-9)
    if len(s) > 10: return False
    # Compare length of string vs length of set of characters
    return len(set(s)) == len(s)

def solve_recursive(s):
    """
    Finds minimum pieces for string 's'.
    Returns float('inf') if impossible.
    """
    # Base Case: Empty string requires 0 pieces
    if not s:
        return 0
    
    min_pieces = float('inf')
    
    # Try cutting a prefix of length 1 up to length 10 (or length of s)
    max_len = min(len(s), 10)
    
    for length in range(1, max_len + 1):
        chunk = s[:length]
        remainder = s[length:]
        
        # 1. Check if the chunk has unique digits
        if has_unique_digits(chunk):
            # 2. Check if the chunk is prime
            if is_prime(int(chunk)):
                # 3. Recursive Step: Solve for the rest
                res_remainder = solve_recursive(remainder)
                
                # If a solution exists for the remainder
                if res_remainder != float('inf'):
                    total = 1 + res_remainder
                    # Keep the minimum result found so far
                    if total < min_pieces:
                        min_pieces = total
                        
    return min_pieces

def main():
    # Robust input reading
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    s = input_data[0]
    n = len(s)
    
    global_min = float('inf')

    # The problem requires AT LEAST 2 pieces.
    # We cannot just call solve_recursive(s) because it might return 1 
    # (if the whole string is a valid prime).
    # We must manually iterate the FIRST cut to ensure splitting happens.
    
    first_cut_limit = min(n, 10)
    
    for length in range(1, first_cut_limit + 1):
        # Ensure we don't take the whole string as one piece (must be at least 2)
        if length == n:
            continue
            
        first_chunk = s[:length]
        rest_of_string = s[length:]
        
        if has_unique_digits(first_chunk):
            if is_prime(int(first_chunk)):
                # Call recursion for the second part onwards
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
    main()
