import csv
import os

def save_result(result, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # Append all data to the main CSV file
    all_smells_file = os.path.join(output_dir, "all_smells.csv")
    write_header = not os.path.exists(all_smells_file)  # Check if header is needed
    with open(all_smells_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["test_method", "isEagerTest", "isMysteryGuest", "isResourceOptimism", "isRedundent"])
        writer.writerow([
            result["test_method"],
            result["isEagerTest"],
            result["isMysteryGuest"],
            result["isResourceOptimism"],
            result["isRedundent"]
        ])
    
    # Append each smell to its respective CSV file
    for smell in ["isEagerTest", "isMysteryGuest", "isResourceOptimism", "isRedundent"]:
        if result[smell] == "0":
            continue
        smell_file = os.path.join(output_dir, f"{smell}.csv")
        write_header = not os.path.exists(smell_file)  # Check if header is needed
        with open(smell_file, 'a', newline='') as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["test_method", smell])
            writer.writerow([result["test_method"], result[smell]])

# # Example usage
# result = {
#     "test_method": "exampleTest",
#     "isEagerTest": True,
#     "isMysteryGuest": False,
#     "isResourceOptimism": True,
#     "isRedundent": False
# }
# save_result(result, "./output")
