from sympy import Rational, simplify


def harmonic_mean(lst):
    n = len(lst)
    sum = 0
    if n <= 0:
        return 0
    for x in lst:
        sum += Rational(1, x)
    return n/sum


def sqrt(x):
    y = 1
    prev = 0
    while 1 <= abs(y-prev):
        prev = y
        y = 1.0/2*(prev+x/prev)
    while (y+1)*(y+1) < x:
        y += 1
    return int(y)


def divisors(x):
    n = sqrt(x)
    lst = []
    for i in range(1, n+1):
        if x % i == 0:
            lst.append(i)
            if i != x/i:
                lst.append(int(x/i))
    lst.sort()
    return lst


def harmonic_divisor(n):
    lst = divisors(n)
    h = harmonic_mean(lst)
    return simplify(h).is_integer

# Test 1
print(harmonic_divisor(1))
# Test 2
print(harmonic_divisor(6))
# Test 3
print(harmonic_divisor(8))
# Test 4
print(harmonic_divisor(10))
# Test 5
print(harmonic_divisor(28))

