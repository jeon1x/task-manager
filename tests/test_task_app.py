import unittest
from task_app import create_task, list_tasks


class TestTaskApp(unittest.TestCase):

    def test_create_task_valid(self):
        tasks = []
        result = create_task("Купить молоко", tasks)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Купить молоко")

    def test_blank_title_is_rejected(self):
        tasks = []
        with self.assertRaises(ValueError):
            create_task("", tasks)

    def test_whitespace_title_is_rejected(self):
        tasks = []
        with self.assertRaises(ValueError):
            create_task("   ", tasks)

    def test_title_is_stripped(self):
        tasks = []
        result = create_task("  Задача с пробелами  ", tasks)
        self.assertEqual(result[0]["title"], "Задача с пробелами")

    def test_task_done_default_false(self):
        tasks = []
        result = create_task("Тест", tasks)
        self.assertFalse(result[0]["done"])

    def test_multiple_tasks(self):
        tasks = []
        create_task("Первая", tasks)
        create_task("Вторая", tasks)
        self.assertEqual(len(tasks), 2)

    def test_list_tasks_empty(self):
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            list_tasks([])
        self.assertIn("пуст", buf.getvalue().lower())

    def test_list_tasks_non_empty(self):
        import io
        from contextlib import redirect_stdout
        tasks = [{"title": "Задача 1", "done": False}]
        buf = io.StringIO()
        with redirect_stdout(buf):
            list_tasks(tasks)
        self.assertIn("Задача 1", buf.getvalue())

    def test_duplicate_titles_allowed(self):
        tasks = []
        create_task("Повтор", tasks)
        create_task("Повтор", tasks)
        self.assertEqual(len(tasks), 2)

    def test_create_task_returns_same_list(self):
        tasks = []
        result = create_task("X", tasks)
        self.assertIs(result, tasks)


if __name__ == "__main__":
    unittest.main()