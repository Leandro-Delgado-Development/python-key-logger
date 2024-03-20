import json

managed_words = []


def op():
    write_file = open("collected_data.txt", "a")
    read_file = open("stmp.txt","r")
    with open('database.json') as database_file:
        database = json.load(database_file)
    content = read_file.read()
    
    for word_to_verify in database["words"]:
        if str(word_to_verify).lower().strip() in content:
            if word_to_verify not in managed_words:
                write_file.write(f"\n{str(word_to_verify).lower().strip()}")
                managed_words.append(word_to_verify)
            else:
                continue
        else:
            continue

    write_file.close()
        

while True:
    op()



