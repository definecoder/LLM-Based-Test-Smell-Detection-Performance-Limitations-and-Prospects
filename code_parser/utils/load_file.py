def read_file(filepath):
    """Read the content of a file and return it as a string."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return None
    
def load_file(TEST_FILE_PATH, MAIN_FILE_PATH):
    # Read the content of both files
    test_file_content = read_file(TEST_FILE_PATH)
    main_file_content = read_file(MAIN_FILE_PATH)

    # Confirm content is loaded
    if test_file_content:
        print("Test file loaded successfully.")
    else:
        print("Failed to load the test file.")

    if main_file_content:
        print("Main file loaded successfully.")
    else:
        print("Failed to load the main file.")
    
    return test_file_content, main_file_content