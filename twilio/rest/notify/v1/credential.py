r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Notify
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
from twilio.base.page import Page


class CredentialInstance(InstanceResource):
    class PushService(object):
        GCM = "gcm"
        APN = "apn"
        FCM = "fcm"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the CredentialInstance

        :returns: twilio.rest.notify.v1.credential.CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "type": payload.get("type"),
            "sandbox": payload.get("sandbox"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[CredentialContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialContext for this CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialContext
        """
        if self._context is None:
            self._context = CredentialContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Credential resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Credential resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def type(self):
        """
        :returns:
        :rtype: CredentialInstance.PushService
        """
        return self._properties["type"]

    @property
    def sandbox(self):
        """
        :returns: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :rtype: str
        """
        return self._properties["sandbox"]

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
    def url(self):
        """
        :returns: The absolute URL of the Credential resource.
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ):
        """
        Update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
        :param str secret: [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            certificate=certificate,
            private_key=private_key,
            sandbox=sandbox,
            api_key=api_key,
            secret=secret,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ):
        """
        Asynchronous coroutine to update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
        :param str secret: [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            certificate=certificate,
            private_key=private_key,
            sandbox=sandbox,
            api_key=api_key,
            secret=secret,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Notify.V1.CredentialInstance {}>".format(context)


class CredentialContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the CredentialContext

        :param Version version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Credential resource to update.

        :returns: twilio.rest.notify.v1.credential.CredentialContext
        :rtype: twilio.rest.notify.v1.credential.CredentialContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Credentials/{sid}".format(**self._solution)

    def delete(self):
        """
        Deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CredentialInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CredentialInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ):
        """
        Update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
        :param str secret: [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ):
        """
        Asynchronous coroutine to update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
        :param str secret: [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Notify.V1.CredentialContext {}>".format(context)


class CredentialPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of CredentialInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.notify.v1.credential.CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        return CredentialInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Notify.V1.CredentialPage>"


class CredentialList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CredentialList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.notify.v1.credential.CredentialList
        :rtype: twilio.rest.notify.v1.credential.CredentialList
        """
        super().__init__(version)

        self._uri = "/Credentials"

    def create(
        self,
        type,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ):
        """
        Create the CredentialInstance

        :param CredentialInstance.PushService type:
        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
        :param str secret: [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.

        :returns: The created CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        data = values.of(
            {
                "Type": type,
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload)

    async def create_async(
        self,
        type,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ):
        """
        Asynchronously create the CredentialInstance

        :param CredentialInstance.PushService type:
        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
        :param str secret: [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.

        :returns: The created CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialInstance
        """
        data = values.of(
            {
                "Type": type,
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload)

    def stream(self, limit=None, page_size=None):
        """
        Streams CredentialInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.credential.CredentialInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams CredentialInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.credential.CredentialInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists CredentialInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.credential.CredentialInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists CredentialInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.credential.CredentialInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of CredentialInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CredentialPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of CredentialInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return CredentialPage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CredentialInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CredentialPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of CredentialInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.notify.v1.credential.CredentialPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CredentialPage(self._version, response)

    def get(self, sid):
        """
        Constructs a CredentialContext

        :param sid: The Twilio-provided string that uniquely identifies the Credential resource to update.

        :returns: twilio.rest.notify.v1.credential.CredentialContext
        :rtype: twilio.rest.notify.v1.credential.CredentialContext
        """
        return CredentialContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a CredentialContext

        :param sid: The Twilio-provided string that uniquely identifies the Credential resource to update.

        :returns: twilio.rest.notify.v1.credential.CredentialContext
        :rtype: twilio.rest.notify.v1.credential.CredentialContext
        """
        return CredentialContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Notify.V1.CredentialList>"
