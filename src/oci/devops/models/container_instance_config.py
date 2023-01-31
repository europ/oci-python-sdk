# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .container_config import ContainerConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerInstanceConfig(ContainerConfig):
    """
    Specifies ContainerInstance configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerInstanceConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ContainerInstanceConfig.container_config_type` attribute
        of this class is ``CONTAINER_INSTANCE_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param container_config_type:
            The value to assign to the container_config_type property of this ContainerInstanceConfig.
            Allowed values for this property are: "CONTAINER_INSTANCE_CONFIG"
        :type container_config_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerInstanceConfig.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this ContainerInstanceConfig.
        :type availability_domain: str

        :param shape_name:
            The value to assign to the shape_name property of this ContainerInstanceConfig.
        :type shape_name: str

        :param shape_config:
            The value to assign to the shape_config property of this ContainerInstanceConfig.
        :type shape_config: oci.devops.models.ShapeConfig

        :param network_channel:
            The value to assign to the network_channel property of this ContainerInstanceConfig.
        :type network_channel: oci.devops.models.NetworkChannel

        """
        self.swagger_types = {
            'container_config_type': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str',
            'shape_name': 'str',
            'shape_config': 'ShapeConfig',
            'network_channel': 'NetworkChannel'
        }

        self.attribute_map = {
            'container_config_type': 'containerConfigType',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'shape_name': 'shapeName',
            'shape_config': 'shapeConfig',
            'network_channel': 'networkChannel'
        }

        self._container_config_type = None
        self._compartment_id = None
        self._availability_domain = None
        self._shape_name = None
        self._shape_config = None
        self._network_channel = None
        self._container_config_type = 'CONTAINER_INSTANCE_CONFIG'

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ContainerInstanceConfig.
        The OCID of the compartment where the ContainerInstance will be created.


        :return: The compartment_id of this ContainerInstanceConfig.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerInstanceConfig.
        The OCID of the compartment where the ContainerInstance will be created.


        :param compartment_id: The compartment_id of this ContainerInstanceConfig.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this ContainerInstanceConfig.
        Availability domain where the ContainerInstance will be created.


        :return: The availability_domain of this ContainerInstanceConfig.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ContainerInstanceConfig.
        Availability domain where the ContainerInstance will be created.


        :param availability_domain: The availability_domain of this ContainerInstanceConfig.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this ContainerInstanceConfig.
        The shape of the ContainerInstance. The shape determines the resources available to the ContainerInstance.


        :return: The shape_name of this ContainerInstanceConfig.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this ContainerInstanceConfig.
        The shape of the ContainerInstance. The shape determines the resources available to the ContainerInstance.


        :param shape_name: The shape_name of this ContainerInstanceConfig.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def shape_config(self):
        """
        **[Required]** Gets the shape_config of this ContainerInstanceConfig.

        :return: The shape_config of this ContainerInstanceConfig.
        :rtype: oci.devops.models.ShapeConfig
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this ContainerInstanceConfig.

        :param shape_config: The shape_config of this ContainerInstanceConfig.
        :type: oci.devops.models.ShapeConfig
        """
        self._shape_config = shape_config

    @property
    def network_channel(self):
        """
        **[Required]** Gets the network_channel of this ContainerInstanceConfig.

        :return: The network_channel of this ContainerInstanceConfig.
        :rtype: oci.devops.models.NetworkChannel
        """
        return self._network_channel

    @network_channel.setter
    def network_channel(self, network_channel):
        """
        Sets the network_channel of this ContainerInstanceConfig.

        :param network_channel: The network_channel of this ContainerInstanceConfig.
        :type: oci.devops.models.NetworkChannel
        """
        self._network_channel = network_channel

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
