"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
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


class CommandList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CommandList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.wireless.v1.command.CommandList
        :rtype: twilio.rest.wireless.v1.command.CommandList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Commands'.format(**self._solution)
        
        
    
    
    
    def create(self, command, sim=values.unset, callback_method=values.unset, callback_url=values.unset, command_mode=values.unset, include_sid=values.unset, delivery_receipt_requested=values.unset):
        """
        Create the CommandInstance

        :param str command: The message body of the Command. Can be plain text in text mode or a Base64 encoded byte string in binary mode.
        :param str sim: The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/wireless/api/sim-resource) to send the Command to.
        :param str callback_method: The HTTP method we use to call `callback_url`. Can be: `POST` or `GET`, and the default is `POST`.
        :param str callback_url: The URL we call using the `callback_url` when the Command has finished sending, whether the command was delivered or it failed.
        :param CommandCommandMode command_mode: 
        :param str include_sid: Whether to include the SID of the command in the message body. Can be: `none`, `start`, or `end`, and the default behavior is `none`. When sending a Command to a SIM in text mode, we can automatically include the SID of the Command in the message body, which could be used to ensure that the device does not process the same Command more than once.  A value of `start` will prepend the message with the Command SID, and `end` will append it to the end, separating the Command SID from the message body with a space. The length of the Command SID is included in the 160 character limit so the SMS body must be 128 characters or less before the Command SID is included.
        :param bool delivery_receipt_requested: Whether to request delivery receipt from the recipient. For Commands that request delivery receipt, the Command state transitions to 'delivered' once the server has received a delivery receipt from the device. The default value is `true`.
        
        :returns: The created CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        data = values.of({ 
            'Command': command,
            'Sim': sim,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'CommandMode': command_mode,
            'IncludeSid': include_sid,
            'DeliveryReceiptRequested': delivery_receipt_requested,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return CommandInstance(self._version, payload)
    
    
    def stream(self, sim=values.unset, status=values.unset, direction=values.unset, transport=values.unset, limit=None, page_size=None):
        """
        Streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/wireless/api/sim-resource) to read.
        :param CommandStatus status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param CommandDirection direction: Only return Commands with this direction value.
        :param CommandTransport transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.command.CommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim,
            status=status,
            direction=direction,
            transport=transport,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, sim=values.unset, status=values.unset, direction=values.unset, transport=values.unset, limit=None, page_size=None):
        """
        Lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/wireless/api/sim-resource) to read.
        :param CommandStatus status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param CommandDirection direction: Only return Commands with this direction value.
        :param CommandTransport transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.command.CommandInstance]
        """
        return list(self.stream(
            sim=sim,
            status=status,
            direction=direction,
            transport=transport,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, status=values.unset, direction=values.unset, transport=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CommandInstance records from the API.
        Request is executed immediately
        
        :param str sim: The `sid` or `unique_name` of the [Sim resources](https://www.twilio.com/docs/wireless/api/sim-resource) to read.
        :param CommandStatus status: The status of the resources to read. Can be: `queued`, `sent`, `delivered`, `received`, or `failed`.
        :param CommandDirection direction: Only return Commands with this direction value.
        :param CommandTransport transport: Only return Commands with this transport value. Can be: `sms` or `ip`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandPage
        """
        data = values.of({ 
            'Sim': sim,
            'Status': status,
            'Direction': direction,
            'Transport': transport,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CommandPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CommandPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CommandContext
        
        :param sid: The SID of the Command resource to fetch.
        
        :returns: twilio.rest.wireless.v1.command.CommandContext
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        return CommandContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a CommandContext
        
        :param sid: The SID of the Command resource to fetch.
        
        :returns: twilio.rest.wireless.v1.command.CommandContext
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        return CommandContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.CommandList>'








class CommandPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.wireless.v1.command.CommandPage
        :rtype: twilio.rest.wireless.v1.command.CommandPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.command.CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        return CommandInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.CommandPage>'




class CommandContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CommandContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Command resource to fetch.

        :returns: twilio.rest.wireless.v1.command.CommandContext
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Commands/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the CommandInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the CommandInstance
        

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CommandInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.CommandContext {}>'.format(context)

class CommandInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the CommandInstance
        :returns: twilio.rest.wireless.v1.command.CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'sim_sid': payload.get('sim_sid'),
            'command': payload.get('command'),
            'command_mode': payload.get('command_mode'),
            'transport': payload.get('transport'),
            'delivery_receipt_requested': payload.get('delivery_receipt_requested'),
            'status': payload.get('status'),
            'direction': payload.get('direction'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CommandContext for this CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandContext
        """
        if self._context is None:
            self._context = CommandContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Command resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Command resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sim_sid(self):
        """
        :returns: The SID of the [Sim resource](https://www.twilio.com/docs/wireless/api/sim-resource) that the Command was sent to or from.
        :rtype: str
        """
        return self._properties['sim_sid']
    
    @property
    def command(self):
        """
        :returns: The message being sent to or from the SIM. For text mode messages, this can be up to 160 characters. For binary mode messages, this is a series of up to 140 bytes of data encoded using base64.
        :rtype: str
        """
        return self._properties['command']
    
    @property
    def command_mode(self):
        """
        :returns: 
        :rtype: CommandCommandMode
        """
        return self._properties['command_mode']
    
    @property
    def transport(self):
        """
        :returns: 
        :rtype: CommandTransport
        """
        return self._properties['transport']
    
    @property
    def delivery_receipt_requested(self):
        """
        :returns: Whether to request a delivery receipt.
        :rtype: bool
        """
        return self._properties['delivery_receipt_requested']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: CommandStatus
        """
        return self._properties['status']
    
    @property
    def direction(self):
        """
        :returns: 
        :rtype: CommandDirection
        """
        return self._properties['direction']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the CommandInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the CommandInstance
        

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.wireless.v1.command.CommandInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.CommandInstance {}>'.format(context)


