from collections import defaultdict

from aocd import data


# data = '''42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1

# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''

class Node:
    def __init__(self, value, level):
        self.value = value
        self.children = {}
        self.is_word = False
        self.level = level


class Trie:
    def __init__(self):
        self.root = Node(None, 0)
        self.ct = 0
        self.max_len = 0
        self.max_level = 0

    def insert(self, message):
        node = self.root
        for i, char in enumerate(message, 1):
            if char not in node.children:
                node.children[char] = Node(char, i)
            node = node.children[char]
        node.is_word = True
        self.max_len = max(self.max_len, i)


def dfs(rule: list, trie: Trie, node: Node = None, level: int = 0):
    # if level > trie.max_level:
    #     trie.max_level = level
    # if level + len(rule) > trie.max_len:
    # if level > 18:
    #     return

    if node is None:
        node = trie.root

    for i, r in enumerate(rule):
        # if r in ('8', '11'):
        #     import pudb;pu.db
        children = rule_map[r]

        if isinstance(children, list):
            if isinstance(children[0], list):
                for child in children:
                    dfs(child+rule[i+1:], trie, node, level + 1)
            else:
                dfs(children+rule[i+1:], trie, node, level + 1)

        else:
            char = children
            if char in node.children:
                node = node.children[char]
            else:
                return

    if node.is_word:
        trie.ct += 1


rules, messages = data.split('\n\n')
rule_map = {}

for rule in rules.splitlines():
    n, rule = rule.split(':')
    if '|' in rule:
        rule = [r.split() for r in rule.split('|')]
    elif 'a' in rule or 'b' in rule:
        rule = rule.strip('" ')
    else:
        rule = rule.split()

    rule_map[n] = rule

trie = Trie()

for message in messages.splitlines():
    trie.insert(message)

# import pudb;pu.db

dfs(rule_map['0'], trie)
print('Part 1:', trie.ct)
# print('max lvl:', trie.max_level)
# raise SystemExit

# trie.ct = 0
# rule_map['8'] = [['42'], ['42', '8']]
# rule_map['8'] = [['42']*i for i in range(1,3)]
# rule_map['11'] = [['42', '31'], ['42', '11', '31']]
# rule_map['11'] = [['42']*i + ['31']*i for i in range(1,3)]
# import pudb;pu.db
# dfs(rule_map['0'], trie)
# print('Part 2:', trie.ct)
