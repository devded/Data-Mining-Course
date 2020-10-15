cups = int(input("Write how many cups of coffee you will need :"))

print("For {0} cups of coffee you will need:".format(cups))

water  = cups * 200
milk = cups * 50
coffee_bean = cups * 15

print("{0} ml of water".format(water))
print("{0} ml of milk" .format(milk))
print("{0} g of coffee beans".format(coffee_bean))