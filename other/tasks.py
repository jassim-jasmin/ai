from celery import Celery

# To run the workder server
# $ celery -A tasks worker --loglevel=info
# Then we can use
# >>> from tasks import add
# >>> add.delay(4, 4)
# For checking task completion
# >>> result.ready()
# For getting result
# result.get(timeout=1)

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1' # for keeping result
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

@app.task
def add(x, y):
    return x + y