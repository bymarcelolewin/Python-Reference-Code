class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4
        
    def speak(self, message):
        print(self.name + f' says: {message}')
        
rocky = Dog("Rocky")
rocky.speak("woof!")
rocky.legs = 5
print(rocky.legs)

balboa = Dog("Balboa")
balboa.speak("Adrian!")
print(balboa.legs)