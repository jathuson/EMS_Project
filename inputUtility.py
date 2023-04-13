import datetime
import re

class OutOfRangeError(Exception): pass


class InvalidOption(Exception): pass


def getPhone() -> str:
    while True:
        try:
            phone = input("PLease Enter the Department phone number in the format (xxx)-xxx-xxxx")
            if re.search("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$",phone):
                return phone
            else:
                raise InvalidOption
        except InvalidOption:
            print(f"Error: {phone} is not in the correct format")


class InvalidOption(Exception): pass


def getName() -> tuple:
    while True:  # While loop repeats until valid input is accepted
        try:
            nameLis = input("Please Enter your Name:\n").split(" ")  # Split on the space
            first = " ".join([x for x in nameLis if x != nameLis[-1]])
            last = nameLis[-1]
            if len(first) == 0:  # Ensure first name is not null
                raise TypeError("First Name is Null")
            elif len(last) == 0:  # Ensure last name is not null
                raise TypeError("Last Name is Null")
            # first = first.lower().capitalize()  # Correct Capitalization
            # last = last.lower().capitalize()
            break  # Escape the while loop and move on
        except ValueError:  # If input cannot be processed correctly it is not valid and the code loops
            print("Error! Name must be in [first] [last] format with space")
            pass
        except TypeError:
            print("Error! One or more of your names is NULL")
            pass
    return first, last


def acceptStr(inpStr: str, memb: set) -> str:
    while True:
        try:
            inp: str = input(inpStr + "\n").lower().strip()
            if inp not in memb:
                raise InvalidOption
            break
        except TypeError:
            print(f"Error in processing input")
        except InvalidOption:
            print(f"{inp} is not a valid option. Please choose from {memb}")
    return inp


def acceptInt(inpStr: str, low: int, high: int) -> int:
    while True:
        try:
            inp: str = input(inpStr + "\n")
            num: int = int(inp)
            if num < low or num > high:
                raise OutOfRangeError
            break
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except OutOfRangeError:
            print(f"Number is out of range!")
    return num


def getDate():
    while True:
        try:
            inp = input("Please enter the employee start date in the format [YYYY] [MM] [DD]")
            yr, month, day = inp.split(" ")
            yr, month, day = int(yr), int(month), int(day)
            return datetime.date(yr, month, day)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
