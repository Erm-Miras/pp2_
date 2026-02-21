# 1: базалык класс
class Animal:
    def speak(s):print("...")
# 2: озгерту 1
class Dog(Animal):
    def speak(s):print("Wouf")
# 3: озгерту 2
class Cat(Animal):
    def speak(s):print("Meow")
# 4: колдану
d=Dog();c=Cat();d.speak();c.speak()