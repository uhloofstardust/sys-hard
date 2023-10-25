

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

def add_rule(filepath, rule, enable=True):
    newlines = []
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if (line.strip().startswith('# '+rule) or line.strip().startswith(rule)):
            if enable:
                newlines.append(rule + '\n')
            else:
                newlines.append('# ' + rule + '\n')
        else:
            newlines.append(line)
    
    with open(filepath, 'w') as f:
        f.writelines(newlines)
        
def password_policy(rule, value=0, enable=True):
    if rule in ['minlen', 'minclass', 'maxrepeat', 'dictcheck', 'usercheck', 'retry']:
        change_rule_status('/etc/security/pwquality', rule, value, enable)
    elif rule in ['enforce_for_root']:
        add_rule('/etc/security/pwquality', rule, enable)
