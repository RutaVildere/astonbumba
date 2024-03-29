import os
import random

def createNextId(id):
    return str(int(id) + 1)

# returns empty if user file is empty
# else returns a list of tuples - (question, answer)
def checkHistory(userId):
    filepath = userId+".txt"
    if os.path.isfile(filepath):
        with open(filepath, 'r') as history:
            lines = history.readlines()
            if os.path.getsize(filepath) == 0: return "Empty"
            else:
                answers = []
                for i in lines:
                    info = i.split(';')
                    answers.append((info[0], info[1].split('\n')[0])) # Deletes the useless \n
            return answers
    else:
        return "Empty"


def addToHistory(question, answer, userId):
    filepath = userId + ".txt"
    newanswer = [question, ';', answer, '\n']
    with open(filepath, 'a+') as history:
        history.writelines(newanswer)


# Returns -1 if username or email is taken. returns 0 on success
def createAccount(name, surname, username, email, password):
    # Account structure:
    # name, surname, username, email, pass, id
    # id - numurs DB
    database = open("userDB.txt", 'r')
    lines = database.readlines()
    database.close()
    lastid = 0
    for i in lines:
        info = i.split(',')
        if info == ['\n']: break
        if info[2] == username or info[3] == email: return -1
        lastid = info[5]

    database = open("userDB.txt", 'a')
    newUser = [
        name, ",",
        surname, ",",
        username, ",",
        email, ",",
        password, ",",
        createNextId(lastid), "", '\n'
    ]
    database.writelines(newUser)
    database.close()
    return lastid  # returns user ID


# returns userID on sucessful login, otherwise False
def loginIntoAccount(username, password):
    database = open("userDB.txt", 'r')
    lines = database.readlines()
    database.close()
    for i in lines:
        info = i.split(',')
        if info == ['\n']: break
        if info[2] == username and info[4] == password:
            return info[5]  # returns user ID

    return False


def answers():
    fails = open("atbildes.txt", "r")
    x = fails.readline()
    atbildes = x.split(";")
    rez = random.randint(0, len(atbildes)-1)
    return atbildes[rez]
if __name__ == '__main__':
    createAccount("vards", "uzvards", "logins1", "email1", "pass")
    addToHistory("Are u friendly?", "No", '0')
    x = checkHistory('0')

