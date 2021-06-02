'''
- Thread 1: 2s/1 lần gọi tới API, nếu có messages mới => In ra
- Thread 2: Chờ người dùng nhâp, enter -> gửi lên messages
  # https://6065d36cb8fbbd00175677e7.mockapi.io/s-group/

'''
import requests
from time import sleep
from threading import Thread
 
BASE_URL = r"https://60b4fb03fe923b0017c835a6.mockapi.io/"
last_msg_id = "0"
userID = "Linh"
 
def send_message():
    global userID
    msg = input("Enter your message : ")
    res = requests.post(BASE_URL + "Mindy", data={
        "userID": userID,
        "message": msg
    })
 
def receive_message():
    global BASE_URL
    global last_msg_id
    global userID
    while True:
        res = requests.get(BASE_URL + "Mindy")
        if res.status_code == "200":
            print(res)
            continue
        messages = res.json()
        tmp = last_msg_id
        for message in messages:
            if int(message["id"]) <= int(tmp) or message.get("userID") == userID:
                continue
            print("from", message.get("userID", "Unknow"), ":", message.get("message", "Nothing"))
            last_msg_id = message["id"]
        sleep(2)
 
if __name__ == "__main__":
    send_msg_thread = Thread(target=send_message, daemon=True)
    receive_msg_thread = Thread(target=receive_message, daemon=True)
 
    send_msg_thread.start()
    receive_msg_thread.start()
 
    send_msg_thread.join()
    receive_msg_thread.join()
 
 
 