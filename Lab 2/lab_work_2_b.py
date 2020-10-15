water = 400
milk = 540
beans = 120
cups = 9
money = 550


def coffee_machine_satus(water, milk, beans, cups, money):
    print("The coffee machine has: ")
    print("{0} of water".format(water))
    print("{0} of milk".format(milk))
    print("{0} of coffee beans".format(beans))
    print("{0} of disposable cups".format(cups))
    print("{0} of money".format(money))

coffee_machine_satus(water, milk, beans, cups, money)

action = input("Write action (buy, fill, take): ")


def action_fill():
    global water, milk, beans, cups, money

    fill_water = int(input("Write how many ml of water do you want to add: "))
    fill_milk = int(input("Write how many ml of milk do you want to add: "))
    fill_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    water += fill_water
    milk += fill_milk
    beans += fill_beans
    cups += fill_cups
    coffee_machine_satus(water, milk, beans, cups, money)
    


def action_take():
    global money
    print('I gave you {0}'.format(money))
    print("")
    money = 0
    coffee_machine_satus(water, milk, beans, cups, money)


def action_buy():
    global water, milk, beans, cups, money

    buy_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")

    if buy_option == "1":
        water -= 250
        beans -= 16
        money += 4

    elif buy_option == "2":
        water -= 350
        milk -= 75
        beans -= 20
        money += 7

    elif buy_option == "3":
        water -= 200
        milk -= 100
        beans -= 12
        money += 6

    coffee_machine_satus(water, milk, beans, cups, money)


def action_execution(action):
    if action == "buy":
        action_buy()
    elif action == "fill":
        action_fill()
    elif action == "take":
        action_take()

action_execution(action)
