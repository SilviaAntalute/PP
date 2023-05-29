from more_itertools import map_reduce

text = "Aceasta este o propozitie de test pentru algoritm."

def map_function(word):
    return (word[0], [word])

def reduce_function(key, values):
    return (key, values)

result = map_reduce(text.split(), map_function, reduce_function)

sorted_pairs = sorted(result, key=lambda pair: pair[0])
for pair in sorted_pairs:
    print(pair)