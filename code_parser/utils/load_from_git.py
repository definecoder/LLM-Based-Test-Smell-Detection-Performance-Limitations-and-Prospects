import urllib.request

def read_github_file(url):
    """Fetch the content of a file from a GitHub URL and return it as a string."""
    try:
        response = urllib.request.urlretrieve(url, filename="temp_file.java")
        with open("temp_file.java", "r") as file:
            response = file.read()        
        return response                   
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def load_github_files(test_file_url, main_file_url):
    # Fetch the content of both files
    test_file_content = read_github_file(test_file_url)
    main_file_content = read_github_file(main_file_url)
    
    
    print( "TEST FILE LEN : ", len(test_file_content))
    print( "MAIN FILE LEN : ", len(main_file_content))

    # Confirm content is loaded
    if test_file_content:
        # print(test_file_content)
        print("Test file loaded successfully from GitHub.")
    else:
        print("Failed to load the test file from GitHub.")

    if main_file_content:
        # print(main_file_content)
        print("Main file loaded successfully from GitHub.")
    else:
        print("Failed to load the main file from GitHub.")
    
    return test_file_content, main_file_content
