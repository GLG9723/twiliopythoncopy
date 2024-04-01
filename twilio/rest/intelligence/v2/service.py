r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Intelligence
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ServiceInstance(InstanceResource):

    class HttpMethod:
        GET = "GET"
        POST = "POST"
        NULL = "NULL"

    """
    :ivar account_sid: The unique SID identifier of the Account the Service belongs to.
    :ivar auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
    :ivar media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
    :ivar auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
    :ivar data_logging: Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
    :ivar date_created: The date that this Service was created, given in ISO 8601 format.
    :ivar date_updated: The date that this Service was updated, given in ISO 8601 format.
    :ivar friendly_name: A human readable description of this resource, up to 64 characters.
    :ivar language_code: The default language code of the audio.
    :ivar sid: A 34 character string that uniquely identifies this Service.
    :ivar unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
    :ivar url: The URL of this resource.
    :ivar webhook_url: The URL Twilio will request when executing the Webhook.
    :ivar webhook_http_method: 
    :ivar version: The version number of this Service.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.auto_redaction: Optional[bool] = payload.get("auto_redaction")
        self.media_redaction: Optional[bool] = payload.get("media_redaction")
        self.auto_transcribe: Optional[bool] = payload.get("auto_transcribe")
        self.data_logging: Optional[bool] = payload.get("data_logging")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.language_code: Optional[str] = payload.get("language_code")
        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.url: Optional[str] = payload.get("url")
        self.webhook_url: Optional[str] = payload.get("webhook_url")
        self.webhook_http_method: Optional["ServiceInstance.HttpMethod"] = payload.get(
            "webhook_http_method"
        )
        self.version: Optional[int] = deserialize.integer(payload.get("version"))

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[ServiceContext] = None

    @property
    def _proxy(self) -> "ServiceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        """
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ServiceInstance":
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ServiceInstance":
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        if_match: Union[str, object] = values.unset,
        auto_transcribe: Union[bool, object] = values.unset,
        data_logging: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        auto_redaction: Union[bool, object] = values.unset,
        media_redaction: Union[bool, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        webhook_http_method: Union["ServiceInstance.HttpMethod", object] = values.unset,
    ) -> "ServiceInstance":
        """
        Update the ServiceInstance

        :param if_match: The If-Match HTTP request header
        :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
        :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param language_code: The default language code of the audio.
        :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
        :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
        :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
        :param webhook_url: The URL Twilio will request when executing the Webhook.
        :param webhook_http_method:

        :returns: The updated ServiceInstance
        """
        return self._proxy.update(
            if_match=if_match,
            auto_transcribe=auto_transcribe,
            data_logging=data_logging,
            friendly_name=friendly_name,
            language_code=language_code,
            unique_name=unique_name,
            auto_redaction=auto_redaction,
            media_redaction=media_redaction,
            webhook_url=webhook_url,
            webhook_http_method=webhook_http_method,
        )

    async def update_async(
        self,
        if_match: Union[str, object] = values.unset,
        auto_transcribe: Union[bool, object] = values.unset,
        data_logging: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        auto_redaction: Union[bool, object] = values.unset,
        media_redaction: Union[bool, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        webhook_http_method: Union["ServiceInstance.HttpMethod", object] = values.unset,
    ) -> "ServiceInstance":
        """
        Asynchronous coroutine to update the ServiceInstance

        :param if_match: The If-Match HTTP request header
        :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
        :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param language_code: The default language code of the audio.
        :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
        :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
        :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
        :param webhook_url: The URL Twilio will request when executing the Webhook.
        :param webhook_http_method:

        :returns: The updated ServiceInstance
        """
        return await self._proxy.update_async(
            if_match=if_match,
            auto_transcribe=auto_transcribe,
            data_logging=data_logging,
            friendly_name=friendly_name,
            language_code=language_code,
            unique_name=unique_name,
            auto_redaction=auto_redaction,
            media_redaction=media_redaction,
            webhook_url=webhook_url,
            webhook_http_method=webhook_http_method,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Intelligence.V2.ServiceInstance {context}>"


class ServiceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this Service.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Services/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ServiceInstance:
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ServiceInstance:
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        if_match: Union[str, object] = values.unset,
        auto_transcribe: Union[bool, object] = values.unset,
        data_logging: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        auto_redaction: Union[bool, object] = values.unset,
        media_redaction: Union[bool, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        webhook_http_method: Union["ServiceInstance.HttpMethod", object] = values.unset,
    ) -> ServiceInstance:
        """
        Update the ServiceInstance

        :param if_match: The If-Match HTTP request header
        :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
        :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param language_code: The default language code of the audio.
        :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
        :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
        :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
        :param webhook_url: The URL Twilio will request when executing the Webhook.
        :param webhook_http_method:

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "AutoTranscribe": serialize.boolean_to_string(auto_transcribe),
                "DataLogging": serialize.boolean_to_string(data_logging),
                "FriendlyName": friendly_name,
                "LanguageCode": language_code,
                "UniqueName": unique_name,
                "AutoRedaction": serialize.boolean_to_string(auto_redaction),
                "MediaRedaction": serialize.boolean_to_string(media_redaction),
                "WebhookUrl": webhook_url,
                "WebhookHttpMethod": webhook_http_method,
            }
        )
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        if_match: Union[str, object] = values.unset,
        auto_transcribe: Union[bool, object] = values.unset,
        data_logging: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        auto_redaction: Union[bool, object] = values.unset,
        media_redaction: Union[bool, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        webhook_http_method: Union["ServiceInstance.HttpMethod", object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronous coroutine to update the ServiceInstance

        :param if_match: The If-Match HTTP request header
        :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
        :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param language_code: The default language code of the audio.
        :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
        :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
        :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
        :param webhook_url: The URL Twilio will request when executing the Webhook.
        :param webhook_http_method:

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "AutoTranscribe": serialize.boolean_to_string(auto_transcribe),
                "DataLogging": serialize.boolean_to_string(data_logging),
                "FriendlyName": friendly_name,
                "LanguageCode": language_code,
                "UniqueName": unique_name,
                "AutoRedaction": serialize.boolean_to_string(auto_redaction),
                "MediaRedaction": serialize.boolean_to_string(media_redaction),
                "WebhookUrl": webhook_url,
                "WebhookHttpMethod": webhook_http_method,
            }
        )
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Intelligence.V2.ServiceContext {context}>"


class ServicePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ServiceInstance:
        """
        Build an instance of ServiceInstance

        :param payload: Payload response from the API
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.ServicePage>"


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services"

    def create(
        self,
        unique_name: str,
        auto_transcribe: Union[bool, object] = values.unset,
        data_logging: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        auto_redaction: Union[bool, object] = values.unset,
        media_redaction: Union[bool, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        webhook_http_method: Union["ServiceInstance.HttpMethod", object] = values.unset,
    ) -> ServiceInstance:
        """
        Create the ServiceInstance

        :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
        :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
        :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param language_code: The default language code of the audio.
        :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
        :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
        :param webhook_url: The URL Twilio will request when executing the Webhook.
        :param webhook_http_method:

        :returns: The created ServiceInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "AutoTranscribe": serialize.boolean_to_string(auto_transcribe),
                "DataLogging": serialize.boolean_to_string(data_logging),
                "FriendlyName": friendly_name,
                "LanguageCode": language_code,
                "AutoRedaction": serialize.boolean_to_string(auto_redaction),
                "MediaRedaction": serialize.boolean_to_string(media_redaction),
                "WebhookUrl": webhook_url,
                "WebhookHttpMethod": webhook_http_method,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    async def create_async(
        self,
        unique_name: str,
        auto_transcribe: Union[bool, object] = values.unset,
        data_logging: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        auto_redaction: Union[bool, object] = values.unset,
        media_redaction: Union[bool, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        webhook_http_method: Union["ServiceInstance.HttpMethod", object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronously create the ServiceInstance

        :param unique_name: Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
        :param auto_transcribe: Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
        :param data_logging: Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
        :param friendly_name: A human readable description of this resource, up to 64 characters.
        :param language_code: The default language code of the audio.
        :param auto_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
        :param media_redaction: Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
        :param webhook_url: The URL Twilio will request when executing the Webhook.
        :param webhook_http_method:

        :returns: The created ServiceInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "AutoTranscribe": serialize.boolean_to_string(auto_transcribe),
                "DataLogging": serialize.boolean_to_string(data_logging),
                "FriendlyName": friendly_name,
                "LanguageCode": language_code,
                "AutoRedaction": serialize.boolean_to_string(auto_redaction),
                "MediaRedaction": serialize.boolean_to_string(media_redaction),
                "WebhookUrl": webhook_url,
                "WebhookHttpMethod": webhook_http_method,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ServiceInstance]:
        """
        Streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ServiceInstance]:
        """
        Asynchronously streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ServiceInstance]:
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ServiceInstance]:
        """
        Asynchronously lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ServicePage:
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ServicePage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ServicePage:
        """
        Asynchronously retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
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
        return ServicePage(self._version, response)

    def get_page(self, target_url: str) -> ServicePage:
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ServicePage(self._version, response)

    async def get_page_async(self, target_url: str) -> ServicePage:
        """
        Asynchronously retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ServicePage(self._version, response)

    def get(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: A 34 character string that uniquely identifies this Service.
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: A 34 character string that uniquely identifies this Service.
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.ServiceList>"
