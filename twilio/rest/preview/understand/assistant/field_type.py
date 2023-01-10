"""
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

from twilio.base.page import Page

from twilio.rest.field_type.field_value import FieldValueListInstance


class FieldTypeContext(InstanceContext):
    def __init__(self, version: Understand, assistant_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(FieldTypeContextList, self).__init__(version)

        # Path Solution
        self._solution = { assistant_sid, sid,  }
        self._uri = '/Assistants/${assistant_sid}/FieldTypes/${sid}'
        
        self._field_values = None
        
        def delete(self):
            
            
            """
            Deletes the FieldTypeInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the FieldTypeInstance

            :returns: The fetched FieldTypeInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return FieldTypeInstance(
                self._version,
                payload,
                assistant_sidsid=self._solution['assistant_sid''sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return FieldTypeInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Understand.FieldTypeContext>'



class FieldTypeInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, sid: str):
        super(FieldTypeInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'friendly_name' = payload.get('friendly_name'),
            'links' = payload.get('links'),
            'assistant_sid' = payload.get('assistant_sid'),
            'sid' = payload.get('sid'),
            'unique_name' = payload.get('unique_name'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = FieldTypeContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def field_values(self):
        return self._proxy.field_values
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.Understand.FieldTypeInstance {}>'.format(context)



class FieldTypeListInstance(ListResource):
    def __init__(self, version: Understand, assistant_sid: str):
        # TODO: needs autogenerated docs
        super(FieldTypeListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { assistant_sid,  }
        self._uri = '/Assistants/${assistant_sid}/FieldTypes'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return FieldTypeInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return FieldTypePage(self._version, payload, assistant_sid=self._solution['assistant_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Understand.FieldTypeListInstance>'

