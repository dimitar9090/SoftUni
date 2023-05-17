the_old_book = input()
current_checking_book = input()
book_is_found = False
check_counter = 0
while current_checking_book != 'No More Books':
    if current_checking_book == the_old_book:
        book_is_found = True
        break
    check_counter += 1
    current_checking_book = input()
if book_is_found:
    print(f'You checked {check_counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {check_counter} books.')
