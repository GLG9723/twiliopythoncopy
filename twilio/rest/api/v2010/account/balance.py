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

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class BalanceInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        """
        Initialize the BalanceInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._balance: Optional[str] = payload.get("balance")
        self._currency: Optional[str] = payload.get("currency")

        self._solution = {
            "account_sid": account_sid,
        }

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The unique SID identifier of the Account.
        """
        return self._account_sid

    @property
    def balance(self) -> Optional[str]:
        """
        :returns: The balance of the Account, in units specified by the unit parameter. Balance changes may not be reflected immediately. Child accounts do not contain balance information
        """
        return self._balance

    @property
    def currency(self) -> Optional[str]:
        """
        :returns: The units of currency for the account balance
        """
        return self._currency

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.BalanceInstance {}>".format(context)


class BalanceList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the BalanceList

        :param version: Version that contains the resource
        :param account_sid: The unique SID identifier of the Account.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Balance.json".format(**self._solution)

    def fetch(self) -> BalanceInstance:
        """
        Asynchronously fetch the BalanceInstance

        :returns: The fetched BalanceInstance
        """
        payload = self._version.fetch(method="GET", uri=self._uri)

        return BalanceInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def fetch_async(self) -> BalanceInstance:
        """
        Asynchronously fetch the BalanceInstance

        :returns: The fetched BalanceInstance
        """
        payload = await self._version.fetch_async(method="GET", uri=self._uri)

        return BalanceInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.BalanceList>"
