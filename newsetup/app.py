import requests

CONTENT_TYPE = "Content-Type"
NODE_JS = "https://nodejs.org/en/"
FILE_NAME = "node-v16.15.1.pkg"
NODE_JS_DOWNLOAD = f"https://nodejs.org/dist/v16.15.1/{FILE_NAME}"
TEMP_FOLDER_NAME = "new-setup-files"


def get_apps():
    response = requests.get(NODE_JS_DOWNLOAD)
    headers = response.headers
    content_type = headers[CONTENT_TYPE]
    content = response.content

    if content_type == "application/octet-stream":
        with open(FILE_NAME, "wb+") as file:
            file.write(content)
