def read_file_lines(file_path):
    """
    Read a file line by line and return the lines as a list.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        list: A list of strings, where each string is a line from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Remove trailing newline characters
        lines = [line.rstrip('\n') for line in lines]
        
        return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")