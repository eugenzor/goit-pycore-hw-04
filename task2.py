from pathlib import Path

CATS_FILE_PATH = "files/cats_file.txt"


def get_cats_info(path: str) -> list[dict]:
    """Прочитати файл із даними про котів та повернути список словників.

    Кожен рядок файлу має формат: ``<id>,<name>,<age>``.
    Некоректні рядки пропускаються мовчки. У разі помилок читання файлу
    піднімає відповідний виняток (``FileNotFoundError``, ``OSError``).
    """
    file_path = Path(path)
    cats: list[dict] = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                continue
            cat_id, name, age = (part.strip() for part in parts)
            cats.append({"id": cat_id, "name": name, "age": age})

    return cats


def main() -> None:
    try:
        cats_info = get_cats_info(CATS_FILE_PATH)
    except FileNotFoundError:
        print(f"Файл '{CATS_FILE_PATH}' не знайдено.")
        return
    except OSError as error:
        print(f"Не вдалося прочитати файл '{CATS_FILE_PATH}': {error}")
        return

    print(cats_info)


if __name__ == "__main__":
    main()
