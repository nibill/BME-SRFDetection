import report
import process

images = process.load("data")
classified = []

for i in images :
    classified.append(process.classify(i))

report = report.create_html(classified)
report_file = open("report.html","w")
report_file.write(report)
report_file.close()