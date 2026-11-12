"""Tool for trying all Caesar cipher keys and identifying a likely result."""

from pathlib import Path
import re

from encrypt_decrypt import caesar_shift


KNOWN_WORDS = {
    "aga",
    "ei",
    "et",
    "ja",
    "kas",
    "kui",
    "ma",
    "me",
    "on",
    "see",
    "sõnum",
    "sõna",
    "te",
    "tundub",
}


def read_message() -> str:
    """Read ciphertext either from the keyboard or from a UTF-8 text file."""
    choice = input("Kas lugeda sõnum failist? (j/e): ").strip().lower()
    if choice != "j":
        return input("Sisesta šifreeritud sõnum: ")

    filename = input("Sisesta faili nimi: ").strip()
    try:
        return Path(filename).read_text(encoding="utf-8")
    except OSError as error:
        print(f"Faili lugemine ebaõnnestus: {error}")
        return ""


def score_candidate(message: str) -> int:
    """Give a candidate a score based on known Estonian words."""
    words = re.findall(r"[^\W\d_]+", message.lower(), flags=re.UNICODE)
    return sum(word in KNOWN_WORDS for word in words)


def crack_cipher(ciphertext: str) -> list[tuple[int, str]]:
    """Return all 25 possible plaintexts with their keys."""
    return [(shift, caesar_shift(ciphertext, -shift)) for shift in range(1, 26)]


def main() -> None:
    print("Caesari šiffer: šifri lahtimurdamine")
    ciphertext = read_message()
    if not ciphertext:
        print("Šifreeritud sõnum puudub.")
        return

    candidates = crack_cipher(ciphertext)
    print("\nKõik võimalikud dešifreeritud variandid:")
    for shift, candidate in candidates:
        print(f"Nihe {shift:2}: {candidate}")

    best_shift, best_message = max(
        candidates,
        key=lambda item: score_candidate(item[1]),
    )
    best_score = score_candidate(best_message)
    print("\nKõige tõenäolisem algne sõnum:")
    print(f"Nihe {best_shift}: {best_message}")
    print(f"Tuntud sõnade vasteid: {best_score}")


if __name__ == "__main__":
    main()
