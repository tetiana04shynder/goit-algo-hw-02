from collections import deque

def is_palindrome(text: str) -> bool:
    # Прибираємо пробіли та приводимо до нижнього регістру
    cleaned_text = ''.join(text.split()).lower()
    
    # Створюємо двосторонню чергу з символів рядка
    d = deque(cleaned_text)
    
    # Порівнюємо символи з обох кінців
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


# Тестові приклади
examples = [
    "Я несу гусення",
    "Привіт",
    "Сон",
    "Потоп"
]

for ex in examples:
    print(f"'{ex}' -> {is_palindrome(ex)}")