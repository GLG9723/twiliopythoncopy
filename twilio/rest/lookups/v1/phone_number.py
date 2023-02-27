"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Lookups
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



class PhoneNumberList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberList
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number to lookup in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        
        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number to lookup in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        
        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups.V1.PhoneNumberList>'

class PhoneNumberContext(InstanceContext):

    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param phone_number: The phone number to lookup in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'phone_number': phone_number,
        }
        self._uri = '/PhoneNumbers/{phone_number}'.format(**self._solution)
        
    
    def fetch(self, country_code=values.unset, type=values.unset, add_ons=values.unset, add_ons_data=values.unset):
        """
        Fetch the PhoneNumberInstance
        
        :params str country_code: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the phone number to fetch. This is used to specify the country when the phone number is provided in a national format.
        :params list[str] type: The type of information to return. Can be: `carrier` or `caller-name`. The default is null.  Carrier information costs $0.005 per phone number looked up.  Caller Name information is currently available only in the US and costs $0.01 per phone number looked up.  To retrieve both types on information, specify this parameter twice; once with `carrier` and once with `caller-name` as the value.
        :params list[str] add_ons: The `unique_name` of an Add-on you would like to invoke. Can be the `unique_name` of an Add-on that is installed on your account. You can specify multiple instances of this parameter to invoke multiple Add-ons. For more information about  Add-ons, see the [Add-ons documentation](https://www.twilio.com/docs/add-ons).
        :params dict add_ons_data: Data specific to the add-on you would like to invoke. The content and format of this value depends on the add-on.

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        
        data = values.of({ 
            'CountryCode': country_code,
            'Type': serialize.map(type, lambda e: e),
            'AddOns': serialize.map(add_ons, lambda e: e),
        })
        data.update(serialize.prefixed_collapsible_map(add_ons_data, 'AddOns'))
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution['phone_number'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V1.PhoneNumberContext {}>'.format(context)

class PhoneNumberInstance(InstanceResource):

    def __init__(self, version, payload, phone_number: str=None):
        """
        Initialize the PhoneNumberInstance
        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        super().__init__(version)

        self._properties = { 
            'caller_name': payload.get('caller_name'),
            'country_code': payload.get('country_code'),
            'phone_number': payload.get('phone_number'),
            'national_format': payload.get('national_format'),
            'carrier': payload.get('carrier'),
            'add_ons': payload.get('add_ons'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'phone_number': phone_number or self._properties['phone_number'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(self._version, phone_number=self._solution['phone_number'],)
        return self._context
    
    @property
    def caller_name(self):
        """
        :returns: The name of the phone number's owner. If `null`, that information was not available.
        :rtype: dict
        """
        return self._properties['caller_name']
    
    @property
    def country_code(self):
        """
        :returns: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) for the phone number.
        :rtype: str
        """
        return self._properties['country_code']
    
    @property
    def phone_number(self):
        """
        :returns: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :rtype: str
        """
        return self._properties['phone_number']
    
    @property
    def national_format(self):
        """
        :returns: The phone number, in national format.
        :rtype: str
        """
        return self._properties['national_format']
    
    @property
    def carrier(self):
        """
        :returns: The telecom company that provides the phone number.
        :rtype: dict
        """
        return self._properties['carrier']
    
    @property
    def add_ons(self):
        """
        :returns: A JSON string with the results of the Add-ons you specified in the `add_ons` parameters. For the format of the object, see [Using Add-ons](https://www.twilio.com/docs/add-ons).
        :rtype: dict
        """
        return self._properties['add_ons']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, country_code=values.unset, type=values.unset, add_ons=values.unset, add_ons_data=values.unset):
        """
        Fetch the PhoneNumberInstance
        
        :params str country_code: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the phone number to fetch. This is used to specify the country when the phone number is provided in a national format.
        :params list[str] type: The type of information to return. Can be: `carrier` or `caller-name`. The default is null.  Carrier information costs $0.005 per phone number looked up.  Caller Name information is currently available only in the US and costs $0.01 per phone number looked up.  To retrieve both types on information, specify this parameter twice; once with `carrier` and once with `caller-name` as the value.
        :params list[str] add_ons: The `unique_name` of an Add-on you would like to invoke. Can be the `unique_name` of an Add-on that is installed on your account. You can specify multiple instances of this parameter to invoke multiple Add-ons. For more information about  Add-ons, see the [Add-ons documentation](https://www.twilio.com/docs/add-ons).
        :params dict add_ons_data: Data specific to the add-on you would like to invoke. The content and format of this value depends on the add-on.

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch(country_code=country_code, type=type, add_ons=add_ons, add_ons_data=add_ons_data, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V1.PhoneNumberInstance {}>'.format(context)


