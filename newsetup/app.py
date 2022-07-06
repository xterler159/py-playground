import requests
import os

CONTENT_TYPE = "Content-Type"
NODE_JS = "https://nodejs.org/en/"
FILE_NAME = "node-v16.15.1.pkg"
NODE_JS_DOWNLOAD = f"https://nodejs.org/dist/v16.15.1/{FILE_NAME}"
TEMP_FOLDER_NAME = "new-setup-files"
YES = "YES"
NO = "NO"


def get_apps():
    response = requests.get(NODE_JS_DOWNLOAD)
    headers = response.headers
    content_type = headers[CONTENT_TYPE]
    content = response.content

    if content_type == "application/octet-stream":
        try:
            with open(FILE_NAME, "wb+") as file:
                file.write(content)

        except FileNotFoundError as ex:
            print("Error:", ex)


def get_user_wanted_apps():
    apps = None
    apps_txt_path = os.path.dirname(__file__) + "/apps.txt"
    user_wanted_apps = []

    try:
        with open(apps_txt_path, "r", encoding="utf8") as file:
            apps = file.read()

    except FileNotFoundError as ex:
        print(f"Error: {ex}")

    finally:
        if apps:
            app_list = apps.split("\n")

            for app in app_list:
                print(f"Do you want to install {app} - {YES}/{NO}?")
                user_response = input("")

                if user_response == YES.lower():
                    user_wanted_apps.append(app)

        return user_wanted_apps
