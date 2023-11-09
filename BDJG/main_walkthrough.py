import random


#Opens the files needed
PunchLines = open('assets\PunchLineDict.txt', 'r')
SetUps = open('assets\SetUpDict.txt', 'r')

SU_Lines = len(SetUps.readlines())
PL_Lines = len(PunchLines.readlines())

SU_Dict = SetUps.readlines()
PL_Dict = PunchLines.readlines()

print(SetUps.readlines())
