def check_numb():
    num = int(input("Enter a number: "))
    if num > 7:
        print("Hello")


def check_nam():
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")


def filt_for_multiples():
    arr = input("You should enter the array elements separated by spaces: ").split()
    arr = [int(x) for x in arr]
    output = []
    for n in arr:
        if n % 3 == 0:
            output.append(n)
    if len(output) > 0:
        print("Multiples of 3:", output)
    else:
        print("No multiples of 3")


print("\n--- Menu ---")
print("1. Check number > 7")
print("2. Check name")
print("3. Filter multiples of 3")
print("4. Exit")

while True:
    choice = input("Choose (1-4): ")

    if choice == "1":
        check_numb()
    elif choice == "2":
        check_nam()
    elif choice == "3":
        filt_for_multiples()
    elif choice == "4":
        print("Bye, thanks!")
        break
    else:
        print("Wrong option")
