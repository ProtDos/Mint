import requests
import utils.utils

class ProxyGeneration:
    def __init__(self):
        self.utils = utils.utils.Utils()

    def generate(self, url, social_media):
        try:
            ip = self.proxy_generator()
            response = requests.get(url, proxies={"https": ip}, timeout=10)
            if social_media == "roblox":
                return response
            else:
                self.check(response, social_media)
        except Exception as error:
            self.utils.logs(f"{error}")

    def proxy_generator(self):
        try:
            response = requests.get('https://api.getproxylist.com/proxy').json()
            proxy = response["protocol"] + "://" + response["ip"] + ":" + str(response["port"])
            return proxy
        except Exception as error:
            self.utils.logs(f"{error}")

    def check(self, response, social_media):
        try:
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media=social_media)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def save(self, social_media):
        try:
            file = open("found_usernames.txt", "a")
            file.write(f"{social_media}:{self.username}\n")
            file.close()
        except:
            self.utils.logs(f"{error}")