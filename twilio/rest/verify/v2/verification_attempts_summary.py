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



class VerificationAttemptsSummaryList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the VerificationAttemptsSummaryList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryList
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self):
        """
        Constructs a VerificationAttemptsSummaryContext
        
        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        return VerificationAttemptsSummaryContext(self._version)

    def __call__(self):
        """
        Constructs a VerificationAttemptsSummaryContext
        
        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        return VerificationAttemptsSummaryContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryList>'

class VerificationAttemptsSummaryContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the VerificationAttemptsSummaryContext

        :param Version version: Version that contains the resource
        

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/Attempts/Summary'.format(**self._solution)
        
    
    def fetch(self, verify_service_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, country=values.unset, channel=values.unset, destination_prefix=values.unset):
        """
        Fetch the VerificationAttemptsSummaryInstance
        
        :params str verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
        :params datetime date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in RFC 2822 format.
        :params datetime date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in RFC 2822 format.
        :params str country: Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
        :params VerificationAttemptsSummaryInstance.Channels channel: Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS` and `CALL`
        :params str destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.

        :returns: The fetched VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        """
        
        data = values.of({ 
            'VerifyServiceSid': verify_service_sid,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'Country': country,
            'Channel': channel,
            'DestinationPrefix': destination_prefix,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return VerificationAttemptsSummaryInstance(
            self._version,
            payload,
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryContext {}>'.format(context)

class VerificationAttemptsSummaryInstance(InstanceResource):

    class Channels(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"

    def __init__(self, version, payload):
        """
        Initialize the VerificationAttemptsSummaryInstance
        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        """
        super().__init__(version)

        self._properties = { 
            'total_attempts': deserialize.integer(payload.get('total_attempts')),
            'total_converted': deserialize.integer(payload.get('total_converted')),
            'total_unconverted': deserialize.integer(payload.get('total_unconverted')),
            'conversion_rate_percentage': deserialize.decimal(payload.get('conversion_rate_percentage')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: VerificationAttemptsSummaryContext for this VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        if self._context is None:
            self._context = VerificationAttemptsSummaryContext(self._version,)
        return self._context
    
    @property
    def total_attempts(self):
        """
        :returns: Total of attempts made according to the provided filters
        :rtype: int
        """
        return self._properties['total_attempts']
    
    @property
    def total_converted(self):
        """
        :returns: Total of  attempts made that were confirmed by the end user, according to the provided filters.
        :rtype: int
        """
        return self._properties['total_converted']
    
    @property
    def total_unconverted(self):
        """
        :returns: Total of attempts made that were not confirmed by the end user, according to the provided filters.
        :rtype: int
        """
        return self._properties['total_unconverted']
    
    @property
    def conversion_rate_percentage(self):
        """
        :returns: Percentage of the confirmed messages over the total, defined by (total_converted/total_attempts)*100. 
        :rtype: float
        """
        return self._properties['conversion_rate_percentage']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, verify_service_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, country=values.unset, channel=values.unset, destination_prefix=values.unset):
        """
        Fetch the VerificationAttemptsSummaryInstance
        
        :params str verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
        :params datetime date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in RFC 2822 format.
        :params datetime date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in RFC 2822 format.
        :params str country: Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
        :params VerificationAttemptsSummaryInstance.Channels channel: Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS` and `CALL`
        :params str destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.

        :returns: The fetched VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        """
        return self._proxy.fetch(verify_service_sid=verify_service_sid, date_created_after=date_created_after, date_created_before=date_created_before, country=country, channel=channel, destination_prefix=destination_prefix, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryInstance {}>'.format(context)


