# sum pridict program

playerName = input("Please enter your name: ")
print(f'Hello {playerName} this program ask to you enter two digit number between 12 and 99. once you \
    enter the number it will predict the total sum that based on the number you are going enter ')

num = int(input("Please enter first number: "))
changedNum = num - 2
PredictedTotal = '2' + str(changedNum)
sum = 0
magicNumber = 99
playterEnteredNum = []
computerEnteredNum = []
print(f'Predicted total will be ' + PredictedTotal)
sum += num
playterEnteredNum.append(num)
for i in range(2):
    newNum = int(input('Enter next number '))
    sum += newNum
    playterEnteredNum.append(newNum)
    computerNum = magicNumber - newNum
    print("computer is adding " + str(computerNum))
    computerEnteredNum.append(computerNum)
    sum += computerNum

print("Numbers you entered are : ")
for num in range(len(playterEnteredNum)):
    print(playterEnteredNum[num])
print("Numbers you computer eneted are : ")
for j in range(len(computerEnteredNum)):
    print(computerEnteredNum[j])
print('--------')
print(sum)
