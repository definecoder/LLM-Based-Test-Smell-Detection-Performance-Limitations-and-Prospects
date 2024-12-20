from code_parser.utils.load_from_git import load_github_files
from code_parser.utils.save_results import save_result
from code_parser.utils.extract_function_implementations import extract_function_implementations
from code_parser.utils.organize_results import organize_results
from code_parser.utils.extract_function_calls import extract_function_calls
from code_parser.utils.extract_test_blocks import extract_test_blocks
from code_parser.utils.load_file import load_file

def test_code_parser(TEST_FILE_PATH, test_case, isEagerTest, isMysteryGuest, isResourceOptimism, isRedundent):
    test_file_content = load_github_files(TEST_FILE_PATH)
    test_methods = extract_test_blocks(test_file_content, test_case)
    print("Matched test blocks", len(test_methods))
    if len(test_methods) == 0:
        return
    # function_calls_in_tests = extract_function_calls(test_methods)
    # print("extracted function calls", len(function_calls_in_tests))
    # print("function calls in tests", function_calls_in_tests)
    # function_implementations = extract_function_implementations(main_file_content, function_calls_in_tests)
    # print("extracted function implementations", len(function_implementations))
    organized_result = organize_results(test_methods, isEagerTest, isMysteryGuest, isResourceOptimism, isRedundent)
    save_result(organized_result, "report")
