r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class BulkHostedNumberOrderInstance(InstanceResource):

    class RequestStatus:
        QUEUED = "QUEUED"
        IN_PROGRESS = "IN_PROGRESS"
        PROCESSED = "PROCESSED"

    """
    :ivar bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
    :ivar request_status: 
    :ivar friendly_name: A 128 character string that is a human-readable text that describes this resource.
    :ivar notification_email: Email address used for send notifications about this Bulk hosted number request.
    :ivar date_created: The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_completed: The date that this resource was completed, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The URL of this BulkHostedNumberOrder resource.
    :ivar total_count: The total count of phone numbers in this Bulk hosting request.
    :ivar results: Contains a list of all the individual hosting orders and their information, for this Bulk request. Each result object is grouped by its order status. To see a complete list of order status, please check 'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        bulk_hosting_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.bulk_hosting_sid: Optional[str] = payload.get("bulk_hosting_sid")
        self.request_status: Optional["BulkHostedNumberOrderInstance.RequestStatus"] = (
            payload.get("request_status")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.notification_email: Optional[str] = payload.get("notification_email")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_completed: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_completed")
        )
        self.url: Optional[str] = payload.get("url")
        self.total_count: Optional[int] = deserialize.integer(
            payload.get("total_count")
        )
        self.results: Optional[List[Dict[str, object]]] = payload.get("results")

        self._solution = {
            "bulk_hosting_sid": bulk_hosting_sid or self.bulk_hosting_sid,
        }
        self._context: Optional[BulkHostedNumberOrderContext] = None

    @property
    def _proxy(self) -> "BulkHostedNumberOrderContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BulkHostedNumberOrderContext for this BulkHostedNumberOrderInstance
        """
        if self._context is None:
            self._context = BulkHostedNumberOrderContext(
                self._version,
                bulk_hosting_sid=self._solution["bulk_hosting_sid"],
            )
        return self._context

    def fetch(
        self, order_status: Union[str, object] = values.unset
    ) -> "BulkHostedNumberOrderInstance":
        """
        Fetch the BulkHostedNumberOrderInstance

        :param order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check 'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.

        :returns: The fetched BulkHostedNumberOrderInstance
        """
        return self._proxy.fetch(
            order_status=order_status,
        )

    async def fetch_async(
        self, order_status: Union[str, object] = values.unset
    ) -> "BulkHostedNumberOrderInstance":
        """
        Asynchronous coroutine to fetch the BulkHostedNumberOrderInstance

        :param order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check 'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.

        :returns: The fetched BulkHostedNumberOrderInstance
        """
        return await self._proxy.fetch_async(
            order_status=order_status,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Numbers.V2.BulkHostedNumberOrderInstance {context}>"


class BulkHostedNumberOrderContext(InstanceContext):

    def __init__(self, version: Version, bulk_hosting_sid: str):
        """
        Initialize the BulkHostedNumberOrderContext

        :param version: Version that contains the resource
        :param bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "bulk_hosting_sid": bulk_hosting_sid,
        }
        self._uri = "/HostedNumber/Orders/Bulk/{bulk_hosting_sid}".format(
            **self._solution
        )

    def fetch(
        self, order_status: Union[str, object] = values.unset
    ) -> BulkHostedNumberOrderInstance:
        """
        Fetch the BulkHostedNumberOrderInstance

        :param order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check 'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.

        :returns: The fetched BulkHostedNumberOrderInstance
        """

        data = values.of(
            {
                "OrderStatus": order_status,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return BulkHostedNumberOrderInstance(
            self._version,
            payload,
            bulk_hosting_sid=self._solution["bulk_hosting_sid"],
        )

    async def fetch_async(
        self, order_status: Union[str, object] = values.unset
    ) -> BulkHostedNumberOrderInstance:
        """
        Asynchronous coroutine to fetch the BulkHostedNumberOrderInstance

        :param order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check 'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.

        :returns: The fetched BulkHostedNumberOrderInstance
        """

        data = values.of(
            {
                "OrderStatus": order_status,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return BulkHostedNumberOrderInstance(
            self._version,
            payload,
            bulk_hosting_sid=self._solution["bulk_hosting_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Numbers.V2.BulkHostedNumberOrderContext {context}>"


class BulkHostedNumberOrderList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the BulkHostedNumberOrderList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/HostedNumber/Orders/Bulk"

    def create(
        self, body: Union[object, object] = values.unset
    ) -> BulkHostedNumberOrderInstance:
        """
        Create the BulkHostedNumberOrderInstance

        :param body:

        :returns: The created BulkHostedNumberOrderInstance
        """
        data = body.to_dict()

        headers = {"Content-Type": "application/json"}

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return BulkHostedNumberOrderInstance(self._version, payload)

    async def create_async(
        self, body: Union[object, object] = values.unset
    ) -> BulkHostedNumberOrderInstance:
        """
        Asynchronously create the BulkHostedNumberOrderInstance

        :param body:

        :returns: The created BulkHostedNumberOrderInstance
        """
        data = body.to_dict()

        headers = {"Content-Type": "application/json"}

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return BulkHostedNumberOrderInstance(self._version, payload)

    def get(self, bulk_hosting_sid: str) -> BulkHostedNumberOrderContext:
        """
        Constructs a BulkHostedNumberOrderContext

        :param bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
        """
        return BulkHostedNumberOrderContext(
            self._version, bulk_hosting_sid=bulk_hosting_sid
        )

    def __call__(self, bulk_hosting_sid: str) -> BulkHostedNumberOrderContext:
        """
        Constructs a BulkHostedNumberOrderContext

        :param bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
        """
        return BulkHostedNumberOrderContext(
            self._version, bulk_hosting_sid=bulk_hosting_sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.BulkHostedNumberOrderList>"
