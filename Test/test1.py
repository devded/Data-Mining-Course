water = 400
milk = 540
beans = 120
cups = 9
money = 550



def remaining_action(water, milk, beans, cups, money):
    print("")
    print("The coffee machine has: ")
    print("{0} of water".format(water))
    print("{0} of milk".format(milk))
    print("{0} of coffee beans".format(beans))
    print("{0} of disposable cups".format(cups))
    print("{0} of money".format(money))
    print("")

    choose_action()

def fill_action():
    global water, milk, beans, cups, money
    
    fill_water = int(input("Write how many ml of water do you want to add: "))
    fill_milk = int(input("Write how many ml of milk do you want to add: "))
    fill_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    water += fill_water
    milk += fill_milk
    beans += fill_beans
    cups += fill_cups

    choose_action()

def take_action():
    global money
    print('I gave you {0}'.format(money))
    money = 0
    print("")

    choose_action()

def buy_action():
    buy_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    if buy_option == "1":
        check_buy(250, 0, 16, 4)
    elif buy_option == "2":
        check_buy(350, 75, 20, 7)
    elif buy_option == "3":
        check_buy(200, 100, 12, 6)
    
    choose_action()


def check_buy(need_water, need_milk, need_beans, cost):
        global water, milk, beans, cups, money
        if water > need_water:
            if milk > need_milk:
                if beans > need_beans:
                    if cups > 1:
                        water -= need_water
                        beans -= need_beans
                        milk -= need_milk
                        cups -= 1
                        money += cost
                        print("I have enough resources, making you a coffee!")
                    else:
                        print("Sorry, not enough Cup!")
                else:
                    print("Sorry, not enough Beans!")
            else:
                print("Sorry, not enough Milk!")
        else:
            print("Sorry, not enough water!")




def exit_action():
    exit()





def choose_action():
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        print("Buy Function")
        buy_action()
    elif action == "fill":
        print("Fill Function")
        fill_action()
    elif action == "take":
        print("Take Function")
        take_action()
    elif action == "remaining":
        print("Remaining Function")
        remaining_action(water, milk, beans, cups, money)
    elif action == "exit":
        print("exit Function")
        exit_action()

choose_action()