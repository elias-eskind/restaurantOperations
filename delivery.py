def welcomeScreen():
    equalS = '=' * 82
    print()
    print(equalS,'\n')
    print('\tWelcome to Miami\'s Best restaurant Delivery Python Application\n')
    print(equalS,'\n')
    print('OPTIONS:')
    print('1. View Open Order')
    print('2. View Closed Orders')
    print('3. View Revenue By Restaurant/Item')
    print('4. Search Order by Order Number to View or Change Status')
    print('5. Search Order by Order Date')
    print('6. Search Order by Restaurant')
    print('7. Exit')
    userChoice = eval(input('What would you like to do? '))
    print('\n')
    return userChoice

#file to list function
def orderToList(filename):
    with open(filename, 'r') as f:
        text = [line.split(',') for line in f]
    text = [[s.strip() for s in nested] for nested in text]
    return text


##################################################
#printing all the tickets
def printOrders(orderList):
    dash = '-' * 100
    print(dash)
    print('{:<1s}{:>15s}{:^29s}{:^30s}{:<11s}{:<12s}'.format('Order#: ','Restaurant:','Item(s)#:','Total:', 'Date:', 'Status:'))
    print(dash)
    i = 0
    for elem in orderList:
        print('{:<12s}{:<21s}{:<31s}{:<16s}{:<10s}{:>9s}'.format(orderList[i][0], orderList[i][1], orderList[i][3],'$'+ orderList[i][4],orderList[i][5],orderList[i][6]))
        print()
        i += 1
    print(dash)
    print()

##################################################            

def viewOpenOrders():
    orderList = orderToList('orders.txt')
    i = 0
    openOrderList = list()
    for elem in orderList:
        if orderList[i][6] == 'OPEN':
            openOrderList.append(orderList[i])
        i+=1
    printOrders(openOrderList)
    runAgainChoice = runAgain()
    return runAgainChoice

##################################################
def viewClosedOrders():
    orderList = orderToList('orders.txt')
    i = 0
    closedOrderList = list()
    for elem in orderList:
        if orderList[i][6] == 'CLOSED':
            closedOrderList.append(orderList[i])
        i+=1
    printOrders(closedOrderList)
    runAgainChoice = runAgain()
    return runAgainChoice

##################################################
def getMenu():
    print('1. Saffron')
    print('2. The Stanley')
    print('3. Heritage Pizza')
    print('4. Mac\'s BBQ')
    print('5. Flower Child')
    while(True):
        choice = eval(input('which restaurant would you like to view? '))
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
    with open(filename, 'r') as f:
        text = [line.split(',') for line in f]
    text = [[s.strip() for s in nested] for nested in text]
    return text, filename, restaurant

def getRevenue(filename, restaurant, text):
    orderList = orderToList('orders.txt')
    i = 0
    itemsOrdered = list()
    for elem in orderList:
        if orderList[i][1] == restaurant:
            itemsOrdered.append(orderList[i][3])
        i+=1
    return itemsOrdered
#************************************************

def getLists(itemsOrdered):
    lst = [words for segments in itemsOrdered for words in segments.split()]
    for i in range(0, len(lst)): 
        lst[i] = int(lst[i])
    lst.sort()
    return lst

def countX(lst, x): 
    return lst.count(x) 

def getOccurances(lst, text):
    newList = []
    for i in range(1,len(text)+1):
        newList.append(countX(lst, i))
    return newList

########################## 
def getResterauntList(filename):
    with open(filename, 'r') as f:
        text = [line.split(',') for line in f]
    text = [[s.strip() for s in nested] for nested in text]
    return text

##########################
def stringToFloat(text):
    amountOrdered = list()
    for i in range(len(text)):
        amountOrdered.append(round(float(text[i][1]),2))
    return amountOrdered    

def floatToString(totalAmount):
    for i in range(len(totalAmount)):
        totalAmount[i] = str(totalAmount[i])
    return totalAmount

def mutilplyingTwoList(newList, amountOrdered):
    totalAmount = [] 
    for i in range(0, len(newList)): 
        totalAmount.append(round(newList[i] * amountOrdered[i],2)) 
    sumTotal = sum(totalAmount)
    newTotalAmount = floatToString(totalAmount) 
    return sumTotal, newTotalAmount

