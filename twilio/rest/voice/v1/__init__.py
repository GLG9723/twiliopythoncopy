"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.voice.v1.archived_call import ArchivedCallList
from twilio.rest.voice.v1.byoc_trunk import ByocTrunkList
from twilio.rest.voice.v1.connection_policy import ConnectionPolicyList
from twilio.rest.voice.v1.dialing_permissions import DialingPermissionsList
from twilio.rest.voice.v1.ip_record import IpRecordList
from twilio.rest.voice.v1.source_ip_mapping import SourceIpMappingList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Voice

        :param domain: The Twilio.voice domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._archived_calls = None
        self._byoc_trunks = None
        self._connection_policies = None
        self._dialing_permissions = None
        self._ip_records = None
        self._source_ip_mappings = None
        
    @property
    def archived_calls(self) -> ArchivedCallList:
        """
        :rtype: twilio.rest.voice.v1.archived_call.ArchivedCallList
        """
        if self._archived_calls is None:
            self._archived_calls = ArchivedCallList(self)
        return self._archived_calls

    @property
    def byoc_trunks(self) -> ByocTrunkList:
        """
        :rtype: twilio.rest.voice.v1.byoc_trunk.ByocTrunkList
        """
        if self._byoc_trunks is None:
            self._byoc_trunks = ByocTrunkList(self)
        return self._byoc_trunks

    @property
    def connection_policies(self) -> ConnectionPolicyList:
        """
        :rtype: twilio.rest.voice.v1.connection_policy.ConnectionPolicyList
        """
        if self._connection_policies is None:
            self._connection_policies = ConnectionPolicyList(self)
        return self._connection_policies

    @property
    def dialing_permissions(self) -> DialingPermissionsList:
        """
        :rtype: twilio.rest.voice.v1.dialing_permissions.DialingPermissionsList
        """
        if self._dialing_permissions is None:
            self._dialing_permissions = DialingPermissionsList(self)
        return self._dialing_permissions

    @property
    def ip_records(self) -> IpRecordList:
        """
        :rtype: twilio.rest.voice.v1.ip_record.IpRecordList
        """
        if self._ip_records is None:
            self._ip_records = IpRecordList(self)
        return self._ip_records

    @property
    def source_ip_mappings(self) -> SourceIpMappingList:
        """
        :rtype: twilio.rest.voice.v1.source_ip_mapping.SourceIpMappingList
        """
        if self._source_ip_mappings is None:
            self._source_ip_mappings = SourceIpMappingList(self)
        return self._source_ip_mappings

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1>'
