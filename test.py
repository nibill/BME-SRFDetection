import report
import process
from threading import Thread
import numpy as np
from queue import Queue

images = process.load("data")
images = list(filter(lambda i: i[0] != "unknown",images))

classified = []
threads = []

q = Queue(maxsize=0)
num_theads = 20

def thread(_q):
    while not _q.empty():
        image = _q.get()
        classified.append(process.classify(image))
        _q.task_done()

for i in images:
    q.put(i)

for t in range(num_theads):
    t = Thread(target=thread, args=(q,))
    t.start()

q.join()
    

classified, evaluation = report.evaluation(classified)
report = report.create_html(classified,evaluation)
report_file = open("report.test.html","w")
report_file.write(report)
report_file.close()