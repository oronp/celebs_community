import os.path

from config.base_config import BaseConfig


class ChatReaderConfig(BaseConfig):
    CHAT_HISTORY_PATH: str = os.path.join(BaseConfig.DATA_DIR, 'chat_history')
    TXT_FILE_PATH: str = os.path.join(CHAT_HISTORY_PATH, '_chat.txt')
    MESSAGE_PATTERN: str = r"\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\] (.*?): (.*)"

