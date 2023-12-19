# Fatorial

print('\n\t\t\t -- Fatorial -- \n')

def fatorial(n):
    fat = 1
    for i in  range(1, n+1):
        fat *= i
    return fat

# teste Fatorial
print(f'\n {8}! = {fatorial(8)}')
