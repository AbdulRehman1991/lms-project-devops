class MemberModule:
    """
    A module to manage library members.

    Attributes:
        members (Dict[str, Dict[str, str]]): Dictionary of members with member_id as keys
    """

    def __init__(self):
        """Initialize an empty MemberModule with a dictionary for members."""
        self.members = {}

    def register_member(self, member_id, name, email, phone):
        """
        Register a new member to the library system.

        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
            phone (str): Phone number of the member

        Returns:
            bool: True if successfully added, False if member_id already exists
        """
        if member_id not in self.members:
            self.members[member_id] = {
                "member_id": member_id,
                "name": name,
                "email": email,
                "phone": phone,
                "borrowed_books": [],  # List to store ISBNs of borrowed books
            }
            return True
        return False

    def update_member(self, member_id, name=None, email=None, phone=None):
        """
        Update member information.

        Args:
            member_id (str): ID of the member to update
            name (str, optional): New name for the member
            email (str, optional): New email for the member
            phone (str, optional): New phone for the member

        Returns:
            bool: True if successfully updated, False if member_id not found
        """
        if member_id in self.members:
            if name:
                self.members[member_id]["name"] = name
            if email:
                self.members[member_id]["email"] = email
            if phone:
                self.members[member_id]["phone"] = phone
            return True
        return False

    def remove_member(self, member_id):
        """
        Remove a member from the library system.

        Args:
            member_id (str): ID of the member to be removed

        Returns:
            bool: True if successfully removed, False if member_id not found
        """
        if member_id in self.members:
            del self.members[member_id]
            return True
        return False

    def get_member(self, member_id):
        """
        Get a member by ID.

        Args:
            member_id (str): ID of the member to retrieve

        Returns:
            dict: Member information if found, None otherwise
        """
        return self.members.get(member_id)

    def list_members(self):
        """
        Get a list of all members.

        Returns:
            list: List of all member dictionaries
        """
        return list(self.members.values())

    def add_borrowed_book(self, member_id, isbn):
        """
        Add a book to the member's borrowed books list.

        Args:
            member_id (str): ID of the member
            isbn (str): ISBN of the book to be borrowed

        Returns:
            bool: True if successfully added, False if member not found
        """
        if member_id in self.members:
            self.members[member_id]["borrowed_books"].append(isbn)
            return True
        return False

    def remove_borrowed_book(self, member_id, isbn):
        """
        Remove a book from the member's borrowed books list.

        Args:
            member_id (str): ID of the member
            isbn (str): ISBN of the book to be returned

        Returns:
            bool: True if successfully removed, False if member or book not found
        """
        if (
            member_id in self.members
            and isbn in self.members[member_id]["borrowed_books"]
        ):
            self.members[member_id]["borrowed_books"].remove(isbn)
            return True
        return False

    def get_borrowed_books(self, member_id):
        """
        Get the list of books borrowed by a member.

        Args:
            member_id (str): ID of the member

        Returns:
            list: List of ISBN strings of borrowed books, empty list if member not found
        """
        if member_id in self.members:
            return self.members[member_id]["borrowed_books"]
        return []

    def search_members(self, keyword):
        """
        Search members by name or ID.

        Args:
            keyword (str): Name or ID to search for

        Returns:
            list: List of member dictionaries matching the search criteria
        """
        keyword = keyword.lower()
        return [
            member
            for member in self.members.values()
            if keyword in member["name"].lower()
            or keyword in member["member_id"].lower()
        ]
