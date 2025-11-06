# Program wyznaczajacy ostatnia niezerowa cyfre liczby N!
# Nmax = 10^100


# rozw naiwne O( N! )
#n = int(input(":"))
'''
n = 12012
k = 1
for i in range(2,n+1):
    k *= i
    if k % 10 == 0:
        k = k // 10
print(k%10)
'''

def T_N_mod_5(last_digit):
    if last_digit == 0:
        return 1
    elif last_digit == 1:
        return 1
    elif last_digit == 2:
        return 2
    elif last_digit == 3:
        return 1
    elif last_digit == 4:
        return 4
    elif last_digit == 5:
        return 4
    elif last_digit == 6:
        return 4
    elif last_digit == 7:
        return 3
    elif last_digit == 8:
        return 4
    else: # elif last_digit == 9:
        return 1


def D(n):
    # base case
    if n == 0 or n == 1:
        return 1
    m = n // 5
    d_m = D(m)
    last_digit = n % 10
    T_N_mod = T_N_mod_5(last_digit)
    m_mod_4 = ((n % 100)) // 5 % 4
    inv_2_m_mod_5 = pow(3, m_mod_4, 5)

    D_N_mod_5 = (T_N_mod * d_m * inv_2_m_mod_5) % 5
    if D_N_mod_5 == 0:
        return 6
    return (D_N_mod_5 * 6) % 10

# O(log2 n)
N = int(input("N: "))
last_digit = D(N)

print(f"Ostatnia niezerowa cyfra {N}! to: {last_digit}")