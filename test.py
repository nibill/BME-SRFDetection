import report
import process

images = process.load("data")
classified = []

oneSRF = False
onenoSRF = False
oneUnknown = False

def thread(input):
    classified.append(process.classify(input))

for i in images :
    if i[0] == "SRF" and oneSRF == True:
        continue
    if i[0] == "noSRF" and onenoSRF == True:
        continue
    if i[0] == "unknown" and oneUnknown == True:
        continue
    if i[0] == "SRF":
        oneSRF = True
    if i[0] == "noSRF":
        onenoSRF = True
    if i[0] == "unknown":
        oneUnknown = True
    threads.append(Thread(target=thread, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

report = report.create_html(classified)
report_file = open("report.test.html","w")
report_file.write(report)
report_file.close()