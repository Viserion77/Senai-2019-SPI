# In this project, you will create an interactive text adventure that takes the user on an adventure to escape the dungeon they are in.

# Instructions:

# 1. Define a variable start that takes in the user input. In the input() you should explain to the user the setting of the story, and then present them with a choice between three items: a dagger, a sword, or a short club. Use \n in your string if you need to start a new line.
start = input(
    "Você vai morrer, ANTES do natal\nand you can choice between three items: a dagger, a sword, or a short club.")

# 2. If they picked a dagger or a short club, define another variable choice2 and in the input, tell them they waited until the guard open their door for a meal and then knocked them out with their weapon. When comparing start to a string, use start.lower() to convert start into lowercase, in case the user writes something like "Dagger", in order to make it more user friendly. if start.lower() == "dagger":
choice2 = ""
if start.lower() == "dagger" or start.lower() == "short club":
    # In the same input, present them with a choice between going right and going left. However, if they did not pick a dagger or a short club, print a statement telling them the guard saw the sword when he walked in because it was so big and called in reinforcements, and the user's escape failed.
    choice2 = input(
        "esperaram até o guarda abrir a porta para uma refeição e depois os nocautearam com a arma(?????) choice between going right and going left?????? kk")
else:
    print("them the guard saw the sword when he walked in because it was so big and called in reinforcements, and the user's escape failed.")

# 3. If choice2 is equal to right, define another variable choice3 and in the input, tell them there are 5 doors labeled 1-5, and tell them to pick one. If they chose to go left, print a statement saying they ran into some guards and failed their mission.
choice3 = 0
if choice2.lower() == "right":
    choice3 = int(input("there are 5 doors labeled 1-5, picka one"))
elif choice2 not == "":
    print("they ran into some guards and failed their mission.")

# 3a. Note that because if they picked the sword at the start, then they would have failed and not gone into the if statement where choice2 was defined, the if statement with choice2 would throw an error because choice2 has not been defined yet. Therefore, you need to use try and except. Use it in this format:
# ou não kkkkk

# try:
#     if choice2.lower() == "right":
#         #do something
#     else:
#         #do something
# except:
#     pass
# Pass will just make the program continue if it is not able to run if choice2.lower() == "right" properly because choice2 is not defined. Keep in mind you will need to do this for every if statement from step 3 onwards.
# '-' ok

# 4. If they picked any door that was not door number four, define another variable choice4 and in the input, tell them they have to choose either going down or up the stairs. Remember to use int() to check if their choice was correct. If they picked door number four, print a statement saying they walked straight into the guards' living quarters and was promptly put back in the dungeon.
choice4 = ""
if choice3 not == 4:
    choice4 = input("them they have to choose either going down or up the stairs.")
elif choice3 not == 0:
    print("they walked straight into the guards' living quarters and was promptly put back in the dungeon.")

# 5. Because this is a dungeon, if they went down, they would only get further trapped, so print out a statement telling them they failed the mission. If they chose up, create a variable choice5 and in the input, tell them there are two guards waiting for them on the right corridor. Give them a choice between fighting the guards or running left.
choice5 = ""
if choice4.lower() == "down":
    print("a statement telling them they failed the mission.")
elif choice4 not == "":
    choice5 = input("there are two guards waiting for them on the right corridor.\nchoice between fighting the guards or running left.")


# 6. Finally if they chose to fight, print out a statement describing their fight with the guards and how they managed to beat them and escape the dungeon. Congratulate them! If they chose to go run left, print out a statement telling them they ran into 5 more guards and was promptly put back into their cell, failing the mission.
if choice5.lower() == "fight":
    print("sua luta com os guardas e como eles conseguiram vencê-los e escapar da masmorra. :D")
elif choice5 not == "":
    print("encontraram mais 5 guardas e foram prontamente colocados de volta em sua cela, falhando na missão. D:")

# 7. Congratulations! You successfully made an exciting, engaging text adventure that you can ask your friends or family members to play through and see if they can escape the dungeon. If you want to change the setting, story, or choices, feel free to be creative and add more things.
# :D