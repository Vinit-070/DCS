from multiprocessing import Queue
import sys

def sender(queue):
  message = "Hello from Sender!"
  queue.put(message)
  print(f"Sent message: {message}")

def receiver(queue):
  # Get message from the queue
  message = queue.get()
  print(f"Received message: {message}")

if __name__ == "__main__":
  # Create a queue for message passing
  queue = Queue()

  # Choose between sender or receiver behavior
  if len(sys.argv) > 1 and sys.argv[1] == "sender":
    sender(queue)
  else:
    receiver(queue)
