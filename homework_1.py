# create 3 int variables. Division result is always a float. Use // to avoid
int_1 = 750
int_2 = int_1 + 60
int_3 = int_2 // 2

# print int variables values
print("line_1=", int_1)
print("line-2=", int_2)
print("line_3=", int_3)

# create 3 float variables
float_1 = 14.2
float_2 = 75.12
float_3 = 11.31

# print 3 float variables values
print(float_1)
print(float_2)
print(float_3)

# The first int variable: should equal to the sum of the second and the third
int_1 = int_2 + int_3
print("sum=", int_1)

# subtract 100 from the second int variable
int_2 -= 100
print("second variable", int_2)

# increment (add 1) third int variable
int_3 += 1
print("third variable", int_3)

# make first float negative
print(-float_1)

# second float should be equal to the twice the value of the third variable, minus the value of the first
float_2 = float_3 * 2 - float_1
print("line_2=", "(line_2*2-line_1=)", float_2)

# divide third float value by 3
print("line_3/3=", float_3 / 3)
