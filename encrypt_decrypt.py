"""Caesar cipher encryption and decryption tool."""

from pathlib import Path


def caesar_shift(message: str, shift: int) -> str:
    """Shift English alphabetic characters and leave all other characters unchanged."""
    result = []
    for character in message:
        if "A" <= character <= "Z":
            result.append(chr((ord(character) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= character <= "z":
            result.append(chr((ord(character) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(character)
    return "".join(result)


def ask_key() -> int:
    """Read a valid Caesar key from the user."""
    while True:
        try:
            key = int(input("Sisesta nihe (1-25): "))
        except ValueError:
            print("Palun sisesta täisarv vahemikus 1-25.")
            continue
        if 1 <= key <= 25:
            return key
        print("Nihe peab olema vahemikus 1-25.")


def save_message(message: str) -> None:
    """Save a message to a UTF-8 text file."""
    filename = input("Sisesta faili nimi (nt salasonum.txt): ").strip()
    if not filename:
        print("Faili nimi ei tohi olla tühi.")
        return

    try:
        Path(filename).write_text(message, encoding="utf-8")
    except OSError as error:
        print(f"Faili salvestamine ebaõnnestus: {error}")
    else:
        print(f"Sõnum salvestati faili {filename}.")


def main() -> None:
    print("Caesari šiffer: šifreerimine ja dešifreerimine")
    message = input("Sisesta sõnum: ")
    key = ask_key()

    encrypted = caesar_shift(message, key)
    decrypted = caesar_shift(message, -key)

    print(f"\nŠifreeritud sõnum: {encrypted}")
    print(f"Dešifreeritud sõnum: {decrypted}")

    if input("\nKas salvestada šifreeritud sõnum faili? (j/e): ").strip().lower() == "j":
        save_message(encrypted)


if __name__ == "__main__":
    main()
