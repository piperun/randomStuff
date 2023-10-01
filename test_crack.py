vowels = ['A', 'E', 'I', 'O', 'U']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
              'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

grammar_rules = ['VCVC', 'CVCV', 'VCCV', 'VCVCVCVC']


def generate_password(rule, index, password, target_password):
    if index == len(rule):
        if password == target_password:
            print(f"Password found: {password}")
            return True
        return False

    if rule[index] == 'V':
        for v in vowels:
            if generate_password(rule, index + 1, password + v, target_password):
                return True
    elif rule[index] == 'C':
        for c in consonants:
            if generate_password(rule, index + 1, password + c, target_password):
                return True

    return False


def crack_password(target_password):
    for rule in grammar_rules:
        if generate_password(rule, 0, "", target_password):
            return
    print("Password not found.")


target = 'OPERETEK'
crack_password(target)
