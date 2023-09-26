import requests
import time

def main():
    while True:
        h = requests.get("http://169.254.169.254/1.0/meta-data")
        print(h.text)
        time.sleep(60)


if __name__ == "__main__":
    main()
