import json
import difflib
from difflib  import SequenceMatcher 
from difflib  import get_close_matches 

my_dict = json.load(open("dictdata.json"))
def wordcheck(word):
    low_word = word.lower()
    if low_word in my_dict:
        test_dict = my_dict[low_word]
        return test_dict
    elif low_word.title() in my_dict:
        return my_dict[low_word.title()]
    elif low_word.upper() in my_dict:
        return my_dict[low_word.upper()]
    elif len(get_close_matches(low_word, my_dict.keys())) > 0:
        confirming = input("Did you mean %s instead? Enter 'Y' if yes and 'N' if no: " % get_close_matches(low_word, my_dict.keys())[0])
        if confirming == 'y':
            return my_dict[get_close_matches(low_word, my_dict.keys())[0]]
        elif confirming == 'n':
            return "That word doesn't exist, kindly check again"
        else:
            return "We don't understand your Entry"
    else:
        return "That word doesn't exist, Kindly check again" 

while True:
    user_word = input("Enter Word: ")
    output = wordcheck(user_word)
    if type(output) == list:
        for items in output:
            print(items)
    else:
        print(output)
    check_again = input("Wish to check again (Y or N): ")
    if check_again == "y":
        continue
    else:
        print("Thanks for using our Application, Goodbye!")
        break