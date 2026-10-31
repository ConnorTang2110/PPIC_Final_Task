import unittest
from todo import Task, TaskPool
from io import StringIO
import sys

class TestTaskPool(unittest.TestCase): 

    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self): 
        task = Task("New Task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self): 
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertEqual(len(open_tasks), 3)
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def test_get_done_tasks(self): 
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertEqual(len(done_tasks), 3)
        self.assertTrue(all(task.status == "Done" for task in done_tasks)) 

if __name__ == "__main__": 
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)

    captured_output = StringIO() 

    runner = unittest.TextTestRunner(stream=captured_output, verbosity=2)
    result = runner.run(suite)

    output_lines = captured_output.getvalue().splitlines()

    for line in output_lines: 
        if "ok" in line: 
            print(line.split(' ')[0] + ' ... ok')

    total_tests = result.testsRun
    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests

    print(f"Total Tests: {total_tests}")

    if total_tests > 0:
        print(f"Passed: {passed_tests} ({(passed_tests / total_tests) * 100:.2f}%)")
        print(f"Failed: {failed_tests} ({(failed_tests / total_tests) * 100:.2f}%)")
    else:
        print("No tests were run.")


