import json
import sys

def split_process_rules(input_file, output_file):
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{input_file}' is not a valid JSON.")
        sys.exit(1)

    original_rules = data.get("rules", [])
    new_rules = []

    for rule in original_rules:
        process_name = rule.get("process_name")
        process_path = rule.get("process_path")

        if process_name:
            new_rules.append({"process_name": process_name})
            del rule["process_name"]
        if process_path:
            new_rules.append({"process_path": process_path})
            del rule["process_path"]
        if rule:
            new_rules.append(rule)

    data["rules"] = new_rules
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Successfully processed '{input_file}' and saved to '{output_file}'.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_process_rules.py <input.json> <output.json>")
        sys.exit(1)
    
    split_process_rules(sys.argv[1], sys.argv[2])
