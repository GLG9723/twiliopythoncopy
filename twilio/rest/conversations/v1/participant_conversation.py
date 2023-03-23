r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import List
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ParticipantConversationInstance(InstanceResource):
    class State(object):
        INACTIVE = "inactive"
        ACTIVE = "active"
        CLOSED = "closed"

    def __init__(self, version, payload):
        """
        Initialize the ParticipantConversationInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "chat_service_sid": payload.get("chat_service_sid"),
            "participant_sid": payload.get("participant_sid"),
            "participant_user_sid": payload.get("participant_user_sid"),
            "participant_identity": payload.get("participant_identity"),
            "participant_messaging_binding": payload.get(
                "participant_messaging_binding"
            ),
            "conversation_sid": payload.get("conversation_sid"),
            "conversation_unique_name": payload.get("conversation_unique_name"),
            "conversation_friendly_name": payload.get("conversation_friendly_name"),
            "conversation_attributes": payload.get("conversation_attributes"),
            "conversation_date_created": deserialize.iso8601_datetime(
                payload.get("conversation_date_created")
            ),
            "conversation_date_updated": deserialize.iso8601_datetime(
                payload.get("conversation_date_updated")
            ),
            "conversation_created_by": payload.get("conversation_created_by"),
            "conversation_state": payload.get("conversation_state"),
            "conversation_timers": payload.get("conversation_timers"),
            "links": payload.get("links"),
        }

        self._solution = {}

    @property
    def account_sid(self) -> str:
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation.
        """
        return self._properties["account_sid"]

    @property
    def chat_service_sid(self) -> str:
        """
        :returns: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
        """
        return self._properties["chat_service_sid"]

    @property
    def participant_sid(self) -> str:
        """
        :returns: The unique ID of the [Participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource).
        """
        return self._properties["participant_sid"]

    @property
    def participant_user_sid(self) -> str:
        """
        :returns: The unique string that identifies the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource).
        """
        return self._properties["participant_user_sid"]

    @property
    def participant_identity(self) -> str:
        """
        :returns: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        """
        return self._properties["participant_identity"]

    @property
    def participant_messaging_binding(self) -> dict:
        """
        :returns: Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of type and address fields of the participant.
        """
        return self._properties["participant_messaging_binding"]

    @property
    def conversation_sid(self) -> str:
        """
        :returns: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) this Participant belongs to.
        """
        return self._properties["conversation_sid"]

    @property
    def conversation_unique_name(self) -> str:
        """
        :returns: An application-defined string that uniquely identifies the Conversation resource.
        """
        return self._properties["conversation_unique_name"]

    @property
    def conversation_friendly_name(self) -> str:
        """
        :returns: The human-readable name of this conversation, limited to 256 characters. Optional.
        """
        return self._properties["conversation_friendly_name"]

    @property
    def conversation_attributes(self) -> str:
        """
        :returns: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
        """
        return self._properties["conversation_attributes"]

    @property
    def conversation_date_created(self) -> datetime:
        """
        :returns: The date that this conversation was created, given in ISO 8601 format.
        """
        return self._properties["conversation_date_created"]

    @property
    def conversation_date_updated(self) -> datetime:
        """
        :returns: The date that this conversation was last updated, given in ISO 8601 format.
        """
        return self._properties["conversation_date_updated"]

    @property
    def conversation_created_by(self) -> str:
        """
        :returns: Identity of the creator of this Conversation.
        """
        return self._properties["conversation_created_by"]

    @property
    def conversation_state(self) -> "ParticipantConversationInstance.State":
        """
        :returns:
        """
        return self._properties["conversation_state"]

    @property
    def conversation_timers(self) -> dict:
        """
        :returns: Timer date values representing state update for this conversation.
        """
        return self._properties["conversation_timers"]

    @property
    def links(self) -> dict:
        """
        :returns: Contains absolute URLs to access the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) and [conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) of this conversation.
        """
        return self._properties["links"]

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.ParticipantConversationInstance {}>".format(
            context
        )


class ParticipantConversationPage(Page):
    def get_instance(self, payload) -> ParticipantConversationInstance:
        """
        Build an instance of ParticipantConversationInstance

        :param dict payload: Payload response from the API
        """
        return ParticipantConversationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ParticipantConversationPage>"


class ParticipantConversationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ParticipantConversationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/ParticipantConversations"

    def stream(
        self, identity=values.unset, address=values.unset, limit=None, page_size=None
    ) -> List[ParticipantConversationInstance]:
        """
        Streams ParticipantConversationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            identity=identity, address=address, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, identity=values.unset, address=values.unset, limit=None, page_size=None
    ) -> List[ParticipantConversationInstance]:
        """
        Asynchronously streams ParticipantConversationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            identity=identity, address=address, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, identity=values.unset, address=values.unset, limit=None, page_size=None
    ) -> List[ParticipantConversationInstance]:
        """
        Lists ParticipantConversationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                identity=identity,
                address=address,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, identity=values.unset, address=values.unset, limit=None, page_size=None
    ) -> List[ParticipantConversationInstance]:
        """
        Asynchronously lists ParticipantConversationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                identity=identity,
                address=address,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        identity=values.unset,
        address=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> ParticipantConversationPage:
        """
        Retrieve a single page of ParticipantConversationInstance records from the API.
        Request is executed immediately

        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantConversationInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "Address": address,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ParticipantConversationPage(self._version, response)

    async def page_async(
        self,
        identity=values.unset,
        address=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> ParticipantConversationPage:
        """
        Asynchronously retrieve a single page of ParticipantConversationInstance records from the API.
        Request is executed immediately

        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantConversationInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "Address": address,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ParticipantConversationPage(self._version, response)

    def get_page(self, target_url) -> ParticipantConversationPage:
        """
        Retrieve a specific page of ParticipantConversationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantConversationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ParticipantConversationPage(self._version, response)

    async def get_page_async(self, target_url) -> ParticipantConversationPage:
        """
        Asynchronously retrieve a specific page of ParticipantConversationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantConversationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ParticipantConversationPage(self._version, response)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ParticipantConversationList>"
