import random
arr = [
    ['소환사의 협곡(랭크)', '소환사의 협곡(일반)', '칼바람 나락', 'U.R.F 모드'],
    ['TOP', 'Jungle', 'Mid', 'ADC', 'Supporter'],
    ['점화', '탈진', '유체화', '정화', '회복', '점멸']
]
game = arr[0][random.randint(0, 3)]
position = arr[1][random.randint(0, 4)]
banned_spell = arr[2][random.randint(0, 5)]

print(''' 
list''')
for list in arr:
    print(list)
print('''
=================================
''')
print('★ ☆ ★ ☆  Welcome to LOL Random Play Application ★ ☆ ★ ☆')
print('Random Picker Result')
print('이번에 진행할 게임 = [' + game + ']')
print('포지션 = [' + position + ']')
print('사용 불가 스펠 = [' + banned_spell + ']')
