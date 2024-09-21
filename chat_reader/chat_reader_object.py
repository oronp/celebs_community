import re

import pandas as pd

from chat_reader_config import ChatReaderConfig
from utils.logger import CelebsLogger

logger = CelebsLogger("chat_reader_object")
config = ChatReaderConfig()


class ChatReaderObject:
    # Lists to store the extracted data
    dates: list = []
    times: list = []
    authors: list = []
    messages: list = []
    df: pd.DataFrame = None

    def text_to_df(self):
        with open(config.TXT_FILE_PATH, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(config.MESSAGE_PATTERN, line)
                if match:
                    date, time, author, message = match.groups()
                    author = self.clean_author_name(author)

                    self.dates.append(date)
                    self.times.append(time)
                    self.authors.append(author)
                    self.messages.append(message)

            # Create a DataFrame with the extracted data
        self.df = pd.DataFrame({
            'Date': self.dates,
            'Time': self.times,
            'Author': self.authors,
            'Message': self.messages
        })

    @staticmethod
    def clean_author_name(author):
        # Remove the "~\u202f" (non-breaking space) prefix if present
        return author.replace("~\u202f", "").strip()

    def get_unique_authors(self):
        return list(set(self.authors))


if __name__ == '__main__':
    a = ChatReaderObject()
    a.text_to_df()
    unique_authors = a.get_unique_authors()
rint(1)
