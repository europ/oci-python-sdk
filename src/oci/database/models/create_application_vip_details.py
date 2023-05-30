# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApplicationVipDetails(object):
    """
    Details to create an application virtual IP (VIP) address on a cloud VM cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApplicationVipDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname_label:
            The value to assign to the hostname_label property of this CreateApplicationVipDetails.
        :type hostname_label: str

        :param db_node_id:
            The value to assign to the db_node_id property of this CreateApplicationVipDetails.
        :type db_node_id: str

        :param cloud_vm_cluster_id:
            The value to assign to the cloud_vm_cluster_id property of this CreateApplicationVipDetails.
        :type cloud_vm_cluster_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateApplicationVipDetails.
        :type subnet_id: str

        :param ip_address:
            The value to assign to the ip_address property of this CreateApplicationVipDetails.
        :type ip_address: str

        """
        self.swagger_types = {
            'hostname_label': 'str',
            'db_node_id': 'str',
            'cloud_vm_cluster_id': 'str',
            'subnet_id': 'str',
            'ip_address': 'str'
        }

        self.attribute_map = {
            'hostname_label': 'hostnameLabel',
            'db_node_id': 'dbNodeId',
            'cloud_vm_cluster_id': 'cloudVmClusterId',
            'subnet_id': 'subnetId',
            'ip_address': 'ipAddress'
        }

        self._hostname_label = None
        self._db_node_id = None
        self._cloud_vm_cluster_id = None
        self._subnet_id = None
        self._ip_address = None

    @property
    def hostname_label(self):
        """
        **[Required]** Gets the hostname_label of this CreateApplicationVipDetails.
        The hostname of the application virtual IP (VIP) address.


        :return: The hostname_label of this CreateApplicationVipDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this CreateApplicationVipDetails.
        The hostname of the application virtual IP (VIP) address.


        :param hostname_label: The hostname_label of this CreateApplicationVipDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def db_node_id(self):
        """
        Gets the db_node_id of this CreateApplicationVipDetails.
        The `OCID`__ of the DB node associated with the application virtual IP (VIP) address.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_node_id of this CreateApplicationVipDetails.
        :rtype: str
        """
        return self._db_node_id

    @db_node_id.setter
    def db_node_id(self, db_node_id):
        """
        Sets the db_node_id of this CreateApplicationVipDetails.
        The `OCID`__ of the DB node associated with the application virtual IP (VIP) address.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_node_id: The db_node_id of this CreateApplicationVipDetails.
        :type: str
        """
        self._db_node_id = db_node_id

    @property
    def cloud_vm_cluster_id(self):
        """
        **[Required]** Gets the cloud_vm_cluster_id of this CreateApplicationVipDetails.
        The `OCID`__ of the cloud VM cluster associated with the application virtual IP (VIP) address.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_vm_cluster_id of this CreateApplicationVipDetails.
        :rtype: str
        """
        return self._cloud_vm_cluster_id

    @cloud_vm_cluster_id.setter
    def cloud_vm_cluster_id(self, cloud_vm_cluster_id):
        """
        Sets the cloud_vm_cluster_id of this CreateApplicationVipDetails.
        The `OCID`__ of the cloud VM cluster associated with the application virtual IP (VIP) address.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_vm_cluster_id: The cloud_vm_cluster_id of this CreateApplicationVipDetails.
        :type: str
        """
        self._cloud_vm_cluster_id = cloud_vm_cluster_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateApplicationVipDetails.
        The `OCID`__ of the subnet associated with the application virtual IP (VIP) address.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateApplicationVipDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateApplicationVipDetails.
        The `OCID`__ of the subnet associated with the application virtual IP (VIP) address.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateApplicationVipDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreateApplicationVipDetails.
        The application virtual IP (VIP) address.


        :return: The ip_address of this CreateApplicationVipDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateApplicationVipDetails.
        The application virtual IP (VIP) address.


        :param ip_address: The ip_address of this CreateApplicationVipDetails.
        :type: str
        """
        self._ip_address = ip_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other