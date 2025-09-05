print("Welcome to Daniel's quiz game")

print("""
Rules:
      For every questions you get correctly, you score +1 points.
      Some questions has higger points.
      For every incorrect questions, 1 point is deducted from your overall points.
      """)

player = input("Do you want to play? ").lower()

if player != "yes":
  quit()
  
answer = input("What is the full meaning of CPU? ").lower()
score = 0

if answer == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect")
  score -=1
  
answer = input("What's the meaning of NMAP? ").lower()
if answer == "network mapper":
  print("Correct!")
  score += 2
else:
  print("Incorrect")
  score -=1
  
answer = input("Which language is most used for scripting in cybersecurity? ").lower()
if answer == "python":
  print("Correct!")
  score += 3
else:
  print("Incorrect")
  score -=1
  
answer = input("What's the meaning of API? ").lower()
if answer == "application programming interface":
  print("Correct!")
  score += 2
else:
  print("Incorrect")
  score -=1
  
answer = input("What does the 's' in 'HTTPS' mean? ").lower()
if answer == "secured":
  print("Correct!")
  score += 2
else:
  print("Incorrect")
  score -=1
  
print("You got " + str(score) + " correctly!")
print("You scored " + str(score / 10 *100) + "%")