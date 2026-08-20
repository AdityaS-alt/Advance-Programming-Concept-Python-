books = ["Python", "Java", "C", "C++"]

new_book = input("Enter new book: ")
books.append(new_book)

search = input("Enter book to search: ")

if search in books:
    print("Book Found")
else:
    print("Book Not Found")

remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)

print("Book List:", books)
print("Total Books:", len(books))