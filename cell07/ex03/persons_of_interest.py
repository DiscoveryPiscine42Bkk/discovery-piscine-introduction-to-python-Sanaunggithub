#!/c/Python313/python

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(women_scientists):
    sorted_scientists = sorted(women_scientists.values(), key=lambda person: person['date_of_birth'])

    for person in sorted_scientists:
        print(f"{person['name']} was born in {person['date_of_birth']}.")

famous_births(women_scientists)