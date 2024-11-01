def string_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_string(binary):
    binary_values = binary.split(' ')
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    return ''.join(ascii_characters)

def main():
    action = input("Do you want to (e)ncode or (d)ecode? ").strip().lower()

    if action == 'e':
        user_input = input("Enter the string to encode: ")
        encoded = string_to_binary(user_input)
        print(f"Encoded binary: {encoded}")

    elif action == 'd':
        user_input = input("Enter the binary to decode (separated by spaces): ")
        try:
            decoded = binary_to_string(user_input)
            print(f"Decoded string: {decoded}")
        except ValueError:
            print("Invalid binary input. Please ensure it is correctly formatted.")

    else:
        print("Invalid option. Please enter 'e' to encode or 'd' to decode.")

if __name__ == "__main__":
    main()

