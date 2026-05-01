from pathlib import Path

SALARY_FILE_PATH = "files/salary_file.txt"


def total_salary(path: str) -> tuple[int, float]:
    """Прочитати файл із зарплатами та повернути (загальну суму, середню).

    Кожен рядок має формат: ``<Прізвище Ім'я>,<сума>``.
    Некоректні рядки пропускаються мовчки. У разі помилок читання файлу
    піднімає відповідний виняток (``FileNotFoundError``, ``OSError``).
    """
    file_path = Path(path)

    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    total = 0
    count = 0
    for line in lines:
        parts = line.split(",")
        if len(parts) != 2:
            continue
        try:
            total += int(parts[1])
        except ValueError:
            continue
        count += 1

    if count == 0:
        return 0, 0

    return total, total / count


def main() -> None:
    try:
        total, average = total_salary(SALARY_FILE_PATH)
    except FileNotFoundError:
        print(f"Файл '{SALARY_FILE_PATH}' не знайдено.")
        return
    except OSError as error:
        print(f"Не вдалося прочитати файл '{SALARY_FILE_PATH}': {error}")
        return

    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )


if __name__ == "__main__":
    main()
