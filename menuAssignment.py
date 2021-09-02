def welcomePage():
    equalS = '=' * 82
    print()
    print(equalS,'\n')
    print('\tWelcome to Miami\'s Best restaurant Delivery Python Application\n')
    print(equalS,'\n')

def printMenuIntro():
    print('\n')
    print('\t\t   Welcome to Miami\'s Favorites Meal Builder')
    print('\t\t   ========================================\n')
    print('\t\t    New Meal(n)\t\t\t     Quit(q)\n')

######################################################
def getMenu():
    #I named the restaurant on that was on the assignment Saffron
    print('1. Saffron')
    print('2. The Stanley')
    print('3. Heritage Pizza')
    print('4. Mac\'s BBQ')
    print('5. Flower Child')
    while(True):
        choice = eval(input('which restaurant would you like to order from? '))
        if choice == 1:
            filename = 'saffronMenu.txt'
            restaurant = 'Saffron'
            break
        elif choice == 2:
            filename = 'stanleyMenu.txt'
            restaurant = 'The Stanley'
            break
        elif choice == 3:
            filename = 'heritageMenu.txt'
            restaurant = 'Heritage Pizza'
            break
        elif choice == 4:
            filename = 'macsMenu.txt'
            restaurant = 'Mac\'s BBQ'
            break
        elif choice == 5:
            filename = 'flowerchildMenu.txt'
            restaurant = 'Flower Child'
            break
        else:
            print(choice, 'wasn\'t an option, please try again')
    return filename, restaurant

def resChoiceMenu(): 
    filename,restaurant = getMenu()
    print(filename)
    with open(filename, 'r') as f:
        text = [line.split(',') for line in f]
    text = [[s.strip() for s in nested] for nested in text]
    return text, filename, restaurant

######################################################
#this function should allow the admin to add a new item to the menu if desired
#without altering the actual print out
def findingIndex(text):
    #find first occurance of app in nested list
    app = 0
    for list in text:
        app += 1
        for elem in list:
            if elem == 'app':
                break
        else:
            continue
        break
    #find first occurance of ent in nested list
    ent = 0
    for list in text:
        ent += 1
        for elem in list:
            if elem == 'ent':
                break
        else:
            continue
        break
    sid = 0
    for list in text:
        sid += 1
        for elem in list:
            if elem == 'sid':
                break
        else:
            continue
        break
    #find first occurance of dnk in nested list
    dnk = 0
    for list in text:
        dnk += 1
        for elem in list:
            if elem == 'dnk':
                break
        else:
            continue
        break
    #find first occurance of des in nested list
    des = 0
    for list in text:
        des += 1
        for elem in list:
            if elem == 'des':
                break
        else:
            continue
        break
    if sid == len(text):
        #so side will never happen if the menu doesn't have it
        sid = 99999
    return app, ent, sid, dnk, des

def printMenu(text, restaurant):
    app, ent, sid, dnk, des = findingIndex(text)
    print ('{:<10s}{:#^62}'.format('', ' ' + restaurant.upper() + ' '))
    dash = '-' * 82
    i = 0
    for elem in text:
        if i == (app-1):
            print(dash)
            print('{:<10s}{:<32s}{:>40s}'.format('#','Item:','Price:'))
            print(dash,'\n')
            print ('{:<20s}{:*^39}'.format('', 'APPETIZERS'))
            print('\n')
            print('{:<10d}{:<32s}{:>40s}'.format(i+1, text[i][0],'$'+ text[i][1]))
            print()
            i += 1
        elif i == (ent-1):
            print()
            print ('{:<20s}{:*^39}'.format('', 'ENTREES'))
            print('\n')
            print('{:<10d}{:<32s}{:>40s}'.format(i+1, text[i][0],'$'+ text[i][1]))
            print()
            i += 1
        elif i == (sid-1):
            print()
            print ('{:<20s}{:*^41}'.format('', 'SIDES'))
            print('\n')
            print('{:<10d}{:<32s}{:>40s}'.format(i+1, text[i][0],'$'+ text[i][1]))
            print()
            i += 1
        elif i == (dnk-1):
            print()
            print ('{:<20s}{:*^41}'.format('', 'DRINKS'))
            print('\n')
            print('{:<10d}{:<32s}{:>40s}'.format(i+1, text[i][0],'$'+ text[i][1]))
            print()
            i += 1
        elif i == (des-1):
            print()
            print ('{:<20s}{:*^41}'.format('', 'DESSERTS'))
            print('\n')
            print('{:<10d}{:<32s}{:>40s}'.format(i+1, text[i][0],'$'+ text[i][1]))
            print()
            i += 1
        else:
            print('{:<10d}{:<32s}{:>40s}'.format(i+1, text[i][0],'$'+ text[i][1]))
            print()
            i += 1

