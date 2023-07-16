*Anki Deck Generator from Webpage Glossary

Creating Anki flashcards can be a tedious and time-consuming process, especially when you have a large glossary or list of terms and definitions from a webpage that you want to convert into flashcards.

The Anki Deck Generator is a Python script that uses the requests and BeautifulSoup libraries to fetch and parse the HTML content of a specified webpage. The script then extracts the glossary entries (terms and definitions) from the HTML, ensuring proper pairing even if the HTML structure has missing or extra elements.

Once the terms and definitions are extracted and paired, the script generates an Anki deck in TSV (Tab-Separated Values) format. Each line in the TSV file represents a flashcard, with the term and definition separated by a tab character. This TSV file can be easily imported into Anki, creating a ready-to-use deck for study.
**How to Use

    Clone or download this repository to your local machine.
    Install the required libraries using pip install requests beautifulsoup4.
    Run the Python script anki_deck_generator.py.
    The script will fetch the glossary from the specified webpage and create an Anki deck file (Design_Patterns_Glossary.txt in this case) in the project directory.

Dependencies

    Python 3.x
    requests library for fetching webpage content
    BeautifulSoup library for parsing HTML content

