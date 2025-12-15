

kwadrat = tuple[int,int,int,int]

def czypok(k1:kwadrat, k2:kwadrat) -> bool:

    if k1[1] <= k2[0] or k1[0] >= k2[1]: return False
    if k1[3] <= k2[2] or k1[2] >= k2[3]: return False
    return True

def are(k: kwadrat) -> int:
    return (k[1] - k[0]) * (k[3] - k[2])


def solv(T:list[kwadrat], zebrane:list[kwadrat]=[], idx:int=0, pole:int=2012) -> bool:
    if len(zebrane) == 13 and pole == 0:
        return True
    if (idx == len(T) or len(zebrane) > 13 or pole < 0):
        return False

    if not any(czypok(T[idx], kwadrat) for kwadrat in zebrane):
        return solv(T, zebrane + [T[idx]], idx+1, pole-are(T[idx]))
    return solv(T, zebrane, idx + 1, pole)




