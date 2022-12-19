ips = []
user_in = ""
while user_in != "done":
    user_in = input("IP address or type done to exit: ")
    if user_in != "done":
        ips.append(user_in)
print(f"Your IPs are: {ips}")
#Infinite Loops
while True:
    best_num=input("What's your favorite number? ")
    if best_num == "42":
        break
    else:
        print(f"{best_num} is not the best number. Try again.")
