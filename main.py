from src.library import Library

def main():
    library = Library()
    initialize_sample_data(library)
    
    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Book Management")
        print("2. Borrower Management")
        print("3. Borrow/Return Books")
        print("4. Search Books")
        print("5. Reports")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            book_management_menu(library)
        elif choice == '2':
            borrower_management_menu(library)
        elif choice == '3':
            borrow_return_menu(library)
        elif choice == '4':
            search_books_menu(library)
        elif choice == '5':
            reports_menu(library)
        elif choice == '6':
            print("Thank you for using Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_management_menu(library):
    while True:
        print("\n=== BOOK MANAGEMENT ===")
        print("1. Add New Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. View All Books")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_new_book(library)
        elif choice == '2':
            update_book(library)
        elif choice == '3':
            remove_book(library)
        elif choice == '4':
            library.show_all_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_book(library):
    print("\n--- Add New Book ---")
    try:
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        genre = input("Enter genre: ").strip()
        quantity = int(input("Enter quantity: ").strip())
        
        if not all([title, author, isbn, genre]):
            print("Error: All fields are required.")
            return
        
        book = library.add_book(title, author, isbn, genre, quantity)
        if book:
            print(f"Book '{title}' added successfully!")
    except ValueError:
        print("Error: Quantity must be a number.")
    except Exception as e:
        print(f"Error adding book: {e}")

def update_book(library):
    print("\n--- Update Book ---")
    isbn = input("Enter ISBN of book to update: ").strip()
    
    book = library.find_book_by_isbn(isbn)
    if not book:
        print("Book not found.")
        return
    
    print(f"Current details: {book}")
    
    try:
        title = input("Enter new title (press Enter to keep current): ").strip()
        author = input("Enter new author (press Enter to keep current): ").strip()
        genre = input("Enter new genre (press Enter to keep current): ").strip()
        quantity_str = input("Enter new quantity (press Enter to keep current): ").strip()
        
        quantity = int(quantity_str) if quantity_str else None
        
        title = title if title else None
        author = author if author else None
        genre = genre if genre else None
        
        if library.update_book(isbn, title, author, genre, quantity):
            print("Book updated successfully!")
        else:
            print("Failed to update book.")
    except ValueError:
        print("Error: Quantity must be a number.")

def remove_book(library):
    print("\n--- Remove Book ---")
    isbn = input("Enter ISBN of book to remove: ").strip()
    library.remove_book(isbn)

def borrower_management_menu(library):
    while True:
        print("\n=== BORROWER MANAGEMENT ===")
        print("1. Add New Borrower")
        print("2. Update Borrower")
        print("3. Remove Borrower")
        print("4. View All Borrowers")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_new_borrower(library)
        elif choice == '2':
            update_borrower(library)
        elif choice == '3':
            remove_borrower(library)
        elif choice == '4':
            library.show_all_borrowers()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_borrower(library):
    print("\n--- Add New Borrower ---")
    name = input("Enter borrower name: ").strip()
    contact = input("Enter contact information: ").strip()
    membership_id = input("Enter membership ID: ").strip()
    
    if not all([name, contact, membership_id]):
        print("Error: All fields are required.")
        return
    
    borrower = library.add_borrower(name, contact, membership_id)
    if borrower:
        print(f"Borrower '{name}' added successfully!")

def update_borrower(library):
    print("\n--- Update Borrower ---")
    membership_id = input("Enter membership ID of borrower to update: ").strip()
    
    borrower = library.find_borrower_by_id(membership_id)
    if not borrower:
        print("Borrower not found.")
        return
    
    print(f"Current details: {borrower}")
    
    new_contact = input("Enter new contact (press Enter to keep current): ").strip()
    new_name = input("Enter new name (press Enter to keep current): ").strip()
    
    new_contact = new_contact if new_contact else None
    new_name = new_name if new_name else None
    
    if library.update_borrower(membership_id, new_contact, new_name):
        print("Borrower updated successfully!")
    else:
        print("Failed to update borrower.")

def remove_borrower(library):
    print("\n--- Remove Borrower ---")
    membership_id = input("Enter membership ID of borrower to remove: ").strip()
    library.remove_borrower(membership_id)

def borrow_return_menu(library):
    while True:
        print("\n=== BORROW/RETURN BOOKS ===")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Borrower's Books")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            borrow_book(library)
        elif choice == '2':
            return_book(library)
        elif choice == '3':
            view_borrower_books(library)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def borrow_book(library):
    print("\n--- Borrow Book ---")
    membership_id = input("Enter borrower membership ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()
    
    if not membership_id or not isbn:
        print("Error: Both membership ID and ISBN are required.")
        return
    
    library.borrow_book(membership_id, isbn)

def return_book(library):
    print("\n--- Return Book ---")
    membership_id = input("Enter borrower membership ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()
    
    if not membership_id or not isbn:
        print("Error: Both membership ID and ISBN are required.")
        return
    
    library.return_book(membership_id, isbn)

def view_borrower_books(library):
    print("\n--- Borrower's Books ---")
    membership_id = input("Enter borrower membership ID: ").strip()
    
    borrowed_books = library.get_borrower_books(membership_id)
    if borrowed_books is None:
        print("Borrower not found.")
        return
    
    if not borrowed_books:
        print("No books currently borrowed.")
        return
    
    print(f"\nBorrowed Books:")
    for i, borrowed in enumerate(borrowed_books, 1):
        due_date_str = borrowed['due_date'].strftime('%Y-%m-%d')
        status = "OVERDUE" if borrowed['due_date'] < library.get_current_date() else "On Time"
        print(f"{i}. {borrowed['book'].title} - Due: {due_date_str} - Status: {status}")

def search_books_menu(library):
    print("\n=== SEARCH BOOKS ===")
    title = input("Enter title to search (press Enter to skip): ").strip()
    author = input("Enter author to search (press Enter to skip): ").strip()
    genre = input("Enter genre to search (press Enter to skip): ").strip()
    
    if not any([title, author, genre]):
        library.show_all_books()
        return
    
    results = library.search_books(title, author, genre)
    
    if not results:
        print("No books found matching your criteria.")
        return
    
    print(f"\nFound {len(results)} book(s):")
    for i, book in enumerate(results, 1):
        status = "Available" if book.is_available() else "Not Available"
        print(f"{i}. {book} - Status: {status}")

def reports_menu(library):
    while True:
        print("\n=== REPORTS ===")
        print("1. Overdue Books Report")
        print("2. All Books Report")
        print("3. All Borrowers Report")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            overdue_books = library.get_overdue_books_report()
            if not overdue_books:
                print("No overdue books.")
            else:
                print("\n=== OVERDUE BOOKS REPORT ===")
                for i, overdue in enumerate(overdue_books, 1):
                    due_date_str = overdue['due_date'].strftime('%Y-%m-%d')
                    print(f"{i}. Book: {overdue['book'].title}")
                    print(f"   Borrower: {overdue['borrower'].name} (ID: {overdue['borrower'].membership_id})")
                    print(f"   Due Date: {due_date_str}")
                    print()
        elif choice == '2':
            library.show_all_books()
        elif choice == '3':
            library.show_all_borrowers()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def initialize_sample_data(library):
    sample_books = [
        ("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Fiction", 3),
        ("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction", 2),
        ("1984", "George Orwell", "9780451524935", "Science Fiction", 4),
        ("Pride and Prejudice", "Jane Austen", "9780141439518", "Romance", 2),
        ("The Hobbit", "J.R.R. Tolkien", "9780547928227", "Fantasy", 3)
    ]
    
    for title, author, isbn, genre, quantity in sample_books:
        library.add_book(title, author, isbn, genre, quantity)
    
    sample_borrowers = [
        ("John Smith", "john.smith@email.com", "MEM001"),
        ("Alice Johnson", "alice.j@email.com", "MEM002"),
        ("Bob Brown", "bob.brown@email.com", "MEM003")
    ]
    
    for name, contact, membership_id in sample_borrowers:
        library.add_borrower(name, contact, membership_id)

if __name__ == "__main__":
    main()
