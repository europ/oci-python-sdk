# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .host_insight import HostInsight
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MacsManagedCloudDatabaseHostInsight(HostInsight):
    """
    Cloud MACS-managed database host insight resource.
    """

    #: A constant which can be used with the platform_type property of a MacsManagedCloudDatabaseHostInsight.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a MacsManagedCloudDatabaseHostInsight.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the platform_type property of a MacsManagedCloudDatabaseHostInsight.
    #: This constant has a value of "SUNOS"
    PLATFORM_TYPE_SUNOS = "SUNOS"

    #: A constant which can be used with the platform_type property of a MacsManagedCloudDatabaseHostInsight.
    #: This constant has a value of "ZLINUX"
    PLATFORM_TYPE_ZLINUX = "ZLINUX"

    #: A constant which can be used with the platform_type property of a MacsManagedCloudDatabaseHostInsight.
    #: This constant has a value of "WINDOWS"
    PLATFORM_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the platform_type property of a MacsManagedCloudDatabaseHostInsight.
    #: This constant has a value of "AIX"
    PLATFORM_TYPE_AIX = "AIX"

    #: A constant which can be used with the platform_type property of a MacsManagedCloudDatabaseHostInsight.
    #: This constant has a value of "HP_UX"
    PLATFORM_TYPE_HP_UX = "HP_UX"

    def __init__(self, **kwargs):
        """
        Initializes a new MacsManagedCloudDatabaseHostInsight object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.MacsManagedCloudDatabaseHostInsight.entity_source` attribute
        of this class is ``MACS_MANAGED_CLOUD_DB_HOST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this MacsManagedCloudDatabaseHostInsight.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", "MACS_MANAGED_CLOUD_HOST", "PE_COMANAGED_HOST", "MACS_MANAGED_CLOUD_DB_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param id:
            The value to assign to the id property of this MacsManagedCloudDatabaseHostInsight.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MacsManagedCloudDatabaseHostInsight.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this MacsManagedCloudDatabaseHostInsight.
        :type host_name: str

        :param host_display_name:
            The value to assign to the host_display_name property of this MacsManagedCloudDatabaseHostInsight.
        :type host_display_name: str

        :param host_type:
            The value to assign to the host_type property of this MacsManagedCloudDatabaseHostInsight.
        :type host_type: str

        :param processor_count:
            The value to assign to the processor_count property of this MacsManagedCloudDatabaseHostInsight.
        :type processor_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MacsManagedCloudDatabaseHostInsight.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MacsManagedCloudDatabaseHostInsight.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MacsManagedCloudDatabaseHostInsight.
        :type system_tags: dict(str, dict(str, object))

        :param status:
            The value to assign to the status property of this MacsManagedCloudDatabaseHostInsight.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this MacsManagedCloudDatabaseHostInsight.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MacsManagedCloudDatabaseHostInsight.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MacsManagedCloudDatabaseHostInsight.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MacsManagedCloudDatabaseHostInsight.
        :type lifecycle_details: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MacsManagedCloudDatabaseHostInsight.
        :type management_agent_id: str

        :param platform_name:
            The value to assign to the platform_name property of this MacsManagedCloudDatabaseHostInsight.
        :type platform_name: str

        :param platform_type:
            The value to assign to the platform_type property of this MacsManagedCloudDatabaseHostInsight.
            Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", "WINDOWS", "AIX", "HP_UX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param platform_version:
            The value to assign to the platform_version property of this MacsManagedCloudDatabaseHostInsight.
        :type platform_version: str

        :param parent_id:
            The value to assign to the parent_id property of this MacsManagedCloudDatabaseHostInsight.
        :type parent_id: str

        :param root_id:
            The value to assign to the root_id property of this MacsManagedCloudDatabaseHostInsight.
        :type root_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'host_display_name': 'str',
            'host_type': 'str',
            'processor_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'management_agent_id': 'str',
            'platform_name': 'str',
            'platform_type': 'str',
            'platform_version': 'str',
            'parent_id': 'str',
            'root_id': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'host_display_name': 'hostDisplayName',
            'host_type': 'hostType',
            'processor_count': 'processorCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'management_agent_id': 'managementAgentId',
            'platform_name': 'platformName',
            'platform_type': 'platformType',
            'platform_version': 'platformVersion',
            'parent_id': 'parentId',
            'root_id': 'rootId'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._host_name = None
        self._host_display_name = None
        self._host_type = None
        self._processor_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._management_agent_id = None
        self._platform_name = None
        self._platform_type = None
        self._platform_version = None
        self._parent_id = None
        self._root_id = None
        self._entity_source = 'MACS_MANAGED_CLOUD_DB_HOST'

    @property
    def management_agent_id(self):
        """
        **[Required]** Gets the management_agent_id of this MacsManagedCloudDatabaseHostInsight.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MacsManagedCloudDatabaseHostInsight.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MacsManagedCloudDatabaseHostInsight.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MacsManagedCloudDatabaseHostInsight.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def platform_name(self):
        """
        Gets the platform_name of this MacsManagedCloudDatabaseHostInsight.
        Platform name.


        :return: The platform_name of this MacsManagedCloudDatabaseHostInsight.
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """
        Sets the platform_name of this MacsManagedCloudDatabaseHostInsight.
        Platform name.


        :param platform_name: The platform_name of this MacsManagedCloudDatabaseHostInsight.
        :type: str
        """
        self._platform_name = platform_name

    @property
    def platform_type(self):
        """
        Gets the platform_type of this MacsManagedCloudDatabaseHostInsight.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS].
        Supported platformType(s) for MACS-managed cloud host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

        Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", "WINDOWS", "AIX", "HP_UX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this MacsManagedCloudDatabaseHostInsight.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this MacsManagedCloudDatabaseHostInsight.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS].
        Supported platformType(s) for MACS-managed cloud host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].


        :param platform_type: The platform_type of this MacsManagedCloudDatabaseHostInsight.
        :type: str
        """
        allowed_values = ["LINUX", "SOLARIS", "SUNOS", "ZLINUX", "WINDOWS", "AIX", "HP_UX"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def platform_version(self):
        """
        Gets the platform_version of this MacsManagedCloudDatabaseHostInsight.
        Platform version.


        :return: The platform_version of this MacsManagedCloudDatabaseHostInsight.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this MacsManagedCloudDatabaseHostInsight.
        Platform version.


        :param platform_version: The platform_version of this MacsManagedCloudDatabaseHostInsight.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def parent_id(self):
        """
        Gets the parent_id of this MacsManagedCloudDatabaseHostInsight.
        The `OCID`__ of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The parent_id of this MacsManagedCloudDatabaseHostInsight.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this MacsManagedCloudDatabaseHostInsight.
        The `OCID`__ of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param parent_id: The parent_id of this MacsManagedCloudDatabaseHostInsight.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def root_id(self):
        """
        Gets the root_id of this MacsManagedCloudDatabaseHostInsight.
        The `OCID`__ of the Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The root_id of this MacsManagedCloudDatabaseHostInsight.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """
        Sets the root_id of this MacsManagedCloudDatabaseHostInsight.
        The `OCID`__ of the Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param root_id: The root_id of this MacsManagedCloudDatabaseHostInsight.
        :type: str
        """
        self._root_id = root_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
