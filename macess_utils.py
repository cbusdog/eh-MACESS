import random
import time

def get_queue_length():
    return random.randint(10, 100)

def get_failed_jobs():
    return random.randint(0, 5)

def get_avg_processing_time():
    return random.uniform(150, 300)
