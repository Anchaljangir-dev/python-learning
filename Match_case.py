def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown status"

print(http_status(200))
print(http_status(404))
print(http_status(3434)) # simpleast way 

# can make merged dictionary using this
dic1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dic2 = {"e": 5, "f": 6, "g": 7, "h": 8}
merged = dic1 | dic2 
print(merged)