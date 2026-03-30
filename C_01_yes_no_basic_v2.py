# functions go here

def  yes_no(question):

    # check user response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response =input(question).lower()

        if response == "yes" or response == ("y"):
            return "yes"
        elif response == "no" or response == ("n"):
            return "no"
        else:
            print("please enter yes / no")

# Main routine

#Testing loop. . .

while True:
    want_instructions = yes_no("Do you want instructions vro? ")
    print(f"you choose {want_instructions}")


print("we done bro")
