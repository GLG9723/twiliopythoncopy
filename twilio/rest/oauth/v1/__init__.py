"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.oauth.v1.device_code import DeviceCodeList
from twilio.rest.oauth.v1.oauth import OauthList
from twilio.rest.oauth.v1.openid_discovery import OpenidDiscoveryList
from twilio.rest.oauth.v1.token import TokenList
from twilio.rest.oauth.v1.user_info import UserInfoList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of oauth

        :param domain: The Twilio.oauth domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._device_code = None
        self._oauth = None
        self._openid_discovery = None
        self._token = None
        self._user_info = None
        
    @property
    def device_code(self) -> DeviceCodeList:
        if self._device_code is None:
            self._device_code = DeviceCodeList(self)
        return self._device_code

    @property
    def oauth(self) -> OauthList:
        if self._oauth is None:
            self._oauth = OauthList(self)
        return self._oauth

    @property
    def openid_discovery(self) -> OpenidDiscoveryList:
        if self._openid_discovery is None:
            self._openid_discovery = OpenidDiscoveryList(self)
        return self._openid_discovery

    @property
    def token(self) -> TokenList:
        if self._token is None:
            self._token = TokenList(self)
        return self._token

    @property
    def user_info(self) -> UserInfoList:
        if self._user_info is None:
            self._user_info = UserInfoList(self)
        return self._user_info

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth.V1>'
