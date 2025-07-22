# See program.txt for code analysis

a = 12
b = a
b -= 1

while True:
    d = a
    a = 0
    c = b
    a += c * d

    b -= 1
    c = b
    d = c

    c += d

    if -16 <= c <= 9:
        print(f"Toggle instruction {c}")

    # changes main loop in line 39
    if c == 2:
        break

print()
print("Registers after main loop", a, b, c, d)

# Toggled instructions

# jnz 1 c       -> cpy 1 c
# cpy 71 c
# jnz 72 d      -> cpy 72 d
# inc a
# inc d         -> dec d
# jnz d -2
# inc c         -> dec c
# jnz c -5

# pseudo code
# c = 1
# c = 71
# do
#     d = 72
#     do
#         a += 1
#         d -= 1
#     while d != 0

#     c -= 1
# while c != 0

# In python
# c = 1
# c = 71
# while True:
#     d = 72
#     while True:
#         a += 1
#         d -= 1
#         if d == 0: break

#     c -= 1
#     if c == 0: break

# or simple
a += 72 * 71


print()
print("Registers at the end", a, b, c, d)
print(f"{a=}")
