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


from datetime import date
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.trunking.v1.trunk.credential_list import CredentialListList
from twilio.rest.trunking.v1.trunk.ip_access_control_list import IpAccessControlListList
from twilio.rest.trunking.v1.trunk.origination_url import OriginationUrlList
from twilio.rest.trunking.v1.trunk.phone_number import PhoneNumberList
from twilio.rest.trunking.v1.trunk.recording import RecordingList


class TrunkList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the TrunkList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.trunking.v1.trunk.TrunkList
        :rtype: twilio.rest.trunking.v1.trunk.TrunkList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Trunks".format(**self._solution)

    def create(
        self,
        friendly_name=values.unset,
        domain_name=values.unset,
        disaster_recovery_url=values.unset,
        disaster_recovery_method=values.unset,
        transfer_mode=values.unset,
        secure=values.unset,
        cnam_lookup_enabled=values.unset,
        transfer_caller_id=values.unset,
    ):
        """
        Create the TrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param str disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param str disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param TrunkInstance.TransferSetting transfer_mode:
        :param bool secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param TrunkInstance.TransferCallerId transfer_caller_id:

        :returns: The created TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DomainName": domain_name,
                "DisasterRecoveryUrl": disaster_recovery_url,
                "DisasterRecoveryMethod": disaster_recovery_method,
                "TransferMode": transfer_mode,
                "Secure": secure,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "TransferCallerId": transfer_caller_id,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(self._version, payload)

    def stream(self, limit=None, page_size=None):
        """
        Streams TrunkInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trunking.v1.trunk.TrunkInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists TrunkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.TrunkInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of TrunkInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TrunkPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TrunkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TrunkPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a TrunkContext

        :param sid: The unique string that we created to identify the OriginationUrl resource to update.

        :returns: twilio.rest.trunking.v1.trunk.TrunkContext
        :rtype: twilio.rest.trunking.v1.trunk.TrunkContext
        """
        return TrunkContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a TrunkContext

        :param sid: The unique string that we created to identify the OriginationUrl resource to update.

        :returns: twilio.rest.trunking.v1.trunk.TrunkContext
        :rtype: twilio.rest.trunking.v1.trunk.TrunkContext
        """
        return TrunkContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Trunking.V1.TrunkList>"


class TrunkPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the TrunkPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trunking.v1.trunk.TrunkPage
        :rtype: twilio.rest.trunking.v1.trunk.TrunkPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TrunkInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trunking.v1.trunk.TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkInstance
        """
        return TrunkInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Trunking.V1.TrunkPage>"


class TrunkInstance(InstanceResource):
    class TransferCallerId(object):
        FROM_TRANSFEREE = "from-transferee"
        FROM_TRANSFEROR = "from-transferor"

    class TransferSetting(object):
        DISABLE_ALL = "disable-all"
        ENABLE_ALL = "enable-all"
        SIP_ONLY = "sip-only"

    def __init__(self, version, payload, sid: str = None):
        """
        Initialize the TrunkInstance

        :returns: twilio.rest.trunking.v1.trunk.TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "domain_name": payload.get("domain_name"),
            "disaster_recovery_method": payload.get("disaster_recovery_method"),
            "disaster_recovery_url": payload.get("disaster_recovery_url"),
            "friendly_name": payload.get("friendly_name"),
            "secure": payload.get("secure"),
            "recording": payload.get("recording"),
            "transfer_mode": payload.get("transfer_mode"),
            "transfer_caller_id": payload.get("transfer_caller_id"),
            "cnam_lookup_enabled": payload.get("cnam_lookup_enabled"),
            "auth_type": payload.get("auth_type"),
            "auth_type_set": payload.get("auth_type_set"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "sid": payload.get("sid"),
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

        :returns: TrunkContext for this TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkContext
        """
        if self._context is None:
            self._context = TrunkContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Trunk resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def domain_name(self):
        """
        :returns: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :rtype: str
        """
        return self._properties["domain_name"]

    @property
    def disaster_recovery_method(self):
        """
        :returns: The HTTP method we use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties["disaster_recovery_method"]

    @property
    def disaster_recovery_url(self):
        """
        :returns: The URL we call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from this URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :rtype: str
        """
        return self._properties["disaster_recovery_url"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def secure(self):
        """
        :returns: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :rtype: bool
        """
        return self._properties["secure"]

    @property
    def recording(self):
        """
        :returns: The recording settings for the trunk. Can be: `do-not-record`, `record-from-ringing`, `record-from-answer`. If set to `record-from-ringing` or `record-from-answer`, all calls going through the trunk will be recorded. The only way to change recording parameters is on a sub-resource of a Trunk after it has been created. e.g.`/Trunks/[Trunk_SID]/Recording -XPOST -d'Mode=record-from-answer'`. See [Recording](https://www.twilio.com/docs/sip-trunking#recording) for more information.
        :rtype: dict
        """
        return self._properties["recording"]

    @property
    def transfer_mode(self):
        """
        :returns:
        :rtype: TrunkInstance.TransferSetting
        """
        return self._properties["transfer_mode"]

    @property
    def transfer_caller_id(self):
        """
        :returns:
        :rtype: TrunkInstance.TransferCallerId
        """
        return self._properties["transfer_caller_id"]

    @property
    def cnam_lookup_enabled(self):
        """
        :returns: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :rtype: bool
        """
        return self._properties["cnam_lookup_enabled"]

    @property
    def auth_type(self):
        """
        :returns: The types of authentication mapped to the domain. Can be: `IP_ACL` and `CREDENTIAL_LIST`. If both are mapped, the values are returned in a comma delimited list. If empty, the domain will not receive any traffic.
        :rtype: str
        """
        return self._properties["auth_type"]

    @property
    def auth_type_set(self):
        """
        :returns: Reserved.
        :rtype: list[str]
        """
        return self._properties["auth_type_set"]

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
    def sid(self):
        """
        :returns: The unique string that we created to identify the Trunk resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the TrunkInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkInstance
        """
        return self._proxy.fetch()

    def update(
        self,
        friendly_name=values.unset,
        domain_name=values.unset,
        disaster_recovery_url=values.unset,
        disaster_recovery_method=values.unset,
        transfer_mode=values.unset,
        secure=values.unset,
        cnam_lookup_enabled=values.unset,
        transfer_caller_id=values.unset,
    ):
        """
        Update the TrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param str disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param str disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param TrunkInstance.TransferSetting transfer_mode:
        :param bool secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param TrunkInstance.TransferCallerId transfer_caller_id:

        :returns: The updated TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            domain_name=domain_name,
            disaster_recovery_url=disaster_recovery_url,
            disaster_recovery_method=disaster_recovery_method,
            transfer_mode=transfer_mode,
            secure=secure,
            cnam_lookup_enabled=cnam_lookup_enabled,
            transfer_caller_id=transfer_caller_id,
        )

    @property
    def credentials_lists(self):
        """
        Access the credentials_lists

        :returns: twilio.rest.trunking.v1.trunk.CredentialListList
        :rtype: twilio.rest.trunking.v1.trunk.CredentialListList
        """
        return self._proxy.credentials_lists

    @property
    def ip_access_control_lists(self):
        """
        Access the ip_access_control_lists

        :returns: twilio.rest.trunking.v1.trunk.IpAccessControlListList
        :rtype: twilio.rest.trunking.v1.trunk.IpAccessControlListList
        """
        return self._proxy.ip_access_control_lists

    @property
    def origination_urls(self):
        """
        Access the origination_urls

        :returns: twilio.rest.trunking.v1.trunk.OriginationUrlList
        :rtype: twilio.rest.trunking.v1.trunk.OriginationUrlList
        """
        return self._proxy.origination_urls

    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.trunking.v1.trunk.PhoneNumberList
        :rtype: twilio.rest.trunking.v1.trunk.PhoneNumberList
        """
        return self._proxy.phone_numbers

    @property
    def recordings(self):
        """
        Access the recordings

        :returns: twilio.rest.trunking.v1.trunk.RecordingList
        :rtype: twilio.rest.trunking.v1.trunk.RecordingList
        """
        return self._proxy.recordings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.TrunkInstance {}>".format(context)


class TrunkContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the TrunkContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that we created to identify the OriginationUrl resource to update.

        :returns: twilio.rest.trunking.v1.trunk.TrunkContext
        :rtype: twilio.rest.trunking.v1.trunk.TrunkContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Trunks/{sid}".format(**self._solution)

        self._credentials_lists = None
        self._ip_access_control_lists = None
        self._origination_urls = None
        self._phone_numbers = None
        self._recordings = None

    def delete(self):
        """
        Deletes the TrunkInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TrunkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        domain_name=values.unset,
        disaster_recovery_url=values.unset,
        disaster_recovery_method=values.unset,
        transfer_mode=values.unset,
        secure=values.unset,
        cnam_lookup_enabled=values.unset,
        transfer_caller_id=values.unset,
    ):
        """
        Update the TrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param str disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param str disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param TrunkInstance.TransferSetting transfer_mode:
        :param bool secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param TrunkInstance.TransferCallerId transfer_caller_id:

        :returns: The updated TrunkInstance
        :rtype: twilio.rest.trunking.v1.trunk.TrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DomainName": domain_name,
                "DisasterRecoveryUrl": disaster_recovery_url,
                "DisasterRecoveryMethod": disaster_recovery_method,
                "TransferMode": transfer_mode,
                "Secure": secure,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "TransferCallerId": transfer_caller_id,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def credentials_lists(self):
        """
        Access the credentials_lists

        :returns: twilio.rest.trunking.v1.trunk.CredentialListList
        :rtype: twilio.rest.trunking.v1.trunk.CredentialListList
        """
        if self._credentials_lists is None:
            self._credentials_lists = CredentialListList(
                self._version,
                self._solution["sid"],
            )
        return self._credentials_lists

    @property
    def ip_access_control_lists(self):
        """
        Access the ip_access_control_lists

        :returns: twilio.rest.trunking.v1.trunk.IpAccessControlListList
        :rtype: twilio.rest.trunking.v1.trunk.IpAccessControlListList
        """
        if self._ip_access_control_lists is None:
            self._ip_access_control_lists = IpAccessControlListList(
                self._version,
                self._solution["sid"],
            )
        return self._ip_access_control_lists

    @property
    def origination_urls(self):
        """
        Access the origination_urls

        :returns: twilio.rest.trunking.v1.trunk.OriginationUrlList
        :rtype: twilio.rest.trunking.v1.trunk.OriginationUrlList
        """
        if self._origination_urls is None:
            self._origination_urls = OriginationUrlList(
                self._version,
                self._solution["sid"],
            )
        return self._origination_urls

    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.trunking.v1.trunk.PhoneNumberList
        :rtype: twilio.rest.trunking.v1.trunk.PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(
                self._version,
                self._solution["sid"],
            )
        return self._phone_numbers

    @property
    def recordings(self):
        """
        Access the recordings

        :returns: twilio.rest.trunking.v1.trunk.RecordingList
        :rtype: twilio.rest.trunking.v1.trunk.RecordingList
        """
        if self._recordings is None:
            self._recordings = RecordingList(
                self._version,
                self._solution["sid"],
            )
        return self._recordings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.TrunkContext {}>".format(context)
