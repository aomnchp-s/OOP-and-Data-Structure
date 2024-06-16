def count_characters(text: str) -> dict[str, int]:
    char_frequencies: dict[str, int] = {}
    for chr in text:
        #print(chr)
        if chr in char_frequencies.keys():
            char_frequencies[chr] += 1 #char_frequencies[chr] = char_frequencies[chr] + 1
        else:
            char_frequencies[chr] = 1
    return char_frequencies

def main() -> None:
    text: str = input('Enter String: ')
    char_frequencies: dict[str, int] = count_characters(text)
    for ch, fre in char_frequencies.items():
        print(f'{ch}: {fre}')

if __name__ == '__main__':
    main()