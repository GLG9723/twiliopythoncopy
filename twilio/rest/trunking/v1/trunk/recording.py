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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource




class RecordingContext(InstanceContext):
    def __init__(self, version: V1, trunk_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid,  }
        self._uri = '/Trunks/${trunk_sid}/Recording'
        
    
    def fetch(self):
        
        """
        Fetch the RecordingInstance

        :returns: The fetched RecordingInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return RecordingInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
        )
        
        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return RecordingInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'], )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.RecordingContext>'



class RecordingInstance(InstanceResource):
    def __init__(self, version, payload, trunk_sid: str):
        super().__init__(version)
        self._properties = { 
            'mode' : payload.get('mode'),
            'trim' : payload.get('trim'),
        }

        self._context = None
        self._solution = {
            'trunk_sid': trunk_sid or self._properties['trunk_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                trunk_sid=self._solution['trunk_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.RecordingInstance {}>'.format(context)



class RecordingListInstance(ListResource):
    def __init__(self, version: V1, trunk_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.RecordingListInstance>'

