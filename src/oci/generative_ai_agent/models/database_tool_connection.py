# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531

from .database_connection import DatabaseConnection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolConnection(DatabaseConnection):
    """
    **DatabaseToolConnection**

    The details of the customer Database Tools Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_agent.models.DatabaseToolConnection.connection_type` attribute
        of this class is ``DATABASE_TOOL_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this DatabaseToolConnection.
            Allowed values for this property are: "DATABASE_TOOL_CONNECTION"
        :type connection_type: str

        :param connection_id:
            The value to assign to the connection_id property of this DatabaseToolConnection.
        :type connection_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'connection_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'connection_id': 'connectionId'
        }

        self._connection_type = None
        self._connection_id = None
        self._connection_type = 'DATABASE_TOOL_CONNECTION'

    @property
    def connection_id(self):
        """
        **[Required]** Gets the connection_id of this DatabaseToolConnection.
        The `OCID`__ of the Database Tools Connection.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connection_id of this DatabaseToolConnection.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this DatabaseToolConnection.
        The `OCID`__ of the Database Tools Connection.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connection_id: The connection_id of this DatabaseToolConnection.
        :type: str
        """
        self._connection_id = connection_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other