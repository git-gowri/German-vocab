from transformers import pipeline

# Translation pipeline for German to English
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en")

def add_german_word():
    return input("Enter a German word: ").strip()

def get_meaning(word):
    result = translator(word)
    return result[0]['translation_text']

def generate_sentence(word):
    from random import choice
    # Example templates - you can expand this list
    templates = [
    f"Ich habe einen {word}.",                         # I have a {word}.
    f"Der {word} ist sehr freundlich.",                 # The {word} is very friendly.
    f"Ein {word} ist im Park.",                         # A {word} is in the park.
    f"Der kleine {word} spielt gerne.",                 # The little {word} likes to play.
    f"Jeder liebt den {word}.",                         # Everyone loves the {word}.
    f"Mein {word} ist schwarz und weiß.",               # My {word} is black and white.
    f"Der {word} rennt schnell.",                       # The {word} runs fast.
    f"Der {word} schläft unter dem Tisch.",             # The {word} sleeps under the table.
    f"Ein {word} bellt laut.",                          # A {word} barks loudly.
    f"Wir sehen den {word} im Garten.",                 # We see the {word} in the garden.
    f"Der {word} ist sehr klug.",                       # The {word} is very clever.
    f"Ich spiele mit meinem {word}.",                   # I play with my {word}.
    f"Der {word} frisst sein Futter.",                  # The {word} eats its food.
    f"Unsere Nachbarn haben einen {word}.",             # Our neighbors have a {word}.
    f"Mein {word} mag Kinder.",                         # My {word} likes children.
    f"Der {word} wartet vor der Tür.",                  # The {word} waits at the door.
    f"Ein {word} kann gut schwimmen.",                  # A {word} can swim well.
    f"Der {word} sitzt auf dem Sofa.",                  # The {word} sits on the sofa.
    f"Gestern habe ich einen {word} gesehen.",          # Yesterday I saw a {word}.
    f"Viele Menschen haben einen {word} als Haustier."  # Many people have a {word} as a pet.
]

    german_sentence = choice(templates)
    # Translate the sentence
    translation = translator(german_sentence)[0]['translation_text']
    return f"{german_sentence}\n(English: {translation})"
