def power_func(p):
    def power(num):
        return num ** p
    return power

num = power_func(2)
print(num(5))