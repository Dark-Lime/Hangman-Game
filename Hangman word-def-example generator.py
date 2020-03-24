def hangman_word_generator():
    from requests import get
    from bs4 import BeautifulSoup
    import random

    hangman_word = []

    hangman_definition = []

    hangman_example = []

    hangman_combination = []

    page_number = str(random.randint(2, 50))

    random_combination = random.randint(0, 6)

    url_1st = "https://www.urbandictionary.com/?page="

    url = url_1st + page_number

    page = get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    type(soup)

    urban_word = soup.find_all("a", class_="word")

    urban_definition = soup.div.find_all("div", class_="meaning")

    urban_example = soup.div.find_all("div", class_="example")

    for word in urban_word:
        list.append(hangman_word, word.text.lower())

    for meaning in urban_definition:
        list.append(hangman_definition, meaning.text)

    for example in urban_example:
        list.append(hangman_example, example.text)

    list.append(hangman_combination, hangman_word[random_combination])
    list.append(hangman_combination, hangman_definition[random_combination])
    list.append(hangman_combination, hangman_example[random_combination])

    return hangman_combination