def printRevenueByOrder(orderList, newList, restaurant):
    amountOrdered = stringToFloat(orderList)
    sumTotal, totalAmount = mutilplyingTwoList(newList, amountOrdered)
    print('\n')
    print ('{:#^70}'.format( ' ' + restaurant.upper() + ' '))
    dash = '-' * 70
    print(dash)
    print('{:<1s}{:>10s}{:>46s}'.format('Total Count:','Item:','Total:', ))
    print(dash)
    i = 0
    for elem in orderList:
        print('{:<17d}{:<45s}{:<8s}'.format(newList[i], orderList[i][0], '$' + totalAmount[i]))
        print()
        i += 1
    equalS = '=' * 70
    print(equalS,'\n')
    print('{:>61s}{:>7s}'.format('Grand Total =  ', '$' + str(sumTotal)))
    print(equalS,'\n')

def printRevenueReport(itemsOrdered, filename, restaurant):
    text = getResterauntList(filename)
    lst = getLists(itemsOrdered)
    newList = getOccurances(lst,text)
    printRevenueByOrder(text,newList, restaurant)

#************************************************
def restaurantRevenue():
    text, filename, restaurant = resChoiceMenu()
    itemsOrdered = getRevenue(filename, restaurant, text)
    printRevenueReport(itemsOrdered,filename, restaurant)
    runAgainChoice = runAgain()
    return runAgainChoice

##################################################
def getOrderNum():
    orderNum = input('Please enter desired Order Number: ')
    return orderNum       

def changeOrderStatus(orderNum):
    while(True):
        statusChoice = input('Would you like to change the order status of order #' + orderNum + '(Y/N)? ').upper()
        if statusChoice != 'Y' and statusChoice != 'N':
            print(statusChoice)
            print('#######ERROR PLEASE ENTER: "Y" for yes or "N" for no########')
        else:
            break
    return statusChoice

def deleteOldOrder(orderNum):
    updatedOrderList = list()
    import csv
    with open('orders.txt',newline='') as f:
      reader=csv.reader(f) 
      for row in reader:
        if row[0]!= orderNum:
            updatedOrderList.append(row)
    with open('orders.txt','w',newline='') as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedOrderList)

def changeStatus(orderNumList, orderNum):
    #deleting outdated order
    deleteOldOrder(orderNum)
    #writing updated order
    orders = open('orders.txt', 'a')
    orders.write(orderNumList[0][0] + ',' + orderNumList[0][1] + ',' + orderNumList[0][2] + ',' + orderNumList[0][3] + ',' + orderNumList[0][4] + ',' + orderNumList[0][5] + ',' + orderNumList[0][6] + '\n')
    orders.close()
    #reorganizing the orders.txt file by order number
    filename = 'orders.txt'
    newOrderText = list()
    with open (filename) as fin:
        for line in fin:
            newOrderText.append(line.strip())
    newOrderText.sort()
    with open (filename, 'w') as fout:
        for band in newOrderText:
            fout.write(band + '\n')

def searchOrderNum():
    while(True):
        orderNum = getOrderNum()
        orderList = orderToList('orders.txt')
        i = 0
        orderNumList = list()
        for elem in orderList:
            if orderList[i][0] == orderNum:
                orderNumList.append(orderList[i])
            i+=1
        if not orderNumList:
            print('We couldn\'t find that number please try again!')
        else:
            break
    printOrders(orderNumList)
    statusChoice = changeOrderStatus(orderNum)
    if statusChoice == 'Y' and orderNumList[0][6] == 'OPEN':
        orderNumList[0][-1] = 'CLOSED'
        print('The status of order #', orderNum, 'is now changed from OPEN to CLOSED')
        printOrders(orderNumList)
        #actually changing the status in the orders.txt file
        changeStatus(orderNumList, orderNum)
    elif statusChoice == 'Y' and orderNumList[0][6] == 'CLOSED':
        orderNumList[0][-1] = 'OPEN'
        print('The status of order #', orderNum, 'is now changed from CLOSED to OPEN')
        printOrders(orderNumList)
        #actually changing the status in the orders.txt file
        changeStatus(orderNumList, orderNum)
    runAgainChoice = runAgain()
    return runAgainChoice

##################################################
def getDate():
    month = input('Please enter month: ')
    if len(month) == 1:
        month = '0' + month
    day = input('Please enter day: ')
    if len(day) == 1:
        day = '0' + day
    year = input('Please enter year: ')
    date = year + '-' + month + '-' + day
    return date

