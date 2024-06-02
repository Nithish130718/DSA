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
    res = ""

    if change >= 2000:
        num = change // 2000
        res += f"{num} two thousand rupee note{'s' if num > 1 else ''}\n"
        change = change % 2000

    if change >= 500:
        num = change // 500
        res += f"{num} five hundred rupee note{'s' if num > 1 else ''}\n"
        change = change % 500

    if change >= 200:
        num = change // 200
        res += f"{num} two hundred rupee note{'s' if num > 1 else ''}\n"
        change = change % 200

    if change >= 100:
        num = change // 100
        res += f"{num} hundred rupee note{'s' if num > 1 else ''}\n"
        change = change % 100

    if change >= 50:
        num = change // 50
        res += f"{num} fifty rupee note{'s' if num > 1 else ''}\n"
        change = change % 50

    if change >= 20:
        num = change // 20
        res += f"{num} twenty rupee note{'s' if num > 1 else ''}\n"
        change = change % 20

    if change >= 10:
        num = change // 10
        res += f"{num} ten rupee note{'s' if num > 1 else ''}\n"
        change = change % 10

    if change >= 5:
        num = change // 5
        res += f"{num} five rupee coin{'s' if num > 1 else ''}\n"
        change = change % 5

    if change >= 2:
        num = change // 2
        res += f"{num} two rupee coin{'s' if num > 1 else ''}\n"
        change = change % 2

    if change >= 1:
        num = change // 1
        res += f"{num} one rupee coin{'s' if num > 1 else ''}\n"
        change = change % 1

    print(res)


bill = int(input("Enter the bill amount: "))
given = int(input("Enter the given amount by the user: "))

if bill < given:
    balance(bill, given)
else:
    print("The given amount should be greater than the bill amount.")
