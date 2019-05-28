import numpy as np
import csv

def evaluation(classified):
    classified = sorted(classified, key=lambda c: c[3][2])
    len_count = len(list(filter(lambda c: c[1] != "unknown",classified)))

    threshold = 0.3
    success = 0

    with open('submission.csv', 'w') as csvfile:
        writer=csv.writer(csvfile, delimiter=',', lineterminator='\n',)
        for c in range(len(classified)):
            if classified[c][3][2] > threshold:
                classified[c][2] = "SRF"
                writer.writerow('0')
            else:
                classified[c][2] = "noSRF"
                writer.writerow('1')

            if classified[c][1] == classified[c][2]:
                success = success + 1

    

    return classified, [success/len_count]
