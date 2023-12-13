N = int(input())
pancakes = {i: "залито тесто" for i in range(1, N + 1)}
time = N

while time:
    
    time -= 1
    for i in pancakes.keys():
        if i % 2 == 0:
            if pancakes[i] == 'перевёрнут':
                pancakes[i] = 'залито тесто'
            else:
                pancakes[i] = 'перевёрнут'

    time -= 1
    for i in pancakes.keys():
        if i % 3 == 0:
            if pancakes[i] == 'перевёрнут':
                pancakes[i] = 'залито тесто'
            else:
                pancakes[i] = 'перевёрнут'

    time -= 1
    for i in pancakes.keys():
        if i % 4 == 0:
            if pancakes[i] == 'перевёрнут':
                pancakes[i] = 'залито тесто'
            else:
                pancakes[i] = 'перевёрнут'

answer = len([i for i in pancakes.keys() if i % 2 != 0 and i % 3 != 0 and i % 4 != 0])
print(answer)