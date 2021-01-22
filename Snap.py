#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:09:48 2020

@author: pundir
"""

#Snap

#GENERAL INFO
print("TO PlAY GAME TYPE: resume")
print("FOR HELP! TYPE: help")
from random import shuffle

def createDeck():
    Deck = []
    
    faceValues = ["A", "J", "Q", "K"]
    for i in range(4):#There are 4 different suits
        for card in range(2,11):#Adding numbers 2 to 10
            Deck.append(str(card))
            
        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)
    return Deck

cardDeck = createDeck()

def divide(l,n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
    
n = 13

deck = list(divide(cardDeck,n))
i = input("WHAT YOU WANT TO DO: ")
#print(deck)



#--------------HELP--------------
if(i == "help"):
    print("1. Deal out the cards around all the players so eaxh player has a pile of cards which they has a pileof cards which they place facedown.")
    print("2. The first player turn over the card at th etop of their pile in the center.")
    print("3. The Next player to their left turns over the card at top of their pile and adds it to the centre pile, and so on.")
    print("4. If there are two cards that match, the first player to yell 'SNAP' wins the cards in the middle.")
    print("5. If a player runs out of cards, they lose.") 

#-------------RESUME-------------
if(i == "resume"):
    print(cardDeck)    
    #PLAYERS
    
    player1 = input("Player 1, Enter Your Name: ")
    player2 = input("Player 2, Enter Your Name: ")
    player3 = input("Player 3, Enter Your Name: ")
    player4 = input("Player 4, Enter Your Name: ")
    while(True):    
        i1 = int(input("Enter 1,2,3,4 for player chance: "))
        if(i1 == 1):
            print(player1, ", TURN:")
            p1 = player1
            p1 = deck[0]
            p1 = [deck[0].pop()]
            print(p1)
            
        if(i1 == 2):
            print(player2, ", TURN:")
            p2 = player2
            p2 = deck[1]
            p2 = [deck[1].pop()]
            print(p2)
        
        if(i1 == 3):
            print(player3, ", TURN:")
            player3 = deck[2]
            player3 = [deck[2].pop()]
            print(player3)
        
        if(i1 == 4):
            print(player4, ", TURN:")
            player4 = deck[3]
            player4 = [deck[3].pop()]
            print(player4)
        
        #condition for 1st player
        if(player1 == player2):
            print(player1,", SNAP")
        elif(player1 == player3):
            print(player1,", SNAP")
        elif(player1 == player4):
            print(player1,", SNAP")
        
        #condition for 2nd player
        elif(player2 == player1):
            print(player2,", SNAP")
        elif(player2 == player3):
            print(player2,", SNAP")
        elif(player2 == player4):
            print(player2,", SNAP")
            
        #condition for 3rd player    
        elif(player3 == player1):
            print(player3,", SNAP")
        elif(player3 == player2):
            print(player3,", SNAP")
        elif(player3 == player4):
            print(player3,", SNAP")
            
        #condition for 4th player    
        elif(player4 == player1):
            print(player4,", SNAP")
        elif(player4 == player2):
            print(player4,", SNAP")
        elif(player4 == player3):
            print(player4,", SNAP")
        