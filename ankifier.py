import requests
from bs4 import BeautifulSoup

url = WEBPAGE

def extract_flashcards(html_content):
    flashcards = []
    soup = BeautifulSoup(html_content, 'html.parser')
    dd_elements = soup.find_all('dd')

    for dd in dd_elements:
        definition = dd.text.strip()
        dt = dd.find_previous('dt')

        # Check if a corresponding <dt> element is found
        if dt:
            term = dt.text.strip()
            flashcard = (term, definition)
            flashcards.append(flashcard)

    return flashcards

def create_anki_deck(flashcards, deck_name):
    with open(deck_name + '.txt', 'w', encoding='utf-8') as file:
        for term, definition in flashcards:
            front_side = term.replace('\t', ' ')  # Replace any tabs in the term with spaces
            back_side = definition.replace('\t', ' ')  # Replace any tabs in the definition with spaces
            file.write(f'{front_side}\t{back_side}\n')

if __name__ == "__main__":
    url = WEBPAGE
    response = requests.get(url)
    if response.status_code == 200:
        flashcards = extract_flashcards(response.content)
        create_anki_deck(flashcards, "Design_Patterns_Glossary")
        print("Anki deck created successfully.")
    else:
        print("Failed to retrieve the webpage.")
