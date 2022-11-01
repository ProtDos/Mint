import requests
import utils.utils

class ProxyRotation:
    def __init__(self):
        self.utils = utils.utils.Utils()

    def rotate(self, social_media, username):
        try:
            if social_media == "github":
                self.github(username, self.generate())
            elif social_media == "facebook":
                self.facebook(username, self.generate())
            elif social_media == "linkedin":
                self.linkedin(username, self.generate())
            elif social_media == "replit":
                self.replit(username, self.generate())
            elif social_media == "paypal":
                self.paypal(username, self.generate())
            elif social_media == "youtube":
                self.youtube(username, self.generate())
            elif social_media == "twitch":
                self.twitch(username, self.generate())
            elif social_media == "instagram":
                self.instagram(username, self.generate())
            elif social_media == "tiktok":
                self.tiktok(username, self.generate())
            elif social_media == "pornhub":
                self.pornhub(username, self.generate())
            elif social_media == "onlyfans":
                self.onlyfans(username, self.generate())
            elif social_media == "feds":
                self.feds(username, self.generate())
            elif social_media == "twitter":
                self.twitter(username, self.generate())
            elif social_media == "reddit":
                self.reddit(username, self.generate())
            elif social_media == "steam":
                self.steam(username, self.generate())
            elif social_media == "discord":
                self.discord(username, self.generate())
            elif social_media == "ogu":
                self.ogu(username, self.generate())
        except Exception as error:
            self.utils.logs(f"{error}")

    def generate(self):
        try:
            return self.proxy_generator()
        except Exception as error:
            self.utils.logs(f"{error}")

    def proxy_generator(self):
        try:
            response = requests.get('https://api.getproxylist.com/proxy').json()
            proxy = response["protocol"] + "://" + response["ip"] + ":" + str(response["port"])
            return proxy
        except Exception as error:
            self.utils.logs(f"{error}")

    def github(self, username, proxy):
        try:
            response = requests.get(f"https://github.com/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="github", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def facebook(self, username, proxy):
        try:
            response = requests.get(f"https://www.facebook.com/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="facebook", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def linkedin(self, username, proxy):
        try:
            response = requests.get(f"https://www.linkedin.com/in/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="linkedin", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def replit(self, username, proxy):
        try:
            response = requests.get(f"https://repl.it/@{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="replit", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def paypal(self, username, proxy):
        try:
            response = requests.get(f"https://paypal.me/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="paypal", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def youtube(self, username, proxy):
        try:
            response = requests.get(f"https://www.youtube.com/user/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="youtube", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def twitch(self, username, proxy):
        try:
            response = requests.get(f"https://www.twitch.tv/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="twitch", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")
    
    def instagram(self, username, proxy):
        try:
            response = requests.get(f"https://www.instagram.com/{username}/", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="instagram", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")
    
    def tiktok(self, username, proxy):
        try:
            response = requests.get(f"https://www.tiktok.com/@{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="tiktok", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def pornhub(self, username, proxy):
        try:
            response = requests.get(f"https://www.pornhub.com/users/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="pornhub", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def onlyfans(self, username, proxy):
        try:
            response = requests.get(f"https://onlyfans.com/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="onlyfans", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def feds(self, username, proxy):
        try:
            response = requests.get(f"https://feds.lol/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="feds", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def twitter(self, username, proxy):
        try:
            response = requests.get(f"https://twitter.com/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="twitter", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def reddit(self, username, proxy):
        try:
            response = requests.get(f"https://www.reddit.com/user/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="reddit", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def steam(self, username, proxy):
        try:
            response = requests.get(f"https://steamcommunity.com/id/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="steam", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def discord(self, username, proxy):
        try:
            response = requests.get(f"https://discord.com/users/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="discord", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def ogu(self, username, proxy):
        try:
            response = requests.get(f"https://ogu.gg/{username}", proxies={"https": proxy}, timeout=10)
            if response.status_code == 200:
                self.utils.logs(f"[{response.status_code}] Found! Saving it on a file and trying another social media...")
                self.save(social_media="ogu", username=username)
            else:
                self.utils.logs(f"[{response.status_code}] Not found! Trying another social media...")
        except Exception as error:
            self.utils.logs(f"{error}")

    def save(self, social_media, username):
        try:
            file = open("found_usernames.txt", "a")
            file.write(f"{social_media}:{username}\n")
            file.close()
        except:
            self.utils.logs(f"{error}")
