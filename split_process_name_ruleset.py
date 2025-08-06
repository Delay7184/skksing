import json
import sys

def split_process_rules(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_rules = []
    for rule in data.get("rules", []):
        if "process_name" in rule or "process_path" in rule:
            # 分离 process_name
            if "process_name" in rule:
                process_name_rule = {"process_name": rule["process_name"]}
                new_rules.append(process_name_rule)
                del rule["process_name"]

            if "process_path" in rule:
                process_path_rule = {"process_path": rule["process_path"]}
                new_rules.append(process_path_rule)
                del rule["process_path"]

        if rule:
            new_rules.append(rule)

    data["rules"] = new_rules

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python split_process_rules.py input.json output.json")
    else:
        split_process_rules(sys.argv[1], sys.argv[2])
