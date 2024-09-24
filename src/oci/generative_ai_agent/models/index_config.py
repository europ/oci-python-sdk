# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndexConfig(object):
    """
    **IndexConfig**

    The index configuration of Knowledge bases.
    """

    #: A constant which can be used with the index_config_type property of a IndexConfig.
    #: This constant has a value of "DEFAULT_INDEX_CONFIG"
    INDEX_CONFIG_TYPE_DEFAULT_INDEX_CONFIG = "DEFAULT_INDEX_CONFIG"

    #: A constant which can be used with the index_config_type property of a IndexConfig.
    #: This constant has a value of "OCI_OPEN_SEARCH_INDEX_CONFIG"
    INDEX_CONFIG_TYPE_OCI_OPEN_SEARCH_INDEX_CONFIG = "OCI_OPEN_SEARCH_INDEX_CONFIG"

    #: A constant which can be used with the index_config_type property of a IndexConfig.
    #: This constant has a value of "OCI_DATABASE_CONFIG"
    INDEX_CONFIG_TYPE_OCI_DATABASE_CONFIG = "OCI_DATABASE_CONFIG"

    def __init__(self, **kwargs):
        """
        Initializes a new IndexConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_agent.models.DefaultIndexConfig`
        * :class:`~oci.generative_ai_agent.models.OciDatabaseConfig`
        * :class:`~oci.generative_ai_agent.models.OciOpenSearchIndexConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param index_config_type:
            The value to assign to the index_config_type property of this IndexConfig.
            Allowed values for this property are: "DEFAULT_INDEX_CONFIG", "OCI_OPEN_SEARCH_INDEX_CONFIG", "OCI_DATABASE_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type index_config_type: str

        """
        self.swagger_types = {
            'index_config_type': 'str'
        }

        self.attribute_map = {
            'index_config_type': 'indexConfigType'
        }

        self._index_config_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['indexConfigType']

        if type == 'DEFAULT_INDEX_CONFIG':
            return 'DefaultIndexConfig'

        if type == 'OCI_DATABASE_CONFIG':
            return 'OciDatabaseConfig'

        if type == 'OCI_OPEN_SEARCH_INDEX_CONFIG':
            return 'OciOpenSearchIndexConfig'
        else:
            return 'IndexConfig'

    @property
    def index_config_type(self):
        """
        **[Required]** Gets the index_config_type of this IndexConfig.
        The type of index.
        The allowed values are:
        - `DEFAULT_INDEX_CONFIG`: DefaultIndexConfig allows the service to create and manage vector store on behalf of the customer.
        - `OCI_OPEN_SEARCH_INDEX_CONFIG`: OciOpenSearchIndexConfig allows customer to configure their OpenSearch cluster.
        - `OCI_DATABASE_CONFIG`: OciDatabaseConfig allows customer to configure their Database.

        Allowed values for this property are: "DEFAULT_INDEX_CONFIG", "OCI_OPEN_SEARCH_INDEX_CONFIG", "OCI_DATABASE_CONFIG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The index_config_type of this IndexConfig.
        :rtype: str
        """
        return self._index_config_type

    @index_config_type.setter
    def index_config_type(self, index_config_type):
        """
        Sets the index_config_type of this IndexConfig.
        The type of index.
        The allowed values are:
        - `DEFAULT_INDEX_CONFIG`: DefaultIndexConfig allows the service to create and manage vector store on behalf of the customer.
        - `OCI_OPEN_SEARCH_INDEX_CONFIG`: OciOpenSearchIndexConfig allows customer to configure their OpenSearch cluster.
        - `OCI_DATABASE_CONFIG`: OciDatabaseConfig allows customer to configure their Database.


        :param index_config_type: The index_config_type of this IndexConfig.
        :type: str
        """
        allowed_values = ["DEFAULT_INDEX_CONFIG", "OCI_OPEN_SEARCH_INDEX_CONFIG", "OCI_DATABASE_CONFIG"]
        if not value_allowed_none_or_none_sentinel(index_config_type, allowed_values):
            index_config_type = 'UNKNOWN_ENUM_VALUE'
        self._index_config_type = index_config_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
