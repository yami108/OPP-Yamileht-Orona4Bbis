from books import book
from users import user
from library import library

# Instances
book1 = book("001", "OOP", "John Lenon", "BBC")
book2 = book("002", "Python for dummies", "Stef Maruzh", "For dummies")
user1 = user("001", "Yam", "Yami123")

library = library()

# Req #1 & #2: Register books and user
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)

library.show_books()

# Req #3: Borrow a book
library.borrow_book(book1, user1)

# Req #4: Can't borrow an already borrowed book
library.borrow_book(book1, user1)

# Req #5: Return a book
library.return_book(book1)

#Requeriments
#1. The system must allow register books.
#2. The system must allow register user.
#3. The system must allow a book to be borrowed by a user.
#4. A book that has already been borrowed can't be borrowed again.
#5. The system must allow a book to returned. 