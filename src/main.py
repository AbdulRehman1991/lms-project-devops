import tkinter as tk # Main GUI library
from tkinter import ttk, messagebox, simpledialog
from authent import authenticate_user
from book import Book, BookManager
from search import search_by_title, search_by_author, search_by_isbn
from member import MemberModule
from issue_return import IssueReturn
from library import LibraryManagementModule
from datetime import datetime


class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")
        self.book_manager = BookManager()
        self.member_module = MemberModule()
        self.issue_return = IssueReturn()
        self.library_module = LibraryManagementModule()
        self.current_user = None

        # Color scheme
        self.colors = {
            "primary": "#1F0318",    # Dark Purple for headers/backgrounds
            "secondary": "#8C705F",  # Beaver for buttons
            "accent": "#7F534B",     # Bole for highlights
            "text": "#FFFFFF",       # White for text on dark backgrounds
            "background": "#E5F2C9", # Pale Spring Bud for main background
            "error": "#E74C3C"       # Red for errors
        }

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("TButton", padding=6, font=("Helvetica", 10),
                             background=self.colors["secondary"],
                             foreground="#000000")  # Black text for buttons
        self.style.configure("TLabel", font=("Helvetica", 10),
                             background=self.colors["background"],
                             foreground=self.colors["primary"])
        self.style.configure("Treeview", font=("Helvetica", 10), rowheight=25,
                             background=self.colors["background"],
                             foreground=self.colors["primary"])
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"),
                             background=self.colors["primary"],
                             foreground=self.colors["text"])
        self.style.map("TButton", background=[("active", self.colors["accent"])],
                       foreground=[("active", "#000000")])  # Black on hover
        self.style.configure("Custom.TFrame", background=self.colors["background"])
        self.style.configure("Custom.TLabelframe",
                             background=self.colors["background"],
                             foreground=self.colors["primary"])
        self.style.configure("Custom.TLabelframe.Label",
                             background=self.colors["background"],
                             foreground=self.colors["primary"])

        self.root.configure(bg=self.colors["background"])
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_window()
        frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        frame.pack(expand=True)

        ttk.Label(frame, text="Library Management System",
                  font=("Helvetica", 16, "bold"),
                  foreground=self.colors["primary"]).grid(row=0, column=0,
                                                          columnspan=2, pady=10)

        ttk.Label(frame, text="Username:").grid(row=1, column=0, sticky="e",
                                                pady=5)
        self.username_entry = ttk.Entry(frame)
        self.username_entry.grid(row=1, column=1, pady=5)
        self.username_entry.bind("<Return>", lambda event: self.login())

        ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky="e",
                                                pady=5)
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)
        self.password_entry.bind("<Return>", lambda event: self.login())

        ttk.Button(frame, text="Login", command=self.login).grid(row=3, column=0,
                                                                 columnspan=2,
                                                                 pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username:
            messagebox.showerror("Error", "Please provide a username.",
                                 parent=self.root)
            return

        if not password:
            messagebox.showerror("Error", "Please provide a password.",
                                 parent=self.root)
            return

        if authenticate_user("", username, password):  # Empty email
            self.current_user = username
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Authentication failed.",
                                 parent=self.root)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_window()
        frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        frame.pack(expand=True)

        ttk.Label(frame, text=f"Welcome, {self.current_user}",
                  font=("Helvetica", 14, "bold"),
                  foreground=self.colors["primary"]).pack(pady=10)
        buttons = [
            ("Book Management", self.book_management),
            ("Member Management", self.member_management),
            ("Search Books", self.search_books),
            ("Issue/Return Books", self.issue_return_books),
            ("Library Settings", self.library_settings),
            ("Logout", self.create_login_screen),
            ("Exit", self.exit_program)
        ]

        for text, command in buttons:
            ttk.Button(frame, text=text, command=command).pack(fill="x", pady=5)

    def exit_program(self):
        """Exit the application."""
        self.root.destroy()

    def book_management(self):
        self.clear_window()
        frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Book Management", font=("Helvetica", 14, "bold"),
                  foreground=self.colors["primary"]).pack(pady=10)

        # Book list
        tree_frame = ttk.Frame(frame, style="Custom.TFrame")
        tree_frame.pack(fill="both", expand=True)
        self.book_tree = ttk.Treeview(tree_frame,
                                      columns=("ISBN", "Title", "Author",
                                               "Copies"),
                                      show="headings")
        self.book_tree.heading("ISBN", text="ISBN")
        self.book_tree.heading("Title", text="Title")
        self.book_tree.heading("Author", text="Author")
        self.book_tree.heading("Copies", text="Copies")
        self.book_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical",
                                  command=self.book_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.book_tree.configure(yscrollcommand=scrollbar.set)

        # Buttons
        button_frame = ttk.Frame(frame, style="Custom.TFrame")
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Add Book",
                   command=self.add_book).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Remove Book",
                   command=self.remove_book).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back",
                   command=self.create_main_menu).pack(side="left", padx=5)

        self.update_book_list()

    def add_book(self):
        isbn = simpledialog.askstring("Input", "Enter ISBN:", parent=self.root)
        title = simpledialog.askstring("Input", "Enter Title:", parent=self.root)
        author = simpledialog.askstring("Input", "Enter Author:",
                                        parent=self.root)
        copies = simpledialog.askinteger("Input", "Enter Number of Copies:",
                                         parent=self.root)

        if isbn and title and author and copies:
            book = Book(isbn, title, author, copies)
            self.book_manager.add_book(book)
            self.update_book_list()
        else:
            messagebox.showerror("Error", "All fields are required.",
                                 parent=self.root)

    def remove_book(self):
        selected = self.book_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a book to remove.",
                                 parent=self.root)
            return

        isbn = self.book_tree.item(selected[0])["values"][0]
        self.book_manager.remove_book(isbn)
        self.update_book_list()

    def update_book_list(self):
        for item in self.book_tree.get_children():
            self.book_tree.delete(item)
        for book in self.book_manager.books.values():
            self.book_tree.insert("", "end", values=(book.isbn, book.title,
                                                     book.author, book.copies))

    def member_management(self):
        self.clear_window()
        frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Member Management",
                  font=("Helvetica", 14, "bold"),
                  foreground=self.colors["primary"]).pack(pady=10)

        # Member list
        tree_frame = ttk.Frame(frame, style="Custom.TFrame")
        tree_frame.pack(fill="both", expand=True)
        self.member_tree = ttk.Treeview(tree_frame,
                                        columns=("ID", "Name", "Email", "Phone"),
                                        show="headings")
        self.member_tree.heading("ID", text="Member ID")
        self.member_tree.heading("Name", text="Name")
        self.member_tree.heading("Email", text="Email")
        self.member_tree.heading("Phone", text="Phone")
        self.member_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical",
                                  command=self.member_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.member_tree.configure(yscrollcommand=scrollbar.set)

        # Buttons
        button_frame = ttk.Frame(frame, style="Custom.TFrame")
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Add Member",
                   command=self.add_member).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Update Member",
                   command=self.update_member).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Remove Member",
                   command=self.remove_member).pack(side="left", padx=5)
        ttk.Button(button_frame, text="View Borrowed Books",
                   command=self.view_borrowed_books).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back",
                   command=self.create_main_menu).pack(side="left", padx=5)

        self.update_member_list()

    def add_member(self):
        member_id = simpledialog.askstring("Input", "Enter Member ID:",
                                           parent=self.root)
        name = simpledialog.askstring("Input", "Enter Name:", parent=self.root)
        email = simpledialog.askstring("Input", "Enter Email:", parent=self.root)
        phone = simpledialog.askstring("Input", "Enter Phone:", parent=self.root)

        if member_id and name and email and phone:
            success = self.member_module.register_member(member_id, name, email,
                                                        phone)
            if success:
                messagebox.showinfo("Success", "Member added successfully.",
                                    parent=self.root)
                self.update_member_list()
            else:
                messagebox.showerror("Error", "Member ID already exists.",
                                     parent=self.root)
        else:
            messagebox.showerror("Error", "All fields are required.",
                                 parent=self.root)

    def update_member(self):
        selected = self.member_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a member to update.",
                                 parent=self.root)
            return

        member_id = self.member_tree.item(selected[0])["values"][0]
        name = simpledialog.askstring("Input",
                                      "Enter New Name (leave blank to keep unchanged):",
                                      parent=self.root)
        email = simpledialog.askstring("Input",
                                       "Enter New Email (leave blank to keep unchanged):",
                                       parent=self.root)
        phone = simpledialog.askstring("Input",
                                       "Enter New Phone (leave blank to keep unchanged):",
                                       parent=self.root)

        success = self.member_module.update_member(member_id, name, email, phone)
        if success:
            messagebox.showinfo("Success", "Member updated successfully.",
                                parent=self.root)
            self.update_member_list()
        else:
            messagebox.showerror("Error", "Member not found.",
                                 parent=self.root)

    def remove_member(self):
        selected = self.member_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a member to remove.",
                                 parent=self.root)
            return

        member_id = self.member_tree.item(selected[0])["values"][0]
        success = self.member_module.remove_member(member_id)
        if success:
            messagebox.showinfo("Success", "Member removed successfully.",
                                parent=self.root)
            self.update_member_list()
        else:
            messagebox.showerror("Error", "Member not found.",
                                 parent=self.root)

    def view_borrowed_books(self):
        selected = self.member_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a member.",
                                 parent=self.root)
            return

        member_id = self.member_tree.item(selected[0])["values"][0]
        borrowed_books = self.member_module.get_borrowed_books(member_id)
        if not borrowed_books:
            messagebox.showinfo("Info", "No books borrowed by this member.",
                                parent=self.root)
            return

        books_info = ""
        for isbn in borrowed_books:
            book = self.book_manager.books.get(isbn)
            if book:
                books_info += f"ISBN: {book.isbn}, Title: {book.title}\n"
        messagebox.showinfo("Borrowed Books", books_info, parent=self.root)

    def update_member_list(self):
        for item in self.member_tree.get_children():
            self.member_tree.delete(item)
        for member in self.member_module.list_members():
            self.member_tree.insert("", "end",
                                    values=(member["member_id"], member["name"],
                                            member["email"], member["phone"]))

    def search_books(self):
        self.clear_window()
        frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Search Books", font=("Helvetica", 14, "bold"),
                  foreground=self.colors["primary"]).pack(pady=10)

        # Search fields
        search_frame = ttk.Frame(frame, style="Custom.TFrame")
        search_frame.pack(fill="x", pady=10)
        ttk.Label(search_frame, text="Title:").pack(side="left", padx=5)
        self.title_entry = ttk.Entry(search_frame)
        self.title_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search by Title",
                   command=self.search_by_title).pack(side="left", padx=5)

        ttk.Label(search_frame, text="Author:").pack(side="left", padx=5)
        self.author_entry = ttk.Entry(search_frame)
        self.author_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search by Author",
                   command=self.search_by_author).pack(side="left", padx=5)

        ttk.Label(search_frame, text="ISBN:").pack(side="left", padx=5)
        self.isbn_entry = ttk.Entry(search_frame)
        self.isbn_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search by ISBN",
                   command=self.search_by_isbn).pack(side="left", padx=5)

        # Search results
        tree_frame = ttk.Frame(frame, style="Custom.TFrame")
        tree_frame.pack(fill="both", expand=True)
        self.search_tree = ttk.Treeview(tree_frame,
                                        columns=("ISBN", "Title", "Author",
                                                 "Copies"),
                                        show="headings")
        self.search_tree.heading("ISBN", text="ISBN")
        self.search_tree.heading("Title", text="Title")
        self.search_tree.heading("Author", text="Author")
        self.search_tree.heading("Copies", text="Copies")
        self.search_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical",
                                  command=self.search_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.search_tree.configure(yscrollcommand=scrollbar.set)

        ttk.Button(frame, text="Back",
                   command=self.create_main_menu).pack(pady=10)

    def search_by_title(self):
        title = self.title_entry.get()
        if not title:
            messagebox.showerror("Error", "Please enter a title to search.",
                                 parent=self.root)
            return

        results = search_by_title(self.book_manager, title)
        self.update_search_results(results)

    def search_by_author(self):
        author = self.author_entry.get()
        if not author:
            messagebox.showerror("Error", "Please enter an author to search.",
                                 parent=self.root)
            return

        results = search_by_author(self.book_manager, author)
        self.update_search_results(results)

    def search_by_isbn(self):
        isbn = self.isbn_entry.get()
        if not isbn:
            messagebox.showerror("Error", "Please enter an ISBN to search.",
                                 parent=self.root)
            return

        book = search_by_isbn(self.book_manager, isbn)
        self.update_search_results([book] if book else [])

    def update_search_results(self, books):
        for item in self.search_tree.get_children():
            self.search_tree.delete(item)
        for book in books:
            self.search_tree.insert("", "end", values=(book.isbn, book.title,
                                                       book.author, book.copies))

    def issue_return_books(self):
        self.clear_window()
        frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Issue/Return Books",
                  font=("Helvetica", 14, "bold"),
                  foreground=self.colors["primary"]).pack(pady=10)

        # Issue book
        issue_frame = ttk.LabelFrame(frame, text="Issue Book", padding="10",
                                     style="Custom.TLabelframe")
        issue_frame.pack(fill="x", pady=5)
        ttk.Label(issue_frame, text="Member ID:").pack(side="left", padx=5)
        self.issue_member_id = ttk.Entry(issue_frame)
        self.issue_member_id.pack(side="left", padx=5)
        ttk.Label(issue_frame, text="ISBN:").pack(side="left", padx=5)
        self.issue_isbn = ttk.Entry(issue_frame)
        self.issue_isbn.pack(side="left", padx=5)
        ttk.Button(issue_frame, text="Issue",
                   command=self.issue_book).pack(side="left", padx=5)

        # Return book
        return_frame = ttk.LabelFrame(frame, text="Return Book", padding="10",
                                      style="Custom.TLabelframe")
        return_frame.pack(fill="x", pady=5)
        ttk.Label(return_frame, text="Member ID:").pack(side="left", padx=5)
        self.return_member_id = ttk.Entry(return_frame)
        self.return_member_id.pack(side="left", padx=5)
        ttk.Label(return_frame, text="ISBN:").pack(side="left", padx=5)
        self.return_isbn = ttk.Entry(return_frame)
        self.return_isbn.pack(side="left", padx=5)
        ttk.Button(return_frame, text="Return",
                   command=self.return_book).pack(side="left", padx=5)
        ttk.Button(return_frame, text="Check Fine",
                   command=self.check_fine).pack(side="left", padx=5)

        ttk.Button(frame, text="Back",
                   command=self.create_main_menu).pack(pady=10)

    def issue_book(self):
        member_id = self.issue_member_id.get()
        isbn = self.issue_isbn.get()

        if not member_id or not isbn:
            messagebox.showerror("Error",
                                 "Please provide both Member ID and ISBN.",
                                 parent=self.root)
            return

        if member_id not in self.member_module.members:
            messagebox.showerror("Error", "Member not found.",
                                 parent=self.root)
            return

        if isbn not in self.book_manager.books:
            messagebox.showerror("Error", "Book not found.",
                                 parent=self.root)
            return

        if self.book_manager.books[isbn].copies <= 0:
            messagebox.showerror("Error", "No copies available.",
                                 parent=self.root)
            return

        self.issue_return.issue_book(member_id, isbn)
        self.member_module.add_borrowed_book(member_id, isbn)
        self.book_manager.books[isbn].copies -= 1
        messagebox.showinfo("Success", "Book issued successfully.",
                            parent=self.root)

    def return_book(self):
        member_id = self.return_member_id.get()
        isbn = self.return_isbn.get()

        if not member_id or not isbn:
            messagebox.showerror("Error",
                                 "Please provide both Member ID and ISBN.",
                                 parent=self.root)
            return

        if member_id not in self.member_module.members:
            messagebox.showerror("Error", "Member not found.",
                                 parent=self.root)
            return

        if isbn not in self.book_manager.books:
            messagebox.showerror("Error", "Book not found.",
                                 parent=self.root)
            return

        if isbn not in self.member_module.get_borrowed_books(member_id):
            messagebox.showerror("Error", "Book not borrowed by this member.",
                                 parent=self.root)
            return

        self.issue_return.return_book(member_id, isbn)
        self.member_module.remove_borrowed_book(member_id, isbn)
        self.book_manager.books[isbn].copies += 1
        messagebox.showinfo("Success", "Book returned successfully.",
                            parent=self.root)

    def check_fine(self):
        member_id = self.return_member_id.get()
        isbn = self.return_isbn.get()

        if not member_id or not isbn:
            messagebox.showerror("Error",
                                 "Please provide both Member ID and ISBN.",
                                 parent=self.root)
            return

        issue_date = simpledialog.askstring("Input",
                                            "Enter Issue Date (YYYY-MM-DD):",
                                            parent=self.root)
        return_date = datetime.now().strftime("%Y-%m-%d")

        if not issue_date:
            messagebox.showerror("Error", "Please provide the issue date.",
                                 parent=self.root)
            return

        try:
            fine = self.library_module.calculate_fine(issue_date, return_date)
            if fine > 0:
                messagebox.showinfo("Fine",
                                    f"Fine for overdue book: ${fine:.2f}",
                                    parent=self.root)
            else:
                messagebox.showinfo("Fine", "No fine applicable.",
                                    parent=self.root)
        except ValueError:
            messagebox.showerror("Error",
                                 "Invalid date format. Use YYYY-MM-DD.",
                                 parent=self.root)

    def library_settings(self):
        self.clear_window()
        frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Library Settings",
                  font=("Helvetica", 14, "bold"),
                  foreground=self.colors["primary"]).pack(pady=10)

        # Settings display
        settings = self.library_module.list_settings()
        for key, value in settings.items():
            ttk.Label(frame, text=f"{key.replace('_', ' ').title()}: {value}"
                      ).pack(anchor="w", padx=10)

        # Update setting
        update_frame = ttk.LabelFrame(frame, text="Update Setting",
                                      padding="10",
                                      style="Custom.TLabelframe")
        update_frame.pack(fill="x", pady=10)
        ttk.Label(update_frame, text="Setting Name:").pack(side="left", padx=5)
        self.setting_name = ttk.Entry(update_frame)
        self.setting_name.pack(side="left", padx=5)
        ttk.Label(update_frame, text="New Value:").pack(side="left", padx=5)
        self.setting_value = ttk.Entry(update_frame)
        self.setting_value.pack(side="left", padx=5)
        ttk.Button(update_frame, text="Update",
                   command=self.update_setting).pack(side="left", padx=5)

        # Library overview
        ttk.Button(frame, text="Show Library Overview",
                   command=self.show_overview).pack(pady=10)
        ttk.Button(frame, text="Back",
                   command=self.create_main_menu).pack(pady=10)

    def update_setting(self):
        setting_name = self.setting_name.get()
        setting_value = self.setting_value.get()

        if not setting_name or not setting_value:
            messagebox.showerror("Error",
                                 "Please provide both setting name and value.",
                                 parent=self.root)
            return

        success = self.library_module.update_settings(setting_name,
                                                     setting_value)
        if success:
            messagebox.showinfo("Success", "Setting updated successfully.",
                                parent=self.root)
            self.library_settings()
        else:
            messagebox.showerror("Error", "Setting not found.",
                                 parent=self.root)

    def show_overview(self):
        overview = self.library_module.get_library_overview(self.book_manager,
                                                           self.member_module,
                                                           self.issue_return)
        overview_text = "\n".join([f"{key.replace('_', ' ').title()}: {value}"
                                   for key, value in overview.items()])
        messagebox.showinfo("Library Overview", overview_text,
                            parent=self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()