with open('raw_saves.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("--- FIRST 500 CHARACTERS ---")
    print(content[:500])
    print("---------------------------")
