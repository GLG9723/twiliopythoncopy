r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ProvisioningStatusInstance(InstanceResource):

    class Status:
        ACTIVE = "active"
        IN_PROGRESS = "in-progress"
        NOT_CONFIGURED = "not-configured"
        FAILED = "failed"

    """
    :ivar status: 
    :ivar url: The absolute URL of the resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.status: Optional["ProvisioningStatusInstance.Status"] = payload.get(
            "status"
        )
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[ProvisioningStatusContext] = None

    @property
    def _proxy(self) -> "ProvisioningStatusContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ProvisioningStatusContext for this ProvisioningStatusInstance
        """
        if self._context is None:
            self._context = ProvisioningStatusContext(
                self._version,
            )
        return self._context

    def fetch(self) -> "ProvisioningStatusInstance":
        """
        Fetch the ProvisioningStatusInstance


        :returns: The fetched ProvisioningStatusInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ProvisioningStatusInstance":
        """
        Asynchronous coroutine to fetch the ProvisioningStatusInstance


        :returns: The fetched ProvisioningStatusInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.ProvisioningStatusInstance>"


class ProvisioningStatusContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the ProvisioningStatusContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/account/provision/status"

    def fetch(self) -> ProvisioningStatusInstance:
        """
        Fetch the ProvisioningStatusInstance


        :returns: The fetched ProvisioningStatusInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ProvisioningStatusInstance(
            self._version,
            payload,
        )

    async def fetch_async(self) -> ProvisioningStatusInstance:
        """
        Asynchronous coroutine to fetch the ProvisioningStatusInstance


        :returns: The fetched ProvisioningStatusInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ProvisioningStatusInstance(
            self._version,
            payload,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.ProvisioningStatusContext>"


class ProvisioningStatusList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ProvisioningStatusList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> ProvisioningStatusContext:
        """
        Constructs a ProvisioningStatusContext

        """
        return ProvisioningStatusContext(self._version)

    def __call__(self) -> ProvisioningStatusContext:
        """
        Constructs a ProvisioningStatusContext

        """
        return ProvisioningStatusContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.ProvisioningStatusList>"
