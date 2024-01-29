import os
from openai import OpenAI 
from dotenv import load_dotenv

API = "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"
client = OpenAI(api_key=API)
load_dotenv()

def ReplyBrain(question, chat_log=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    chat_log_path = os.path.join(base_dir, "DataBase", "chat_log.txt")  # Construct the full path to the chat log

    with open(chat_log_path, "r", encoding= 'utf-8') as file_log:
        chat_log_template = file_log.read()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nMarsh : '
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "from now on you are an AI desktop assistant"},
            {"role": "system", "content": "your name is maarsh"},
            {"role": "system", "content": "you were created by  harsh and  maddy"},
            {"role": "system", "content": " harsh and  maddy are your creator"},
            {"role": "system", "content": " harsh and  maddy created you"},
            {"role": "system", "content": "you were made by  harsh and  maddy"},
            {"role": "system", "content": " harsh and  maddy are your makers"},
            {"role": "system", "content": " always add the prefix 'Sir' before mentioning Harsh and Maddy"},
            {"role": "system", "content": chat_log},
            {"role": "user", "content": question}
        ],
        temperature=0.5,
        max_tokens=60,
    )
    answer = response.choices[0].message.content.strip()

    chat_log_template_update = chat_log_template + f"\nYou : {question} \nMarsh : {answer}"
    with open(chat_log_path, "w", encoding='utf-8') as file_log:
        file_log.write(chat_log_template_update)

    return answer
