import utils.proxy_rotation
import utils.utils
import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM
import time
from utils.proxy_generation import ProxyGeneration

class UsernameChecker:
    def __init__(self, username, social_media_list):
        self.username = username
        self.social_media_list = social_media_list
        self.proxy_rotation = utils.proxy_rotation.ProxyRotation()
        self.proxy_generation = ProxyGeneration()
        self.utils = utils.utils.Utils()

    def start(self):
        for social_media in self.social_media_list:
            self.utils.logs(f"[...] Finding {self.username} on {social_media}...")
            if social_media == "roblox":
                try:
                    roblox_id = self.roblox()
                    if roblox_id != None:
                        self.save(social_media, roblox_id)
                except Exception as error:
                    self.utils.logs(f"{error}")
            else:
                try:
                    self.proxy_rotation.rotate(social_media, self.username)
                except Exception as error:
                    self.utils.logs(f"{error}")

    def roblox(self):
        try:
            response = self.proxy_generation.generate("https://api.roblox.com/users/get-by-username?username=" + self.username, "roblox")
            roblox_id = response.json()["Id"]
            self.utils.logs(f"[{roblox_id}] Found! Saving it on a file and trying another social media...")
            return roblox_id
        except KeyError:
            self.utils.logs("[404] Not found! Trying another social media...")
            return None

    def save(self, social_media, roblox_id):
        file = open("found_usernames.txt", "a")
        file.write(f"{social_media}:{self.username}:{roblox_id}\n")
        file.close()