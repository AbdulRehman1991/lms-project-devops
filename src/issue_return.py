class IssueReturn:
    """A class to manage issuing and returning books in a library system."""

    def __init__(self):
        """Initialize an empty dictionary to track borrowed books."""
        self.borrows = {}

    def issue_book(self, member_id, ISBN):
        """
        Issue a book to a member.

        Args:
            member_id (str): ID of the member borrowing the book
            ISBN (int): ISBN of the book to be issued
        """
        self.borrows[ISBN] = member_id
        print(f"Book ISBN:[{ISBN}] issued to student:[{member_id}]")

    def return_book(self, member_id, ISBN):
        """
        Return a book from a member.

        Args:
            member_id (str): ID of the member returning the book
            ISBN (int): ISBN of the book to be returned
        """
        if ISBN in self.borrows:
            del self.borrows[ISBN]
            print(f"Student ID:[{member_id}] and Book ISBN:[{ISBN}] returned successfully.")
        else:
            print("Book ID not found in issued list.")