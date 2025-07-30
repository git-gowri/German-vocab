from german_helpers import add_german_word, get_meaning, generate_sentence

def main():
    word = add_german_word()
    print(f"\nYou entered: {word}")

    meaning = get_meaning(word)
    print(f"\nMeaning in English: {meaning}")

    sentence = generate_sentence(word)
    print(f"\nSample German sentence and translation:\n{sentence}")

if __name__ == "__main__":
    main()
