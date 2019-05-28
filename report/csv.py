def create_csv(classified):
    csv = "filename,label\n"
    for item in classified:
        if item[2] == "SRF":
            csv += item[0] + "1\n"
        else:
            csv += item[0] + "0\n"
    return csv