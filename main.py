# Isaac Kim

from Array import Array

array_A = Array(6)
array_B = Array(6)

for n in range(3):
    array_A[n] = n
    array_B[n] = n

str = ""

""" Very Simple Menu used to try different values when trying to change the values in Array A and B
    You can also change the value to None just as long as you pick the correct index. 
    The examples using the __eq__ operator will print when you close the menu. """
while True:
    str += (f"\nArray A: {array_A}") + "\n" + (f"Array B: {array_B}")
    str += ("\nEnter 1 to try and change an index in one of the arrays") + ("\nEnter q to quit and see comparison between"
                                                                          " arrays")
    print(str)
    option = input("Enter an option: ")

    if (option=='q'):
        break
    elif (option=='1'):
        opt = input("Enter 1 for array A or 2 for array B: ")
        index = int(input("Which index would you like to change? "))
        newval = input("Enter the new value: ")
        if (opt=='1'):
            try:
                if (newval=="None"):
                    array_A.__setitem__(index, None)
                else:
                    array_A.__setitem__(index,int(newval))
            except Exception:
                print("INDEX ERROR")
        elif (opt=='2'):
            try:
                if (newval=="None"):
                    array_B.__setitem__(index, None)
                else:
                    array_B.__setitem__(index, int(newval))
            except Exception:
                print("INDEX ERROR")

    str = ""


print(f"\nArray A logical size: {array_A.logical_size()}")
print(f"Array B logical size: {array_B.logical_size()}\n")
if (array_A==array_B):
    print("Using the __eq__ operator, Array A IS equal to Array B")
else:
    print("Using the __eq__ operator, Array A is NOT equal to Array B")





