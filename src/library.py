class LibraryManagementModule:
    """
    A module to manage library settings and provide an overview of the library system.

    Attributes:
        settings (Dict[str, str]): Dictionary of library settings
    """

    def __init__(self):
        """Initialize LibraryManagementModule with default settings."""
        self.settings = {
            "library_name": "Default Library",
            "max_borrow_days": "14",
            "fine_per_day": "1.00",
            "max_books_per_member": "5",
        }

    def update_settings(self, setting_name, setting_value):
        """
        Update a library setting.

        Args:
            setting_name (str): Name of the setting to update
            setting_value (str): New value for the setting

        Returns:
            bool: True if setting was updated, False if setting doesn't exist
        """
        if setting_name in self.settings:
            self.settings[setting_name] = setting_value
            return True
        return False

    def get_setting(self, setting_name):
        """
        Get a library setting.

        Args:
            setting_name (str): Name of the setting to retrieve

        Returns:
            str: Value of the setting if found, None otherwise
        """
        return self.settings.get(setting_name)

    def list_settings(self):
        """
        Get all library settings.

        Returns:
            dict: Dictionary of all settings
        """
        return self.settings

    def get_library_overview(self, book_module, member_module, issue_return_module):
        """
        Generate an overview of the library system.

        Args:
            book_module: Instance of BookModule
            member_module: Instance of MemberModule
            issue_return_module: Instance of IssueReturnModule

        Returns:
            dict: Overview statistics including total books, members, and books issued
        """
        total_books = len(book_module.books)
        total_members = len(member_module.members)

        # Calculate total number of books available (not borrowed)
        available_books = 0
        for isbn, book in book_module.books.items():
            # Assuming book['quantity'] or similar field exists
            if "quantity" in book:
                available_books += int(book["quantity"])

        # Calculate total books borrowed
        borrowed_books = (
            len(issue_return_module.borrows)
            if hasattr(issue_return_module, "borrows")
            else 0
        )

        return {
            "library_name": self.settings["library_name"],
            "total_books": total_books,
            "available_books": available_books,
            "total_members": total_members,
            "books_issued": borrowed_books,
            "max_borrow_days": self.settings["max_borrow_days"],
        }

    def is_book_overdue(self, issue_date, current_date):
        """
        Check if a book is overdue based on the issue date and current date.

        Args:
            issue_date (str): Date the book was issued in format 'YYYY-MM-DD'
            current_date (str): Current date in format 'YYYY-MM-DD'

        Returns:
            bool: True if book is overdue, False otherwise
        """
        from datetime import datetime

        date_format = "%Y-%m-%d"
        issue_datetime = datetime.strptime(issue_date, date_format)
        current_datetime = datetime.strptime(current_date, date_format)

        # Calculate difference in days
        delta = current_datetime - issue_datetime
        days_difference = delta.days

        # Check if days difference exceeds max_borrow_days
        return days_difference > int(self.settings["max_borrow_days"])

    def calculate_fine(self, issue_date, return_date):
        """
        Calculate fine for an overdue book.

        Args:
            issue_date (str): Date the book was issued in format 'YYYY-MM-DD'
            return_date (str): Date the book was returned in format 'YYYY-MM-DD'

        Returns:
            float: Fine amount, 0 if not overdue
        """
        from datetime import datetime

        date_format = "%Y-%m-%d"
        issue_datetime = datetime.strptime(issue_date, date_format)
        return_datetime = datetime.strptime(return_date, date_format)

        # Calculate difference in days
        delta = return_datetime - issue_datetime
        days_difference = delta.days

        # Calculate fine if overdue
        max_days = int(self.settings["max_borrow_days"])
        if days_difference > max_days:
            overdue_days = days_difference - max_days
            fine_rate = float(self.settings["fine_per_day"])
            return overdue_days * fine_rate
        return 0.0
