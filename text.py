import copy


class BankAccount:
    def __init__(self, surname='', name='', personal_code='', account_number='', balance=0, currency=''):
        """
        Метод инициализации объекта BankAccount.

        :param surname: фамилия владельца счета
        :param name: имя владельца счета
        :param personal_code: персональный код владельца счета
        :param account_number: номер банковского счета
        :param balance: баланс счета
        :param currency: валюта счета
        """
        self.surname = surname
        self.name = name
        self.personal_code = personal_code
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def __str__(self):
        """
        Метод, который возвращает строковое представление объекта BankAccount.

        :return: строковое представление объекта BankAccount
        """
        return f"{self.surname};{self.name};{self.personal_code};{self.account_number};{self.balance};{self.currency}"

    def __eq__(self, other):
        """
        Метод сравнения объектов BankAccount по номеру банковского счета.

        :param other: другой объект BankAccount
        :return: True, если номера счетов равны, иначе False
        """
        return isinstance(other, BankAccount) and self.account_number == other.account_number

    def __copy__(self):
        """
        Метод, который создает поверхностную копию объекта BankAccount.

        :return: поверхностная копия объекта BankAccount
        """
        return BankAccount(self.surname, self.name, self.personal_code, self.account_number, self.balance, self.currency)

    def __deepcopy__(self, memo):
        """
        Метод, который создает глубокую копию объекта BankAccount.

        :param memo: словарь, используемый для хранения уже скопированных объектов
        :return: глубокая копия объекта BankAccount
        """
        return BankAccount(copy.deepcopy(self.surname, memo), copy.deepcopy(self.name, memo), copy.deepcopy(self.personal_code, memo),
                           copy.deepcopy(self.account_number, memo), copy.deepcopy(self.balance, memo), copy.deepcopy(self.currency, memo))

    def read_from_file(self, line):
        """
        Метод, который считывает данные объекта BankAccount из строки.

        :param line: строка, содержащая данные объекта BankAccount
        """
        self.surname, self.name, self.personal_code, self.account_number, self.balance, self.currency = line.strip().split(";")

    def write_to_file(self, file):
        """
        Метод, который записывает данные в файл.

        :param file: файл, в который записываются данные 
        """
        file.write(str(self) + "\n")


if __name__ == '__main__':
    with open('bank_accounts.txt') as f:
        accounts = []
        for line in f:
            account = BankAccount()
            account.read_from_file(line)
            accounts.append(account)

    for account in accounts:
        print(account)
