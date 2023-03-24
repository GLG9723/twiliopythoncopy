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


from typing import Dict, Optional

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class InsightsSettingsCommentInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the InsightsSettingsCommentInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._comments: Optional[Dict[str, object]] = payload.get("comments")
        self._url: Optional[str] = payload.get("url")

        self._solution = {}

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
        """
        return self._account_sid

    @property
    def comments(self) -> Optional[Dict[str, object]]:
        return self._comments

    @property
    def url(self) -> Optional[str]:
        return self._url

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsSettingsCommentInstance {}>".format(context)


class InsightsSettingsCommentList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsSettingsCommentList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Insights/QM/Settings/CommentTags"

    def fetch(self) -> InsightsSettingsCommentInstance:
        """
        Asynchronously fetch the InsightsSettingsCommentInstance

        :returns: The fetched InsightsSettingsCommentInstance
        """
        payload = self._version.fetch(method="GET", uri=self._uri)

        return InsightsSettingsCommentInstance(self._version, payload)

    async def fetch_async(self) -> InsightsSettingsCommentInstance:
        """
        Asynchronously fetch the InsightsSettingsCommentInstance

        :returns: The fetched InsightsSettingsCommentInstance
        """
        payload = await self._version.fetch_async(method="GET", uri=self._uri)

        return InsightsSettingsCommentInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsSettingsCommentList>"
