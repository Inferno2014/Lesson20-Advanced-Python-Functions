books = ["Geronimo Stilton","Perck Jackson","Harry Potter","Sudha Murty","Ruskin Bond"]
copy_counts = [20, 9, 0, 11, 15]
library = {book: count for book, count in zip(books, copy_counts)}
print("Full Library Stock:", library)
available_books = [book for book in books if library[book] > 0]
print("Books Available:", available_books)
chosen_book = input("Which book do you want to borrow? ")
if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, "is not available!")
library[chosen_book] = library[chosen_book] - 1
print(chosen_book, "borrowed! Remaining copies:", library[chosen_book])