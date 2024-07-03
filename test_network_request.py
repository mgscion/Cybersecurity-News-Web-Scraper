import requests

def test_network_request():
    url = 'https://krebsonsecurity.com/'
    response = requests.get(url)
    if response.status_code == 200:
        print("Network request successful")
        print(response.text[:500])  # Print the first 500 characters of the response
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    test_network_request()
