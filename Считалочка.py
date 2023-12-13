N = int(input())
K = int(input())
people_in_ring = [i for i in range(1, N + 1)]
selected_person_index = 0

while len(people_in_ring) > 1:

    for i in range(1, K):
        
        next_person_index = selected_person_index + 1

        if next_person_index >= len(people_in_ring):
            next_person_index -= len(people_in_ring)

        selected_person_index = next_person_index

    people_in_ring.remove(people_in_ring[selected_person_index])

print(people_in_ring[0])