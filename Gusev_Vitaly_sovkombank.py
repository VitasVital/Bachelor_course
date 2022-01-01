#Гусев Виталий Евгеньевич

import numpy as np
from random import randint
import pyodbc
from datetime import datetime

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-BH0GV9U\MSSQLSERVER01;"
                      "Database=Sovcombank;"
                      "Trusted_Connection=yes;")

# joy = ["\U0001f600", "\U0001f603", "\U0001F601", "\U0001F604", "\U0001F602", "\U0001F60A", "\U0001F606", "\U0001F973", "\U0001F929"]
# sadness = []
# anger = ["\U0001F47F", "\U0001F62C", "\U0001F624", "\U0001F621", "\U0001F47A", "\U0001F480", "\U0001F620", "\U0001F92F", "\U0001F928"]

joy = ["U0001f600", "U0001f603", "U0001F601", "U0001F604", "U0001F602", "U0001F60A", "U0001F606", "U0001F973", "U0001F929"]
sadness = ["U0001F644", "U0001F614", "U0001F60C", "U0001F641", "U0001F615", "U0002639", "U0001F629", "U0001F62B", "U0001F613"]
anger = ["U0001F47F", "U0001F62C", "U0001F624", "U0001F621", "U0001F47A", "U0001F480", "U0001F620", "U0001F92F", "U0001F928"]

cursor = cnxn.cursor()
client_id = cursor.execute("select max(Id_client) from Message;").fetchval() #создаём айди нового клиента при запуске приложения
if (client_id == None):
    client_id = 1
else:
    client_id += 1

while (True):
    messages_last = ""
    message = input("Клиент: ")
    if (message in joy): #сессия начинается после первого правильно введенного сообщения
        print("Привет! Рад, что ты в хорошем настроении\n")
        messages_last = message
    elif (message in sadness):
        print("Привет! Не грусти!!!\n")
        messages_last = message
    elif (message in anger):
        print("Привет! Что-то ты сегодня злой(\n")
        messages_last = message
    else:
        print("Я тебя не понимаю\n")
        continue
    session_start = datetime.now()  # время начала сессии
    cursor.execute("INSERT INTO Session(Time_start) VALUES(?) ", (session_start))
    cnxn.commit()
    session_id = cursor.execute("SELECT @@IDENTITY;").fetchval() #айди начавшейся сессии
    cursor.execute("INSERT INTO Message(Time, Id_session, Text, Id_client) VALUES(?, ?, ?, ?) ", (session_start, session_id, message, client_id))
    cnxn.commit()
    message_last_time = session_start #время последнего сообщения
    while (True):
        message = input("Клиент: ")
        if ((datetime.now() - message_last_time).total_seconds() > 60):
            session_end = datetime.now()
            cursor.execute("UPDATE Session SET Time_end = ? WHERE Id = ?;", (session_end, session_id))
            cnxn.commit()
            print("Время сессии вышло\n")
            break
        elif (message in joy):
            cursor.execute("INSERT INTO Message(Time, Id_session, Text, Id_client) VALUES(?, ?, ?, ?) ",
                           (datetime.now(), session_id, message, client_id))
            cnxn.commit()
            if (messages_last in joy):
                print("Рад, что не унываешь\n")
            elif (messages_last in sadness):
                print("Наконец-то ты развеселился\n")
            elif (messages_last in anger):
                print("Радостный ты лучше, чем злой\n")
            messages_last = message
            message_last_time = datetime.now()
        elif (message in sadness):
            cursor.execute("INSERT INTO Message(Time, Id_session, Text, Id_client) VALUES(?, ?, ?, ?) ",
                           (datetime.now(), session_id, message, client_id))
            cnxn.commit()
            if (messages_last in joy):
                print("Ты чего приуныл?\n")
            elif (messages_last in sadness):
                print("Перестань грустить, наконец\n")
            elif (messages_last in anger):
                print("Извини, если обидел\n")
            messages_last = message
            message_last_time = datetime.now()
        elif (message in anger):
            cursor.execute("INSERT INTO Message(Time, Id_session, Text, Id_client) VALUES(?, ?, ?, ?) ",
                           (datetime.now(), session_id, message, client_id))
            cnxn.commit()
            if (messages_last in joy):
                print("Ты чего разозлился? Ты же радовался\n")
            elif (messages_last in sadness):
                print("Ты очень мило злишься с заплаканным лицом\n")
            elif (messages_last in anger):
                print("Ты всегда такой злой?\n")
            messages_last = message
            message_last_time = datetime.now()
        else:
            session_end = datetime.now()
            cursor.execute("UPDATE Session SET Time_end = ? WHERE Id = ?;", (session_end, session_id))
            cnxn.commit()
            print("Я тебя не понимаю\n")
            break

