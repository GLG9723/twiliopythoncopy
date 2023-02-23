"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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
from twilio.rest.verify.v2.service.access_token import AccessTokenList
from twilio.rest.verify.v2.service.entity import EntityList
from twilio.rest.verify.v2.service.messaging_configuration import MessagingConfigurationList
from twilio.rest.verify.v2.service.rate_limit import RateLimitList
from twilio.rest.verify.v2.service.verification import VerificationList
from twilio.rest.verify.v2.service.verification_check import VerificationCheckList
from twilio.rest.verify.v2.service.webhook import WebhookList


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.verify.v2.service.ServiceList
        :rtype: twilio.rest.verify.v2.service.ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, code_length=values.unset, lookup_enabled=values.unset, skip_sms_to_landlines=values.unset, dtmf_input_required=values.unset, tts_name=values.unset, psd2_enabled=values.unset, do_not_share_warning_enabled=values.unset, custom_code_enabled=values.unset, push_include_date=values.unset, push_apn_credential_sid=values.unset, push_fcm_credential_sid=values.unset, totp_issuer=values.unset, totp_time_step=values.unset, totp_code_length=values.unset, totp_skew=values.unset, default_template_sid=values.unset):
        """
        Create the ServiceInstance

        :param str friendly_name: A descriptive string that you create to describe the verification service. It can be up to 30 characters long. **This value should not contain PII.**
        :param int code_length: The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
        :param bool lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone number.
        :param bool skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
        :param bool dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call.
        :param str tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
        :param bool psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
        :param bool do_not_share_warning_enabled: Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: `Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code`
        :param bool custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
        :param bool push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the one found in `date_created`, please use that one instead.
        :param str push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
        :param str push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
        :param str totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
        :param int totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
        :param int totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
        :param int totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
        :param str default_template_sid: The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
        
        :returns: The created ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'CodeLength': code_length,
            'LookupEnabled': lookup_enabled,
            'SkipSmsToLandlines': skip_sms_to_landlines,
            'DtmfInputRequired': dtmf_input_required,
            'TtsName': tts_name,
            'Psd2Enabled': psd2_enabled,
            'DoNotShareWarningEnabled': do_not_share_warning_enabled,
            'CustomCodeEnabled': custom_code_enabled,
            'Push.IncludeDate': push_include_date,
            'Push.ApnCredentialSid': push_apn_credential_sid,
            'Push.FcmCredentialSid': push_fcm_credential_sid,
            'Totp.Issuer': totp_issuer,
            'Totp.TimeStep': totp_time_step,
            'Totp.CodeLength': totp_code_length,
            'Totp.Skew': totp_skew,
            'DefaultTemplateSid': default_template_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.ServiceInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServicePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ServicePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        
        :returns: twilio.rest.verify.v2.service.ServiceContext
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        
        :returns: twilio.rest.verify.v2.service.ServiceContext
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.ServiceList>'










class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.service.ServicePage
        :rtype: twilio.rest.verify.v2.service.ServicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.ServicePage>'




class ServiceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.

        :returns: twilio.rest.verify.v2.service.ServiceContext
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Services/{sid}'.format(**self._solution)
        
        self._access_tokens = None
        self._entities = None
        self._messaging_configurations = None
        self._rate_limits = None
        self._verifications = None
        self._verification_checks = None
        self._webhooks = None
    
    def delete(self):
        """
        Deletes the ServiceInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, code_length=values.unset, lookup_enabled=values.unset, skip_sms_to_landlines=values.unset, dtmf_input_required=values.unset, tts_name=values.unset, psd2_enabled=values.unset, do_not_share_warning_enabled=values.unset, custom_code_enabled=values.unset, push_include_date=values.unset, push_apn_credential_sid=values.unset, push_fcm_credential_sid=values.unset, totp_issuer=values.unset, totp_time_step=values.unset, totp_code_length=values.unset, totp_skew=values.unset, default_template_sid=values.unset):
        """
        Update the ServiceInstance
        
        :params str friendly_name: A descriptive string that you create to describe the verification service. It can be up to 30 characters long. **This value should not contain PII.**
        :params int code_length: The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
        :params bool lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone number.
        :params bool skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
        :params bool dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call.
        :params str tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
        :params bool psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
        :params bool do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.**
        :params bool custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
        :params bool push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter.
        :params str push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
        :params str push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
        :params str totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI.
        :params int totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
        :params int totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
        :params int totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
        :params str default_template_sid: The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'CodeLength': code_length,
            'LookupEnabled': lookup_enabled,
            'SkipSmsToLandlines': skip_sms_to_landlines,
            'DtmfInputRequired': dtmf_input_required,
            'TtsName': tts_name,
            'Psd2Enabled': psd2_enabled,
            'DoNotShareWarningEnabled': do_not_share_warning_enabled,
            'CustomCodeEnabled': custom_code_enabled,
            'Push.IncludeDate': push_include_date,
            'Push.ApnCredentialSid': push_apn_credential_sid,
            'Push.FcmCredentialSid': push_fcm_credential_sid,
            'Totp.Issuer': totp_issuer,
            'Totp.TimeStep': totp_time_step,
            'Totp.CodeLength': totp_code_length,
            'Totp.Skew': totp_skew,
            'DefaultTemplateSid': default_template_sid,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def access_tokens(self):
        """
        Access the access_tokens

        :returns: twilio.rest.verify.v2.service.AccessTokenList
        :rtype: twilio.rest.verify.v2.service.AccessTokenList
        """
        if self._access_tokens is None:
            self._access_tokens = AccessTokenList(self._version, self._solution['sid'],
            )
        return self._access_tokens
    
    @property
    def entities(self):
        """
        Access the entities

        :returns: twilio.rest.verify.v2.service.EntityList
        :rtype: twilio.rest.verify.v2.service.EntityList
        """
        if self._entities is None:
            self._entities = EntityList(self._version, self._solution['sid'],
            )
        return self._entities
    
    @property
    def messaging_configurations(self):
        """
        Access the messaging_configurations

        :returns: twilio.rest.verify.v2.service.MessagingConfigurationList
        :rtype: twilio.rest.verify.v2.service.MessagingConfigurationList
        """
        if self._messaging_configurations is None:
            self._messaging_configurations = MessagingConfigurationList(self._version, self._solution['sid'],
            )
        return self._messaging_configurations
    
    @property
    def rate_limits(self):
        """
        Access the rate_limits

        :returns: twilio.rest.verify.v2.service.RateLimitList
        :rtype: twilio.rest.verify.v2.service.RateLimitList
        """
        if self._rate_limits is None:
            self._rate_limits = RateLimitList(self._version, self._solution['sid'],
            )
        return self._rate_limits
    
    @property
    def verifications(self):
        """
        Access the verifications

        :returns: twilio.rest.verify.v2.service.VerificationList
        :rtype: twilio.rest.verify.v2.service.VerificationList
        """
        if self._verifications is None:
            self._verifications = VerificationList(self._version, self._solution['sid'],
            )
        return self._verifications
    
    @property
    def verification_checks(self):
        """
        Access the verification_checks

        :returns: twilio.rest.verify.v2.service.VerificationCheckList
        :rtype: twilio.rest.verify.v2.service.VerificationCheckList
        """
        if self._verification_checks is None:
            self._verification_checks = VerificationCheckList(self._version, self._solution['sid'],
            )
        return self._verification_checks
    
    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.verify.v2.service.WebhookList
        :rtype: twilio.rest.verify.v2.service.WebhookList
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(self._version, self._solution['sid'],
            )
        return self._webhooks
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.ServiceContext {}>'.format(context)

class ServiceInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the ServiceInstance
        :returns: twilio.rest.verify.v2.service.ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'code_length': deserialize.integer(payload.get('code_length')),
            'lookup_enabled': payload.get('lookup_enabled'),
            'psd2_enabled': payload.get('psd2_enabled'),
            'skip_sms_to_landlines': payload.get('skip_sms_to_landlines'),
            'dtmf_input_required': payload.get('dtmf_input_required'),
            'tts_name': payload.get('tts_name'),
            'do_not_share_warning_enabled': payload.get('do_not_share_warning_enabled'),
            'custom_code_enabled': payload.get('custom_code_enabled'),
            'push': payload.get('push'),
            'totp': payload.get('totp'),
            'default_template_sid': payload.get('default_template_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Service resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the verification service. **This value should not contain PII.**
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def code_length(self):
        """
        :returns: The length of the verification code to generate.
        :rtype: int
        """
        return self._properties['code_length']
    
    @property
    def lookup_enabled(self):
        """
        :returns: Whether to perform a lookup with each verification started and return info about the phone number.
        :rtype: bool
        """
        return self._properties['lookup_enabled']
    
    @property
    def psd2_enabled(self):
        """
        :returns: Whether to pass PSD2 transaction parameters when starting a verification.
        :rtype: bool
        """
        return self._properties['psd2_enabled']
    
    @property
    def skip_sms_to_landlines(self):
        """
        :returns: Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
        :rtype: bool
        """
        return self._properties['skip_sms_to_landlines']
    
    @property
    def dtmf_input_required(self):
        """
        :returns: Whether to ask the user to press a number before delivering the verify code in a phone call.
        :rtype: bool
        """
        return self._properties['dtmf_input_required']
    
    @property
    def tts_name(self):
        """
        :returns: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
        :rtype: str
        """
        return self._properties['tts_name']
    
    @property
    def do_not_share_warning_enabled(self):
        """
        :returns: Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: `Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code`
        :rtype: bool
        """
        return self._properties['do_not_share_warning_enabled']
    
    @property
    def custom_code_enabled(self):
        """
        :returns: Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
        :rtype: bool
        """
        return self._properties['custom_code_enabled']
    
    @property
    def push(self):
        """
        :returns: Configurations for the Push factors (channel) created under this Service.
        :rtype: dict
        """
        return self._properties['push']
    
    @property
    def totp(self):
        """
        :returns: Configurations for the TOTP factors (channel) created under this Service.
        :rtype: dict
        """
        return self._properties['totp']
    
    @property
    def default_template_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['default_template_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the ServiceInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, code_length=values.unset, lookup_enabled=values.unset, skip_sms_to_landlines=values.unset, dtmf_input_required=values.unset, tts_name=values.unset, psd2_enabled=values.unset, do_not_share_warning_enabled=values.unset, custom_code_enabled=values.unset, push_include_date=values.unset, push_apn_credential_sid=values.unset, push_fcm_credential_sid=values.unset, totp_issuer=values.unset, totp_time_step=values.unset, totp_code_length=values.unset, totp_skew=values.unset, default_template_sid=values.unset):
        """
        Update the ServiceInstance
        
        :params str friendly_name: A descriptive string that you create to describe the verification service. It can be up to 30 characters long. **This value should not contain PII.**
        :params int code_length: The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
        :params bool lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone number.
        :params bool skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
        :params bool dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call.
        :params str tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
        :params bool psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
        :params bool do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.**
        :params bool custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
        :params bool push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter.
        :params str push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
        :params str push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
        :params str totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI.
        :params int totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
        :params int totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
        :params int totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
        :params str default_template_sid: The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        return self._proxy.update(friendly_name=friendly_name, code_length=code_length, lookup_enabled=lookup_enabled, skip_sms_to_landlines=skip_sms_to_landlines, dtmf_input_required=dtmf_input_required, tts_name=tts_name, psd2_enabled=psd2_enabled, do_not_share_warning_enabled=do_not_share_warning_enabled, custom_code_enabled=custom_code_enabled, push_include_date=push_include_date, push_apn_credential_sid=push_apn_credential_sid, push_fcm_credential_sid=push_fcm_credential_sid, totp_issuer=totp_issuer, totp_time_step=totp_time_step, totp_code_length=totp_code_length, totp_skew=totp_skew, default_template_sid=default_template_sid, )
    
    @property
    def access_tokens(self):
        """
        Access the access_tokens

        :returns: twilio.rest.verify.v2.service.AccessTokenList
        :rtype: twilio.rest.verify.v2.service.AccessTokenList
        """
        return self._proxy.access_tokens
    
    @property
    def entities(self):
        """
        Access the entities

        :returns: twilio.rest.verify.v2.service.EntityList
        :rtype: twilio.rest.verify.v2.service.EntityList
        """
        return self._proxy.entities
    
    @property
    def messaging_configurations(self):
        """
        Access the messaging_configurations

        :returns: twilio.rest.verify.v2.service.MessagingConfigurationList
        :rtype: twilio.rest.verify.v2.service.MessagingConfigurationList
        """
        return self._proxy.messaging_configurations
    
    @property
    def rate_limits(self):
        """
        Access the rate_limits

        :returns: twilio.rest.verify.v2.service.RateLimitList
        :rtype: twilio.rest.verify.v2.service.RateLimitList
        """
        return self._proxy.rate_limits
    
    @property
    def verifications(self):
        """
        Access the verifications

        :returns: twilio.rest.verify.v2.service.VerificationList
        :rtype: twilio.rest.verify.v2.service.VerificationList
        """
        return self._proxy.verifications
    
    @property
    def verification_checks(self):
        """
        Access the verification_checks

        :returns: twilio.rest.verify.v2.service.VerificationCheckList
        :rtype: twilio.rest.verify.v2.service.VerificationCheckList
        """
        return self._proxy.verification_checks
    
    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.verify.v2.service.WebhookList
        :rtype: twilio.rest.verify.v2.service.WebhookList
        """
        return self._proxy.webhooks
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.ServiceInstance {}>'.format(context)


