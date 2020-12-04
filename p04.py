import re

from aocd import data as passports


passport_pattern = re.compile(r'(\w+):(.+?)(?:\s|$)')
hgt_pattern = re.compile(r'(\d+)(\w+)')
hcl_pattern = re.compile(r'#[0-9a-f]{6}')
pid_pattern = re.compile(r'\d{9}')

validation = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': lambda v: ((hgt := hgt_pattern.search(v))
                      and ((150 <= int(hgt[1]) <= 193 and hgt[2] == 'cm')
                           or (59 <= int(hgt[1]) <= 76 and hgt[2] == 'in'))),
    'hcl': lambda v: hcl_pattern.fullmatch(v),
    'ecl': lambda v: v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda v: pid_pattern.fullmatch(v),
    'cid': lambda v: True
}

valid_fields = 0
valid_values = 0
for passport in passports.split('\n\n'):
    fields = set(re.findall(r'(\w+):', passport))

    if len(fields - {'cid'}) == 7:
        valid_fields += 1

        info = passport_pattern.findall(passport)
        for key, value in info:
            if not validation[key](value):
                break
        else:
            valid_values += 1

print('Part 1:', valid_fields)
print('Part 2:', valid_values)
