def do_change():

    blocks = {}

    symbols_start = []

    f = open(f'data/slovar.txt', encoding='utf8')
    text = f.readlines()

    for el in text:
        el = el.strip()
        el = el.split(': ')
        blocks[el[0]] = el[1]

    for sym in blocks.keys():
        symbols_start.append(sym)

    print('Выберите символ')
    symbol = input().upper()

    print('Выберите текстуру')
    tex = input()

    print('Выбери номер (от 1 до 5)')
    number = int(input()) - 1

    symbols = []

    key_del = el_del = ''

    if symbol not in symbols_start and 0 <= number <= 4:
        file = open('data/slovar.txt', 'w', encoding='utf8')

        for num, value in enumerate(blocks.items()):
            key = value[0]
            el = value[1]
            if num == number:
                file.write(f'{symbol}: data/{tex}')
                symbols.append(symbol)
                key_del, el_del = key, el
            else:
                symbols.append(key)
                file.write(f'{key}: {el}')
            file.write('\n')

        symbols.append(key_del)
        file.write(f'{key_del}: {el_del}')

        file.close()

        do_new_list_of_blocks()


def do_new_list_of_blocks():
    f = open('data/slovar.txt', 'r', encoding='utf8')
    out = open('data/bloks_list.txt', 'w', encoding='utf8')
    text = f.readlines()
    for el in text:
        el = el.strip()
        el = el[0]
        out.write(el + '\n')
    f.close()
    out.close()


def get_list_of_blocks():
    f = open('data/bloks_list.txt', 'r', encoding='utf8')
    text = f.readlines()
    lst = []
    for i in text:
        i = i.strip()
        lst.append(i)
    return lst


def get_dict():
    blocks = {}

    f = open(f'data/slovar.txt', encoding='utf8')
    text = f.readlines()

    for el in text:
        el = el.strip()
        el = el.split(': ')
        blocks[el[0]] = el[1]

    return blocks


def reset_all():
    with open('data/map_0.txt', 'r', encoding='utf8') as place:
        f = open('data/map.txt', 'w', encoding='utf8')
        text = place.readlines()
        for line in text:
            line = line.rstrip()
            f.write(line)
            f.write('\n')

    with open('data/slovar_0.txt', 'r', encoding='utf8') as dic:
        f = open('data/slovar.txt', 'w', encoding='utf8')
        text = dic.readlines()
        for line in text:
            line = line.rstrip()
            f.write(line)
            f.write('\n')

    with open('data/bloks_list_0.txt', 'r', encoding='utf8') as lst:
        f = open('data/bloks_list.txt', 'w', encoding='utf8')
        text = lst.readlines()
        for line in text:
            line = line.rstrip()
            f.write(line)
            f.write('\n')

