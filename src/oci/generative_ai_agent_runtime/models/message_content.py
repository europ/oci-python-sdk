# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MessageContent(object):
    """
    The content of the message.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MessageContent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this MessageContent.
        :type text: str

        :param citations:
            The value to assign to the citations property of this MessageContent.
        :type citations: list[oci.generative_ai_agent_runtime.models.Citation]

        """
        self.swagger_types = {
            'text': 'str',
            'citations': 'list[Citation]'
        }

        self.attribute_map = {
            'text': 'text',
            'citations': 'citations'
        }

        self._text = None
        self._citations = None

    @property
    def text(self):
        """
        **[Required]** Gets the text of this MessageContent.
        The content of the message.


        :return: The text of this MessageContent.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this MessageContent.
        The content of the message.


        :param text: The text of this MessageContent.
        :type: str
        """
        self._text = text

    @property
    def citations(self):
        """
        Gets the citations of this MessageContent.
        Citations to data sources used for generating an agent's message.


        :return: The citations of this MessageContent.
        :rtype: list[oci.generative_ai_agent_runtime.models.Citation]
        """
        return self._citations

    @citations.setter
    def citations(self, citations):
        """
        Sets the citations of this MessageContent.
        Citations to data sources used for generating an agent's message.


        :param citations: The citations of this MessageContent.
        :type: list[oci.generative_ai_agent_runtime.models.Citation]
        """
        self._citations = citations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other