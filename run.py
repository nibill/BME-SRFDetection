import report
import process
from threading import Thread

images = process.load("data")
classified = []
threads = []

def thread(input):
    classified.append(process.classify(input))

for i in images :
    threads.append(Thread(target=thread, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()
    
report = report.create_html(classified)
report_file = open("report.html","w")
report_file.write(report)
report_file.close()