def initialChoice():
    while(True):
        initialChoice = input('Please enter "N" for New Meal OR "Q" to Quit ').upper()
        if initialChoice == 'N' or initialChoice == 'Q':
            return initialChoice
        else:
            print(initialChoice, 'isn\'t a Y or N...')
            print('Let\'s try again shall we!')

def antiAbrv(itemType):
    if itemType == 'app':
        itemType = 'Appetizer'
    elif itemType == 'ent':
        itemType = 'Entree'
    elif itemType == 'dnk':
        itemType = 'Drink'
    elif itemType == 'sid':
        itemType = 'Side'
    else:
        itemType = 'Dessert'
    return itemType
#######################################################
def printRunningTotal(runningTotalList):
    subtotal = sum(runningTotalList)
    print('{:>75s}{:>7s}'.format('Subtotal =  ', '$' + str(subtotal)))
    tax = round(subtotal * .06,2)
    print('{:>75s}{:>7s}'.format('Tax =  ', '$' + str(tax)))
    tip = round(subtotal * .2,2)
    print('{:>75s}{:>7s}'.format('Tip =  ', '$' + str(tip)))
    total = round(subtotal + tax + tip,2)
    print('{:>75s}{:>7s}'.format('Total =  ', '$' + str(total)))

def runningList(item, orderList, runningTotalList, price = 0, itemType = 0, orderNum = 0):
    if item != False:
        itemType = antiAbrv(itemType)
        orderList.append([orderNum,item,itemType,price])
    else:
        orderList.sort()
    i = 0
    equalS = '=' * 82
    print()
    print(equalS,'\n')
    print('Your meal currently has:', len(orderList), 'item(s)','\n')
    for elem in orderList:
        print('{:<10d}{:<32s}{:>15s}{:>25s}'.format(orderList[i][0], orderList[i][1],orderList[i][2],'$'+ str(orderList[i][3])))
        print()
        i += 1
    print(equalS,'\n')
    #editing running total list
    if item != False:
        j = len(runningTotalList)
        runningTotalList.append(orderList[j][3])
    printRunningTotal(runningTotalList)
    return orderList, runningTotalList
    
def keepOrdering():
    while(True):
        choice = input('Would you like to order another item (Y/N)? ').upper()
        if choice == 'N' or choice == 'Y':
            return choice
        else:
            print(choice, 'isn\'t a Y or N...')
            print('Let\'s try again shall we!')

def getOrderChoice(text):
    while(True):
        orderNum = eval(input('Please Enter an Item (1-' + str(len(text)) + '): '))
        if orderNum <= 0 or orderNum > len(text):
            print(orderNum, 'is either too high or too low of a number, try again!')
        else:
            break
        #If one wants to add a verification step (remove quotes and break above)
        '''
        print()
        choice = input('You choose item #' + str(orderNum) + ' is this correct(Y/N)? ').upper()
        if choice == 'Y':
            break
        elif choice == 'N':
            print('Let\'s try again shall we!')
        else:
            print(orderNum, 'isn\'t a Y or N...')
            print('Let\'s try again shall we!')
        '''
    return orderNum

