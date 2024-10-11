def all_variants(text):
    if not text:
        yield 'Текс не введен!'
        return
    else:
        for x in range(len(text)):
            for y in range(x + 1, len(text) + 1):
                yield text[x:y]


input_text = input('Введите текст: ')


a = all_variants(input_text)
for i in a:
    print(i)
