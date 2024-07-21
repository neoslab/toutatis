""" coding: utf-8 """

# Import libraries
from json import dumps, decoder
from phonenumbers.phonenumberutil import region_code_for_country_code
from urllib.parse import quote_plus
import argparse
import phonenumbers
import pycountry
import requests


# @name: getuserid()
# @description: Get Instagram user ID
# @return: string
def getuserid(username, sessid):
    """ Get Instagram user ID """
    headers = {"User-Agent": "iphone_ua", "x-ig-app-id": "936619743392459"}
    api = requests.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}',
                       headers=headers,
                       cookies={'sessionid': sessid})
    try:
        if api.status_code == 404:
            return {"id": None, "error": "User not found"}
        uid = api.json()["data"]['user']['id']
        return {"id": uid, "error": None}
    except decoder.JSONDecodeError:
        return {"id": None, "error": "Rate limit"}


# @name: getinfo()
# @description: Get Instagram user information
# @return: string
def getinfo(username, sessid):
    """ Get Instagram user information """
    userid = getuserid(username, sessid)
    if userid["error"]:
        return userid

    response = requests.get(f'https://i.instagram.com/api/v1/users/{userid["id"]}/info/',
                            headers={'User-Agent': 'Instagram 64.0.0.14.96'},
                            cookies={'sessionid': sessid}).json()["user"]
    userinfo = {"userID": userid["id"]}
    userinfo.update(response)  # Add the user info to the userinfo dictionary
    return {"user": userinfo, "error": None}


# @name: advlookup()
# @description: Advanced information lookup
# @return: array
def advlookup(username):
    """ Advanced information lookup """
    data = "signed_body=SIGNATURE." + quote_plus(dumps({"q": username, "skip_recovery": "1"}, separators=(",", ":")))
    api = requests.post('https://i.instagram.com/api/v1/users/lookup/', headers={
        "Accept-Language": "en-US",
        "User-Agent": "Instagram 101.0.0.15.120",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-IG-App-ID": "124024574287414",
        "Accept-Encoding": "gzip, deflate",
        "Host": "i.instagram.com",
        "Connection": "keep-alive",
        "Content-Length": str(len(data))
    }, data=data)
    try:
        return {"user": api.json(), "error": None}
    except decoder.JSONDecodeError:
        return {"user": None, "error": "rate limit"}


