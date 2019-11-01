# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

import json
from twilio.base.obsolete import deprecated_method
from twilio.twiml import (
    TwiML,
    format_language,
)


class FaxResponse(TwiML):
    """ <Response> TwiML for Faxes """

    def __init__(self, **kwargs):
        super(FaxResponse, self).__init__(**kwargs)
        self.name = 'Response'

    def receive(self, action=None, method=None, **kwargs):
        """
        Create a <Receive> element

        :param action: Receive action URL
        :param method: Receive action URL method
        :param kwargs: additional attributes

        :returns: <Receive> element
        """
        return self.nest(Receive(action=action, method=method, **kwargs))


class Receive(TwiML):
    """ <Receive> TwiML Verb """

    def __init__(self, **kwargs):
        super(Receive, self).__init__(**kwargs)
        self.name = 'Receive'
