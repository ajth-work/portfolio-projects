import requests
from bs4 import BeautifulSoup
import os


def fetch_and_print_words_learned(username):
    duolingo_user = Duolingo_User(username)
    words_learned = duolingo_user.words_learned

    if words_learned:
        print("Words Learned:")
        for word in words_learned:
            print(word)
    else:
        print("No words learned data available.")


class Duolingo_User():

    def __init__(self, username):
        self.username = username
        self.words_learned = self.get_words_learned(username)

    def get_words_learned(self, username):
        url = f"https://duome.eu/{username}/progress"
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            words_learned = [
                link.get_text() for link in soup.find_all('a', class_='wA')
            ]
            return words_learned
        else:
            print("Error: Unable to fetch data from Duome")
            return []


if __name__ == '__main__':
    username = os.environ.get('DuolingoUsername')
    if username:
        item = Duolingo_User(username)
        print("Words Learned:")
        for word in item.words_learned:
            print(word)
    else:
        print("Error: DuolingoUsername environment variable not set.")
