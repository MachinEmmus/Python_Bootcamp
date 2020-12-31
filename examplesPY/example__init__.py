#!/usr/bin/python3
class Robot:
 
    def __init__(self, name=None):
        self.name = name   
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

if __name__ == '__main__':
    x = Robot()
    x.say_hi()
    y = Robot("Marvin")
    y.say_hi()
