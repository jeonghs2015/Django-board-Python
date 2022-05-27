champions = [
    {'name':'Draven', 'address':'Noxus', 'interest':'Spinning Axe'},
    {'name':'Lee Sin', 'address':'Ionia', 'interest':'Martial Arts'},
    {'name':'Garen', 'address':'Demacia', 'interest':'Judgement'}
]

print('==== champions ====')
for champion in champions:
    for key in champion:
     print(key, ' : ', champion[key])
    print('----------------------------------------------------------------------')