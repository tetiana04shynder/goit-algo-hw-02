import queue
import time
import random

# Створюємо чергу
requests = queue.Queue()
request_id = 0  

def generate_request():
    """Генерація нової заявки і додавання до черги"""
    global request_id
    request_id += 1
    new_request = f"Заявка №{request_id}"
    requests.put(new_request)
    print(f"[+] Додано {new_request}")

def process_request():
    """Обробка заявки (якщо вона є  у черзі)"""
    if not requests.empty():
        current_request = requests.get()
        print(f"[~] Обробка {current_request}...")
        time.sleep(1)  # імітація часу обробки
        print(f"[✓] {current_request} оброблено")
    else:
        print("[!] Черга порожня, немає заявок для обробки")

def main():
    print("Система обробки заявок запущена. Натиснути Ctrl+C для завершення.\n")
    try:
        while True:
            # Випадково генеруємо нові заявки
            if random.choice([True, False]):
                generate_request()
            
            # Завжди намагаємось обробити заявку
            process_request()

            time.sleep(1)  # невелика пауза між циклами
    except KeyboardInterrupt:
        print("\n[!] Програму завершено користувачем.")

if __name__ == "__main__":
    main()