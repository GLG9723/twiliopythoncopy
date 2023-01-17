"""
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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

# 


class AnnotationContext(InstanceContext):
    def __init__(self, version: Version, call_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'call_sid': call_sid,  }
        self._uri = '/Voice/${call_sid}/Annotation'
        
    
    def fetch(self):
        
        """
        Fetch the AnnotationInstance

        :returns: The fetched AnnotationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AnnotationInstance(self._version, payload, call_sid=self._solution['call_sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return AnnotationInstance(self._version, payload, call_sid=self._solution['call_sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AnnotationContext>'



class AnnotationInstance(InstanceResource):
    def __init__(self, version, payload, call_sid: str):
        super().__init__(version)
        self._properties = { 
            'call_sid' : payload.get('call_sid'),
            'account_sid' : payload.get('account_sid'),
            'answered_by' : payload.get('answered_by'),
            'connectivity_issue' : payload.get('connectivity_issue'),
            'quality_issues' : payload.get('quality_issues'),
            'spam' : payload.get('spam'),
            'call_score' : payload.get('call_score'),
            'comment' : payload.get('comment'),
            'incident' : payload.get('incident'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'call_sid': call_sid or self._properties['call_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AnnotationContext(
                self._version,
                call_sid=self._solution['call_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.AnnotationInstance {}>'.format(context)



class AnnotationListInstance(ListResource):
    def __init__(self, version: Version, call_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'call_sid': call_sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AnnotationListInstance>'

