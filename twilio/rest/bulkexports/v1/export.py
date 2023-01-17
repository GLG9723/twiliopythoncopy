"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Bulkexports
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

from twilio.rest.export.day import DayListInstancefrom twilio.rest.export.export_custom_job import ExportCustomJobListInstancefrom twilio.rest.export.job import JobListInstance


class ExportContext(InstanceContext):
    def __init__(self, version: V1, resource_type: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'resource_type': resource_type,  }
        self._uri = '/Exports/${resource_type}'
        
        self._days = None
        self._export_custom_jobs = None
    
    def fetch(self):
        
        """
        Fetch the ExportInstance

        :returns: The fetched ExportInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return ExportInstance(
            self._version,
            payload,
            resource_type=self._solution['resource_type'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ExportContext>'



class ExportInstance(InstanceResource):
    def __init__(self, version, payload, resource_type: str):
        super().__init__(version)
        self._properties = { 
            'resource_type' : payload.get('resource_type'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'resource_type': resource_type or self._properties['resource_type']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ExportContext(
                self._version,
                resource_type=self._solution['resource_type'],
            )
        return self._context

    @property
    def days(self):
        return self._proxy.days
    @property
    def export_custom_jobs(self):
        return self._proxy.export_custom_jobs
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ExportInstance {}>'.format(context)



class ExportListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Exports'
        
        self._jobs = None
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ExportListInstance>'

