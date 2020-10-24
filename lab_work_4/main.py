class coffee_machine:
  water = 400
  milk = 540
  beans = 120
  cups = 9
  money = 550

  def __init__(self):
    pass  
    
  def remaining_action(self,water, milk, beans, cups, money):
    print("")
    print("The coffee machine has: ")
    print("{0} of water".format(water))
    print("{0} of milk".format(milk))
    print("{0} of coffee beans".format(beans))
    print("{0} of disposable cups".format(cups))
    print("${0} of money".format(money))
    print("")
    self.choose_action()

  def fill_action(self):
    self.fill_water = int(input("Write how many ml of water do you want to add: "))
    self.fill_milk = int(input("Write how many ml of milk do you want to add: "))
    self.fill_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    self.fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    self.water += self.fill_water
    self.milk += self.fill_milk
    self.beans += self.fill_beans
    self.cups += self.fill_cups
    print("")
    self.choose_action()


  def take_action(self):
    print('I gave you ${0}'.format(self.money))
    self.money = 0
    print("")
    self.choose_action()


  def buy_action(self):
    self.buy_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    if self.buy_option == "1":
        self.check_buy(250, 0, 16, 4)
    elif self.buy_option == "2":
        self.check_buy(350, 75, 20, 7)
    elif self.buy_option == "3":
        self.check_buy(200, 100, 12, 6)
    elif self.buy_option == "back":
        self.choose_action()

    
    print("")
    self.choose_action()

  def check_buy(self,need_water, need_milk, need_beans, cost):
        if self.water > need_water:
            if self.milk > need_milk:
                if self.beans > need_beans:
                    if self.cups > 1:
                        self.water -= need_water
                        self.beans -= need_beans
                        self.milk -= need_milk
                        self.cups -= 1
                        self.money += cost
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
    quit()
  
  def choose_action(self):
    self.action = input("Write action (buy, fill, take, remaining, exit): ")
    if self.action == "buy":
      #print("Buy")
      self.buy_action()
    elif self.action == "fill":
      #print("Fill")
      self.fill_action()
    elif self.action == "take":
      #print("Take")
      self.take_action()
    elif self.action == "remaining":
      #print("remaining")
      self.remaining_action(self.water, self.milk, self.beans, self.cups, self.money)
    elif self.action == "exit":
      #print("Exit")
      exit()
    



run = coffee_machine()
run.choose_action()
