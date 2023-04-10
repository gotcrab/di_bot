from data.user_data import usr_dict

def add_words(words: str):
    pass

def get_words(group_name: dict):
    words = ''
    for word, meaning in group_name.items():
        jn = word + ' - ' + meaning
        words += f'|{jn:^38}|\n'

    return words

if __name__ == '__main__':
    print(get_words({'Go': 'идём', 'Skkkkktop': 'стоим'}))
