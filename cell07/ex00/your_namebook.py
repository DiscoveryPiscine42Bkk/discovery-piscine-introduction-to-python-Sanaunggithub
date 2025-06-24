#!/c/Python313/python

def array_of_names(d):
    lst = []

    for first, last in d.items():
        name = first + " " + last
        lst.append(name.title())

    return lst

persons = {
    "jean" : "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier"
}

print(array_of_names(persons))