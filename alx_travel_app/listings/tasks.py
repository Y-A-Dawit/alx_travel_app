# listings/tasks.py

from celery import shared_task
import time

@shared_task
def sample_task():
    print("This is a test task from Celery")
    return "Task complete"

@shared_task
def demo_sleep(seconds=3):
    time.sleep(seconds)
    return f"Slept for {seconds}"