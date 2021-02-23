print("Enter first number")
num1 = int(input())
print("Enter second number")
num2 = int(input())
print("What you want to be?\n"
      "type 1 for +\n"
      "type 2 for *\n"
      "type 3 for /\n")
func = int(input())
if num1 == 45 and num2 == 3 and func == 2:
    print("Your answer is 555")
elif num1 == 56 and num2 == 9 and func == 1:
    print("Your answer is 77")
elif num1 == 56 and num2 == 6 and func == 3:
    print("Your answer is 4")
elif func == 1:
    print("Your answer is\n", int(num1)+int(num2))
elif func == 2:
    print("Your answer is\n", int(num1)*int(num2))
elif func == 3:
    print("Your answer is\n", float(int(num1)/int(num2)))
else:
    print("Some error occurred")