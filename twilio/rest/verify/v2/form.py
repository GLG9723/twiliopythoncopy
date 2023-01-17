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

# 


class FormContext(InstanceContext):
    def __init__(self, version: Version, form_type: FormFormTypes):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'form_type': form_type,  }
        self._uri = '/Forms/${form_type}'
        
    
    def fetch(self):
        
        """
        Fetch the FormInstance

        :returns: The fetched FormInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FormInstance(self._version, payload, form_type=self._solution['form_type'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.FormContext>'



class FormInstance(InstanceResource):
    def __init__(self, version, payload, form_type: FormFormTypes):
        super().__init__(version)
        self._properties = { 
            'form_type' : payload.get('form_type'),
            'forms' : payload.get('forms'),
            'form_meta' : payload.get('form_meta'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'form_type': form_type or self._properties['form_type'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = FormContext(
                self._version,
                form_type=self._solution['form_type'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.FormInstance {}>'.format(context)



class FormListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.FormListInstance>'

