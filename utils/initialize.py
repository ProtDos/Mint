from utils.username_checker import UsernameChecker
from utils.utils import Utils

class Initialize:
    def __init__(self, username):
        self.social_media_list = ["github", "roblox", "facebook", "linkedin", "replit", "paypal", "youtube", "twitch", "tiktok", "instagram", "pornhub", "onlyfans", "twitter", "steam", "reddit", "feds", "discord"]
        self.username = username
        self.keyword_list = ["404", "500", "Found", "Not found", "ip", "IP", "ipaddress", "IPADDRESS", "success", "Success"]
        self.username_checker = UsernameChecker(username, self.social_media_list)
        self.utils = Utils()
        self.utils.logs(f"{self.username} - {self.username_checker.social_media_list}")
        self.username_checker.start()

username = input("[*] Enter a username: ")
Initialize(username)