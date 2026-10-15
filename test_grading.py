
import tempfile
import unittest
from pathlib import Path

from grading import calculate_grade, read_students


class TestGrading(unittest.TestCase):

    def test_boundary_values(self):
        expected = {
            39: "F", 40: "C", 59: "C",
            60: "B", 79: "B", 80: "A", 100: "A"
        }
        for marks, grade in expected.items():
            with self.subTest(marks=marks):
                self.assertEqual(calculate_grade(marks), grade)

    def test_invalid_marks(self):
        for marks in (-1, 101):
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    calculate_grade(marks)

    def test_non_numeric_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade("abc")

    def test_non_finite_marks(self):
        for marks in ("NaN", "inf", "-inf"):
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    calculate_grade(marks)

    def test_malformed_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "students.csv"
            path.write_text(
                "id,name,marks\n1,Aarav,\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "line 2"):
                read_students(str(path))

    def test_missing_csv_column(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "students.csv"
            path.write_text(
                "id,name\n1,Aarav\n", encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                read_students(str(path))


if __name__ == "__main__":
    unittest.main()
