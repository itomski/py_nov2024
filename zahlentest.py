zahl = 0b100101
print(zahl)

a = 10
b = 3
print(a % b)
print(a // b)
print(a ** b)

print()

# a: 00001010
# b: 00000011
# &: 00000010
print(a & b)

# a: 00001010
# b: 00000011
# |: 00001011
print(a | b)

# a: 00001010
# b: 00000011
# ^: 00001001
print(a ^ b)

# Nur mit Variablen möglich
#print(7 += 1) # 7 = 7 + 1
#print(7++) # 7 = 7 + 1
a += 1
(a := a + 1)
print(a)