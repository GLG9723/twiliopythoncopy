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
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Attempts/Summary'
        
    
    def fetch(self, verify_service_sid, date_created_after, date_created_before, country, channel, destination_prefix):
        
        """
        Fetch the VerificationAttemptsSummaryInstance

        :returns: The fetched VerificationAttemptsSummaryInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return VerificationAttemptsSummaryInstance(self._version, payload, )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryContext>'



class VerificationAttemptsSummaryInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'total_attempts' : payload.get('total_attempts'),
            'total_converted' : payload.get('total_converted'),
            'total_unconverted' : payload.get('total_unconverted'),
            'conversion_rate_percentage' : payload.get('conversion_rate_percentage'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = VerificationAttemptsSummaryContext(
                self._version,
                
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryInstance {}>'.format(context)



