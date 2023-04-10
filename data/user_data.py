from dataclasses import dataclass

usr_dict: dict[int, [dict[str, dict[str, str]]]] = {}

@dataclass
class User:
    user_id: str

@dataclass
class UserDict:
    dict_name: str
    tr_from: str
    tr_to: str
    words: dict[str, str]

    def __call__(self):
        print(self.dict_name)
        print(f'from {self.tr_from} to {self.tr_to}')
        for key, value in self.words.items():
            print(f'{key} - {value}')
        return print(len(self))

    def __len__(self):
        return len(self.words)

# d: UserDict = UserDict('first', 'eng', 'rus', {'mail': 'pochta', 'gas': 'benzin', 'one': 'raz'})

# if __name__ == '__main__':
    # d()
    # print(len(d))