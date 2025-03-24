from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.

    Args:
        date (str or datetime): The starting date in 'YYYY-MM-DD' format or a datetime object.
        days (int): Number of days to add (can be positive or negative).

    Returns:
        str: The resulting date in 'YYYY-MM-DD' format.

    Raises:
        TypeError: If date is not a string or datetime object.
        ValueError: If date string is not in the correct format.
    """
    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format")
    
    # Check if date is a datetime object
    if not isinstance(date, datetime):
        raise TypeError("Date must be a string or datetime object")
    
    # Check if days is an integer
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")
    
    # Add days
    new_date = date + timedelta(days=days)
    
    # Return as formatted string
    return new_date.strftime('%Y-%m-%d')