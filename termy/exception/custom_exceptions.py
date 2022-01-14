class GoogleSheetAuthRequiredException(Exception):
    """Thrown when google sheet requires authentication for accessing it"""
    pass


class GoogleSheetNotFoundException(Exception):
    """Thrown when google sheet is not found or invalid"""
    pass

class UnknownException(Exception):
    """Generic Exception"""
    pass