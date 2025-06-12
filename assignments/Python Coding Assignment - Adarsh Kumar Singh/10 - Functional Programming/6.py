def add_x(x):
    def add_y(y):
        def add_z(z):
            return x+y+z
        return add_z
    return add_y

result_1 = add_x(5)
result_2 = result_1(4)
print(result_2(6))

print(add_x(2)(4)(5))