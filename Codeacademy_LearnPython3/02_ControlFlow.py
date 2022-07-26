

def item_3():
    print("Bool test")
    print((5 * 2) - 1 == 8 + 1)
    print(13 - 6 != (3 * 2) + 1)
    print(3 * (2 - 1) == 4 - 1)


def item_4():
    print("Bool function type")
    my_baby_bool = "true"
    print(type(my_baby_bool))
    my_baby_bool_two = True
    print(type(my_baby_bool_two))

def item_5():
    # Enter a user name here, make sure to make it a string
    user_name = "angela_catlady_87"
    if user_name == "Dave":
        print("Get off my computer Dave!")
    if user_name == "angela_catlady_87":
        print("I know it is you, Dave! Go away!")

def item_6():
    x = 20
    y = 20

    # Write the first if statement here:
    if x == y:
        print("These numbers are the same")

    credits = 120

    # Write the second if statement here:
    if credits >= 120:
        print("You have enough credits to graduate!")

def item_7():
    statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

    statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
    print(statement_one,statement_two)
    credits = 120
    gpa = 3.4

    if credits >= 120 and gpa >= 2.0:
        print("You meet the requirements to graduate!")

def main():
    functions_to_run =[item_3,item_4,item_5,item_6,item_7]
    for func in functions_to_run:
        print("Corriendo ", func.__name__)
        func()



if __name__ == "__main__":
    main()