def getOrder(orderNum,filename):
    #finds line in resterauntMenu.txt
    import linecache
    itemAndPrice = linecache.getline(filename,orderNum)
    itemAndPriceSplit = itemAndPrice.split(',')
    itemAndPriceSplit[-1] = itemAndPriceSplit[-1].strip()
    item = itemAndPriceSplit[0]
    price = itemAndPriceSplit[1]
    itemType = itemAndPriceSplit[2]
    price = float(price)
    return item, price, itemType

def exitScrene():
    print('\n')
    print('\t##########Thank you for using Miami\'s Favorites Meal Builder##########')
    print('\n')

def printMenuAndGetChoice(text,filename,restaurant,testingMetric,orderList,runningTotalList):
    i = 0
    while(True):
        printMenu(text, restaurant)
        if i == 0 and testingMetric == 0 or testingMetric == 1:
            if testingMetric == 1:
                testingMetric = 2
                printMenu(text, restaurant)
                orderNum = getOrderChoice(text)
                item, price, itemType = getOrder(orderNum,filename)
                i += 1
            else:
                IC = initialChoice()
                if IC == 'Q':
                    return False, False, False
                else:
                    printMenu(text, restaurant)
                    orderNum = getOrderChoice(text)
                    item, price, itemType = getOrder(orderNum,filename)
                    orderList = list()
                    runningTotalList = list()
                    i += 1
        else:
            orderList, runningTotalList = runningList(item, orderList,runningTotalList, price, itemType, orderNum)
            choice = keepOrdering()
            if choice == 'N':
                break
            else:
                orderNum = getOrderChoice(text)
                item, price, itemType = getOrder(orderNum,filename)
    return item, orderList, runningTotalList



def checkOrder():
    while(True):
        choice = input('Is this the Correct Order (Y/N)? ').upper()
        if choice == 'N' or choice == 'Y':
            return choice
        else:
            print(choice, 'isn\'t a Y or N...')
            print('Let\'s try again shall we!')

def printItemDropMenu(orderList):
    i = 0
    equalS = '=' * 82
    print()
    print(equalS,'\n')
    print('Your meal currently has:', len(orderList), 'item(s)','\n')
    for elem in orderList:
        print('{:<10d}{:<32s}{:>15s}{:>25s}'.format(orderList[i][0], orderList[i][1],orderList[i][2],'$'+ str(orderList[i][3])))
        print()
        i += 1
    print(equalS,'\n')

def correctOrder(orderList, runningTotalList):
    print('Looks like your order isn\'t correct!')
    print('Add "A"')
    print('Drop "D"')
    print('Start Over Entirely "S"')
    while(True):
        optionChoosen = input('Please select an option: ').upper()
        if optionChoosen == 'A':
            return orderList,runningTotalList, optionChoosen
        elif optionChoosen == 'S':
            import sys
            sys.exit(0)
        elif optionChoosen == 'D':
            listOfItems = list()
            for i in range(len(orderList)):
                listOfItems.append(orderList[i][0])
            itemToDrop = list()
            while(True):
                printItemDropMenu(orderList)
                if len(orderList) == 0:
                    print('Well you deleted your whole order so the program is just gonna exit now...')
                    import sys
                    sys.exit(0)
                if len(itemToDrop) > 0:
                    print('Item(s) DROPPED:', itemToDrop)
                choice = eval(input('Please Select an item to DROP, enter item # OR to STOP enter "0": '))
                if choice == 0:
                    break
                elif choice not in listOfItems:
                    print('You can not drop item #', choice)
                    print('It is not in your order')
                else:
                    for i in range(len(orderList)):
                        print(i)
                        print(orderList[i])
                        if choice == orderList[i][0]:
                            print('TEST', orderList[i])
                            orderList.pop(i)
                            runningTotalList.pop(i)
                            break
            break
        else:
            print(optionChoosen, 'wasn\'t an option, try again')
    return orderList, runningTotalList, optionChoosen   

