def print_rangoli(size):
    if size == 1:
        print('a')
        return
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    all_lines = []

    for i in range(size):
        dsfdsf = size*2-1
        my_alphabet_r = alphabet[:size]
        my_alphabet_l = alphabet[:size]
        ggg = my_alphabet_l[::-1]
        dsfdsfdsfsdf = ('-'.join(ggg[:+i+1-1])).rjust(dsfdsf-2, '-')+'-'+('-'.join(my_alphabet_r[-i-1:])).ljust(dsfdsf, '-')
        all_lines.append(dsfdsfdsfsdf)

    for p in range(size-1):
        dsfdsf = size*2-1
        sss = '-'.join(ggg[:-p-1-1]).rjust(dsfdsf-2, '-')+'-'+('-'.join(my_alphabet_r[p+1:])).ljust(dsfdsf, '-')
        all_lines.append(sss)

    print(*all_lines, sep="\n")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