def openOrClosed(orderList, date):
    while(True):
        statusChoice = input('Would you like to return orders on ' + date + ' with the status:\nOPEN, CLOSED, or ALL ORDERS (O/C/A)? ').upper()
        if statusChoice != 'O' and statusChoice != 'C' and statusChoice != 'A':
            print(statusChoice)
            print('#######ERROR PLEASE ENTER: "O" for OPEN, "C" for CLOSED, or "A" for ALL ORDERS########')
        else:
            break
    i = 0
    if statusChoice == 'O':
        openOrderList = list()
        for elem in orderList:
            if orderList[i][6] == 'OPEN':
                openOrderList.append(orderList[i])
            i+=1
        return openOrderList
    elif statusChoice == 'C':
        closedOrderList = list()
        for elem in orderList:
            if orderList[i][6] == 'CLOSED':
                closedOrderList.append(orderList[i])
            i+=1
        return closedOrderList
    else:
        return orderList


def searchOrderDate():
    while(True):
        date = getDate()
        orderList = orderToList('orders.txt')
        newOrderList = openOrClosed(orderList, date)
        i = 0
        orderDateList = list()
        for elem in newOrderList:
            if newOrderList[i][5] == date:
                orderDateList.append(newOrderList[i])
            i+=1
        if not orderDateList:
            print('We couldn\'t find any orders that meet the criteria please try again!')
        else:
            break
    printOrders(orderDateList)
    runAgainChoice = runAgain()
    return runAgainChoice

##################################################
def restaurantOpenOrClosed(orderList, restaurant):
    while(True):
        statusChoice = input('Would you like to return orders for ' + restaurant + ' with the status:\nOPEN, CLOSED, or ALL ORDERS (O/C/A)? ').upper()
        if statusChoice != 'O' and statusChoice != 'C' and statusChoice != 'A':
            print(statusChoice)
            print('#######ERROR PLEASE ENTER: "O" for OPEN, "C" for CLOSED, or "A" for ALL ORDERS########')
        else:
            break
    i = 0
    if statusChoice == 'O':
        openOrderList = list()
        for elem in orderList:
            if orderList[i][6] == 'OPEN':
                openOrderList.append(orderList[i])
            i+=1
        return openOrderList
    elif statusChoice == 'C':
        closedOrderList = list()
        for elem in orderList:
            if orderList[i][6] == 'CLOSED':
                closedOrderList.append(orderList[i])
            i+=1
        return closedOrderList
    else:
        return orderList

def searchOrderByRestaurant():
    filename, restaurant = getMenu()
    orderList = orderToList('orders.txt')
    newOrderList = restaurantOpenOrClosed(orderList, restaurant)
    i = 0
    restaurantOrderList = list()
    print(restaurant)
    for elem in newOrderList:
        if newOrderList[i][1] == restaurant:
            restaurantOrderList.append(newOrderList[i])
        i+=1
    printOrders(restaurantOrderList)
    runAgainChoice = runAgain()
    return runAgainChoice

##################################################
def runAgain():
    while(True):
        runAgainChoice = input('Would you like to return to the main menu(Y/N)? ').upper()
        if runAgainChoice != 'Y' and runAgainChoice != 'N':
            print(runAgainChoice)
            print('#######ERROR PLEASE ENTER: Y for Yes or N for No########')
        else:
            break
    return runAgainChoice

##################################################
def runQuit():
    equalS = '=' * 82
    print()
    print(equalS,'\n')
    print('\tThanks for Using Miami\'s Best Restaurant Delivery Python Application\n')
    print(equalS,'\n')

##################################################
def main():
    while(True):
        while(True):
            userChoice = welcomeScreen()
            if userChoice <= 7 and userChoice > 0:
                break
            else:
                print("#############ERROR PLEASE ENTER NUMBER 1-6#############")
        #Which program to run
        if userChoice == 1:
            runAgain = viewOpenOrders()
            if runAgain == 'N':
                runQuit()
                break
        if userChoice == 2:
            runAgain = viewClosedOrders()
            if runAgain == 'N':
                runQuit()
                break
        if userChoice == 3:
            runAgain = restaurantRevenue()
            if runAgain == 'N':
                runQuit()
                break
        if userChoice == 4:
            runAgain = searchOrderNum()
            if runAgain == 'N':
                runQuit()
                break
        if userChoice == 5:
            runAgain = searchOrderDate()
            if runAgain == 'N':
                runQuit()
                break
        if userChoice == 6:
            runAgain = searchOrderByRestaurant()
            if runAgain == 'N':
                runQuit()
                break
        if userChoice == 7:
            runQuit()
            break

if __name__ == "__main__":
    main()
    