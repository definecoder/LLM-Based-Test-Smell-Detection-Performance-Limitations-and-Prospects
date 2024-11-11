import re

def extract_test_blocks(test_content, method_name_full):
    """
    Extract test methods from the test file content.
    Each method begins with `@Test` and ends with a closing brace.
    """
    # Regex pattern to match @Test annotated methods
    test_method_pattern = r'(?s)@Test\s+public\s+void\s+\w+\s*\([^)]*\)\s*(?:throws\s+\w+\s*)?{.*?}'
    
    # Find all test method blocks
    test_methods = re.findall(test_method_pattern, test_content, re.DOTALL)
    print("Test blocks found : ", len(test_methods))
    
    # Extract the actual method name from the full string (last part after the last dot)
    method_name = method_name_full.split('.')[-1].lower()    
    # print(len(test_methods))
    
    # Search for the matching test method block in lowercase
    matched_method = []
    for method in test_methods:
        # print(method_name, " >> ", method.lower())
        if method_name in method.lower():
            matched_method.append(method)
            break
    
    # Print or return the matched test method
    # if matched_method:
    #     print(f"Matched Test Method:\n{matched_method}")
    # else:
    #     print("No matching test method found.")
    
    return matched_method