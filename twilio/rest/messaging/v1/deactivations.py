r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class DeactivationsInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the DeactivationsInstance

        :returns: twilio.rest.messaging.v1.deactivations.DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsInstance
        """
        super().__init__(version)

        self._properties = {
            "redirect_to": payload.get("redirect_to"),
        }

        self._solution = {}
        self._context: Optional[DeactivationsContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeactivationsContext for this DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsContext
        """
        if self._context is None:
            self._context = DeactivationsContext(
                self._version,
            )
        return self._context

    @property
    def redirect_to(self):
        """
        :returns: Returns an authenticated url that redirects to a file containing the deactivated numbers for the requested day. This url is valid for up to two minutes.
        :rtype: str
        """
        return self._properties["redirect_to"]

    def fetch(self, date=values.unset):
        """
        Fetch the DeactivationsInstance

        :param date date: The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.

        :returns: The fetched DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsInstance
        """
        return self._proxy.fetch(
            date=date,
        )

    async def fetch_async(self, date=values.unset):
        """
        Asynchronous coroutine to fetch the DeactivationsInstance

        :param date date: The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.

        :returns: The fetched DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsInstance
        """
        return await self._proxy.fetch_async(
            date=date,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.DeactivationsInstance {}>".format(context)


class DeactivationsContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the DeactivationsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.deactivations.DeactivationsContext
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsContext
        """
        super().__init__(version)

        self._uri = "/Deactivations"

    def fetch(self, date=values.unset):
        """
        Fetch the DeactivationsInstance

        :param date date: The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.

        :returns: The fetched DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsInstance
        """

        data = values.of(
            {
                "Date": serialize.iso8601_date(date),
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return DeactivationsInstance(
            self._version,
            payload,
        )

    async def fetch_async(self, date=values.unset):
        """
        Asynchronous coroutine to fetch the DeactivationsInstance

        :param date date: The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.

        :returns: The fetched DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsInstance
        """

        data = values.of(
            {
                "Date": serialize.iso8601_date(date),
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return DeactivationsInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """

        return "<Twilio.Messaging.V1.DeactivationsContext>"


class DeactivationsList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the DeactivationsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.deactivations.DeactivationsList
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsList
        """
        super().__init__(version)

    def get(self):
        """
        Constructs a DeactivationsContext


        :returns: twilio.rest.messaging.v1.deactivations.DeactivationsContext
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsContext
        """
        return DeactivationsContext(self._version)

    def __call__(self):
        """
        Constructs a DeactivationsContext


        :returns: twilio.rest.messaging.v1.deactivations.DeactivationsContext
        :rtype: twilio.rest.messaging.v1.deactivations.DeactivationsContext
        """
        return DeactivationsContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Messaging.V1.DeactivationsList>"
