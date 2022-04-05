from datetime import timedelta

from django.conf import settings
from django.utils import timezone

import jwt
import requests

SOCIAL_AUTH_APPLE_KEY_ID = settings.SOCIAL_AUTH_APPLE_KEY_ID
SOCIAL_AUTH_APPLE_TEAM_ID = settings.SOCIAL_AUTH_APPLE_TEAM_ID
CLIENT_ID = settings.APPLE_CLIENT_ID
SOCIAL_AUTH_APPLE_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgNDK7DALElrrA+pAg
2Pu/G5mfxslQaZhrG6LtN+3w4a2gCgYIKoZIzj0DAQehRANCAATU1gCxrWnvd41T
TvttuEzDs9XI9wRFOFGwNp/TJMi/1fYfnmy/YMlSllGrIDFTzXWwqaBWcjwOaM1b
wBKv1IVw
-----END PRIVATE KEY-----"""


class Apple:
    """apple authentication backend"""

    def __init__(self, is_mobile=False):
        self.client_id = f"{CLIENT_ID}" if is_mobile is False else f"{CLIENT_ID}.com"

    ACCESS_TOKEN_URL = "https://appleid.apple.com/auth/token"

    def do_auth(self, access_token):
        """
        Finish the auth process once the access_token was retrieved
        Get the email from ID token received from apple
        """
        client_id, client_secret = self.get_key_and_secret()
        headers = {"content-type": "application/x-www-form-urlencoded"}
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": access_token,
            "grant_type": "authorization_code",
        }
        res = requests.post(self.ACCESS_TOKEN_URL, data=data, headers=headers)
        id_token = res.json().get("id_token", None)
        if id_token:
            decoded = jwt.decode(
                id_token, "", options={"verify_signature": False}
            )
            email = decoded.get("email")
            if email:
                data = dict(
                    email=email, username=email.split("@")[0]
                )
                return data
        return None

    def get_key_and_secret(self):
        headers = {"kid": SOCIAL_AUTH_APPLE_KEY_ID, "alg": "ES256"}
        iat =  timezone.now()
        exp = iat + timedelta(days=180)
        payload = {
            "iss": SOCIAL_AUTH_APPLE_TEAM_ID,
            "iat": int(iat.timestamp()),
            "exp": int(exp.timestamp()),
            "aud": "https://appleid.apple.com",
            "sub": self.client_id,
        }

        client_secret = jwt.encode(
            payload,
            SOCIAL_AUTH_APPLE_PRIVATE_KEY,
            algorithm="ES256",
            headers=headers,
        )

        return self.client_id, client_secret