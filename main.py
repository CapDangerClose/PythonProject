print ("Select Operation")
print ("1.Area")
print("2.Perimeter")
print("\n")
print("-----------------")
print("\n")
choice = input ("Enter Choice(1/2):")
if choice == '1':
  num1 = int(input("Enter Width:"))
  num2 = int(input("Enter Height:"))
if choice == '1':
  print(num1, "*",num2,"=", num1 * num2)

if choice == '1':
  print("  -----------")
  print("|           |")
  print("|           |","Height:" , num2)
  print("|           |")
  print("|           |")
  print("  -----------")
  print("   Width:", num1)
  print("\n")
  print("--------------------")
  print("\n")
  print("Area=", num1*num2)

def add(num1, num2):
  return num1 + num2
def multiply(x, y):
  return x * y
if choice == '2':
  print("\n")
  print("You can calculate the perimeter of a square by adding up all four side.")
  print("\n")
  num3 = int(input("Enter first side:"))
  num4 = int(input("Enter second side:"))
  num5 = int(input("Enter your third side"))
  num6 = int(input("Enter your fourth side"))
  print("\n")
if choice == '2':
  print("         ",    num5)
  print("       -----------")
  print("      |           |")
  print(num6, "    |           |",num4)
  print("      |           |")
  print("      |           |")
  print("       -----------")
  print("          ",num3)
  print("Perimeter =", num3 + num4 + num5 + num6)