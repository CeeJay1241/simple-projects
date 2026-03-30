import string

def caesar(text, shift, direction):
    result = []
    shift = shift % 26
    if direction == "decode":
        shift = -shift
    for ch in text:
        if not ch.isalpha():
            result.append(ch)
            continue
        base = ord('a') if ch.islower() else ord('A')
        shifted = (ord(ch) - base + shift) % 26 + base
        result.append(chr(shifted))
    return "".join(result)

def get_direction():
    while True:
        d = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
        if d in ("encode", "decode"):
            return d
        print("Wrong command!")

def get_shift():
    while True:
        s = input("Type the shift number:\n").strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter an integer for the shift.")

def main():
    is_running = True
    while is_running:
        direction = get_direction()
        text = input("Type your message:\n")
        shift = get_shift()
        output = caesar(text, shift, direction)
        print(f"Result: {output}")

        while True:
            resume = input('Type "yes" to continue or "no" to exit:\n').strip().lower()
            if resume in ("yes", "no"):
                break
            print("Incorrect command!")
        if resume == "no":
            print("Goodbye")
            is_running = False

if __name__ == "__main__":
    main()
    