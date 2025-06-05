import os
import requests
from logging import getLogger
logger = getLogger(__name__)

HF_URL = os.getenv("HF_URL", "https://huggingface.co")

def token_information(token):
    if token.startswith("hf_oauth"):
        _api_url = HF_URL + "/oauth/userinfo"
    else:
        _api_url = HF_URL + "/api/whoami-v2"
    headers = {}
    cookies = {}
    if token.startswith("hf_"):
        headers["Authorization"] = f"Bearer {token}"
    else:
        cookies = {"token": token}
    try:
        response = requests.get(
            _api_url,
            headers=headers,
            cookies=cookies,
            timeout=3,
        )
    except (requests.Timeout, ConnectionError) as err:
        logger.error(f"Failed to request whoami-v2 - {repr(err)}")
        raise Exception("Hugging Face Hub is unreachable, please try again later.")

    if response.status_code != 200:
        logger.error(f"Failed to request whoami-v2 - {response.status_code}")
        raise Exception("Invalid token.")

    resp = response.json()
    user_info = {}

    if token.startswith("hf_oauth"):
        user_info["id"] = resp["sub"]
        user_info["name"] = resp["preferred_username"]
        user_info["orgs"] = [resp["orgs"][k]["preferred_username"] for k in range(len(resp["orgs"]))]
    else:
        user_info["id"] = resp["id"]
        user_info["name"] = resp["name"]
        user_info["orgs"] = [resp["orgs"][k]["name"] for k in range(len(resp["orgs"]))]
    return user_info



if __name__ == "__main__":
    token = open("/home/kirill.trapeznikov/.cache/huggingface/token").read().strip()
    user_info = token_information(token)
    print(user_info)