try:
  age=int(input("enter age:"))
  if age>=18:
    print("eligible")
  else:
    print("not eligible")
except ValueError:
  print("invalid")
