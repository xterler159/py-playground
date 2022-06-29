import requests
import os

CONTENT_TYPE = 'Content-Type'
NODE_JS = "https://nodejs.org/en/"
NODE_JS_DOWNLOAD = "https://nodejs.org/dist/v16.15.1/node-v16.15.1.pkg"


def get_apps():
    if os.name == "posix":
        response = requests.get(NODE_JS_DOWNLOAD)
        headers = response.headers
        content_type = response.headers[CONTENT_TYPE]
        content = response.content

        print(f"get_apps __name__:{__name__}")

        if content_type == "application/octet-stream":
            with open("test.pkg", "wb+") as file:
                file.write(content)

        # print(f'content_type: {content_type}')
        # print(f'headers: {headers}')
