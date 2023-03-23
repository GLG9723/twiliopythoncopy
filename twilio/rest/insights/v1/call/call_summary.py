r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class CallSummaryInstance(InstanceResource):
    class AnsweredBy(object):
        UNKNOWN = "unknown"
        MACHINE_START = "machine_start"
        MACHINE_END_BEEP = "machine_end_beep"
        MACHINE_END_SILENCE = "machine_end_silence"
        MACHINE_END_OTHER = "machine_end_other"
        HUMAN = "human"
        FAX = "fax"

    class CallState(object):
        RINGING = "ringing"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        CANCELED = "canceled"
        ANSWERED = "answered"
        UNDIALED = "undialed"

    class CallType(object):
        CARRIER = "carrier"
        SIP = "sip"
        TRUNKING = "trunking"
        CLIENT = "client"

    class ProcessingState(object):
        COMPLETE = "complete"
        PARTIAL = "partial"

    def __init__(self, version, payload, call_sid: str):
        """
        Initialize the CallSummaryInstance

        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryInstance
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "call_sid": payload.get("call_sid"),
            "call_type": payload.get("call_type"),
            "call_state": payload.get("call_state"),
            "answered_by": payload.get("answered_by"),
            "processing_state": payload.get("processing_state"),
            "created_time": deserialize.iso8601_datetime(payload.get("created_time")),
            "start_time": deserialize.iso8601_datetime(payload.get("start_time")),
            "end_time": deserialize.iso8601_datetime(payload.get("end_time")),
            "duration": deserialize.integer(payload.get("duration")),
            "connect_duration": deserialize.integer(payload.get("connect_duration")),
            "_from": payload.get("from"),
            "to": payload.get("to"),
            "carrier_edge": payload.get("carrier_edge"),
            "client_edge": payload.get("client_edge"),
            "sdk_edge": payload.get("sdk_edge"),
            "sip_edge": payload.get("sip_edge"),
            "tags": payload.get("tags"),
            "url": payload.get("url"),
            "attributes": payload.get("attributes"),
            "properties": payload.get("properties"),
            "trust": payload.get("trust"),
            "annotation": payload.get("annotation"),
        }

        self._solution = {
            "call_sid": call_sid,
        }
        self._context: Optional[CallSummaryContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CallSummaryContext for this CallSummaryInstance
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        """
        if self._context is None:
            self._context = CallSummaryContext(
                self._version,
                call_sid=self._solution["call_sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def call_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["call_sid"]

    @property
    def call_type(self):
        """
        :returns:
        :rtype: CallSummaryInstance.CallType
        """
        return self._properties["call_type"]

    @property
    def call_state(self):
        """
        :returns:
        :rtype: CallSummaryInstance.CallState
        """
        return self._properties["call_state"]

    @property
    def answered_by(self):
        """
        :returns:
        :rtype: CallSummaryInstance.AnsweredBy
        """
        return self._properties["answered_by"]

    @property
    def processing_state(self):
        """
        :returns:
        :rtype: CallSummaryInstance.ProcessingState
        """
        return self._properties["processing_state"]

    @property
    def created_time(self):
        """
        :returns:
        :rtype: datetime
        """
        return self._properties["created_time"]

    @property
    def start_time(self):
        """
        :returns:
        :rtype: datetime
        """
        return self._properties["start_time"]

    @property
    def end_time(self):
        """
        :returns:
        :rtype: datetime
        """
        return self._properties["end_time"]

    @property
    def duration(self):
        """
        :returns:
        :rtype: int
        """
        return self._properties["duration"]

    @property
    def connect_duration(self):
        """
        :returns:
        :rtype: int
        """
        return self._properties["connect_duration"]

    @property
    def _from(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["_from"]

    @property
    def to(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["to"]

    @property
    def carrier_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["carrier_edge"]

    @property
    def client_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["client_edge"]

    @property
    def sdk_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["sdk_edge"]

    @property
    def sip_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["sip_edge"]

    @property
    def tags(self):
        """
        :returns:
        :rtype: List[str]
        """
        return self._properties["tags"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    @property
    def attributes(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["attributes"]

    @property
    def properties(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["properties"]

    @property
    def trust(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["trust"]

    @property
    def annotation(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["annotation"]

    def fetch(self, processing_state=values.unset):
        """
        Fetch the CallSummaryInstance

        :param CallSummaryInstance.ProcessingState processing_state:

        :returns: The fetched CallSummaryInstance
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryInstance
        """
        return self._proxy.fetch(
            processing_state=processing_state,
        )

    async def fetch_async(self, processing_state=values.unset):
        """
        Asynchronous coroutine to fetch the CallSummaryInstance

        :param CallSummaryInstance.ProcessingState processing_state:

        :returns: The fetched CallSummaryInstance
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryInstance
        """
        return await self._proxy.fetch_async(
            processing_state=processing_state,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.CallSummaryInstance {}>".format(context)


class CallSummaryContext(InstanceContext):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the CallSummaryContext

        :param Version version: Version that contains the resource
        :param call_sid:

        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }
        self._uri = "/Voice/{call_sid}/Summary".format(**self._solution)

    def fetch(self, processing_state=values.unset):
        """
        Fetch the CallSummaryInstance

        :param CallSummaryInstance.ProcessingState processing_state:

        :returns: The fetched CallSummaryInstance
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryInstance
        """

        data = values.of(
            {
                "ProcessingState": processing_state,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return CallSummaryInstance(
            self._version,
            payload,
            call_sid=self._solution["call_sid"],
        )

    async def fetch_async(self, processing_state=values.unset):
        """
        Asynchronous coroutine to fetch the CallSummaryInstance

        :param CallSummaryInstance.ProcessingState processing_state:

        :returns: The fetched CallSummaryInstance
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryInstance
        """

        data = values.of(
            {
                "ProcessingState": processing_state,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return CallSummaryInstance(
            self._version,
            payload,
            call_sid=self._solution["call_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.CallSummaryContext {}>".format(context)


class CallSummaryList(ListResource):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the CallSummaryList

        :param Version version: Version that contains the resource
        :param call_sid:

        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryList
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }

    def get(self):
        """
        Constructs a CallSummaryContext


        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        """
        return CallSummaryContext(self._version, call_sid=self._solution["call_sid"])

    def __call__(self):
        """
        Constructs a CallSummaryContext


        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        """
        return CallSummaryContext(self._version, call_sid=self._solution["call_sid"])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Insights.V1.CallSummaryList>"
