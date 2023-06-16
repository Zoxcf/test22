slovo = str(input("введите слово:"))
a = slovo[::-1]

if slovo == a:
  print("является")
else:
  print("не является")