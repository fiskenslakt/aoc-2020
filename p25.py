from aocd import data as public_keys


card_pubkey, door_pubkey = map(int, public_keys.splitlines())

modulus = 20201227
subject_number = 7
loop_size = 1

while True:
    if pow(subject_number, loop_size, modulus) == card_pubkey:
        break
    loop_size += 1

print('Part 1:', pow(door_pubkey, loop_size, modulus))
