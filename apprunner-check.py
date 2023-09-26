import requests

def main():
    h = requests.get("http://169.254.169.254/1.0/meta-data")
    print(h.text)


if __name__ == "__main__":
    main()
