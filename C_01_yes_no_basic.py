

while True:

# check if user says yes / no

    want_instructions =input("Do you want instructions vro? ").lower()

    if want_instructions == "yes" or want_instructions == ("y"):
        print("You said yes bro")
        break
    elif want_instructions == "no" or want_instructions == ("n"):
        print("you said no bro")
        break
    else:
        print("please enter yes / no")
        continue
print("we done bro")