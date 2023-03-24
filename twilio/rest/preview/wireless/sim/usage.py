r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class UsageInstance(InstanceResource):
    def __init__(self, version, payload, sim_sid: str):
        """
        Initialize the UsageInstance
        """
        super().__init__(version)

        self._properties = {
            "sim_sid": payload.get("sim_sid"),
            "sim_unique_name": payload.get("sim_unique_name"),
            "account_sid": payload.get("account_sid"),
            "period": payload.get("period"),
            "commands_usage": payload.get("commands_usage"),
            "commands_costs": payload.get("commands_costs"),
            "data_usage": payload.get("data_usage"),
            "data_costs": payload.get("data_costs"),
            "url": payload.get("url"),
        }

        self._solution = {
            "sim_sid": sim_sid,
        }
        self._context: Optional[UsageContext] = None

    @property
    def _proxy(self) -> "UsageContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UsageContext for this UsageInstance
        """
        if self._context is None:
            self._context = UsageContext(
                self._version,
                sim_sid=self._solution["sim_sid"],
            )
        return self._context

    @property
    def sim_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["sim_sid"]

    @property
    def sim_unique_name(self) -> str:
        """
        :returns:
        """
        return self._properties["sim_unique_name"]

    @property
    def account_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["account_sid"]

    @property
    def period(self) -> dict:
        """
        :returns:
        """
        return self._properties["period"]

    @property
    def commands_usage(self) -> dict:
        """
        :returns:
        """
        return self._properties["commands_usage"]

    @property
    def commands_costs(self) -> dict:
        """
        :returns:
        """
        return self._properties["commands_costs"]

    @property
    def data_usage(self) -> dict:
        """
        :returns:
        """
        return self._properties["data_usage"]

    @property
    def data_costs(self) -> dict:
        """
        :returns:
        """
        return self._properties["data_costs"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    def fetch(self, end=values.unset, start=values.unset) -> "UsageInstance":
        """
        Fetch the UsageInstance

        :param str end:
        :param str start:

        :returns: The fetched UsageInstance
        """
        return self._proxy.fetch(
            end=end,
            start=start,
        )

    async def fetch_async(
        self, end=values.unset, start=values.unset
    ) -> "UsageInstance":
        """
        Asynchronous coroutine to fetch the UsageInstance

        :param str end:
        :param str start:

        :returns: The fetched UsageInstance
        """
        return await self._proxy.fetch_async(
            end=end,
            start=start,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Wireless.UsageInstance {}>".format(context)


class UsageContext(InstanceContext):
    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the UsageContext

        :param version: Version that contains the resource
        :param sim_sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sim_sid": sim_sid,
        }
        self._uri = "/Sims/{sim_sid}/Usage".format(**self._solution)

    def fetch(self, end=values.unset, start=values.unset) -> UsageInstance:
        """
        Fetch the UsageInstance

        :param str end:
        :param str start:

        :returns: The fetched UsageInstance
        """

        data = values.of(
            {
                "End": end,
                "Start": start,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return UsageInstance(
            self._version,
            payload,
            sim_sid=self._solution["sim_sid"],
        )

    async def fetch_async(self, end=values.unset, start=values.unset) -> UsageInstance:
        """
        Asynchronous coroutine to fetch the UsageInstance

        :param str end:
        :param str start:

        :returns: The fetched UsageInstance
        """

        data = values.of(
            {
                "End": end,
                "Start": start,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return UsageInstance(
            self._version,
            payload,
            sim_sid=self._solution["sim_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Wireless.UsageContext {}>".format(context)


class UsageList(ListResource):
    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the UsageList

        :param version: Version that contains the resource
        :param sim_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sim_sid": sim_sid,
        }

    def get(self) -> UsageContext:
        """
        Constructs a UsageContext

        """
        return UsageContext(self._version, sim_sid=self._solution["sim_sid"])

    def __call__(self) -> UsageContext:
        """
        Constructs a UsageContext

        """
        return UsageContext(self._version, sim_sid=self._solution["sim_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Wireless.UsageList>"
