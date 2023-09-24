drama = 0.0
crime = 0.0
action = 0.0
thriller = 0.0
horror = 0.0
comedy = 0.0
romance = 0.0


class PersonQuiz:

    def __init__(self, name, age, pronouns, gossip, holiday, fight):
        self.name = name
        self.age = age
        self.pro = pronouns
        self.gos = gossip
        self.hol = holiday
        self.fight = fight
        self.genres = [drama, crime, action, thriller, horror, comedy, romance]

    # genres[0] = drama, genres[1] = crime, genres[2] = action, genres[3] = thriller, genres[4] = horror, genres[5] =
    # comedy, genres[6] = romance

    def exam(self):
        genres = self.genres
        if self.pro.lower() == "he/him":
            genres[2] += 1 #action
            genres[3] += 1 #thriller
            genres[4] += 1 #horror
        elif self.pro.lower() == "she/her":
            genres[0] += 1 #drama
            genres[1] += 1 #crime
            genres[5] += 1 #comedy
            genres[6] += 1 #romance
        if self.age <= 20:
            genres[5] += 1
            genres[3] += 1
            genres[4] += 0.5
            genres[2] += 1
            genres[6] += 1
        elif self.age < 40:
            genres[0] += 1
            genres[5] += 0.5
            genres[4] += 1
            genres[1] += 0.5
            genres[2] += 1
            genres[3] += 0.5
            genres[6] += 0.5
        else:
            genres[0] += 0.5
            genres[1] += 1
            genres[2] += 0.5
            genres[4] += 0.5
        if self.gos.lower() == "never":
            genres[5] += 0.5
        elif self.gos.lower() == "sometimes":
            genres[0] += 0.5
            genres[1] += 0.5
            genres[2] += 0.5
            genres[6] += 0.5
        elif self.gos.lower() == "often":
            genres[0] += 1
            genres[1] += 1
            genres[4] += 0.5
            genres[6] += 0.5

        if self.hol.lower() == "valentine's day":
            genres[0] += 0.5
            genres[5] += 0.5
            genres[6] += 1
        elif self.hol.lower() == "halloween":
            genres[4] += 1
            genres[3] += 0.5
            genres[1] += 0.5
        elif self.hol.lower() == "new years":
            genres[0] += 0.5
            genres[5] += 0.5
            genres[6] += 0.5

        if self.fight.lower() == "yes":
            genres[3] += 1
            genres[2] += 1
            genres[4] += 0.5
            genres[1] += 0.5
        elif self.fight.lower() == "no":
            genres[5] += 0.5
            genres[6] += 0.5

        self.genres = genres


