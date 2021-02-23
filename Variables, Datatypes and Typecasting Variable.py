# string variable
var1 = "Hello world"
var2 = "I am"
var3 = "Devraj Seth"

print(var1)
print(var2, var3)
print(type(var1))

# integer variable
var4 = 8
var5 = 4

print(var4+var5)
print(type(var4))
print(type(var4+var5))

# floating variable
var6 = 10.5
var7 = 5.2

#typecasting
var8 = "10"
var9 = "90"
print(int(var8)+int(var9))

print(5 * str(int(var8)+int(var9)))

print(5 * "here i type 5 times")
print(5 * "here i type 5 times\n")

#input function
print("Enter your number")
inp = input()
print("You enter", inp)
print("You enter", int(inp)+10)
