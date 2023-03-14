r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.ip_messaging.v2.credential import CredentialList
from twilio.rest.ip_messaging.v2.service import ServiceList


class V2(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V2 version of IpMessaging

        :param domain: The Twilio.ip_messaging domain
        """
        super().__init__(domain)
        self.version = "v2"
        self._credentials = None
        self._services = None

    @property
    def credentials(self) -> CredentialList:
        """
        :rtype: twilio.rest.ip_messaging.v2.credential.CredentialList
        """
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    @property
    def services(self) -> ServiceList:
        """
        :rtype: twilio.rest.ip_messaging.v2.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.IpMessaging.V2>"
