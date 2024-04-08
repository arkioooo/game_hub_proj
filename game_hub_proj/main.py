import webbrowser
import random
import time

txt1="Welcome to the Game Hub!"
x=txt1.center(20)
print(x)

print("*The project is still under development. Pacman and Fruit Ninja are still being developed")

a=input("Enter username:")
b=input("Enter password:")

print("Random Fact of the day:")
facts=["Avocados are a fruit, not a vegetable","Australia is wider than the moon","Human teeth are the only part of the body that cannot heal themselves","The English word with the most definitions is 'set'"]
fact=random.choice(facts)
print(fact)
time.sleep(2)
print("Now redirecting you to the Game Hub (Early Access)...")
time.sleep(2)

   
run_once = 0
while 1:
    if run_once == 0:
        webbrowser.open('index.html')
        run_once = 1
