print("Math Game")
print()
multiple = int(input("Name your multiples: "))
print()
counter = 0
for i in range(1, 11):
  correct_answer = i*multiple
  print(i, "x", multiple)
  answer = int(input("> "))
  if answer == correct_answer:
    print("You got it right!")
    counter += 1
  else:
    print("That's not correct. It should have been", correct_answer)
  
