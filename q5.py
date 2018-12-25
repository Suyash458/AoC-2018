import string

polymer = open('q5.txt', 'r').read()

def is_reactive(a, b):
    return (a.upper() == b.upper()) and ((a.isupper() and b.islower()) or (a.islower() and b.isupper()))

pairs = ['{}{}'.format(i, i.upper()) for i in string.ascii_lowercase] + ['{}{}'.format(i.upper(), i) for i in string.ascii_lowercase]

def get_polymer_length(polymer):
    changed = True
    original_polymer = polymer
    while changed:
        for pair in pairs:
            polymer = polymer.replace(pair, '')
        if original_polymer != polymer:
            original_polymer = polymer
        else:
            changed = False
    return len(polymer)

print(get_polymer_length(polymer))

polymer_lengths = [get_polymer_length(polymer.replace(i, '').replace(i.upper(), '')) for i in set(polymer.lower())]
print(min(polymer_lengths))