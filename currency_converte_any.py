import requests

def currency_converter():
    '''
    The user enters the base (currency that he wants to convert),
    the amount and the currency in which he wants to get the result.
    
    Returns the amount in the result currency, the base, the entered amount and the currency.
    '''
    
    flag1 = False
    flag2 = False
    flag3 = False
    
    #base
    while flag1 == False:
        try:
            base = input('Enter the base: ')
            link = 'http://api.fixer.io/latest?base={}'.format(base)
            req = requests.get(link)
            data = req.json()
            data['rates'].keys()
        except KeyError:
            print('There is no such currency')
        else:
            flag1 = True
    
    #summa
    while flag2 == False:
        try:
            summa = float(input('Enter the amount to convert: '))
        except ValueError:
            print("The entered amount is not a number")
        else:
            if summa <= 0:
                print("The entered amount must be positive")
            else:
                flag2 = True

    #currency
    while flag3 == False:
        to_currency = input('Enter the currency to convert: ')
        if to_currency in data['rates'].keys():
            flag3 = True
        else:
            print()
            print('There is no such currency')
            print('Available currencies: ', end =' ')
            for currency in data['rates'].keys():
                print(currency,end =' ')
            print()         

    for currency in data['rates'].keys():
        if to_currency == currency:
            result = data['rates'][currency] * summa
    return [result, base, summa, to_currency]



Answer = currency_converter()
print()  
print(str(Answer[2]) + ' ' + str(Answer[1]) + ' is ' + str(Answer[0])+' '+str(Answer[3]))