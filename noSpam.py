#menu = [
 #   ["egg", "bacon"],
  #  ["egg", "sausage", "bacon"],
   # ["egg", "spam"],
    #["egg", "bacon", "spam"],
 #   ["egg", "bacon", "sausage", "spam"],
  #  ["spam", "bacon", "sausage", "spam"],
   # ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    #["spam", "egg", "spam", "spam", "bacon", "spam"],
#]

#for meal in menu:
 #   for item in meal:
  #      if "spam"==item:
   #         continue
    #    else:
     #       print(item)


numbers = ["9","223","372","036","854","775","807"]
for index in range(len(numbers)):
    numbers[index]=int(numbers[index])
print(numbers)