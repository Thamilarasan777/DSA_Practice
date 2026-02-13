from symspellpy import SymSpell, Verbosity

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load custom dictionary
dictionary_path = "filtered_drug_names.txt"  # Path to your custom word list
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1,encoding='UTF-8')

# Function to correct spelling and provide suggestions in a sentence
def correct_and_suggest(sentence):
    corrected_words = []
    misseplled_words = {}
    word_suggessions = {}
    for word in sentence.split():
        if len(word)>=6:
            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
            if suggestions:
                misseplled_words[word] = suggestions[0].term
                # Take the first suggestion and add it to corrected words
                corrected_words.append(suggestions[0].term)
                # Print other suggestions if needed
                if len(suggestions) > 1:
                    word_suggessions[word] = [s.term for s in suggestions[:]]
                    #print(f"Suggestions for '{word}': {[s.term for s in suggestions[:]]}")
            else:
                corrected_words.append(word)  # If no suggestion found, keep original word
        else:
            corrected_words.append(word)  # If no suggestion found, keep original word
    return " ".join(corrected_words), misseplled_words, word_suggessions

# Example usage
sentence = '''Alkeine'''
corrected_sentence, misseplled_words, word_suggessions = correct_and_suggest(sentence)
#print(f"Original Sentence: {sentence}")
#print(f"Corrected Sentence: {corrected_sentence}")
#print(f"Misseplled words: {misseplled_words}")
print(f"Word suggestions: {word_suggessions}")

