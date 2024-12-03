# Python counter from 1 to 10 with 2 seconds delay and print's the container ID

import os
import time

# Print numbers from 1 to 10 with 2 seconds delay
for i in range(1, 11):
    print(i)
    time.sleep(2)

# Print the container ID
def get_container_id():
    container_id = os.getenv("HOSTNAME")
    if container_id:
        print(f"This script is running inside the container with ID: {container_id}")
    else:
        print("HOSTNAME environment variable is not set.")

if __name__ == "__main__":
    get_container_id()