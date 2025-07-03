from django.test import TestCase
from todo.models import Task
from django.utils import timezone
from datetime import datetime

# Create your tests here.
class SampleTestCase(TestCase):
    def test_sample(self):
        self.assertEqual(1+2,3)

class TaskModelTestCase(TestCase):
    def test_create_task1(self):
        due = timezone.make_aware(datetime(2024, 6, 30, 23, 59, 59))
        task=Task(title='Task 1', due_at=due)
        task.save()

        task=Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, 'Task 1')
        self.assertFalse(task.completed)
        self.assertEqual(task.due_at, due)
    
    def test_create_task2(self):
        task=Task(title='Task 2')
        task.save()

        task=Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, 'Task 2')
        self.assertFalse(task.completed)
        self.assertIsNone(task.due_at,None)

    def test_is_overdue(self):
        due = timezone.make_aware(datetime(2024, 6, 30, 23, 59, 59))
        current=timezone.make_aware(datetime(2024, 6, 30, 0, 0, 0))
        task=Task(title='Task 1', due_at=due)
        task.save()

        self.assertFalse(task.is_overdue(current))