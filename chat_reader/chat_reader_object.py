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

        logger.info("Data extracted successfully")
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

    def save_df_to_csv(self, file_path: str = "chat_as_df.csv"):
        self.df.to_csv(file_path, index=False)
        logger.info(f"Data saved to {file_path}")

    def extract_celebs_names(self):
        # Extract messages that contain Hebrew names of Israeli celebs
        hebrew_celebs = self.df['Message'].dropna().tolist()

        # Filter only those messages that seem like they are names, based on their length and Hebrew content
        # Assuming celeb names typically are short and consist of 2-3 Hebrew words
        import re

        # Define a basic pattern for Hebrew names (assuming celeb names would be mostly 2 or 3 words)
        hebrew_name_pattern = re.compile(r'^[\u0590-\u05FF]+(?: [\u0590-\u05FF]+){1,2}$')

        # Filter the messages that match this pattern
        filtered_celebs = [msg for msg in hebrew_celebs if hebrew_name_pattern.match(msg)]

        return filtered_celebs

