from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "numbers.txt"


def load_numbers() -> list[int]:
    raw_lines = DATA_PATH.read_text(encoding="utf-8").strip().splitlines()
    return [int(line.strip()) for line in raw_lines if line.strip()]


def calculate_stats(numbers: list[int]) -> dict[str, float | int]:
    average = sum(numbers) / len(numbers)
    return {
        "average": average,
        "minimum": min(numbers),
        "maximum": max(numbers),
    }


def main() -> None:
    numbers = load_numbers()
    stats = calculate_stats(numbers)
    print(f"Average: {stats['average']:.2f}")
    print(f"Minimum: {stats['minimum']}")
    print(f"Maximum: {stats['maximum']}")


if __name__ == "__main__":
    main()
