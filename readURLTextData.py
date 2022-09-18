import requests
try:
    url = "https://www..txt"
    data = requests.get(url)
    data = data.text 
    data = data.split()
except:
    print("Invalid URL or error occured!")

emailCount = {}
flag = False
#print(data)
for check in data:
    if flag:
        emailAddress = check
        emailCount[emailAddress] = emailCount.get(emailAddress,0) + 1
        flag = False    
    if check =="From:":
        flag = True

#print(emailCount)

counts=emailCount.values()
sortedCount=sorted(counts)
secondLargest=sortedCount[-2]
#print(secondLargest)
print("Second greatest email sender/s:")
for email, count in emailCount.items():
    if count == secondLargest:
        print(email)
