# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddressList(object):
    """
    List of addresses with a reference name.
    The value of an entry is a list of IP addresses or prefixes in CIDR notation or FQDNs.
    The associated key is the identifier by which the IP address list is referenced.
    """

    #: A constant which can be used with the type property of a AddressList.
    #: This constant has a value of "FQDN"
    TYPE_FQDN = "FQDN"

    #: A constant which can be used with the type property of a AddressList.
    #: This constant has a value of "IP"
    TYPE_IP = "IP"

    def __init__(self, **kwargs):
        """
        Initializes a new AddressList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AddressList.
        :type name: str

        :param type:
            The value to assign to the type property of this AddressList.
            Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param addresses:
            The value to assign to the addresses property of this AddressList.
        :type addresses: list[str]

        :param total_addresses:
            The value to assign to the total_addresses property of this AddressList.
        :type total_addresses: int

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this AddressList.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'addresses': 'list[str]',
            'total_addresses': 'int',
            'parent_resource_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'addresses': 'addresses',
            'total_addresses': 'totalAddresses',
            'parent_resource_id': 'parentResourceId'
        }

        self._name = None
        self._type = None
        self._addresses = None
        self._total_addresses = None
        self._parent_resource_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AddressList.
        Unique name to identify the group of addresses to be used in the policy rules.


        :return: The name of this AddressList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AddressList.
        Unique name to identify the group of addresses to be used in the policy rules.


        :param name: The name of this AddressList.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AddressList.
        Type of address List. The accepted values are - * FQDN * IP

        Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AddressList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AddressList.
        Type of address List. The accepted values are - * FQDN * IP


        :param type: The type of this AddressList.
        :type: str
        """
        allowed_values = ["FQDN", "IP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def addresses(self):
        """
        **[Required]** Gets the addresses of this AddressList.
        List of addresses.


        :return: The addresses of this AddressList.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this AddressList.
        List of addresses.


        :param addresses: The addresses of this AddressList.
        :type: list[str]
        """
        self._addresses = addresses

    @property
    def total_addresses(self):
        """
        **[Required]** Gets the total_addresses of this AddressList.
        Count of total Addresses in the AddressList


        :return: The total_addresses of this AddressList.
        :rtype: int
        """
        return self._total_addresses

    @total_addresses.setter
    def total_addresses(self, total_addresses):
        """
        Sets the total_addresses of this AddressList.
        Count of total Addresses in the AddressList


        :param total_addresses: The total_addresses of this AddressList.
        :type: int
        """
        self._total_addresses = total_addresses

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this AddressList.
        OCID of the Network Firewall Policy this Address List belongs to.


        :return: The parent_resource_id of this AddressList.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this AddressList.
        OCID of the Network Firewall Policy this Address List belongs to.


        :param parent_resource_id: The parent_resource_id of this AddressList.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other