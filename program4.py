alphabet = ['A', 'O', 'U']
count = 0
for b1 in alphabet:
    for b2 in alphabet:
        for b3 in alphabet:
            for b4 in alphabet:
                for b5 in alphabet:
                    count += 1
                    print(count, ':', b1, b2, b3, b4, b5)