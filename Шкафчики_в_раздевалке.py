N = int(input())
S = int(input())
closets = [i for i in range(1, N + 1)]
answer = 0
while sum(closets) != S:
    if sum(closets) > S:
        needed_number = sum(closets) - S
        if closets[-1] > needed_number:
            if needed_number in closets:
                closets.remove(needed_number)
                needed_number = 0
            else:
                for i in closets:
                    if i < needed_number:
                        needed_number -= 1
                        closets.remove(i)
                        break
            
        else:
            needed_number -= closets[-1]
            closets.pop()
    else:
        needed_number = S - sum(closets)

        for index, i in enumerate(closets):

            closets[index] += needed_number
            break

    answer += 1

print(answer)