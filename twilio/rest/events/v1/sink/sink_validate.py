r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SinkValidateInstance(InstanceResource):
    """
    :ivar result: Feedback indicating whether the given Sink was validated.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sid: str):
        super().__init__(version)

        self.result: Optional[str] = payload.get("result")

        self._solution = {
            "sid": sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Events.V1.SinkValidateInstance {context}>"


class SinkValidateList(ListResource):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SinkValidateList

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies the Sink being validated.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Sinks/{sid}/Validate".format(**self._solution)

    def create(self, test_id: str) -> SinkValidateInstance:
        """
        Create the SinkValidateInstance

        :param test_id: A 34 character string that uniquely identifies the test event for a Sink being validated.

        :returns: The created SinkValidateInstance
        """

        data = values.of(
            {
                "TestId": test_id,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SinkValidateInstance(self._version, payload, sid=self._solution["sid"])

    async def create_async(self, test_id: str) -> SinkValidateInstance:
        """
        Asynchronously create the SinkValidateInstance

        :param test_id: A 34 character string that uniquely identifies the test event for a Sink being validated.

        :returns: The created SinkValidateInstance
        """

        data = values.of(
            {
                "TestId": test_id,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SinkValidateInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Events.V1.SinkValidateList>"
