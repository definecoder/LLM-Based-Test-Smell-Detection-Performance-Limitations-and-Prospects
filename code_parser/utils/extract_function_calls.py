import re


def extract_function_calls(test_methods):
    """
    Extracts function calls from each test method.
    
    Parameters:
    - test_methods: List of strings, each containing a test method code block.
    
    Returns:
    - A dictionary where each test method has a list of called function names.
    """
    # Pattern to match a function call like `functionName(...)`
    function_call_pattern = r'\b(\w+)\s*\([^)]*\)'

    test_function_calls = []
    
    # Iterate over each test method and extract function calls
    for i, method in enumerate(test_methods, 1):
        # Extract function names
        function_calls = re.findall(function_call_pattern, method)
        
        # remove the first one
        function_calls = function_calls[1:]
        
        # remove if starts with 'assert' or 'log'        
        function_calls = [f for f in function_calls if not f.startswith('assert') and not f.startswith('log')]                
        
        
        # Store the results
        test_function_calls = function_calls
        # print(f"\nFunction calls in {function_calls[0]}:", function_calls)
    
    return test_function_calls