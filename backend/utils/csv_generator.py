import lorem
import csv
import random
import string
import secrets

USERS_COUNT = 30
CHATS_COUNT = 10
MESSAGE_COUNT = 1000

MODEL_COLUMNS = {
    "USER": ["name", "email", "password"],
    "CHAT": [ "admin_pk", "name"],
    "MESSAGE": ["text", "user_pk", "chat_pk"],
    "USER_HAS_CHAT": ["user_pk", "chat_pk"]
}

FIRSTNAMES = [
"Aurora",
"Xavier",
"Seraphina",
"Darius",
"Luna",
"Ezekiel",
"Freya",
"Orion",
"Selene",
"Dante",
"Nova",
"Silas",
"Ember",
"Atticus",
"Celeste",
"Kieran",
"Lyra",
"Thaddeus",
"Isadora",
"Phoenix"
]
LASTNAMES = [
"Blackwood",
"Nightingale",
"Hawthorne",
"Silverstone",
"Frost",
"Evergreen",
"Stormborn",
"Wilde",
"Moonstone",
"Ironheart",
"Winterbourne",
"Firestone",
"Riversong",
"Ashbourne",
"Shadowhunter",
"Starling",
"Skylark",
"Stonehaven",
"Whitewood",
"Summersong"
]

class CSVGenerator:
    def __init__(self, user_count: int = USERS_COUNT, chat_count: int = CHATS_COUNT, message_count: int = MESSAGE_COUNT):
        self.user_count = user_count
        self.chat_count = chat_count
        self.message_count = message_count

        self.chatId = 1


    def generate_csv(self):
        with open('backend/csv_files/users.csv', 'w+') as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(MODEL_COLUMNS["USER"])

            for _ in range(self.user_count):
                writer.writerow(self.generate_user())

        with open('backend/csv_files/chats.csv', 'w+') as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(MODEL_COLUMNS["CHAT"])

            for _ in range(self.chat_count):
                writer.writerow(self.generate_chat())

        with open('backend/csv_files/messages.csv', 'w+') as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(MODEL_COLUMNS["MESSAGE"])

            for _ in range(self.message_count):
                writer.writerow(self.generate_text())

        with open('backend/csv_files/user_has_chat.csv', 'w+') as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(MODEL_COLUMNS["USER_HAS_CHAT"])

            for chat_id in range(1, self.chat_count + 1):
                for user_id in random.sample(range(1, self.user_count + 1), k=random.randint(2, self.user_count / 2)):
                    writer.writerow([user_id, chat_id])


    def generate_user(self) -> list[str]:
        user = []
        firstname = random.choice(FIRSTNAMES)
        lastname = random.choice(LASTNAMES)

        user.append(self.__get_username(firstname, lastname))
        user.append(self.__get_email(firstname, lastname))
        user.append(self.__generate_password())

        return user


    def generate_chat(self) -> list[str]:
        chat = []

        chat.append(f"{random.randint(1, self.user_count)}")
        chat.append(f"Chat{self.chatId}")

        self.chatId += 1
        return chat


    def generate_text(self) -> list[str]:
        text = lorem.get_sentence()
        user_id = random.randint(1, self.user_count)
        chat_id = random.randint(1, self.chat_count)
        return [text, user_id, chat_id]


    def __get_username(self, firstname: str, lastname: str) -> str:
        return f"{firstname} {lastname}"


    def __get_email(self, firstname: str, lastname: str) -> str:
        return f"{firstname.lower()}.{lastname.lower()}{random.randint(0, 99)}@gmail.com"


    def __generate_password(self) -> str:
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(random.randint(6, 15)))
        return password
