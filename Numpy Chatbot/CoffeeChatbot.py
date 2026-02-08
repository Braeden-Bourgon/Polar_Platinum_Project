# Define your functions
def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  style = get_drink_style()
  cup = get_cup()
  drinks = []
  print(f"Alright, that's a size {size} {drink_type} {style} in {cup}", f"and {drinks}", "!")
  additional_drink = input("Would you like something else?")
  name = input("And can I get your name?")
  print(f"Thanks, {name}! Your drink will be ready shortly.")
  return

def get_size():
  orderCode = {"a": "Small", "b": "Medium", "c": "Large"}
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ').replace(" ", '')
  size = ""
  for code in orderCode.keys():
    if code == res:
        size = code
    continue 
  if size:
    print(orderCode.get(size)) 
    return orderCode.get(size)
  else:
    print("That is not a flavor please try again: ")
    return get_size() 

def get_drink_type():
  orderCode = {"a": "Brewed Coffee", "b": "Mocha", "c": "Latte"}
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ').replace(" ", '')
  drink_type = ""
  for code in orderCode.keys():
    if code == res:
      drink_type = code
    continue 
  if drink_type: 
    print(orderCode.get(drink_type))
    if orderCode.get(drink_type) == "Latte":
        milk = order_latte()
        return (f"{milk} {orderCode.get(drink_type)}")
    return orderCode.get(drink_type)

  else: 
    print("That is not a type of coffee. Please try again: ")
    return get_drink_type()
  
def get_drink_style(): 
   res = input('Would you like it hot or iced? \n[a] Hot \n[b] Iced')
   style = ""
   if res == 'a':
      style = "hot"
   elif res == 'b':
      style = "iced"
   else: 
      print("Sorry but we do not offer that. Please choose an actual cup: ")
      return get_drink_style()  
   return style



def order_latte():
  milkCode = {"a": "2% Milk", "b": "Non-fat Milk", "c": "Soy Milk"}
  mes = input('And what kind of milk would you like? \n[a] 2% Milk \n[b] Non-fat Milk \n[c] Soy Milk \n> ').replace(" ", '')
  milk_type = ""
  for code in milkCode.keys(): 
        if code == mes:
          milk_type = code
        continue
  if milk_type:
    return milkCode.get(milk_type)
  else: 
     print("That is not a milk type. Please try again: ")
     return order_latte()

def get_cup():
   res = input("Would you like a plastic or would you like to use yours? \n[a] Plastic \n[b] Your own").replace(" ", '')
   cup = ""
   if res == 'a':
      cup = "a plastic cup"
   elif res == 'b':
      cup = "your own cup"
   else: 
      print("Sorry but we do not offer that. Please choose an actual cup: ")
      return get_cup()  
   return cup
  

# Call coffee_bot()!
coffee_bot()