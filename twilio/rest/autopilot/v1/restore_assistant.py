"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class RestoreAssistantList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the RestoreAssistantList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.autopilot.v1.restore_assistant.RestoreAssistantList
        :rtype: twilio.rest.autopilot.v1.restore_assistant.RestoreAssistantList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Assistants/Restore".format(**self._solution)

    def update(self, assistant):
        """
        Update the RestoreAssistantInstance

        :param str assistant: The Twilio-provided string that uniquely identifies the Assistant resource to restore.

        :returns: The created RestoreAssistantInstance
        :rtype: twilio.rest.autopilot.v1.restore_assistant.RestoreAssistantInstance
        """
        data = values.of(
            {
                "Assistant": assistant,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RestoreAssistantInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Autopilot.V1.RestoreAssistantList>"


class RestoreAssistantInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the RestoreAssistantInstance

        :returns: twilio.rest.autopilot.v1.restore_assistant.RestoreAssistantInstance
        :rtype: twilio.rest.autopilot.v1.restore_assistant.RestoreAssistantInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "sid": payload.get("sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "unique_name": payload.get("unique_name"),
            "friendly_name": payload.get("friendly_name"),
            "needs_model_build": payload.get("needs_model_build"),
            "latest_model_build_sid": payload.get("latest_model_build_sid"),
            "log_queries": payload.get("log_queries"),
            "development_stage": payload.get("development_stage"),
            "callback_url": payload.get("callback_url"),
            "callback_events": payload.get("callback_events"),
        }

        self._context = None
        self._solution = {}

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Assistant resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Assistant resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource. It is not unique and can be up to 255 characters long.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def needs_model_build(self):
        """
        :returns: Whether model needs to be rebuilt.
        :rtype: bool
        """
        return self._properties["needs_model_build"]

    @property
    def latest_model_build_sid(self):
        """
        :returns: Reserved.
        :rtype: str
        """
        return self._properties["latest_model_build_sid"]

    @property
    def log_queries(self):
        """
        :returns: Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
        :rtype: bool
        """
        return self._properties["log_queries"]

    @property
    def development_stage(self):
        """
        :returns: A string describing the state of the assistant.
        :rtype: str
        """
        return self._properties["development_stage"]

    @property
    def callback_url(self):
        """
        :returns: Reserved.
        :rtype: str
        """
        return self._properties["callback_url"]

    @property
    def callback_events(self):
        """
        :returns: Reserved.
        :rtype: str
        """
        return self._properties["callback_events"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.RestoreAssistantInstance {}>".format(context)
