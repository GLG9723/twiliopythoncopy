"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.api.v2010.sip.credential_lists import CredentialListList
from twilio.rest.api.v2010.sip.domains import DomainList
from twilio.rest.api.v2010.sip.ip_access_control_lists import IpAccessControlListList


class SipList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the SipList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read.
        
        :returns: twilio.rest.api.v2010.account.sip.SipList
        :rtype: twilio.rest.api.v2010.account.sip.SipList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/SIP.json'.format(**self._solution)
        
        self._credential_lists = None
        self._domains = None
        self._ip_access_control_lists = None
        

    @property
    def credential_lists(self):
        """
        Access the credential_lists

        :returns: twilio.rest.api.v2010.account.sip.CredentialListList
        :rtype: twilio.rest.api.v2010.account.sip.CredentialListList
        """
        if self._credential_lists is None:
            self._credential_lists = CredentialListList(self._version, account_sid=self._solution['account_sid'])
        return self.credential_lists

    @property
    def domains(self):
        """
        Access the domains

        :returns: twilio.rest.api.v2010.account.sip.DomainList
        :rtype: twilio.rest.api.v2010.account.sip.DomainList
        """
        if self._domains is None:
            self._domains = DomainList(self._version, account_sid=self._solution['account_sid'])
        return self.domains

    @property
    def ip_access_control_lists(self):
        """
        Access the ip_access_control_lists

        :returns: twilio.rest.api.v2010.account.sip.IpAccessControlListList
        :rtype: twilio.rest.api.v2010.account.sip.IpAccessControlListList
        """
        if self._ip_access_control_lists is None:
            self._ip_access_control_lists = IpAccessControlListList(self._version, account_sid=self._solution['account_sid'])
        return self.ip_access_control_lists


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SipList>'




