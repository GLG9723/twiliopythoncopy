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


from datetime import date
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class UserDefinedMessageSubscriptionList(ListResource):
    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the UserDefinedMessageSubscriptionList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages.

        :returns: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionList
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessageSubscriptions.json".format(
            **self._solution
        )

    def create(self, callback, idempotency_key=values.unset, method=values.unset):
        """
        Create the UserDefinedMessageSubscriptionInstance

        :param str callback: The URL we should call using the `method` to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted).
        :param str idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
        :param str method: The HTTP method Twilio will use when requesting the above `Url`. Either `GET` or `POST`. Default is `POST`.

        :returns: The created UserDefinedMessageSubscriptionInstance
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionInstance
        """
        data = values.of(
            {
                "Callback": callback,
                "IdempotencyKey": idempotency_key,
                "Method": method,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserDefinedMessageSubscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    def get(self, sid):
        """
        Constructs a UserDefinedMessageSubscriptionContext

        :param sid: The SID that uniquely identifies this User Defined Message Subscription.

        :returns: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionContext
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionContext
        """
        return UserDefinedMessageSubscriptionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a UserDefinedMessageSubscriptionContext

        :param sid: The SID that uniquely identifies this User Defined Message Subscription.

        :returns: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionContext
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionContext
        """
        return UserDefinedMessageSubscriptionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.UserDefinedMessageSubscriptionList>"


class UserDefinedMessageSubscriptionInstance(InstanceResource):
    def __init__(
        self, version, payload, account_sid: str, call_sid: str, sid: str = None
    ):
        """
        Initialize the UserDefinedMessageSubscriptionInstance

        :returns: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionInstance
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "call_sid": payload.get("call_sid"),
            "sid": payload.get("sid"),
            "date_created": deserialize.rfc2822_datetime(payload.get("date_created")),
            "uri": payload.get("uri"),
        }

        self._context = None
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserDefinedMessageSubscriptionContext for this UserDefinedMessageSubscriptionInstance
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionContext
        """
        if self._context is None:
            self._context = UserDefinedMessageSubscriptionContext(
                self._version,
                account_sid=self._solution["account_sid"],
                call_sid=self._solution["call_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def call_sid(self):
        """
        :returns: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.
        :rtype: str
        """
        return self._properties["call_sid"]

    @property
    def sid(self):
        """
        :returns: The SID that uniquely identifies this User Defined Message Subscription.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def date_created(self):
        """
        :returns: The date that this User Defined Message Subscription was created, given in RFC 2822 format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def uri(self):
        """
        :returns: The URI of the User Defined Message Subscription Resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties["uri"]

    def delete(self):
        """
        Deletes the UserDefinedMessageSubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.UserDefinedMessageSubscriptionInstance {}>".format(
            context
        )


class UserDefinedMessageSubscriptionContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        """
        Initialize the UserDefinedMessageSubscriptionContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.
        :param sid: The SID that uniquely identifies this User Defined Message Subscription.

        :returns: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionContext
        :rtype: twilio.rest.api.v2010.account.call.user_defined_message_subscription.UserDefinedMessageSubscriptionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessageSubscriptions/{sid}.json".format(
            **self._solution
        )

    def delete(self):
        """
        Deletes the UserDefinedMessageSubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.UserDefinedMessageSubscriptionContext {}>".format(
            context
        )
