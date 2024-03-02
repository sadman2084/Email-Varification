email = input("Enter the email: ")
k, j, l = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        l = 1
                if k == 0 and j == 0 and l == 0:
                    print("Correct email")
            else:
                print("wrong input")
        else:
            print("wrong input")
    else:
        print("wrong input")
else:
    print("wrong input")

if k == 1:
    print("Space is not allowed!")
if j == 1:
    print("Uppercase letter is not allowed!")
if l == 1:
    print("Special characters are not allowed!")
