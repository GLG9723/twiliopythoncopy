"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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

from twilio.base.page import Page




class EventTypeContext(InstanceContext):
    def __init__(self, version: V1, type: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'type': type,  }
        self._uri = '/Types/${type}'
        
    
    def fetch(self):
        
        """
        Fetch the EventTypeInstance

        :returns: The fetched EventTypeInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return EventTypeInstance(
            self._version,
            payload,
            type=self._solution['type'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.EventTypeContext>'



class EventTypeInstance(InstanceResource):
    def __init__(self, version, payload, type: str):
        super().__init__(version)
        self._properties = { 
            'type' : payload.get('type'),
            'schema_id' : payload.get('schema_id'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'description' : payload.get('description'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'type': type or self._properties['type']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = EventTypeContext(
                self._version,
                type=self._solution['type'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.EventTypeInstance {}>'.format(context)



class EventTypeListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Types'
        
    
    def page(self, schema_id, page_size):
        
        data = values.of({
            'schema_id': schema_id,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return EventTypePage(self._version, payload, )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.EventTypeListInstance>'

