#note this .py takes no user input just reorganizes people1.txt in the desired format (CSV)
def orderToList(filename):
    with open(filename, 'r') as f:
        text = [line.split(' ') for line in f]
    text = [[s.strip() for s in nested] for nested in text]
    return text
#################################
def getAttributes(peopleOneList,x):
    i = 0
    attributes = list()
    for elem in peopleOneList:
        attributes.append(peopleOneList[i][x])
        i+=1
    return attributes

#################################
def getSS(peopleOneList):
    x = 0
    SSList = getAttributes(peopleOneList,x)
    return SSList

#################################
def getFirstNames(peopleOneList):
    x = 1
    firstNamesList = getAttributes(peopleOneList,x)
    return firstNamesList

#################################
def getLastNames(peopleOneList):
    x = 2
    lastNameList = getAttributes(peopleOneList,x)
    return lastNameList

#################################
def getBirthdays(peopleOneList):
    x = 3
    birthdayList = getAttributes(peopleOneList,x)
    return birthdayList

#################################
def getStates(peopleOneList):
    x = 4
    stateList = getAttributes(peopleOneList,x)
    return stateList

#################################
def formatSSNumList(SSNumList):
    #formatedSSNumList = list()
    middleTwoSSNum = list()
    for i in range(len(SSNumList)):
        d = SSNumList[i]
        y = d[4:6]
        middleTwoSSNum.append(y)
        '''
        x = '-'.join([d[:4], d[4:6], d[6:]])
        formatedSSNumList.append(x)
        '''
    return middleTwoSSNum #,formatedSSNumList

def getFirstLetterOfFN(firstNamesList):
    firstLetterFN = list()
    for i in range(len(firstNamesList)):
        d = firstNamesList[i]
        y = d[0]
        firstLetterFN.append(y.lower())
    return firstLetterFN

def getLastThreeLettersOfLN(lastNameList):
    lastThreeLN = list()
    for i in range(len(lastNameList)):
        d = lastNameList[i]
        y = d[-3:]
        lastThreeLN.append(y)
    return lastThreeLN

def getRandomNumber(x,y):
    from random import randrange as rr
    randNum = rr(x,y)
    return randNum

def getRandHostName(SSNumList):
    x = 1
    y = 4
    hostNameList = list()
    for i in range(len(SSNumList)):
        randNum = getRandomNumber(x,y)
        if randNum == 1:
            hostNameList.append('@gmail.com') 
        elif randNum == 2:
            hostNameList.append('@Hotmail.com')
        else:
            hostNameList.append('@yahoo.com')
    return hostNameList

def makeEmailList(middleTwoSSNum, firstLetterFN, lastThreeLN, hostNameList):
    emailList = list()
    for i in range(len(middleTwoSSNum)):
        emailList.append(firstLetterFN[i] + lastThreeLN[i] + middleTwoSSNum[i] + hostNameList[i])
    return emailList

def makeEmail(SSNumList, firstNamesList, lastNameList):
    middleTwoSSNum = formatSSNumList(SSNumList) #formatedSSNumList, 
    firstLetterFN = getFirstLetterOfFN(firstNamesList)
    lastThreeLN = getLastThreeLettersOfLN(lastNameList)
    hostNameList = getRandHostName(SSNumList)
    emailList = makeEmailList(middleTwoSSNum, firstLetterFN, lastThreeLN, hostNameList)
    return emailList
#************************
def getRandPass(length):
    import random
    import string
    randString = string.ascii_letters + string.digits
    randPass = ''.join((random.choice(randString) for i in range(length)))
    return randPass

def randomPassword(SSNumList):
    randPassList = list()
    for i in range(len(SSNumList)):
        x = getRandPass(8)
        randPassList.append(x)
    return randPassList

#************************
def getBankAccNum(SSNumList):
    x = 100000
    y = 999999
    randBankAccNumList = list()
    for i in range(len(SSNumList)):
        randBankAccNumList.append(getRandomNumber(x,y))
    return randBankAccNumList

def getBalance(SSNumList):
    x = 0
    y = 10001
    randBalanceList = list()
    for i in range(len(SSNumList)):
        randBalanceList.append(getRandomNumber(x,y))
    return randBalanceList


#************************
def makeOtherLists(SSNumList, firstNamesList, lastNameList, birthdayList):
    emailList = makeEmail(SSNumList, firstNamesList, lastNameList)
    randBankAccNumList = getBankAccNum(SSNumList)
    randPassList = randomPassword(SSNumList)
    randBalanceList = getBalance(SSNumList)
    return emailList, randBankAccNumList, randPassList, randBalanceList

#################################
def clearbankInfotxtFile():
    open('bankInfo.txt', 'w').close()

def writeTotxtFile(SSNumList, firstNamesList, lastNameList, birthdayList, stateList, emailList, randBankAccNumList, randPassList, randBalanceList):
    #clearing bankInfo.txt (otherwise every time this program ran there would be duplicates)
    clearbankInfotxtFile()
    bankInfo = open('bankInfo.txt', 'a')
    for i in range(len(SSNumList)):
        bankInfo.write(str(randBankAccNumList[i]) + ',' + firstNamesList[i] + ',' + lastNameList[i] + ',' + SSNumList[i] + ',' + stateList[i] + ',' + birthdayList[i] + ',' + emailList[i] + ',' + randPassList[i] + ',' + str(randBalanceList[i]) + '\n')
    bankInfo.close()
    #reorganizing the orders.txt file by acc number
    filename = 'bankInfo.txt'
    newOrderText = list()
    with open (filename) as fin:
        for line in fin:
            newOrderText.append(line.strip())
    newOrderText.sort()
    with open (filename, 'w') as fout:
        for band in newOrderText:
            fout.write(band + '\n')

#################################
def main():
    filename = 'people1.txt'
    peopleOneList = orderToList(filename)
    SSNumList = getSS(peopleOneList)
    firstNamesList = getFirstNames(peopleOneList)
    lastNameList = getLastNames(peopleOneList)
    birthdayList = getBirthdays(peopleOneList)
    stateList = getStates(peopleOneList)
    emailList, randBankAccNumList, randPassList, randBalanceList = makeOtherLists(SSNumList, firstNamesList, lastNameList, birthdayList)
    writeTotxtFile(SSNumList, firstNamesList, lastNameList, birthdayList, stateList, emailList, randBankAccNumList, randPassList, randBalanceList)


if __name__ == ('__main__'):
    main()
    