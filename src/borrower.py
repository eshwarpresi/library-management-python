from datetime import datetime, timedelta

class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = []  # List of dictionaries: {'book': book, 'due_date': due_date}

    def update_contact(self, new_contact):
        """Update borrower contact information"""
        self.contact = new_contact
        return True

    def borrow_book(self, book, due_date):
        """Add a book to borrower's borrowed list"""
        self.borrowed_books.append({
            'book': book,
            'due_date': due_date,
            'borrow_date': datetime.now()
        })

    def return_book(self, isbn):
        """Remove a book from borrower's borrowed list"""
        for i, borrowed in enumerate(self.borrowed_books):
            if borrowed['book'].isbn == isbn:
                returned_book = self.borrowed_books.pop(i)
                return returned_book
        return None

    def get_overdue_books(self):
        """Get list of overdue books"""
        overdue_books = []
        for borrowed in self.borrowed_books:
            if datetime.now() > borrowed['due_date']:
                overdue_books.append(borrowed)
        return overdue_books

    def get_borrowed_books(self):
        """Get all currently borrowed books"""
        return self.borrowed_books

    def __str__(self):
        return f"Borrower: {self.name} (ID: {self.membership_id}) - Contact: {self.contact}"

    def to_dict(self):
        """Convert borrower object to dictionary"""
        return {
            'name': self.name,
            'contact': self.contact,
            'membership_id': self.membership_id,
            'borrowed_books_count': len(self.borrowed_books)
        }
