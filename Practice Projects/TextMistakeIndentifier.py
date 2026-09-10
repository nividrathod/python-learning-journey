from spellchecker import SpellChecker


class SpellcheckerProgram:

    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)

            if corrected_word is None:
                corrected_word = word

            if corrected_word != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}'")

            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    def run(self):
        print("\nSpell Checker")

        while True:
            text = input("\nEnter text to check (or type 'exit' to quit): ")

            if text.lower() == 'exit':
                print("Closing the program..")
                break

            corrected_text = self.correct_text(text)

            print(f"Corrected Text: {corrected_text}")


if __name__ == "__main__":
    SpellcheckerProgram().run()
