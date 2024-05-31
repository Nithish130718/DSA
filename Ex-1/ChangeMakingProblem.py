# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:05:40 2023

@author: NITHISH S

Change-Making Problem. 

It involves determining the minimum number of currency notes (or coins) needed to make a given amount of change from a larger payment. 
The goal is to provide the change in such a way that it is optimal, meaning it uses the least number of currency denominations possible.
"""


def balance(bill, given):

    change = given - bill

    str = ""

    if change % 2000 > 0:
        if change % 2000 == 1:
            str += "1 two thousand rupee note"
            change = change - change // 2000 * 2000
        elif change % 2000 > 1:
            str += str(change % 2000) + "two thousand rupee note"
            change = change - change // 2000 * 2000

    if change % 500 > 0:
        if change % 500 == 1:
            str += "1 five hundred rupee note"
            change = change - change // 500 * 500
        elif change % 500 > 1:
            str += str(change % 2000) + "five hundred rupee notes"
            change = change - change // 500 * 500

    if change % 200 > 0:
        if change % 500 == 1:
            str += "1 two hundred rupee note"
            change = change - change // 200 * 200
        elif change % 500 > 1:
            str += str(change % 2000) + "two hundred rupee notes"
            change = change - change // 200 * 200

    if change % 100 > 0:
        if change % 100 == 1:
            str += "1 hundred rupee note"
            change = change - change // 100 * 100
        elif change % 100 > 1:
            str += str(change % 2000) + "hundred rupee notes"
            change = change - change // 100 * 100

    if change % 50 > 0:
        if change % 50 == 1:
            str += "1 fifty rupee note"
            change = change - change // 50 * 50
        elif change % 500 > 1:
            str += str(change % 2000) + "fifty rupee notes"
            change = change - change // 50 * 50

    print(str)


bill = int(input("Enter the bill amount:"))
given = int(input("Enter the given amount by the user:"))

if bill < given:
    balance(bill, given)
