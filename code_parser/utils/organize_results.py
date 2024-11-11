def organize_results(test_function_calls, function_implementations):
    """
    Organizes test methods, called functions, and their implementations into a structured format.
    
    Parameters:
    - test_function_calls: Dictionary of test methods and their function calls.
    - function_implementations: Dictionary of function names and their implementation code.
    
    Returns:
    - Structured dictionary of organized results.
    """
    results = {}
    
    for test_name, functions in test_function_calls:
        results[test_name] = {
            "called_functions": {},
        }
        
        # print(f"\nTest method: {test_name}")
        
        for function_name in functions:
            implementation = function_implementations.get(function_name, "Not found in main file")
            if implementation != "Not found in main file":
                results[test_name]["called_functions"][function_name] = implementation
                # print(f"\nFunction: {function_name}\nImplementation: {implementation}")
    
    return results
