#Write a Python program to find the sum of all the numbers except odd numbers between 1 and 20 using a loop. Can you also do this using a while loop?

# for i in range (1,21):
#     if i%2==0:
#         print(i)
# for i in range (1,21):
#     if i%2==1:
#         continue
#     print(i)

# Write a Python program to find the sum of all the numbers except even numbers between 1 and 20 using a loop. Can you also do this using a while loop?

# for i in range(1,21):
#     if i%2==1:
#         print(i)

# After throwing the dice several times, you got this result,
# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# Using a for loop find out the followings:
# How many times have you got 6s

# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# count=0
# # print(dice_result[5])
# print (len(dice_result))
# for i in range (len(dice_result)):
#     if dice_result[i]==6:
#         count=count+1
# print(count)

#How many times have you got 1s

# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# count=0
# # print(len(dice_result))
# for i in range (len(dice_result)):
#     # print(dice_result[i])
#     if dice_result[i]==1:
#
#         count=count+1
# print(count)
#How many times have you got 6s two times in a row

# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
#
# count=0
# for i in range(len(dice_result)):
#     if dice_result[i] == 6 and dice_result[i + 1] == 6:
#         count=count+1
# print(count)

#How many times have you got 6s two times in a row

# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
#
# count=0
# for i in range(len(dice_result)):
#     if dice_result[i] == 1 and dice_result[i + 1] == 1:
#         count=count+1
# print(count)


# Let's say you are doing push-ups and you have to complete 50 push-ups daily, write a program that,
 # Upon completing 10 push-ups in a go, asks you, “Are you tired?”

# for i in range(1,50):
#     if i==10:
#         print("Are you tired?")
'''
If you reply “yes” or “y” then it should break and print “You did total push-ups.”

For example: If you did only 30  push-ups and answered “yes” to your program. It will break the loop and print “You did a total of 30 push-ups”

If you reply “no” or “n” then it should continue and display how many push-ups are remaining  now after that ask you again “Are you tired?”

For Example: if you answered “no” then it should display that 20 push-ups are remaining and ask you again “Are you tired?”

If you complete all 50 push-ups, then it should print the “Congratulations! You made it” and stopped the program.
'''
for i in range(1,50):
    if i==10:
        answer= input("Are you tired?,yes or no \n")
        if answer == y:
            break
            print("you did total push-ups", i)






