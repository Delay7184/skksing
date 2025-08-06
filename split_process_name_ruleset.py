import json
import sys

def split_process_name_ruleset(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_rules = []
    for rule in data.get("rules", []):
        if "process_name" in rule:
            process_rule = {"process_name": rule["process_name"]}
            rule_without_process = {k: v for k, v in rule.items() if k != "process_name"}
            if rule_without_process:
                new_rules.append(rule_without_process)
            new_rules.append(process_rule)
        else:
            new_rules.append(rule)

    data["rules"] = new_rules

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python split_process_name_ruleset.py input.json output.json")
    else:
        split_process_name_ruleset(sys.argv[1], sys.argv[2])
