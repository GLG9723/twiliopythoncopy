"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class RecordingList(ListResource):
    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the RecordingList

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the recording settings.

        :returns: twilio.rest.trunking.v1.trunk.recording.RecordingList
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }

    def get(self):
        """
        Constructs a RecordingContext


        :returns: twilio.rest.trunking.v1.trunk.recording.RecordingContext
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingContext
        """
        return RecordingContext(self._version, trunk_sid=self._solution["trunk_sid"])

    def __call__(self):
        """
        Constructs a RecordingContext


        :returns: twilio.rest.trunking.v1.trunk.recording.RecordingContext
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingContext
        """
        return RecordingContext(self._version, trunk_sid=self._solution["trunk_sid"])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Trunking.V1.RecordingList>"


class RecordingInstance(InstanceResource):
    class RecordingMode(object):
        DO_NOT_RECORD = "do-not-record"
        RECORD_FROM_RINGING = "record-from-ringing"
        RECORD_FROM_ANSWER = "record-from-answer"
        RECORD_FROM_RINGING_DUAL = "record-from-ringing-dual"
        RECORD_FROM_ANSWER_DUAL = "record-from-answer-dual"

    class RecordingTrim(object):
        TRIM_SILENCE = "trim-silence"
        DO_NOT_TRIM = "do-not-trim"

    def __init__(self, version, payload, trunk_sid: str):
        """
        Initialize the RecordingInstance

        :returns: twilio.rest.trunking.v1.trunk.recording.RecordingInstance
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingInstance
        """
        super().__init__(version)

        self._properties = {
            "mode": payload.get("mode"),
            "trim": payload.get("trim"),
        }

        self._context = None
        self._solution = {
            "trunk_sid": trunk_sid,
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RecordingContext for this RecordingInstance
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingContext
        """
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                trunk_sid=self._solution["trunk_sid"],
            )
        return self._context

    @property
    def mode(self):
        """
        :returns:
        :rtype: RecordingInstance.RecordingMode
        """
        return self._properties["mode"]

    @property
    def trim(self):
        """
        :returns:
        :rtype: RecordingInstance.RecordingTrim
        """
        return self._properties["trim"]

    def fetch(self):
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingInstance
        """
        return self._proxy.fetch()

    def update(self, mode=values.unset, trim=values.unset):
        """
        Update the RecordingInstance

        :param RecordingInstance.RecordingMode mode:
        :param RecordingInstance.RecordingTrim trim:

        :returns: The updated RecordingInstance
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingInstance
        """
        return self._proxy.update(
            mode=mode,
            trim=trim,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.RecordingInstance {}>".format(context)


class RecordingContext(InstanceContext):
    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the RecordingContext

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk that will have its recording settings updated.

        :returns: twilio.rest.trunking.v1.trunk.recording.RecordingContext
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/Recording".format(**self._solution)

    def fetch(self):
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RecordingInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
        )

    def update(self, mode=values.unset, trim=values.unset):
        """
        Update the RecordingInstance

        :param RecordingInstance.RecordingMode mode:
        :param RecordingInstance.RecordingTrim trim:

        :returns: The updated RecordingInstance
        :rtype: twilio.rest.trunking.v1.trunk.recording.RecordingInstance
        """
        data = values.of(
            {
                "Mode": mode,
                "Trim": trim,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RecordingInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.RecordingContext {}>".format(context)
