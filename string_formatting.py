def print_formatted(number):
<<<<<<< HEAD
    for i in range(number):
        num_dec = i+1
        num_octal = oct(i+1)[2:]
        num_hex = hex(i+1)[2:]
        num_binary = bin(i+1)[2:]
        
        print(num_dec, num_octal, num_hex, num_binary)

if __name__ == '__main__':
    n = int(input('entered number '))
    print_formatted(n)


def print_formatted(number):
  max_binary_len = len(bin(number)[2:])

  for i in range(number):
    num_dec = i + 1
    num_octal = oct(i + 1)[2:]
    num_hex = hex(i + 1)[2:]
    num_binary = bin(i + 1)[2:]

    padded_dec = str(num_dec).rjust(max_binary_len)
    padded_octal = num_octal.rjust(max_binary_len)
    padded_hex = num_hex.rjust(max_binary_len)
    padded_binary = num_binary.rjust(max_binary_len)

    print(padded_dec, padded_octal, padded_hex, padded_binary, sep=' ')
=======
	max_binary_len = len(bin(number)[2:])

	for i in range(1, number+1):
		num_dec = i
		num_octal = oct(i)[2:]
		num_hex = hex(i)[2:].upper()
		num_binary = bin(i)[2:]

		padded_dec = str(num_dec).rjust(max_binary_len)
		padded_octal = num_octal.rjust(max_binary_len)
		padded_hex = num_hex.rjust(max_binary_len)
		padded_binary = num_binary.rjust(max_binary_len)

		print(padded_dec, padded_octal, padded_hex, padded_binary, sep=' ')
if __name__ == '__main__':
	n = int(input('entered number '))
	print_formatted(n)
>>>>>>> 4e913b3 (updated progress of hackerranl)
