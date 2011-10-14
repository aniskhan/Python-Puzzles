#!/usr/bin/env python
# encoding: utf-8
"""
stockportfolio.py

Created by Anisa Khandkar on 2011-10-10.
Copyright (c) 2011. All rights reserved.

Suppose the file portfolio.dat contains information about some stocks that you purchased. There are three columns showing the name, number of shares, and purchase price.
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44

A different file, prices.dat, contains a list of current stock prices. The columns in this file are the stock name and price.
GOOG 509.71
YHOO 28.34
IBM 106.11
MSFT 30.47
AAPL 122.13
SUNW 5.01
AA 39.91
CAT 78.58
GE 37.38
HPQ 38.15

Write a program that reads the stock portfolio in portfolio.dat, the stock prices from prices.dat, and prints out how much the entire portfolio has increased or decreased in value.

"""

import sys
import os
from decimal import *



portfolio = open('portfolio.dat', 'r').readlines()
stockcost = []
sharesdict = {}

for line in portfolio:
	stock,shares,price = line.split( )
	sharesdict.setdefault(stock, 0)
	sharesdict[stock] += Decimal(shares) #this adds the share count where the same stock was purchased on more than one occasion

	
	
stockinfo = (line.split() for line in portfolio)
for item in stockinfo:
	stockcost.append (Decimal(item[1])*Decimal(item[2]))

portfolio_cost = sum(stockcost)

#print portfolio_cost




prices = open('prices.dat').readlines()

stockvalue = []
pricedict = {}
for line in prices:
	stock,value = line.split( )
	pricedict[stock] = Decimal(value)

for k in pricedict:
	if k in sharesdict:
		stockvalue.append(sharesdict[k]*pricedict[k])


portfolio_value = sum(stockvalue)

#print portfolio_value

print (portfolio_value) - (portfolio_cost)






