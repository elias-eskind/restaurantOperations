def getUserBankInfo(username):
    accFound = False
    filename = open('bankInfo.txt', 'r')
    userBankInfo = list()
    for line in filename:
        bankInfo = line.split(',')
        if bankInfo[6] == username:
            userBankInfo = bankInfo
            accFound = True
    return userBankInfo, accFound

def verifyUser():
    while(True):
        username = input('Please enter your username: ')
        userBankInfo, accFound = getUserBankInfo(username)
        if accFound == False:
            print('Sorry we did not find any account registered to the user:', username, 'please try again')
        else:
            break
    i = 4
    while(True):
        password = input('Please enter your password: ')
        i -= 1
        if i == 0:
            print('You took to many tries, exiting program!!!')
            return False
        elif userBankInfo[7] != password:
            print('That was the incorrect password for user:', username, i,'tries left')
        else:
            break
    userBankInfo[8] = userBankInfo[8].strip()
    return userBankInfo
#####################################
def updatingUserBalance(userBankInfo, total, oldBalance):
    oldBalance = float(oldBalance)
    total = float(total)
    updatedBalance = oldBalance - total
    updatedBalance = str(updatedBalance)
    userBankInfo[8] = updatedBalance
    return userBankInfo


def deleteOldAcc(accNum):
    updatedBankInfo = list()
    import csv
    with open('bankInfo.txt',newline='') as f:
      reader=csv.reader(f) 
      for row in reader:
        if row[0]!= accNum:
            updatedBankInfo.append(row)
    with open('bankInfo.txt','w',newline='') as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedBankInfo)

def changeBalance(userBankInfo, accNum):
    #deleting outdated order
    deleteOldAcc(accNum)
    #writing updated order
    bankInfo = open('bankInfo.txt', 'a')
    bankInfo.write(userBankInfo[0] + ',' + userBankInfo[1] + ',' + userBankInfo[2] + ',' + userBankInfo[3] + ',' + userBankInfo[4] + ',' + userBankInfo[5] + ',' + userBankInfo[6] + ',' + userBankInfo[7] + ',' + userBankInfo[8] +'\n')
    bankInfo.close()
    #reorganizing the bankInfo.txt file by order number
    filename = 'bankInfo.txt'
    newOrderText = list()
    with open (filename) as fin:
        for line in fin:
            newOrderText.append(line.strip())
    newOrderText.sort()
    with open (filename, 'w') as fout:
        for band in newOrderText:
            fout.write(band + '\n')

def updateBalance(userBankInfo, total, oldBalance):
    accNum = userBankInfo[0]
    updatedUserInfo = updatingUserBalance(userBankInfo, total, oldBalance)
    changeBalance(updatedUserInfo, accNum)
    return updatedUserInfo

#####################################
def printAccInfo(account, oldBalance, total):
    print('\n')
    print('Welcome back', account[1], account[2] + '!!!')
    print('After your transaction of $' + str(total))
    print('Your updated balance is now $' + account[8])
    if float(account[8]) < 0:
        print()
        print('UH OH looks like you\'re out of money, but this one is on us') #this would probaly never happen haha
        print('Please deposit at least $' + str(total), 'ASAP')
        print()
    print('If you have any question about this transaction please call us at:')
    print('1 (800) 432-1000')
    print('Thanks, and have a great day!!!')
    print()

#####################################
def main():
    #getting total
    #all of the .txt & .py docs are all in the same file
    import menuAssignment as menu
    total = menu.main()
    userBankInfo = verifyUser()
    if userBankInfo == False:
        return
    oldBalance = userBankInfo[8]
    updatedUserInfo = updateBalance(userBankInfo, total, oldBalance)
    printAccInfo(updatedUserInfo, oldBalance, total)

if __name__ == ('__main__'):
    main()
    