r"""
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




from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping import (
    AuthCallsCredentialListMappingList,
)
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_ip_access_control_list_mapping import (
    AuthCallsIpAccessControlListMappingList,
)


class AuthTypeCallsList(ListResource):
    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the AuthTypeCallsList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
        :param domain_sid: The SID of the SIP domain that contains the resource to fetch.

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.AuthTypeCallsList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.AuthTypeCallsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls.json".format(
                **self._solution
            )
        )

        self._credential_list_mappings = None
        self._ip_access_control_list_mappings = None

    @property
    def credential_list_mappings(self):
        """
        Access the credential_list_mappings

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.AuthCallsCredentialListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.AuthCallsCredentialListMappingList
        """
        if self._credential_list_mappings is None:
            self._credential_list_mappings = AuthCallsCredentialListMappingList(
                self._version,
                account_sid=self._solution["account_sid"],
                domain_sid=self._solution["domain_sid"],
            )
        return self._credential_list_mappings

    @property
    def ip_access_control_list_mappings(self):
        """
        Access the ip_access_control_list_mappings

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.AuthCallsIpAccessControlListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.AuthCallsIpAccessControlListMappingList
        """
        if self._ip_access_control_list_mappings is None:
            self._ip_access_control_list_mappings = (
                AuthCallsIpAccessControlListMappingList(
                    self._version,
                    account_sid=self._solution["account_sid"],
                    domain_sid=self._solution["domain_sid"],
                )
            )
        return self._ip_access_control_list_mappings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.AuthTypeCallsList>"
