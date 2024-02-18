def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)

def solve_diophantine(a, b, c):
    gcd, x0, y0 = extended_gcd(a, b)
    
    if c % gcd != 0:
        return "Não tem solução inteira."
    
    else:
        # Encontrar uma solução particular
        x0 *= c // gcd
        y0 *= c // gcd
        return (x0, y0)

# Exemplo de uso
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

solution = solve_diophantine(a, b, c)
print("Solução para a equação {}x + {}y = {}: x = {}, y = {}".format(a, b, c, solution[0], solution[1]))