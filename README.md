# Restaurant Operations

### This is a delivery service simulator written in Python

### There are several different files in this repository

# 

## menuAssignment.py
This is were a customer would order a meal from any of the resteraunts. There are currently 5 different restaurants: Saffron, Macs, Heritage, Flower Child, & Stanley. A user would select a restaurant which returns the menu for said restaurant. They then enter in their order. Once complete this prints out a ticket/receipt and the order is saved to orders.txt.

## delivery.py
This is what the restaurant users would use to manage any given order. Once a ticket has been created it is given a unique order number, restaurant name, order itselfs, price, date, and status. A user would be able to select a restaurant and view all orders. They can also filter by date, status, and order number. Additionally, the user can also see which items have sold the most and how much money that is.

## bankUser.py
This .py takes no user input just reorganizes people1.txt in the desired format (CSV) in bankInfo.txt. This format is unique 6 digit ID #, first name, last name, state, DOB, email (created by taking the first letter of the first name and the last 3 letter of the last name and combining them with a random number 10-90 and random host), a random password, and a random dollar amount 100-10,000

## orderAndBankCombo.py
After an order from a customer is complete money from said customer is taken out of their account. This requires the customer to login in using their email and password.

If you have any questions feel free to send me an email: eliaseskind@gmail.com
