"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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

# 


class FieldValueContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, field_type_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'field_type_sid': field_type_sid, 'sid': sid,  }
        self._uri = '/Assistants/${assistant_sid}/FieldTypes/${field_type_sid}/FieldValues/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the FieldValueInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the FieldValueInstance

        :returns: The fetched FieldValueInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FieldValueInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], field_type_sid=self._solution['field_type_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.FieldValueContext>'



class FieldValueInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, field_type_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'field_type_sid' : payload.get('field_type_sid'),
            'language' : payload.get('language'),
            'assistant_sid' : payload.get('assistant_sid'),
            'sid' : payload.get('sid'),
            'value' : payload.get('value'),
            'url' : payload.get('url'),
            'synonym_of' : payload.get('synonym_of'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid'],'field_type_sid': field_type_sid or self._properties['field_type_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = FieldValueContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],field_type_sid=self._solution['field_type_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.FieldValueInstance {}>'.format(context)



class FieldValueListInstance(ListResource):
    def __init__(self, version: Version, assistant_sid: str, field_type_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'field_type_sid': field_type_sid,  }
        self._uri = '/Assistants/${assistant_sid}/FieldTypes/${field_type_sid}/FieldValues'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return FieldValueInstance(self._version, payload, assistant_sid=self._solution['assistant_sid']field_type_sid=self._solution['field_type_sid'])
        
    """
    
    """
    def page(self, language, page_size):
        
        data = values.of({
            'language': language,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return FieldValuePage(self._version, payload, assistant_sid=self._solution['assistant_sid'], field_type_sid=self._solution['field_type_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.FieldValueListInstance>'

