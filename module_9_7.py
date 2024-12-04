def is_prime (funk):
    def wrapper (*args):
        result = funk (*args)
        sum1 = sum (args)
        k = 0
        for i in range(2, sum1 // 2 + 1):
            if sum1 % i == 0:
                k = k + 1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

