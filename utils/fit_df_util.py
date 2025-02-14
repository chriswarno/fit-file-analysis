csv = []

def csv_head(record_fields):
    header = []
    header.append(record_fields)
    csv.append(header)
    return csv


def csv_body(record_data):
    body = []
    body.append(record_data)
    csv.append(body)
    return csv