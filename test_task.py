
import unittest
from Add_task import add_task, view_tasks
from manage_task import complete_task, delete_task

class TestTaskFunctions(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        add_task(tasks, "Task 1")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Task 1")
        self.assertFalse(tasks[0]["completed"])

    def test_complete_task(self):
        tasks = [{"task": "Task 1", "completed": False}]
        complete_task(tasks, 0)
        self.assertTrue(tasks[0]["completed"])

    def test_delete_task(self):
        tasks = [{"task": "Task 1", "completed": False}]
        delete_task(tasks, 0)
        self.assertEqual(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()
