from datetime import datetime, date

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime.date): First date in ISO format (YYYY-MM-DD) or datetime.date object
        date2 (str or datetime.date): Second date in ISO format (YYYY-MM-DD) or datetime.date object

    Returns:
        int: Number of days between the two dates (absolute value)

    Raises:
        ValueError: If dates are in an invalid format or cannot be parsed
    """
    # Convert input to date objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.strptime(date1, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for date1: {date1}. Use YYYY-MM-DD format.")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.strptime(date2, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for date2: {date2}. Use YYYY-MM-DD format.")
    
    # Validate input is a date object
    if not (isinstance(date1, date) and isinstance(date2, date)):
        raise ValueError("Dates must be either datetime.date objects or strings in YYYY-MM-DD format")
    
    # Calculate absolute difference in days
    return abs((date2 - date1).days)