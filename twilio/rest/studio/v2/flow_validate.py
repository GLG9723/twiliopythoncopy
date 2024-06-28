r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class FlowValidateInstance(InstanceResource):

    class Status:
        DRAFT = "draft"
        PUBLISHED = "published"

    """
    :ivar valid: Boolean if the flow definition is valid.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.valid: Optional[bool] = payload.get("valid")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Studio.V2.FlowValidateInstance>"


class FlowValidateList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the FlowValidateList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Flows/Validate"

    def update(
        self,
        friendly_name: str,
        status: "FlowValidateInstance.Status",
        definition: object,
        commit_message: Union[str, object] = values.unset,
    ) -> FlowValidateInstance:
        """
        Update the FlowValidateInstance

        :param friendly_name: The string that you assigned to describe the Flow.
        :param status:
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The created FlowValidateInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
                "Definition": serialize.object(definition),
                "CommitMessage": commit_message,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FlowValidateInstance(self._version, payload)

    async def update_async(
        self,
        friendly_name: str,
        status: "FlowValidateInstance.Status",
        definition: object,
        commit_message: Union[str, object] = values.unset,
    ) -> FlowValidateInstance:
        """
        Asynchronously update the FlowValidateInstance

        :param friendly_name: The string that you assigned to describe the Flow.
        :param status:
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The created FlowValidateInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
                "Definition": serialize.object(definition),
                "CommitMessage": commit_message,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FlowValidateInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V2.FlowValidateList>"
