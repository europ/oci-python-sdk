# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceLocation(object):
    """
    The location of the data files that the agent will use.
    """

    #: A constant which can be used with the source_location_type property of a SourceLocation.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    SOURCE_LOCATION_TYPE_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    #: A constant which can be used with the source_location_type property of a SourceLocation.
    #: This constant has a value of "OCI_OPEN_SEARCH"
    SOURCE_LOCATION_TYPE_OCI_OPEN_SEARCH = "OCI_OPEN_SEARCH"

    #: A constant which can be used with the source_location_type property of a SourceLocation.
    #: This constant has a value of "OCI_DATABASE"
    SOURCE_LOCATION_TYPE_OCI_DATABASE = "OCI_DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new SourceLocation object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_agent_runtime.models.OciObjectStorageSourceLocation`
        * :class:`~oci.generative_ai_agent_runtime.models.OciOpenSearchSourceLocation`
        * :class:`~oci.generative_ai_agent_runtime.models.OciDatabaseSourceLocation`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_location_type:
            The value to assign to the source_location_type property of this SourceLocation.
            Allowed values for this property are: "OCI_OBJECT_STORAGE", "OCI_OPEN_SEARCH", "OCI_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_location_type: str

        """
        self.swagger_types = {
            'source_location_type': 'str'
        }

        self.attribute_map = {
            'source_location_type': 'sourceLocationType'
        }

        self._source_location_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sourceLocationType']

        if type == 'OCI_OBJECT_STORAGE':
            return 'OciObjectStorageSourceLocation'

        if type == 'OCI_OPEN_SEARCH':
            return 'OciOpenSearchSourceLocation'

        if type == 'OCI_DATABASE':
            return 'OciDatabaseSourceLocation'
        else:
            return 'SourceLocation'

    @property
    def source_location_type(self):
        """
        **[Required]** Gets the source_location_type of this SourceLocation.
        The type of the data source that contains data files for the agent.

        Allowed values for this property are: "OCI_OBJECT_STORAGE", "OCI_OPEN_SEARCH", "OCI_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_location_type of this SourceLocation.
        :rtype: str
        """
        return self._source_location_type

    @source_location_type.setter
    def source_location_type(self, source_location_type):
        """
        Sets the source_location_type of this SourceLocation.
        The type of the data source that contains data files for the agent.


        :param source_location_type: The source_location_type of this SourceLocation.
        :type: str
        """
        allowed_values = ["OCI_OBJECT_STORAGE", "OCI_OPEN_SEARCH", "OCI_DATABASE"]
        if not value_allowed_none_or_none_sentinel(source_location_type, allowed_values):
            source_location_type = 'UNKNOWN_ENUM_VALUE'
        self._source_location_type = source_location_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other