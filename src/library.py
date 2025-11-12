from datetime import datetime, timedelta
from .book import Book
from .borrower import Borrower

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []
        self.borrowing_period_days = 14

    def add_book(self, title, author, isbn, genre, quantity):
        for book in self.books:
            if book.isbn == isbn:
                print(f"Book with ISBN {isbn} already exists. Updating quantity instead.")
                book.quantity += quantity
                return book
        
        new_book = Book(title, author, isbn, genre, quantity)
        self.books.append(new_book)
        return new_book

    def update_book(self, isbn, title=None, author=None, genre=None, quantity=None):
        book = self.find_book_by_isbn(isbn)
        if book:
            if title or author or genre:
                book.update_details(title, author, genre)
            if quantity is not None:
                book.update_quantity(quantity)
            return True
        return False

    def remove_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                if self.is_book_borrowed(isbn):
                    print(f"Cannot remove book '{book.title}' as copies are currently borrowed.")
                    return False
                removed_book = self.books.pop(i)
                print(f"Book '{removed_book.title}' removed successfully.")
                return True
        print(f"Book with ISBN {isbn} not found.")
        return False

    def add_borrower(self, name, contact, membership_id):
        for borrower in self.borrowers:
            if borrower.membership_id == membership_id:
                print(f"Borrower with membership ID {membership_id} already exists.")
                return None
        
        new_borrower = Borrower(name, contact, membership_id)
        self.borrowers.append(new_borrower)
        return new_borrower

    def update_borrower(self, membership_id, new_contact=None, new_name=None):
        borrower = self.find_borrower_by_id(membership_id)
        if borrower:
            if new_contact:
                borrower.update_contact(new_contact)
            if new_name:
                borrower.name = new_name
            return True
        return False

    def remove_borrower(self, membership_id):
        borrower = self.find_borrower_by_id(membership_id)
        if borrower:
            if borrower.borrowed_books:
                print(f"Cannot remove borrower {borrower.name} as they have borrowed books.")
                return False
            self.borrowers.remove(borrower)
            print(f"Borrower {borrower.name} removed successfully.")
            return True
        print(f"Borrower with membership ID {membership_id} not found.")
        return False

    def borrow_book(self, membership_id, isbn):
        borrower = self.find_borrower_by_id(membership_id)
        book = self.find_book_by_isbn(isbn)
        
        if not borrower:
            print(f"Borrower with ID {membership_id} not found.")
            return False
        
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return False
        
        if not book.is_available():
            print(f"Book '{book.title}' is not available for borrowing.")
            return False
        
        due_date = datetime.now() + timedelta(days=self.borrowing_period_days)
        book.quantity -= 1
        borrower.borrow_book(book, due_date)
        
        print(f"Book '{book.title}' borrowed successfully. Due date: {due_date.strftime('%Y-%m-%d')}")
        return True

    def return_book(self, membership_id, isbn):
        borrower = self.find_borrower_by_id(membership_id)
        book = self.find_book_by_isbn(isbn)
        
        if not borrower:
            print(f"Borrower with ID {membership_id} not found.")
            return False
        
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return False
        
        returned = borrower.return_book(isbn)
        if returned:
            book.quantity += 1
            if datetime.now() > returned['due_date']:
                print(f"Book '{book.title}' returned successfully. Note: This book was overdue.")
            else:
                print(f"Book '{book.title}' returned successfully.")
            return True
        else:
            print(f"Borrower {borrower.name} doesn't have this book borrowed.")
            return False

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books:
            match = True
            if title and title.lower() not in book.title.lower():
                match = False
            if author and author.lower() not in book.author.lower():
                match = False
            if genre and genre.lower() not in book.genre.lower():
                match = False
            
            if match:
                results.append(book)
        return results

    def show_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        
        print("\n=== ALL BOOKS IN LIBRARY ===")
        for i, book in enumerate(self.books, 1):
            status = "Available" if book.is_available() else "Not Available"
            print(f"{i}. {book} - Status: {status}")

    def show_all_borrowers(self):
        if not self.borrowers:
            print("No borrowers registered.")
            return
        
        print("\n=== ALL BORROWERS ===")
        for i, borrower in enumerate(self.borrowers, 1):
            print(f"{i}. {borrower} - Borrowed Books: {len(borrower.borrowed_books)}")

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_borrower_by_id(self, membership_id):
        for borrower in self.borrowers:
            if borrower.membership_id == membership_id:
                return borrower
        return None

    def is_book_borrowed(self, isbn):
        for borrower in self.borrowers:
            for borrowed in borrower.borrowed_books:
                if borrowed['book'].isbn == isbn:
                    return True
        return False

    def get_overdue_books_report(self):
        overdue_books = []
        for borrower in self.borrowers:
            borrower_overdue = borrower.get_overdue_books()
            for overdue in borrower_overdue:
                overdue_books.append({
                    'borrower': borrower,
                    'book': overdue['book'],
                    'due_date': overdue['due_date']
                })
        return overdue_books

    def get_borrower_books(self, membership_id):
        borrower = self.find_borrower_by_id(membership_id)
        if borrower:
            return borrower.get_borrowed_books()
        return []

    def get_current_date(self):
        return datetime.now()
