import requests
import json

class BookstackAPI:
    def __init__(self) -> None:
        pass

    def LoadCredential(self, cred):
        self.header = BookstackAPI.AuthenticationHeader(cred['token'],cred['secret'])
        self.cred = cred

    def AuthenticationHeader(token, secret):
        # Set up the API request headers and payload
        return {
            "Authorization": f'Token {token}:{secret}'
        }

    def create_page(self, book_id, title, content):
        # Send the API request
        payload = {
            "book_id": book_id,
            "name": title,
            "markdown": content
        }
        header = self.header
        header["Content-Type"]: 'application/json'

        response = requests.post(
            self.cred['url']+'api/pages', header, json=payload)

        # Check if the request was successful (201 status code)
        if response.status_code == 200:
            # Print the API response data
            print("request suceed")
            return response.json()
        else:
            # Print the error message if the request failed
            print(f"API request failed: {response.text}")
            return None
        
    def create_attachment(self, page_id, title, file_path):
        header = self.header
        header["Content-Type"]: 'multipart/form-data'

        payload = {
            "uploaded_to": page_id,
            "name": title,
        }
        file_data = {"file": ("test.png",open(file_path, "rb"),"image")}

        response = requests.post(
            self.cred['url']+'api/attachments', headers=header, data=payload, files=file_data)

        # Check if the request was successful (200 status code)
        if response.status_code == 200:
            # Print the API response data
            print("request suceed")
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            # Print the error message if the request failed
            print(f"API request failed: {response.text}")
            return None