
import csv
import math


def calculate_grade(marks):
    marks = float(marks)

    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    for threshold, grade in [(80, "A"), (60, "B"), (40, "C")]:
        if marks >= threshold:
            return grade

    return "F"


def read_students(filename="students.csv"):
    students = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for line_number, row in enumerate(reader, start=2):
            try:
                if not row.get("id") or not row.get("name"):
                    raise ValueError("Missing ID or name")
                if not row.get("marks"):
                    raise ValueError("Missing marks")

                marks = float(row["marks"])
                grade = calculate_grade(marks)

                students.append({
                    "id": row["id"],
                    "name": row["name"],
                    "marks": marks,
                    "grade": grade,
                })
            except (ValueError, TypeError) as exc:
                raise ValueError(
                    f"Invalid CSV record at line {line_number}: {exc}"
                ) from exc

    return students

def generate_report(filename="students.csv"):
    students = read_students(filename)

    print("ID | Name | Marks | Grade")
    print("-" * 30)

    for student in students:
        print(
            f'{student["id"]} | {student["name"]} | '
            f'{student["marks"]:.1f} | {student["grade"]}'
        )


if __name__ == "__main__":
    generate_report()
