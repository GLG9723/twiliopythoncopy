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



from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class InsightsSettingsCommentList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsSettingsCommentList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentList
        :rtype: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Insights/QM/Settings/CommentTags".format(**self._solution)

    def fetch(self):
        """
        Asynchronously fetch the InsightsSettingsCommentInstance

        :returns: The fetched InsightsSettingsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentInstance
        """
        payload = self._version.fetch(method="GET", uri=self._uri)

        return InsightsSettingsCommentInstance(self._version, payload)

    async def fetch_async(self):
        """
        Asynchronously fetch the InsightsSettingsCommentInstance

        :returns: The fetched InsightsSettingsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentInstance
        """
        payload = await self._version.fetch_async(method="GET", uri=self._uri)

        return InsightsSettingsCommentInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InsightsSettingsCommentList>"


class InsightsSettingsCommentInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the InsightsSettingsCommentInstance

        :returns: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_settings_comment.InsightsSettingsCommentInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "comments": payload.get("comments"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {}

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def comments(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["comments"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsSettingsCommentInstance {}>".format(context)
