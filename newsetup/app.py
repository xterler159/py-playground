import requests
import urllib3
import platform

from rich.logging import RichHandler

# disabling warning. this is bad
# have to configure properly SSL stuff with request
# because creative is using a custom certificate.
urllib3.disable_warnings()

CONTENT_TYPE = "Content-Type"
NODE_JS = "https://nodejs.org/en/"
FILE_NAME = "node-v16.15.1.pkg"
NODE_JS_DOWNLOAD = f"https://nodejs.org/dist/v16.15.1/{FILE_NAME}"
TEMP_FOLDER_NAME = "new-setup-files"
WINDOWS = "Windows"
LINUX = "Linux"
DARWIN = "Darwin"


def get_apps():
    try:
        file_extension = get_platform_extension()
        response = requests.get(NODE_JS_DOWNLOAD, verify=False)

    except requests.exceptions.SSLError as ex:
        print(f"Error while downloading: {ex}")

    headers = response.headers
    content_type = headers[CONTENT_TYPE]
    content = response.content

    if content_type == "application/octet-stream":
        with open(FILE_NAME, "wb+") as file:
            file.write(content)


def get_platform_extension():
    """
    Function to determine which extension to use,
    depending on the os (windows, linux or macos)
    """

    if platform.system() == WINDOWS:
        return ".exe"

    if platform.system() == DARWIN:
        return ".pkg"

    if platform.system() == LINUX:
        return LINUX
