import sys

import task1
import task2
import task3
import task4

TASK3_TARGET = "."


def run_section(title: str, runner) -> None:
    print(f"\n=== {title} ===")
    runner()


def run_task3() -> None:
    original_argv = sys.argv
    sys.argv = ["task3.py", TASK3_TARGET]
    try:
        task3.main()
    finally:
        sys.argv = original_argv


def main() -> None:
    run_section("Task 1: total_salary", task1.main)
    run_section("Task 2: get_cats_info", task2.main)
    run_section(f"Task 3: directory tree for '{TASK3_TARGET}'", run_task3)
    run_section("Task 4: assistant bot", task4.main)


if __name__ == "__main__":
    main()
