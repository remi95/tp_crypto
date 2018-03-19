#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import cryptocompare

def getList() :
    listCoins = cryptocompare.get_coin_list(format=True)
    for coin in listCoins:
        print(coin)

def getCoinPrice(coin):
    if (cryptocompare.get_price(coin)):
        price = cryptocompare.get_price(coin)
        print(price.get(coin).get('EUR'), '€\n')
    else:
        print('La monnaie', coin,'ne semble pas exister.\n')


while (True):
    search = input('De quelle monnaie voulez-vous voir le prix ?\n"list" pour voir l\'ensemble des monnaies.)\n')

    if (search == 'list'):
        getList()
    else:
        getCoinPrice(search)
