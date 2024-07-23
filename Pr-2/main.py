import multiprocessing
import time

def sender(queue):
    messages = ["Hello", "World"]
    for message in messages:
        print(f"Sending: {message}")
        queue.put(message)
        time.sleep(1)
    queue.put("END")

def receiver(queue):
    while True:
        message = queue.get()
        if message == "END":
            break
        print(f"Received: {message}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    sender_process = multiprocessing.Process(target=sender, args=(queue,))
    receiver_process = multiprocessing.Process(target=receiver, args=(queue,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()
