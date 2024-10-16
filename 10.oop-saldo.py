class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def cash_deposit(self, cash):
        self.balance = self.balance + cash
    def cash_withdraw(self, cash):
        self.balance = self.balance - cash
    def display(self):
        print(f'Nomor Akun :', self.account_number)
        print(f'Nama Akun  :', self.name)
        print(f'Saldo Akun : Rp', self.balance)
nasabah_1 = BankAccount(12345, 'Fatmawati Mantika', 300_000_000)
nasabah_1.cash_deposit(50_000)
nasabah_1.cash_withdraw(50_000)
nasabah_1.display()
