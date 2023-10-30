import itertools

length = int(input())
sacred_words = filter(lambda x: x.count('TOR') == 2, map(''.join, itertools.product('TOR', repeat=length)))
sorted_sacred_words = sorted(sacred_words)


print(', '.join(sorted_sacred_words))
