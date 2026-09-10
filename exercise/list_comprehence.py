def valiate_mail(mails):
    return [mail.lower().strip() for mail in mails if mail.find("@") != -1]


raw_emails = ["  Alice@gmail.com ", "bob_at_yahoo.com",
              "CHARLIE@outlook.com", "invalid_email", "  delta@company.com  "]
print(valiate_mail(raw_emails))


def filter_api(logs):
    return [log for log in logs if log["status"] == 404 or log["status"] == 500]


print(filter_api([
    {"req_id": "A101", "status": 200, "path": "/home"},
    {"req_id": "B202", "status": 404, "path": "/about-us-old"},
    {"req_id": "C303", "status": 200, "path": "/dashboard"},
    {"req_id": "D404", "status": 500, "path": "/checkout"},
]))