def finalTicket(item, orderList, runningTotalList, text, restaurant):
    item = False
    while True:
        runningList(item, orderList, runningTotalList)
        isOrderCorrect = checkOrder()
        if isOrderCorrect == 'N':
            orderList, runningTotalList, optionChoosen = correctOrder(orderList, runningTotalList)
            if optionChoosen == 'A':
                testingMetric = 1
                return testingMetric
        else:
            break
    print('\n\n')
    print ('{:<10s}{:*^61}'.format('', 'FINAL TICKET'))
    item = False
    runningList(item, orderList, runningTotalList)
    testingMetric = 2  
    return testingMetric

def getTotal(runningTotalList):
    subtotal = sum(runningTotalList)
    tax = round(subtotal * .06,2)
    tip = round(subtotal * .2,2)
    total = round(subtotal + tax + tip,2)
    return total

######################################################
#Working with orders.txt
#getting random order number(1000-9999)
def numToString(orderList):
    for i in range(len(orderList)):
        orderList[i][0] = str(orderList[i][0])
        orderList[i][3] = str(orderList[i][3])
    orderNums = str()
    for j in range(len(orderList)):
        if j+1 < len(orderList):
            orderNums += orderList[j][0] + ' '
        else:
            orderNums += orderList[j][0]
    return orderList,orderNums

def nestedListToString(newOrderList):
    from itertools import chain
    strOrderList = ' ' .join(chain.from_iterable(newOrderList))
    return strOrderList

def getRandomNumber():
    from random import randrange as rr
    randNum = rr(1000,9999)
    return randNum

#making sure order number is availabe
def isOrderNumAvailable():
    while(True):
        randNum = getRandomNumber()
        testOrders = list()
        filename = open('orders.txt', 'r')
        for line in filename:
            orderNums = line.split(',')
            testOrders.append(orderNums[0])
        res = [ele for ele in testOrders if(ele in str(randNum))]
        numOkay = not bool(res)
        if numOkay == True:
            break
        else:
            continue
    return randNum

def getDate():
    from datetime import date
    date = date.today()
    return date

def addingNewOrder(total, runningTotalList, restaurant, orderNums):
    orderNum = isOrderNumAvailable()
    date = getDate()
    orders = open('orders.txt', 'a')
    orders.write(str(orderNum) + ',' + restaurant + ',' + runningTotalList + ',' + orderNums + ',' + str(total) + ',' + str(date) + ',' +'OPEN' + '\n')
    orders.close()
    filename = 'orders.txt'
    newOrderText = list()
    with open (filename) as fin:
        for line in fin:
            newOrderText.append(line.strip())
    newOrderText.sort()
    with open (filename, 'w') as fout:
        for band in newOrderText:
            fout.write(band + '\n')
    return orderNum

######################################################
def main():
    welcomePage()
    text, filename, restaurant = resChoiceMenu()
    printMenuIntro()
    testingMetric = 0
    orderList = None 
    runningTotalList = None
    while(True):
        item, orderList, runningTotalList = printMenuAndGetChoice(text, filename, restaurant, testingMetric, orderList, runningTotalList)
        if runningTotalList == False:
            exitScrene()
            return
        testingMetric = finalTicket(item, orderList, runningTotalList, text, restaurant)
        if testingMetric == 2:
            break
    total = getTotal(runningTotalList)
    #I now have order and total to put into another .txt
    #turning list into string
    newOrderList, orderNums = numToString(orderList)
    strOrderList = nestedListToString(newOrderList)
    addingNewOrder(total, strOrderList, restaurant, orderNums)
    exitScrene()
    return total

if __name__ == ('__main__'):
    #so I can access total in orderAndBankCombo.py
    total = main()
