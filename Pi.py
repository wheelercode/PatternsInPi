def load_file_string(filename):
    with open(filename, 'r') as infile:
        return infile.read()

def save_file_string(string, filename):
    with open(filename, 'w+') as outfile:
        outfile.write(string)

def pi_list(decimals):
    pi_string = load_file_string('pi_dec_1m.txt')
    return [int(p) for p in pi_string[2:decimals+2]]

def repeating_elements(L):
    """ Find the largest number of identical
        consecutive  e elements in a list. Return
        the number of elements in a row, index,
        where the sequence begins, and value repeating. """
    prev = L[0]
    max_n = 0
    max_v = 0
    max_i = 0
    i = 1
    while True:
        n = 0
        while i < len(L) and L[i] == prev:
            n += 1
            i += 1
        if n > max_n:
            max_n = n
            max_i = i - n
            max_v = prev
        if i == len(L):
            break
        prev = L[i]
        n = 1
    return max_n, max_i, max_v

pi = pi_list(10000000)
max_n, max_i, max_v = repeating_elements(pi)
output = """Max number of digits in a row: {}
Index of start of digit sequence: {}
Repeating digit: {}
Surrounding slice of pi: {}""".format(max_n, max_i, max_v, pi[max_i-3:max_i+max_n+3])
save_file_string(output, 'pi_repeating_digits.txt')