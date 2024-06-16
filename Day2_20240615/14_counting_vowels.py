def count_vowels(text: str) -> int:
    vowels = 'aeiouAEIOU'
    count = 0 
    for w in text:
        if w in vowels:
            count += 1
    return count

def main():
    text = input('Enter text: ')
    count = count_vowels(text)
    print(f'The vowels is {count}')
    
if __name__ == '__main__':
    main()