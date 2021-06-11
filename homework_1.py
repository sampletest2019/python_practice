from selenium import webdriver
import time

line_1 = 750
line_2 = line_1 + 60
line_3 = line_2 // 2

print("line_1=", line_1)
print("line-2=", line_2)
print("line_3=", line_3)

float_1 = 14.2
float_2 = 75.12
float_3 = 11.31

print(float_1)
print(float_2)
print(float_3)

# The first variable: should equal to the sum of the second and the third
line_1 = line_2 + line_3
print("sum=", line_1)
line_2 -= 100
print("second variable", line_2)
line_3 += 1
print("third variable", line_3)

print(-float_1)

# negate the value
print("negate_the_value=", line_3 - line_1)

# The second variable: should be reduced by 100
print("reduced_by_100=", line_2 - 100)
# should equal to the twice the value of the third variable, minus the value of the first
float_2 = float_3 * 2 - float_1
print("line_2=", "(line_2*2-line_1=)", float_2)

# The third variable: increment its value (means “add 1”)
print("increment_its_value=", line_3 + 1)
# divide its value by 31
print("line_3/3=", float_3 / 3)
