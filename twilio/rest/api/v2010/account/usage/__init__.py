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

from typing import Optional


from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.api.v2010.account.usage.record import RecordList
from twilio.rest.api.v2010.account.usage.trigger import TriggerList


class UsageList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the UsageList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Usage.json".format(**self._solution)

        self._records: Optional[RecordList] = None
        self._triggers: Optional[TriggerList] = None

    @property
    def records(self) -> RecordList:
        """
        Access the records
        """
        if self._records is None:
            self._records = RecordList(
                self._version, account_sid=self._solution["account_sid"]
            )
        return self._records

    @property
    def triggers(self) -> TriggerList:
        """
        Access the triggers
        """
        if self._triggers is None:
            self._triggers = TriggerList(
                self._version, account_sid=self._solution["account_sid"]
            )
        return self._triggers

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.UsageList>"
