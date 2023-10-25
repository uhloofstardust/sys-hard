

def change_rule_status(filepath, rule, value=0, enable=True):
    newlines = []
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if (line.strip().startswith('# '+rule) or line.strip().startswith(rule)):
            if enable:
                newlines.append(rule + '=' + value + '\n')
            else:
                newlines.append('# ' + rule + '=' + value + '\n')
        else:
            newlines.append(line)
    
    with open(filepath, 'w') as f:
        f.writelines(newlines)
        
def password_policy():
    
