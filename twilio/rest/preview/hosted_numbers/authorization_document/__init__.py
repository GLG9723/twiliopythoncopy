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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.hosted_numbers.authorization_document.dependent_hosted_number_order import (
    DependentHostedNumberOrderList,
)


class AuthorizationDocumentList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AuthorizationDocumentList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentList
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/AuthorizationDocuments".format(**self._solution)

    def create(
        self,
        hosted_number_order_sids,
        address_sid,
        email,
        contact_title,
        contact_phone_number,
        cc_emails=values.unset,
    ):
        """
        Create the AuthorizationDocumentInstance

        :param list[str] hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param str address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param str contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param str contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
        :param list[str] cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.

        :returns: The created AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        data = values.of(
            {
                "HostedNumberOrderSids": serialize.map(
                    hosted_number_order_sids, lambda e: e
                ),
                "AddressSid": address_sid,
                "Email": email,
                "ContactTitle": contact_title,
                "ContactPhoneNumber": contact_phone_number,
                "CcEmails": serialize.map(cc_emails, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AuthorizationDocumentInstance(self._version, payload)

    async def create_async(
        self,
        hosted_number_order_sids,
        address_sid,
        email,
        contact_title,
        contact_phone_number,
        cc_emails=values.unset,
    ):
        """
        Asynchronously create the AuthorizationDocumentInstance

        :param list[str] hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param str address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param str contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param str contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
        :param list[str] cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.

        :returns: The created AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        data = values.of(
            {
                "HostedNumberOrderSids": serialize.map(
                    hosted_number_order_sids, lambda e: e
                ),
                "AddressSid": address_sid,
                "Email": email,
                "ContactTitle": contact_title,
                "ContactPhoneNumber": contact_phone_number,
                "CcEmails": serialize.map(cc_emails, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AuthorizationDocumentInstance(self._version, payload)

    def stream(
        self, email=values.unset, status=values.unset, limit=None, page_size=None
    ):
        """
        Streams AuthorizationDocumentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentInstance.Status status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(email=email, status=status, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, email=values.unset, status=values.unset, limit=None, page_size=None
    ):
        """
        Asynchronously streams AuthorizationDocumentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentInstance.Status status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            email=email, status=status, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(self, email=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Lists AuthorizationDocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentInstance.Status status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance]
        """
        return list(
            self.stream(
                email=email,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, email=values.unset, status=values.unset, limit=None, page_size=None
    ):
        """
        Asynchronously lists AuthorizationDocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentInstance.Status status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance]
        """
        return list(
            await self.stream_async(
                email=email,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        email=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately

        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentInstance.Status status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        data = values.of(
            {
                "Email": email,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AuthorizationDocumentPage(self._version, response, self._solution)

    async def page_async(
        self,
        email=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately

        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentInstance.Status status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        data = values.of(
            {
                "Email": email,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AuthorizationDocumentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AuthorizationDocumentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AuthorizationDocumentPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a AuthorizationDocumentContext

        :param sid:

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        """
        return AuthorizationDocumentContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a AuthorizationDocumentContext

        :param sid:

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        """
        return AuthorizationDocumentContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.HostedNumbers.AuthorizationDocumentList>"


class AuthorizationDocumentPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the AuthorizationDocumentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AuthorizationDocumentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        return AuthorizationDocumentInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.HostedNumbers.AuthorizationDocumentPage>"


class AuthorizationDocumentInstance(InstanceResource):
    class Status(object):
        OPENED = "opened"
        SIGNING = "signing"
        SIGNED = "signed"
        CANCELED = "canceled"
        FAILED = "failed"

    def __init__(self, version, payload, sid: str = None):
        """
        Initialize the AuthorizationDocumentInstance

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "address_sid": payload.get("address_sid"),
            "status": payload.get("status"),
            "email": payload.get("email"),
            "cc_emails": payload.get("cc_emails"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._context = None
        self._solution = {
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AuthorizationDocumentContext for this AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        """
        if self._context is None:
            self._context = AuthorizationDocumentContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this AuthorizationDocument.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def address_sid(self):
        """
        :returns: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :rtype: str
        """
        return self._properties["address_sid"]

    @property
    def status(self):
        """
        :returns:
        :rtype: AuthorizationDocumentInstance.Status
        """
        return self._properties["status"]

    @property
    def email(self):
        """
        :returns: Email that this AuthorizationDocument will be sent to for signing.
        :rtype: str
        """
        return self._properties["email"]

    @property
    def cc_emails(self):
        """
        :returns: Email recipients who will be informed when an Authorization Document has been sent and signed.
        :rtype: list[str]
        """
        return self._properties["cc_emails"]

    @property
    def date_created(self):
        """
        :returns: The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["links"]

    def fetch(self):
        """
        Fetch the AuthorizationDocumentInstance


        :returns: The fetched AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AuthorizationDocumentInstance


        :returns: The fetched AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        hosted_number_order_sids=values.unset,
        address_sid=values.unset,
        email=values.unset,
        cc_emails=values.unset,
        status=values.unset,
        contact_title=values.unset,
        contact_phone_number=values.unset,
    ):
        """
        Update the AuthorizationDocumentInstance

        :param list[str] hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param str address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param list[str] cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param AuthorizationDocumentInstance.Status status:
        :param str contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param str contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        return self._proxy.update(
            hosted_number_order_sids=hosted_number_order_sids,
            address_sid=address_sid,
            email=email,
            cc_emails=cc_emails,
            status=status,
            contact_title=contact_title,
            contact_phone_number=contact_phone_number,
        )

    async def update_async(
        self,
        hosted_number_order_sids=values.unset,
        address_sid=values.unset,
        email=values.unset,
        cc_emails=values.unset,
        status=values.unset,
        contact_title=values.unset,
        contact_phone_number=values.unset,
    ):
        """
        Asynchronous coroutine to update the AuthorizationDocumentInstance

        :param list[str] hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param str address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param list[str] cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param AuthorizationDocumentInstance.Status status:
        :param str contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param str contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        return await self._proxy.update_async(
            hosted_number_order_sids=hosted_number_order_sids,
            address_sid=address_sid,
            email=email,
            cc_emails=cc_emails,
            status=status,
            contact_title=contact_title,
            contact_phone_number=contact_phone_number,
        )

    @property
    def dependent_hosted_number_orders(self):
        """
        Access the dependent_hosted_number_orders

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.DependentHostedNumberOrderList
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.DependentHostedNumberOrderList
        """
        return self._proxy.dependent_hosted_number_orders

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.HostedNumbers.AuthorizationDocumentInstance {}>".format(
            context
        )


class AuthorizationDocumentContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the AuthorizationDocumentContext

        :param Version version: Version that contains the resource
        :param sid:

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/AuthorizationDocuments/{sid}".format(**self._solution)

        self._dependent_hosted_number_orders = None

    def fetch(self):
        """
        Fetch the AuthorizationDocumentInstance


        :returns: The fetched AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AuthorizationDocumentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AuthorizationDocumentInstance


        :returns: The fetched AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AuthorizationDocumentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        hosted_number_order_sids=values.unset,
        address_sid=values.unset,
        email=values.unset,
        cc_emails=values.unset,
        status=values.unset,
        contact_title=values.unset,
        contact_phone_number=values.unset,
    ):
        """
        Update the AuthorizationDocumentInstance

        :param list[str] hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param str address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param list[str] cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param AuthorizationDocumentInstance.Status status:
        :param str contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param str contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        data = values.of(
            {
                "HostedNumberOrderSids": serialize.map(
                    hosted_number_order_sids, lambda e: e
                ),
                "AddressSid": address_sid,
                "Email": email,
                "CcEmails": serialize.map(cc_emails, lambda e: e),
                "Status": status,
                "ContactTitle": contact_title,
                "ContactPhoneNumber": contact_phone_number,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AuthorizationDocumentInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    async def update_async(
        self,
        hosted_number_order_sids=values.unset,
        address_sid=values.unset,
        email=values.unset,
        cc_emails=values.unset,
        status=values.unset,
        contact_title=values.unset,
        contact_phone_number=values.unset,
    ):
        """
        Asynchronous coroutine to update the AuthorizationDocumentInstance

        :param list[str] hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param str address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param list[str] cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param AuthorizationDocumentInstance.Status status:
        :param str contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param str contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        data = values.of(
            {
                "HostedNumberOrderSids": serialize.map(
                    hosted_number_order_sids, lambda e: e
                ),
                "AddressSid": address_sid,
                "Email": email,
                "CcEmails": serialize.map(cc_emails, lambda e: e),
                "Status": status,
                "ContactTitle": contact_title,
                "ContactPhoneNumber": contact_phone_number,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AuthorizationDocumentInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    @property
    def dependent_hosted_number_orders(self):
        """
        Access the dependent_hosted_number_orders

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.DependentHostedNumberOrderList
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.DependentHostedNumberOrderList
        """
        if self._dependent_hosted_number_orders is None:
            self._dependent_hosted_number_orders = DependentHostedNumberOrderList(
                self._version,
                self._solution["sid"],
            )
        return self._dependent_hosted_number_orders

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.HostedNumbers.AuthorizationDocumentContext {}>".format(
            context
        )
