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

from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class AnnotationInstance(InstanceResource):
    class AnsweredBy(object):
        UNKNOWN_ANSWERED_BY = "unknown_answered_by"
        HUMAN = "human"
        MACHINE = "machine"

    class ConnectivityIssue(object):
        UNKNOWN_CONNECTIVITY_ISSUE = "unknown_connectivity_issue"
        NO_CONNECTIVITY_ISSUE = "no_connectivity_issue"
        INVALID_NUMBER = "invalid_number"
        CALLER_ID = "caller_id"
        DROPPED_CALL = "dropped_call"
        NUMBER_REACHABILITY = "number_reachability"

    """
    :ivar call_sid: The unique SID identifier of the Call.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar answered_by: 
    :ivar connectivity_issue: 
    :ivar quality_issues: Specifies if the call had any subjective quality issues. Possible values are one or more of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, or `static_noise`.
    :ivar spam: Specifies if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Is of type Boolean: true, false. Use true if the call was a spam call.
    :ivar call_score: Specifies the Call Score, if available. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
    :ivar comment: Specifies any comments pertaining to the call. Twilio does not treat this field as PII, so no PII should be included in comments.
    :ivar incident: Incident or support ticket associated with this call. The `incident` property is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in `incident`.
    :ivar url: The URL of this resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], call_sid: str):
        super().__init__(version)

        self.call_sid: Optional[str] = payload.get("call_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.answered_by: Optional["AnnotationInstance.AnsweredBy"] = payload.get(
            "answered_by"
        )
        self.connectivity_issue: Optional["AnnotationInstance.ConnectivityIssue"] = (
            payload.get("connectivity_issue")
        )
        self.quality_issues: Optional[List[str]] = payload.get("quality_issues")
        self.spam: Optional[bool] = payload.get("spam")
        self.call_score: Optional[int] = deserialize.integer(payload.get("call_score"))
        self.comment: Optional[str] = payload.get("comment")
        self.incident: Optional[str] = payload.get("incident")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "call_sid": call_sid,
        }
        self._context: Optional[AnnotationContext] = None

    @property
    def _proxy(self) -> "AnnotationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AnnotationContext for this AnnotationInstance
        """
        if self._context is None:
            self._context = AnnotationContext(
                self._version,
                call_sid=self._solution["call_sid"],
            )
        return self._context

    def fetch(self) -> "AnnotationInstance":
        """
        Fetch the AnnotationInstance


        :returns: The fetched AnnotationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AnnotationInstance":
        """
        Asynchronous coroutine to fetch the AnnotationInstance


        :returns: The fetched AnnotationInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        answered_by: Union["AnnotationInstance.AnsweredBy", object] = values.unset,
        connectivity_issue: Union[
            "AnnotationInstance.ConnectivityIssue", object
        ] = values.unset,
        quality_issues: Union[str, object] = values.unset,
        spam: Union[bool, object] = values.unset,
        call_score: Union[int, object] = values.unset,
        comment: Union[str, object] = values.unset,
        incident: Union[str, object] = values.unset,
    ) -> "AnnotationInstance":
        """
        Update the AnnotationInstance

        :param answered_by:
        :param connectivity_issue:
        :param quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`. Use comma separated values to indicate multiple quality issues for the same call.
        :param spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use `true` if the call was a spam call.
        :param call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
        :param comment: Specify any comments pertaining to the call. `comment` has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the `comment`.
        :param incident: Associate this call with an incident or support ticket. The `incident` parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in `incident`.

        :returns: The updated AnnotationInstance
        """
        return self._proxy.update(
            answered_by=answered_by,
            connectivity_issue=connectivity_issue,
            quality_issues=quality_issues,
            spam=spam,
            call_score=call_score,
            comment=comment,
            incident=incident,
        )

    async def update_async(
        self,
        answered_by: Union["AnnotationInstance.AnsweredBy", object] = values.unset,
        connectivity_issue: Union[
            "AnnotationInstance.ConnectivityIssue", object
        ] = values.unset,
        quality_issues: Union[str, object] = values.unset,
        spam: Union[bool, object] = values.unset,
        call_score: Union[int, object] = values.unset,
        comment: Union[str, object] = values.unset,
        incident: Union[str, object] = values.unset,
    ) -> "AnnotationInstance":
        """
        Asynchronous coroutine to update the AnnotationInstance

        :param answered_by:
        :param connectivity_issue:
        :param quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`. Use comma separated values to indicate multiple quality issues for the same call.
        :param spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use `true` if the call was a spam call.
        :param call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
        :param comment: Specify any comments pertaining to the call. `comment` has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the `comment`.
        :param incident: Associate this call with an incident or support ticket. The `incident` parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in `incident`.

        :returns: The updated AnnotationInstance
        """
        return await self._proxy.update_async(
            answered_by=answered_by,
            connectivity_issue=connectivity_issue,
            quality_issues=quality_issues,
            spam=spam,
            call_score=call_score,
            comment=comment,
            incident=incident,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.AnnotationInstance {}>".format(context)


class AnnotationContext(InstanceContext):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the AnnotationContext

        :param version: Version that contains the resource
        :param call_sid: The unique string that Twilio created to identify this Call resource. It always starts with a CA.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }
        self._uri = "/Voice/{call_sid}/Annotation".format(**self._solution)

    def fetch(self) -> AnnotationInstance:
        """
        Fetch the AnnotationInstance


        :returns: The fetched AnnotationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AnnotationInstance(
            self._version,
            payload,
            call_sid=self._solution["call_sid"],
        )

    async def fetch_async(self) -> AnnotationInstance:
        """
        Asynchronous coroutine to fetch the AnnotationInstance


        :returns: The fetched AnnotationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AnnotationInstance(
            self._version,
            payload,
            call_sid=self._solution["call_sid"],
        )

    def update(
        self,
        answered_by: Union["AnnotationInstance.AnsweredBy", object] = values.unset,
        connectivity_issue: Union[
            "AnnotationInstance.ConnectivityIssue", object
        ] = values.unset,
        quality_issues: Union[str, object] = values.unset,
        spam: Union[bool, object] = values.unset,
        call_score: Union[int, object] = values.unset,
        comment: Union[str, object] = values.unset,
        incident: Union[str, object] = values.unset,
    ) -> AnnotationInstance:
        """
        Update the AnnotationInstance

        :param answered_by:
        :param connectivity_issue:
        :param quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`. Use comma separated values to indicate multiple quality issues for the same call.
        :param spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use `true` if the call was a spam call.
        :param call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
        :param comment: Specify any comments pertaining to the call. `comment` has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the `comment`.
        :param incident: Associate this call with an incident or support ticket. The `incident` parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in `incident`.

        :returns: The updated AnnotationInstance
        """
        data = values.of(
            {
                "AnsweredBy": answered_by,
                "ConnectivityIssue": connectivity_issue,
                "QualityIssues": quality_issues,
                "Spam": spam,
                "CallScore": call_score,
                "Comment": comment,
                "Incident": incident,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AnnotationInstance(
            self._version, payload, call_sid=self._solution["call_sid"]
        )

    async def update_async(
        self,
        answered_by: Union["AnnotationInstance.AnsweredBy", object] = values.unset,
        connectivity_issue: Union[
            "AnnotationInstance.ConnectivityIssue", object
        ] = values.unset,
        quality_issues: Union[str, object] = values.unset,
        spam: Union[bool, object] = values.unset,
        call_score: Union[int, object] = values.unset,
        comment: Union[str, object] = values.unset,
        incident: Union[str, object] = values.unset,
    ) -> AnnotationInstance:
        """
        Asynchronous coroutine to update the AnnotationInstance

        :param answered_by:
        :param connectivity_issue:
        :param quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`. Use comma separated values to indicate multiple quality issues for the same call.
        :param spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use `true` if the call was a spam call.
        :param call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
        :param comment: Specify any comments pertaining to the call. `comment` has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the `comment`.
        :param incident: Associate this call with an incident or support ticket. The `incident` parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in `incident`.

        :returns: The updated AnnotationInstance
        """
        data = values.of(
            {
                "AnsweredBy": answered_by,
                "ConnectivityIssue": connectivity_issue,
                "QualityIssues": quality_issues,
                "Spam": spam,
                "CallScore": call_score,
                "Comment": comment,
                "Incident": incident,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AnnotationInstance(
            self._version, payload, call_sid=self._solution["call_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.AnnotationContext {}>".format(context)


class AnnotationList(ListResource):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the AnnotationList

        :param version: Version that contains the resource
        :param call_sid: The unique SID identifier of the Call.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }

    def get(self) -> AnnotationContext:
        """
        Constructs a AnnotationContext

        """
        return AnnotationContext(self._version, call_sid=self._solution["call_sid"])

    def __call__(self) -> AnnotationContext:
        """
        Constructs a AnnotationContext

        """
        return AnnotationContext(self._version, call_sid=self._solution["call_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.AnnotationList>"
