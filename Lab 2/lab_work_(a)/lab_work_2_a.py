water = int(input('Write how many ml of water the coffee machine has:'))
milk = int(input('Write how many ml of milk the coffee machine has: '))
beans = int(input('Write how many grams of coffee beans the coffee machine has:'))
cups = int(input('Write how many cups of coffee you will need: '))


def calculation(water,milk,beans,cups):
  count_water = water // 220
  count_milk = milk // 50
  count_bean = beans // 15

  possible_cup_coffee = min(count_water,count_milk, count_bean)

  if possible_cup_coffee == cups:
    message = 'Yes, I can make that amount of coffee'
  
  elif possible_cup_coffee > cups:
    more = possible_cup_coffee - cups 
    message = "Yes, I can make that amount of coffee (and even {0} more than that)".format(more)
  
  if possible_cup_coffee < cups:
    message = 'No, I can make only {0} cups of coffee'. format(possible_cup_coffee)

  return message

print(calculation(water,milk,beans,cups))
