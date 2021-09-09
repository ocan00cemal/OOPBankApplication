import csv
from accounts import Accounts
import random

file_name = "accounts.txt"
name_input = ""
pin_input = ""

file = open(file_name,"a+")

def csv_a():

    with open(file_name, "a", newline ="") as csvfile:
        writer = csv.writer(csvfile)

        generate_no()
        writer.writerow([name_input, pin_input, card_no, 0])

def csv_update():

    with open(file_name, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')

        for i in Accounts.account_list:
            csvwriter.writerow([i.name, i.pin, i.card_no, i.balance])


def csv_open_create():
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)

        del Accounts.account_list[:]
        for row in reader:
            Accounts(row[0], row[1], int(row[2]), int(row[3]))

def generate_no():
    global card_no
    card_no = random.randint(100000, 999999)
    return card_no

def main():
    first_menu()

def first_menu():
    global name_input
    global pin_input

    csv_open_create()

    while True:

        print("1. Create an account\n"
              "2. Log into account\n"
              "0. Exit\n")

        main_menu_input = str(input())

        if main_menu_input == "1":

            name_input = str(input("Please write your name: "))
            pin_input = str(input("Please write a pin :").rstrip().lstrip())

            if name_input in Accounts.account_dict:
                print("This name is already taken. Please take another name.\n ")
            elif len(pin_input) != 4:
                print("Your pin must be 4 digit.\n ")

            else:
                csv_a()
                csv_open_create()

                text = "\nYou created an account. Your generated card number is {0}. Please note that and do not share it with anyone. \n"

                print(text.format(Accounts.account_list[-1].card_no, "\n"))

                second_menu()
                break


        elif main_menu_input == "2":

            while_breaker = True
            while while_breaker:

                name_input = str(input("Please write your name: "))
                pin_input = str(input("Please write pin: "))

                check_name_pin = False

                for i in Accounts.account_list:

                    if i.name == name_input and i.pin == pin_input:
                        print("\nYou are logged into the account.\n ")
                        check_name_pin = True
                        second_menu()
                        while_breaker = False
                        break

                if check_name_pin == False:
                    print("This name and pin pair does not match our records.\n ")
            break


        elif main_menu_input == "0":
            exit()

        else:
            print("Please insert 0,1 or 2 : \n")

def second_menu():
    while True:

        csv_update()

        scnd_menu_input = str(input("1. Balance\n"
              "2. Add income\n"
              "3. Do transfer\n"
              "4. Close Account\n"
              "5. Log out\n"
              "0. Exit\n"))

        if scnd_menu_input == "1":
            show_balance()

        elif scnd_menu_input == "2":
            add_income()

        elif scnd_menu_input == "3":
            money_transfer()

        elif scnd_menu_input == "4":
            close_account()

        elif scnd_menu_input == "5":
            main()

        elif scnd_menu_input == "0":
            exit()

def show_balance():
    balance = Accounts.account_dict[name_input].balance
    text = "You have {0} dolar(s) in your account.\n"
    print(text.format(balance))

def add_income():

    add_money_amount = int(input("How much money do you want to add?: \n"))
    Accounts.account_dict[name_input].balance += add_money_amount
    text = "{0} dolars are added to your account. New balance is {1} dolars.\n"
    print(text.format(add_money_amount, Accounts.account_dict[name_input].balance))
    csv_update()

def money_transfer():
    while True:

        user_card_no = int(input("Please insert the card no of yourself: \n"))

        if user_card_no != Accounts.account_dict[name_input].card_no:
            print("That is not your card no. Please try again. \n")
        else:
            break

    check = False
    while not check:

        target_card_no = int(input("Please insert the card no of target account: "))

        for target in Accounts.account_list:
            if target.name != name_input and target.card_no == target_card_no:
                temp = target
                check = True
                break

        if check == False:
            print("Try Again. ")

    money_transfer = int(input("How much money do you want to transfer: "))

    while True:
        if Accounts.account_dict[name_input].balance < money_transfer:
            print("You do not have that much money.")
        else:
            Accounts.account_dict[name_input].balance -= money_transfer
            temp.balance += money_transfer
            csv_update()
            text = "{0} dolars are transfered from your account to {1}."
            print(text.format(money_transfer, target_card_no))
        break

def close_account():
    while True:

        user_card_no = int(input("Please insert the card no of yourself: "))

        if user_card_no != Accounts.account_dict[name_input].card_no:
            print("That is not your card no. Please try again. \n")
        elif user_card_no == 0:
            exit()
        else:

            closed = Accounts.account_dict[name_input]

            del Accounts.account_dict[name_input]
            Accounts.account_list.remove(closed)

            csv_update()

            print("Your account has been closed.")
            exit()


main()