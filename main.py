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

print(user1.genres[0])
#items = ia.search_movie('Harry Potter')

#for i in items:
    #print(i)