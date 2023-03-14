r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Accounts
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""




from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.accounts.v1.credential.aws import AwsList
from twilio.rest.accounts.v1.credential.public_key import PublicKeyList


class CredentialList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CredentialList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.accounts.v1.credential.CredentialList
        :rtype: twilio.rest.accounts.v1.credential.CredentialList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Credentials".format(**self._solution)

        self._aws = None
        self._public_key = None

    @property
    def aws(self):
        """
        Access the aws

        :returns: twilio.rest.accounts.v1.credential.AwsList
        :rtype: twilio.rest.accounts.v1.credential.AwsList
        """
        if self._aws is None:
            self._aws = AwsList(self._version)
        return self._aws

    @property
    def public_key(self):
        """
        Access the public_key

        :returns: twilio.rest.accounts.v1.credential.PublicKeyList
        :rtype: twilio.rest.accounts.v1.credential.PublicKeyList
        """
        if self._public_key is None:
            self._public_key = PublicKeyList(self._version)
        return self._public_key

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Accounts.V1.CredentialList>"
