import re


def extract_function_implementations(main_content, function_calls):
    """
    Extracts the implementation of each function from the main file.
    
    Parameters:
    - main_content: The full text of the main Java file.
    - function_calls: A dictionary where keys are test methods and values are lists of function names.
    
    Returns:
    - A dictionary where each function name maps to its full implementation block.
    """
    # Updated regex pattern to find the start of a function definition
    function_impl_pattern_template = (
        r'(public|private|protected)\s+(static\s+)?\w+(\s+\w+)?\s+{function_name}\s*\([^)]*\)\s*'
        r'(?:throws\s+\w+(\s*,\s*\w+)*)?\s*{'
    )

    
    function_implementations = {}

    # Loop through each test method and its called functions
    for function_name in function_calls:        
        # Build regex pattern specific to the current function name
        function_impl_pattern = function_impl_pattern_template.replace('{function_name}', function_name)
        
        # Search for the function definition's starting point
        match = re.search(function_impl_pattern, main_content, re.DOTALL)  # Include re.DOTALL for multiline matching            
        
        if match:
            # Start from the matched position to capture the full function body                
            start_index = match.start()
            brace_count = -1
            end_index = start_index

            # Find the full function body by counting braces
            while end_index < len(main_content):
                char = main_content[end_index]
                if char == '{' and brace_count == -1:
                    brace_count += 2
                elif char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                end_index += 1
                
                # Break when all braces are closed
                if brace_count == 0:
                    break
            
            # Extract the full function implementation
            function_implementation = main_content[start_index:end_index]
            function_implementations[function_name] = function_implementation.strip()
            # print(f"\nImplementation for {function_name}:\n")
            # print(function_implementation)
        # else:
        #     print(f"\nFunction {function_name} not found in the main file.")
    
    return function_implementations
