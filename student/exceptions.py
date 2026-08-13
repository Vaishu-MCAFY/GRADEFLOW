class InvalidMarksException(Exception):
    """Raised when marks are not between 0 and 100"""
    pass

def validate_marks(marks):
    """
    Validate that all subject marks are between 0 and 100.

    Parameters:
        marks (list): List of subject marks

    Returns:
        True if all marks are valid

    Raises:
        InvalidMarksException
    """

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarksException(
                f"Invalid Marks: {mark}. Marks must be between 0 and 100."
            )

    return True