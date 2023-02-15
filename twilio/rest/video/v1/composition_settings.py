"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
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



class CompositionSettingsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CompositionSettingsList
        :param Version version: Version that contains the resource
        
        :returns: twilio.video.v1.composition_settings..CompositionSettingsList
        :rtype: twilio.video.v1.composition_settings..CompositionSettingsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''.format(**self._solution)


    
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionSettingsList>'


class CompositionSettingsContext(InstanceContext):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/CompositionSettings/Default'
        
    
    def create(self, body):
        
        

        
    
    def fetch(self):
        
        """
        Fetch the CompositionSettingsInstance

        :returns: The fetched CompositionSettingsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CompositionSettingsInstance(self._version, payload, )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionSettingsContext>'



class CompositionSettingsInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'aws_credentials_sid' : payload.get('aws_credentials_sid'),
            'aws_s3_url' : payload.get('aws_s3_url'),
            'aws_storage_enabled' : payload.get('aws_storage_enabled'),
            'encryption_key_sid' : payload.get('encryption_key_sid'),
            'encryption_enabled' : payload.get('encryption_enabled'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CompositionSettingsContext(
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
        return '<Twilio.Video.V1.CompositionSettingsInstance {}>'.format(context)



