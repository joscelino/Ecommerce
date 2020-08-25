import re


def cpf_validator(cpf):

    """ Make cpf validation """
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    new_cpf = cpf[:-2]                 # Eliminates the last two digits of the CPF
    reverse = 10                       # Reverse counter
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # First index goes from 0 to 9,
            index -= 9                  # These are the first 9 digits of the CPF

        total += int(new_cpf[index]) * reverse  # Total multiplication value

        reverse -= 1                    # Decreases the reverse counter
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            new_cpf += str(d)          # Concatenates the digit generated in the new cpf

    # Avoid sequences. Ex.: 11111111111, 00000000000...
    sequency = new_cpf == str(new_cpf[0]) * len(cpf)

    # Last check
    if cpf == new_cpf and not sequency:
        return True
    else:
        return False
