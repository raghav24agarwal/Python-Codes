from abc import ABC
# from Address import Address

from enum import Enum

class Test(Enum):
    BLUE = 1
    RED = 2
    GREEN = 3

print(Test.BLUE.value)

class ATMState(ABC):

    def insert_card(self, atm):
        print("Oops, something went wrong")

    def authenticate_pin(self, atm, card, pin):
        print("Oops, something went wrong")

    def select_operation(self, atm, card, tnxn_type):
        print("Oops, something went wrong")

    def cash_withdrawl(self, atm, card, withdraw_amt):
        print("Oops, something went wrong")

    def display_balance(self, atm, card):
        print("Oops, something went wrong")

    def return_card(self):
        print("Oops, something went wrong")

    def exit_atm(self, atm):
        print("Oops, something went wrong")


class IdleState(ATMState):

    def __init__(self, atm):
        self.atm = atm
        print("Idle State")

    def insert_card(self, atm):
        print("Card is inserted")
        self.atm.set_current_atm_state(HasCardState(self.atm))



class HasCardState(ATMState):

    def __init__(self, atm):
        self.atm = atm
        print("Has Card State")

    def has_card_state(self):
        print("Enter your pin")

    def authenticate_pin(self, atm, card, pin):
        is_correct_pin = card.check_pin(pin)

        if is_correct_pin:
            atm.set_current_atm_state("SelectOperationState")
        else:
            print("Invalid pin")
            self.exit_atm(atm)

    def exit_atm(self, atm):
        self.return_card()
        atm.set_current_atm_state("IdleState")
        print("Exiting...")

    def return_card(self):
        print("Please collect your card")


class SelectOperationState(ATMState):

    def select_operation_state(self):
        self.show_operations()

    def select_operation(self, atm, card, tnxn_type):
        if tnxn_type == "CASH_WITHDRAWL":
            atm.set_current_atm_state("CashWithdrawlState")
        elif tnxn_type == "BALANCE_CHECK":
            atm.set_current_atm_state("BalanceCheckState")
        else:
            print("Invalid option")
            self.exit_atm(atm)

    def exit_atm(self, atm):
        self.return_card()
        atm.set_current_atm_state("IdleState")
        print("Exiting...")

    def return_card(self):
        print("Please collect your card")

    def show_operations(self):
        print("Please select the operation")
        TransactionType.show_all_transaction_types()


class CashWithdrawalState(ATMState):

    def cash_withdrawl_state(self):
        print("Please enter the withdrawl amt")

    def cash_withdrawl(self, atm, card, withdraw_amt):
        if atm.get_balance() < withdraw_amt:
            print("Insufficient balance in ATM machine")
            self.exit(atm)

        elif card.get_bank_balance() < withdraw_amt:
            print("Insufficient balance in account")

        else:
            card.deduct_bank_balance(withdraw_amt)
            atm.deduct_atm_balance(withdraw_amt)

            # Chain of resposibility logic

            self.exit_atm(atm)


class ATM:

    def __init__(self):
        self.current_atm_state = IdleState(self)
        self.atm_balance = 0
        self.no_of_two_thousand = 0
        self.no_of_five_hundred = 0
        self.no_of_hundred = 0

    def set_current_atm_state(self, current_atm_state):
        self.current_atm_state = current_atm_state

    def get_current_atm_state(self):
        print(self.current_atm_state)
        return self.current_atm_state
    
    def get_atm_balance(self):
        print(self.atm_balance)
        return self.atm_balance

    def print_current_atm_balance(self):
        print(f"Total Balance - {self.atm_balance}")
        print(f"Two Thousand Notes - {self.no_of_two_thousand}")
        print(f"Five Hundred Notes - {self.no_of_five_hundred}")
        print(f"Hundred notes - {self.no_of_hundred}")

    def set_atm_balance(self, atm_balance, no_of_two_thousand, no_of_five_hundred, no_of_hundred):
        self.atm_balance = atm_balance
        self.no_of_two_thousand = no_of_two_thousand
        self.no_of_five_hundred = no_of_five_hundred
        self.no_of_hundred = no_of_hundred

    # get no of two thousand notes
    # get no of five hundred notes


class User:

    def __init__(self, name):
        self.name = name
        self.bank_account = None
        
    def set_bank_account(self, bank_account):
        self.bank_account = bank_account

        # Card card
        # BankAcc acc

    # get_card
    # set_card

class Card:

    def __init__(self, bank_account):
        self.card_number = "11223344"
        self.pin = "1234"
        self.holder_name = "Karthi"
        self.expiry_date = "2026-07-31"
        self.bank_account = bank_account


class BankAccount:

    def __init__(self):
        self.balance = 0
        self.card = Card(self)

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw_balance(self, amt):
        self.balance = self.balance - amt
        
        

class ATMRoom:

    def __init__(self, atm, user):
        self.atm = atm
        self.user = user

    def set_state(self, state):
        self.state = state

    def cycle(self):

        self.atm.get_current_atm_balance()


if __name__ == "__main__":

    user = User("Karthi")
    user.set_bank_account(BankAccount())
    user.bank_account.set_balance(3000)

    atm_room = ATMRoom(ATM(), user)
    atm_room.atm.set_atm_balance(3500, 1, 2, 5)
    atm_room.atm.print_current_atm_balance()

    atm_room.atm.get_current_atm_state()


    



# class ATM:

#     def __init__(self, address):
#         self.address = address

#     def get_address(self):
#         return self.address

    
# addr = Address(241699, 'indra nagar', 'delhi', 'delhi', 'india')


