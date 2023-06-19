class Father():
    def skills (self):
        print ("I enjoy gardening,programming")

class Mother ():
    def skills (self):
        print("I love cooking,art")

class Child (Father,Mother):
    def skills (self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c= Child ()
c.skills()