r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class AnonymizeInstance(InstanceResource):
    class Status(object):
        CONNECTED = "connected"
        DISCONNECTED = "disconnected"

    """
    :ivar sid: The unique string that we created to identify the RoomParticipant resource.
    :ivar room_sid: The SID of the participant's room.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RoomParticipant resource.
    :ivar status: 
    :ivar identity: The SID of the participant.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar start_time: The time of participant connected to the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    :ivar end_time: The time when the participant disconnected from the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    :ivar duration: The duration in seconds that the participant was `connected`. Populated only after the participant is `disconnected`.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], room_sid: str, sid: str
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.room_sid: Optional[str] = payload.get("room_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.status: Optional["AnonymizeInstance.Status"] = payload.get("status")
        self.identity: Optional[str] = payload.get("identity")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.start_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("start_time")
        )
        self.end_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("end_time")
        )
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "room_sid": room_sid,
            "sid": sid,
        }
        self._context: Optional[AnonymizeContext] = None

    @property
    def _proxy(self) -> "AnonymizeContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AnonymizeContext for this AnonymizeInstance
        """
        if self._context is None:
            self._context = AnonymizeContext(
                self._version,
                room_sid=self._solution["room_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def update(self) -> "AnonymizeInstance":
        """
        Update the AnonymizeInstance


        :returns: The updated AnonymizeInstance
        """
        return self._proxy.update()

    async def update_async(self) -> "AnonymizeInstance":
        """
        Asynchronous coroutine to update the AnonymizeInstance


        :returns: The updated AnonymizeInstance
        """
        return await self._proxy.update_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.AnonymizeInstance {}>".format(context)


class AnonymizeContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, sid: str):
        """
        Initialize the AnonymizeContext

        :param version: Version that contains the resource
        :param room_sid: The SID of the room with the participant to update.
        :param sid: The SID of the RoomParticipant resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "sid": sid,
        }
        self._uri = "/Rooms/{room_sid}/Participants/{sid}/Anonymize".format(
            **self._solution
        )

    def update(self) -> AnonymizeInstance:
        """
        Update the AnonymizeInstance


        :returns: The updated AnonymizeInstance
        """
        data = values.of({})

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AnonymizeInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self) -> AnonymizeInstance:
        """
        Asynchronous coroutine to update the AnonymizeInstance


        :returns: The updated AnonymizeInstance
        """
        data = values.of({})

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AnonymizeInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.AnonymizeContext {}>".format(context)


class AnonymizeList(ListResource):
    def __init__(self, version: Version, room_sid: str, sid: str):
        """
        Initialize the AnonymizeList

        :param version: Version that contains the resource
        :param room_sid: The SID of the room with the participant to update.
        :param sid: The SID of the RoomParticipant resource to update.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "sid": sid,
        }

    def get(self) -> AnonymizeContext:
        """
        Constructs a AnonymizeContext

        """
        return AnonymizeContext(
            self._version,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    def __call__(self) -> AnonymizeContext:
        """
        Constructs a AnonymizeContext

        """
        return AnonymizeContext(
            self._version,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.AnonymizeList>"
