
def multi(a, b):
    return a * b

print(multi(10,15))

multi_l = lambda a,b : a * b

print(multi_l(10,15))

def get_multi_value(zahl):
    return lambda wert : wert * zahl;

dyn_func = get_multi_value(100)
print(dyn_func(5))
print(dyn_func(7))
print(dyn_func(15))
print(dyn_func(3))

dyn_func = get_multi_value(10)
print(dyn_func(5))
print(dyn_func(7))
print(dyn_func(15))
print(dyn_func(3))