# @name: main()
# @description: Parse user request and proceed
# @return: array
def main():
    """ Parse user request and proceed """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sessionid', help="Instagram session ID", required=True)
    parser.add_argument('-u', '--username', help="One username", required=True)
    args = parser.parse_args()
    sessid = args.sessionid
    infos = getinfo(args.username, sessid)

    if "user" in infos:
        userinfo = infos["user"]
        print("-" * 72)
        if isinstance(userinfo, dict):
            print("-" * 72)
            print("[+] Username                    : {}".format(userinfo.get("username", "N/D")))
            print("[+] UserID                      : {}".format(userinfo.get("userID", "N/D")))
            print("[+] Full Name                   : {}".format(userinfo.get("full_name", "N/D")))
            print("[+] Verified                    : {}".format(userinfo.get("is_verified", "N/D")))
            print("[+] Business                    : {}".format(userinfo.get("is_business", "N/D")))
            print("[+] Private                     : {}".format(userinfo.get("is_private", "N/D")))
            print("[+] Category                    : {}".format(userinfo.get("category", "N/D")))
            print("[+] Daily Limit                 : {}".format(userinfo.get("daily_time_limit", "N/D")))
            print("[+] API Enabled                 : {}".format(userinfo.get("is_api_user", "N/D")))
            print("-" * 72)
            print("[+] Followers                   : {}".format(userinfo.get("follower_count", "N/D")))
            print("[+] Following                   : {}".format(userinfo.get("following_count", "N/D")))
            print("[+] Posts                       : {}".format(userinfo.get("media_count", "N/D")))
            print("[+] Fan Club ID                 : {}".format(userinfo.get("fan_club_id", "N/D")))
            print("[+] Fan Club Name               : {}".format(userinfo.get("fan_club_name", "N/D")))
            print("-" * 72)
            print("[+] External URL                : {}".format(userinfo.get("external_url", "N/D")))
            print("[+] IGTV Posts                  : {}".format(userinfo.get("total_igtv_videos", "N/D")))
            print("[+] WhatsApp                    : {}".format(userinfo.get("is_whatsapp_linked", "N/D")))
            print("[+] Memorial                    : {}".format(userinfo.get("is_memorialized", "N/D")))
            print("[+] New IG User                 : {}".format(userinfo.get("is_new_to_instagram", "N/D")))
            print("[+] User (< 30 days)            : {}".format(userinfo.get("is_new_to_instagram_30d", "N/D")))
            print("[+] Canada Based                : {}".format(userinfo.get("is_in_canada", "N/D")))
            print("[+] Parent Control              : {}".format(userinfo.get("is_parenting_account", "N/D")))
            print("[+] Quiet Mode                  : {}".format(userinfo.get("is_quiet_mode_enabled", "N/D")))
            print("[+] Secondary Account           : {}".format(userinfo.get("is_secondary_account_creation", "N/D")))
            print("[+] Biography                   : {}".format(userinfo.get("biography", "N/D")))
            print("-" * 72)
            print("[+] Anonymous Profile           : {}".format(userinfo.get("has_anonymous_profile_picture", "N/D")))
            print("[+] Guide                       : {}".format(userinfo.get("has_guides", "N/D")))
            print("[+] Highlight Reels             : {}".format(userinfo.get("has_highlight_reels", "N/D")))
            print("[+] IG Profile                  : {}".format(userinfo.get("has_ig_profile", "N/D")))
            print("[+] Music Profile               : {}".format(userinfo.get("has_music_on_profile", "N/D")))
            print("[+] Placed Orders               : {}".format(userinfo.get("has_placed_orders", "N/D")))
            print("[+] Private Collections         : {}".format(userinfo.get("has_private_collections", "N/D")))
            print("[+] Saved Items                 : {}".format(userinfo.get("has_saved_items", "N/D")))
            print("[+] Video Features              : {}".format(userinfo.get("has_videos", "N/D")))
            print("[+] Creator Agent               : {}".format(userinfo.get("is_creator_agent_enabled", "N/D")))
            print("-" * 72)
            print("[+] Hiding Comment              : {}".format(userinfo.get("is_hide_more_comment_enabled", "N/D")))
            print("[+] Hiding Stories              : {}".format(userinfo.get("is_hiding_stories_from_someone", "N/D")))
            print("-" * 72)
            if "linked_fb_info" in userinfo:
                fbuser = userinfo["linked_fb_info"].get("linked_fb_user", {})
                print("[+] FB User ID                  : {}".format(fbuser.get("ID", "N/D")))
                print("[+] FB Name                     : {}".format(fbuser.get("name", "N/D")))
                print("[+] FB Registration             : {}".format(fbuser.get("fb_account_creation_time", "N/D")))
                print("-" * 72)
            if "public_email" in userinfo:
                if userinfo["public_email"]:
                    print("[+] Public Email                : {}".format(userinfo.get("public_email", "N/D")))
                    print("-" * 72)
            if "public_phone_number" in userinfo:
                if str(userinfo["public_phone_number"]):
                    phonenr = "+" + str(userinfo["public_phone_country_code"]) + str(userinfo["public_phone_number"])
                    try:
                        pn = phonenumbers.parse(phonenr)
                        nbrcode = region_code_for_country_code(pn.country_code)
                        country = pycountry.countries.get(alpha_2=nbrcode)
                        phonenr = phonenr + " ({}) ".format(country.name)
                    except ImportError:
                        pass
                    print("[+] Public Phone                : {}".format(phonenr))
                    print("-" * 72)

            other_infos = advlookup(args.username)
            if other_infos["error"] == "rate limit":
                print("[x] Rate limit please wait a few minutes before you try again")
            elif "message" in other_infos["user"].keys():
                if other_infos["user"]["message"] == "No users found":
                    print("[x] The lookup did not work on this account")
                else:
                    print(other_infos["user"]["message"])
            else:
                if "obfuscated_email" in other_infos["user"].keys():
                    if other_infos["user"]["obfuscated_email"]:
                        print("[+] Obfuscated Email            : {}".format(other_infos["user"]["obfuscated_email"]))
                        print("-" * 72)
                    else:
                        print("[+] No obfuscated email found")
                if "obfuscated_phone" in other_infos["user"].keys():
                    if str(other_infos["user"]["obfuscated_phone"]):
                        print("[+] Obfuscated Phone            : {}".format(other_infos["user"]["obfuscated_phone"]))
                        print("-" * 72)
                    else:
                        print("[+] No obfuscated phone found")
            if "profile_pic_url" in userinfo:
                print("[+] Profile Picture URL         : {}".format(userinfo.get("profile_pic_url", "N/D")))
                print("-" * 72)
    else:
        print("[x] This username is not found")


# Callback
if __name__ == '__main__':
    main()
