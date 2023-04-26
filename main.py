import sys
import pyperclip

print(f"\nHenlo👋")
while True:
    print("Add quotation marks?\ntype: \ny/n")
    user_choise = input()
    todo = pyperclip.paste()
    print("Enter splitter: N - for new lines, space character or any other character")
    user_splitter = input()
    if user_splitter == 'N':
        list_with_input = list(todo.split('\n'))
    else:
        list_with_input = list(todo.split(user_splitter))

    if user_choise == 'y':
        print("Added quotation marks with commas, it's already in clipboard.\nVerify content ↓")
        for i in range(len(list_with_input)):
            list_with_input[i] = "'" + list_with_input[i] + "'"
            if i < (len(list_with_input) - 1):
                list_with_input[i] = list_with_input[i] + ','
    if user_choise == 'n':
        print("Commas added, it's already in clipboard.\nVerify content ↓")
        for i in range(len(list_with_input)):
            if i < (len(list_with_input) - 1):
                list_with_input[i] = list_with_input[i] + ','

    done = ' '.join(list_with_input)
    pyperclip.copy(done)
    print("In clipboard:\n" + done)
    print("\nif output is not as expected, try again by copying original valueas and running the program\n--exit--")
    sys.exit()
