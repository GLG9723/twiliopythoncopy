"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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

from twilio.rest.add_on_result.payload import PayloadListInstance


class AddOnResultContext(InstanceContext):
    def __init__(self, version: V2010, account_sid: str, reference_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'reference_sid': reference_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/Recordings/${reference_sid}/AddOnResults/${sid}.json'
        
        self._payloads = None
    
    def delete(self):
        
        
        """
        Deletes the AddOnResultInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the AddOnResultInstance

        :returns: The fetched AddOnResultInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return AddOnResultInstance(
            self._version,
            payload,
            account_sidreference_sidsid=self._solution['account_sid''reference_sid''sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AddOnResultContext>'



class AddOnResultInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, reference_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'status' : payload.get('status'),
            'add_on_sid' : payload.get('add_on_sid'),
            'add_on_configuration_sid' : payload.get('add_on_configuration_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'date_completed' : payload.get('date_completed'),
            'reference_sid' : payload.get('reference_sid'),
            'subresource_uris' : payload.get('subresource_uris'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid']'reference_sid': reference_sid or self._properties['reference_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AddOnResultContext(
                self._version,
                account_sid=self._solution['account_sid'],reference_sid=self._solution['reference_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def payloads(self):
        return self._proxy.payloads
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AddOnResultInstance {}>'.format(context)



class AddOnResultListInstance(ListResource):
    def __init__(self, version: V2010, account_sid: str, reference_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'reference_sid': reference_sid,  }
        self._uri = '/Accounts/${account_sid}/Recordings/${reference_sid}/AddOnResults.json'
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return AddOnResultPage(self._version, payload, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AddOnResultListInstance>'

