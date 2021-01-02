from aocd import data


def check_rules(word, rules):
    if not rules:
        yield word
    else:
        rule, *rules = rules
        for remaining in check_rule(word, rule):
            yield from check_rules(remaining, rules)


def check_rule(word, rule):
    if isinstance(rule_map[rule], list):
        for rules in rule_map[rule]:
            yield from check_rules(word, rules)
    elif word and word[0] == rule_map[rule]:
        yield word[1:]


def match(word, rule):
    return any(remaining == '' for remaining in check_rule(word, rule))


rules, messages = data.split('\n\n')
rule_map = {}

for rule in rules.splitlines():
    n, rule = rule.split(':')
    if '|' in rule:
        rule = [r.split() for r in rule.split('|')]
    elif 'a' in rule or 'b' in rule:
        rule = rule.strip('" ')
    else:
        rule = [rule.split()]

    rule_map[n] = rule

messages = messages.splitlines()

print('Part 1:', sum(match(message, '0') for message in messages))

rule_map['8'] = [['42'], ['42', '8']]
rule_map['11'] = [['42', '31'], ['42', '11', '31']]
print('Part 2:', sum(match(message, '0') for message in messages))
