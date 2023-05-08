import decimal

output_folder = './phi/'

def calculate_phi(digits):
    decimal.getcontext().prec = digits + 1
    sqrt5 = decimal.Decimal(5).sqrt()
    phi = (1 + sqrt5) / 2
    return phi

def save_to_file(phi, digits_per_file):
    phi_str = str(phi)[2:]
    num_files = len(phi_str) // digits_per_file
    for i in range(num_files):
        start = i * digits_per_file
        end = start + digits_per_file
        filename = output_folder + f"phi_{start+1}-{end}.txt"
        with open(filename, "w") as f:
            f.write(phi_str[start:end])

def main():
    digits = int(input("Enter the number of digits to calculate: "))
    digits_per_file = 1000000
    phi = calculate_phi(digits)
    save_to_file(phi, digits_per_file)

if __name__ == "__main__":
    main()