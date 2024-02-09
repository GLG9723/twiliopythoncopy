r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DependentHostedNumberOrderInstance(InstanceResource):
    class Status(object):
        RECEIVED = "received"
        PENDING_VERIFICATION = "pending-verification"
        VERIFIED = "verified"
        PENDING_LOA = "pending-loa"
        CARRIER_PROCESSING = "carrier-processing"
        TESTING = "testing"
        COMPLETED = "completed"
        FAILED = "failed"
        ACTION_REQUIRED = "action-required"

    class VerificationType(object):
        PHONE_CALL = "phone-call"
        PHONE_BILL = "phone-bill"

    """
    :ivar sid: A 34 character string that uniquely identifies this Authorization Document
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
    :ivar address_sid: A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
    :ivar signing_document_sid: A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder.
    :ivar phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
    :ivar capabilities: 
    :ivar friendly_name: A human readable description of this resource, up to 64 characters.
    :ivar unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
    :ivar status: 
    :ivar failure_reason: A message that explains why a hosted_number_order went to status \"action-required\"
    :ivar date_created: The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar verification_attempts: The number of attempts made to verify ownership of the phone number that is being hosted.
    :ivar email: Email of the owner of this phone number that is being hosted.
    :ivar cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
    :ivar verification_type: 
    :ivar verification_document_sid: A 34 character string that uniquely identifies the Identity Document resource that represents the document for verifying ownership of the number to be hosted.
    :ivar extension: A numerical extension to be used when making the ownership verification call.
    :ivar call_delay: A value between 0-30 specifying the number of seconds to delay initiating the ownership verification call.
    :ivar verification_code: The digits passed during the ownership verification call.
    :ivar verification_call_sids: A list of 34 character strings that are unique identifiers for the calls placed as part of ownership verification.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], signing_document_sid: str
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.incoming_phone_number_sid: Optional[str] = payload.get(
            "incoming_phone_number_sid"
        )
        self.address_sid: Optional[str] = payload.get("address_sid")
        self.signing_document_sid: Optional[str] = payload.get("signing_document_sid")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.capabilities: Optional[str] = payload.get("capabilities")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.status: Optional["DependentHostedNumberOrderInstance.Status"] = (
            payload.get("status")
        )
        self.failure_reason: Optional[str] = payload.get("failure_reason")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.verification_attempts: Optional[int] = deserialize.integer(
            payload.get("verification_attempts")
        )
        self.email: Optional[str] = payload.get("email")
        self.cc_emails: Optional[List[str]] = payload.get("cc_emails")
        self.verification_type: Optional[
            "DependentHostedNumberOrderInstance.VerificationType"
        ] = payload.get("verification_type")
        self.verification_document_sid: Optional[str] = payload.get(
            "verification_document_sid"
        )
        self.extension: Optional[str] = payload.get("extension")
        self.call_delay: Optional[int] = deserialize.integer(payload.get("call_delay"))
        self.verification_code: Optional[str] = payload.get("verification_code")
        self.verification_call_sids: Optional[List[str]] = payload.get(
            "verification_call_sids"
        )

        self._solution = {
            "signing_document_sid": signing_document_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.HostedNumbers.DependentHostedNumberOrderInstance {}>".format(
            context
        )


class DependentHostedNumberOrderPage(Page):
    def get_instance(
        self, payload: Dict[str, Any]
    ) -> DependentHostedNumberOrderInstance:
        """
        Build an instance of DependentHostedNumberOrderInstance

        :param payload: Payload response from the API
        """
        return DependentHostedNumberOrderInstance(
            self._version,
            payload,
            signing_document_sid=self._solution["signing_document_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.HostedNumbers.DependentHostedNumberOrderPage>"


class DependentHostedNumberOrderList(ListResource):
    def __init__(self, version: Version, signing_document_sid: str):
        """
        Initialize the DependentHostedNumberOrderList

        :param version: Version that contains the resource
        :param signing_document_sid: A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "signing_document_sid": signing_document_sid,
        }
        self._uri = "/AuthorizationDocuments/{signing_document_sid}/DependentHostedNumberOrders".format(
            **self._solution
        )

    def stream(
        self,
        status: Union[
            "DependentHostedNumberOrderInstance.Status", object
        ] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[DependentHostedNumberOrderInstance]:
        """
        Streams DependentHostedNumberOrderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;DependentHostedNumberOrderInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 64 characters.
        :param str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            unique_name=unique_name,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status: Union[
            "DependentHostedNumberOrderInstance.Status", object
        ] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[DependentHostedNumberOrderInstance]:
        """
        Asynchronously streams DependentHostedNumberOrderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;DependentHostedNumberOrderInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 64 characters.
        :param str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            status=status,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            unique_name=unique_name,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status: Union[
            "DependentHostedNumberOrderInstance.Status", object
        ] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DependentHostedNumberOrderInstance]:
        """
        Lists DependentHostedNumberOrderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;DependentHostedNumberOrderInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 64 characters.
        :param str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                status=status,
                phone_number=phone_number,
                incoming_phone_number_sid=incoming_phone_number_sid,
                friendly_name=friendly_name,
                unique_name=unique_name,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status: Union[
            "DependentHostedNumberOrderInstance.Status", object
        ] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DependentHostedNumberOrderInstance]:
        """
        Asynchronously lists DependentHostedNumberOrderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;DependentHostedNumberOrderInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 64 characters.
        :param str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                status=status,
                phone_number=phone_number,
                incoming_phone_number_sid=incoming_phone_number_sid,
                friendly_name=friendly_name,
                unique_name=unique_name,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        status: Union[
            "DependentHostedNumberOrderInstance.Status", object
        ] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DependentHostedNumberOrderPage:
        """
        Retrieve a single page of DependentHostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DependentHostedNumberOrderInstance
        """
        data = values.of(
            {
                "Status": status,
                "PhoneNumber": phone_number,
                "IncomingPhoneNumberSid": incoming_phone_number_sid,
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DependentHostedNumberOrderPage(self._version, response, self._solution)

    async def page_async(
        self,
        status: Union[
            "DependentHostedNumberOrderInstance.Status", object
        ] = values.unset,
        phone_number: Union[str, object] = values.unset,
        incoming_phone_number_sid: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DependentHostedNumberOrderPage:
        """
        Asynchronously retrieve a single page of DependentHostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DependentHostedNumberOrderInstance
        """
        data = values.of(
            {
                "Status": status,
                "PhoneNumber": phone_number,
                "IncomingPhoneNumberSid": incoming_phone_number_sid,
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return DependentHostedNumberOrderPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> DependentHostedNumberOrderPage:
        """
        Retrieve a specific page of DependentHostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DependentHostedNumberOrderInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DependentHostedNumberOrderPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> DependentHostedNumberOrderPage:
        """
        Asynchronously retrieve a specific page of DependentHostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DependentHostedNumberOrderInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DependentHostedNumberOrderPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.HostedNumbers.DependentHostedNumberOrderList>"
