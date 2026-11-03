srtt = ("message")
print(srtt.strip())
if len(srtt) == 0:
    print("empty")
elif "spam" in srtt.lower():
    print("BLOCKED")
else:
    print(srtt)
    

    messages = ["  ", "Get cheap loans now! SPAM", "Hello, how are you?", "  Important update  "]

for msg in messages:
    cleaned_msg = msg.strip()
    
    if len(cleaned_msg) == 0:
        print("empty")
    elif "spam" in cleaned_msg.lower():
        print("BLOCKED")
    else:
        print(cleaned_msg)