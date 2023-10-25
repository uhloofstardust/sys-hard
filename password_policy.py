

def change_rule_status(filepath, before, after):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if before in line:
            if "# "+before in line:
                lines[i].replace("# "+before, after)
            elif "# "+before not in line:
                lines[i].replace(before, after)
    
    with open(filepath, 'w') as f:
        f.writelines(lines)

