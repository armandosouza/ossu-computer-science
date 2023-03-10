import inflect
p = inflect.engine()

adieu = 'Adieu, adieu, to'
list_names = list()
while True:
    try:
        name = input()
        if name != '':
            list_names.append(name)
        else:
            pass
    except EOFError:
        print(adieu, p.join(list_names, final_sep=","))
        break