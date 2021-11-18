# Imports the random library
import random

# Creates the variables and randomizes their value from 1 - 8
r = random.randint(1, 8)
a = random.randint(1, 8)
s = random.randint(1, 8)
x = random.randint(1, 8)
b = random.randint(1, 8)
t = random.randint(1, 8)
y = random.randint(1, 8)
u = random.randint(1, 8)

# Creates the conditions required for the if statement
r_cond = r != a + 1 and a - 1 and s + 1 and s - 1 and x + 1 and x - 1
a_cond = a != r + 1 and r - 1 and s + 1 and s - 1 and b + 1 and b - 1 and t + 1 and t - 1
s_cond = s != r + 1 and r - 1 and a + 1 and a - 1 and x + 1 and x - 1 and b + 1 and b - 1 and t + 1 and t - 1 and y + 1 and y - 1
x_cond = x != r + 1 and r - 1 and s + 1 and s - 1 and t + 1 and t - 1 and y + 1 and y - 1
b_cond = b != a + 1 and a - 1 and s + 1 and s - 1 and t + 1 and t - 1 and u + 1 and u - 1
t_cond = t != u + 1 and u - 1 and a + 1 and a - 1 and x + 1 and x - 1 and b + 1 and b - 1 and s + 1 and s - 1 and y + 1 and y - 1
y_cond = y != x + 1 and x - 1 and s + 1 and s - 1 and t + 1 and t - 1 and u + 1 and u - 1
u_cond = u != b + 1 and b - 1 and t + 1 and t - 1 and y + 1 and y - 1

# Creates the variable "true" so it can be changed to false
true = True

while true:

    # While the while statement is true, randomize the variables
    r = random.randint(1, 8)
    a = random.randint(1, 8)
    s = random.randint(1, 8)
    x = random.randint(1, 8)
    b = random.randint(1, 8)
    t = random.randint(1, 8)
    y = random.randint(1, 8)
    u = random.randint(1, 8)

    # Print the last value called
    print(r)
    print(a)
    print(s)
    print(x)
    print(b)
    print(t)
    print(y)
    print(u)

    if r_cond and a_cond and s_cond and x_cond and b_cond and t_cond and y_cond and u_cond and r > s is True:
        true = False
        print("Final answers:")
        print("r: " + str(r))
        print("a: " + str(a))
        print("s: " + str(s))
        print("x: " + str(x))
        print("b: " + str(b))
        print("t: " + str(t))
        print("y: " + str(y))
        print("u: " + str(u))

    else:
        print("Calculating, please wait")
