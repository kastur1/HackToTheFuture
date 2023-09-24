import imdb
from PersonQuiz import PersonQuiz
ia = imdb.IMDb()

print("Hello! Welcome to Dating the Films!")
print("Time to take the personality quiz!")

name = str(input("\nWhat is your name? "))
age = int(input("\nHow old are you? "))
pro = str(input("\nWhat are your preferred pronouns? (he/him / she/her / they/them) "))
gos = input("\nHow often do you gossip? (never/sometimes/often) ")
hol = input("\nOut of the three, what is your favorite Holiday? (Valentine's Day/Halloween/New Years) ")
fight = input("\nHave you ever gotten into a physical fight? (yes/no) ")

user1 = PersonQuiz(name, age, pro, gos, hol, fight)

user1.exam()


maxvalue = max(user1.genres)
index = user1.genres.index(maxvalue)

if(index == 0):
    items = ia.search_movie("Godfather")
    for i in items:
      print(i)
elif(index == 1):
    items = ia.search_movie("Law and Order")
    for i in items:
        print(i)
elif(index == 2):
    items = ia.search_movie("Jumanji")
    for i in items:
        print(i)
elif(index == 3):
    items = ia.search_movie("Scream")
    for i in items:
        print(i)
elif(index == 4):
    items = ia.search_movie("IT")
    for i in items:
        print(i)
elif(index == 5):
    items = ia.search_movie("Dumb and Dumber")
    for i in items:
        print(i)
elif(index == 6):
    items = ia.search_movie("La La Land")
    for i in items:
      print(i)
