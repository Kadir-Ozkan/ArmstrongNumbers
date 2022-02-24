number = input("Enter a number to learn if it is an Armstrong number:").strip()
basamak = len(number)
Armstrong = 0
i = 0
while i < basamak:
    if number[i] not in "1234567890" and number[i] in (".", "-", ","):
        print("Please enter a positive number in  digits!")
        break
    else:
        Armstrong += int(number[i]) ** len(number)
        print(Armstrong, end=",")
    i += 1
if Armstrong == int(number):
    print("You've just entered an Artmstrong number")
else:
    print("Sorry this is not an Armstrong number")
