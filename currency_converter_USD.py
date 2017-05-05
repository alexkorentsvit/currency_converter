import requests

def currency_converter():
    '''
    The user enters the amount in US dollars (USD) 
    and the currency in which he wants to get the result.
    
    Returns the amount in the result currency, the entered amount and the currency.
    '''
    
    req = requests.get('http://api.fixer.io/latest?base=USD')
    data = req.json()
    flag1 = False
    flag2 = False

    #summa
    while flag1 == False:
        try:
            summa = float(input('Enter the amount (in USD) to convert: '))
        except ValueError:
            print("The entered amount is not a number")
        else:
            if summa <= 0:
                print("The entered amount must be positive")
            else:
                flag1 = True
            
    #currency
    while flag2 == False:
        to_currency = input('Enter the currency to convert: ')
        if to_currency in data['rates'].keys():
            flag2 = True
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
    return [result, summa, to_currency]

        
Answer = currency_converter()
print()  
print(str(Answer[1]) + ' ' + 'USD is '+ str(Answer[0])+' '+str(Answer[2]))