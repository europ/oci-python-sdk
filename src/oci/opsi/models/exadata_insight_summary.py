# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInsightSummary(object):
    """
    Summary of an Exadata insight resource.
    """

    #: A constant which can be used with the entity_source property of a ExadataInsightSummary.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_EXADATA"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_EXADATA = "EM_MANAGED_EXTERNAL_EXADATA"

    #: A constant which can be used with the exadata_type property of a ExadataInsightSummary.
    #: This constant has a value of "DBMACHINE"
    EXADATA_TYPE_DBMACHINE = "DBMACHINE"

    #: A constant which can be used with the exadata_type property of a ExadataInsightSummary.
    #: This constant has a value of "EXACS"
    EXADATA_TYPE_EXACS = "EXACS"

    #: A constant which can be used with the exadata_type property of a ExadataInsightSummary.
    #: This constant has a value of "EXACC"
    EXADATA_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the exadata_rack_type property of a ExadataInsightSummary.
    #: This constant has a value of "FULL"
    EXADATA_RACK_TYPE_FULL = "FULL"

    #: A constant which can be used with the exadata_rack_type property of a ExadataInsightSummary.
    #: This constant has a value of "HALF"
    EXADATA_RACK_TYPE_HALF = "HALF"

    #: A constant which can be used with the exadata_rack_type property of a ExadataInsightSummary.
    #: This constant has a value of "QUARTER"
    EXADATA_RACK_TYPE_QUARTER = "QUARTER"

    #: A constant which can be used with the exadata_rack_type property of a ExadataInsightSummary.
    #: This constant has a value of "EIGHTH"
    EXADATA_RACK_TYPE_EIGHTH = "EIGHTH"

    #: A constant which can be used with the status property of a ExadataInsightSummary.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a ExadataInsightSummary.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a ExadataInsightSummary.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ExadataInsightSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExadataInsightSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExadataInsightSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExadataInsightSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ExadataInsightSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExadataInsightSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInsightSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.EmManagedExternalExadataInsightSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this ExadataInsightSummary.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param id:
            The value to assign to the id property of this ExadataInsightSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExadataInsightSummary.
        :type compartment_id: str

        :param exadata_name:
            The value to assign to the exadata_name property of this ExadataInsightSummary.
        :type exadata_name: str

        :param exadata_display_name:
            The value to assign to the exadata_display_name property of this ExadataInsightSummary.
        :type exadata_display_name: str

        :param exadata_type:
            The value to assign to the exadata_type property of this ExadataInsightSummary.
            Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_type: str

        :param exadata_rack_type:
            The value to assign to the exadata_rack_type property of this ExadataInsightSummary.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_rack_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExadataInsightSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExadataInsightSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ExadataInsightSummary.
        :type system_tags: dict(str, dict(str, object))

        :param status:
            The value to assign to the status property of this ExadataInsightSummary.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this ExadataInsightSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExadataInsightSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExadataInsightSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExadataInsightSummary.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'exadata_name': 'str',
            'exadata_display_name': 'str',
            'exadata_type': 'str',
            'exadata_rack_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'exadata_name': 'exadataName',
            'exadata_display_name': 'exadataDisplayName',
            'exadata_type': 'exadataType',
            'exadata_rack_type': 'exadataRackType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._exadata_name = None
        self._exadata_display_name = None
        self._exadata_type = None
        self._exadata_rack_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'EM_MANAGED_EXTERNAL_EXADATA':
            return 'EmManagedExternalExadataInsightSummary'
        else:
            return 'ExadataInsightSummary'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this ExadataInsightSummary.
        Source of the Exadata system.

        Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this ExadataInsightSummary.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this ExadataInsightSummary.
        Source of the Exadata system.


        :param entity_source: The entity_source of this ExadataInsightSummary.
        :type: str
        """
        allowed_values = ["EM_MANAGED_EXTERNAL_EXADATA"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExadataInsightSummary.
        The `OCID`__ of the Exadata insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ExadataInsightSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExadataInsightSummary.
        The `OCID`__ of the Exadata insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExadataInsightSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExadataInsightSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExadataInsightSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExadataInsightSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExadataInsightSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def exadata_name(self):
        """
        **[Required]** Gets the exadata_name of this ExadataInsightSummary.
        The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.


        :return: The exadata_name of this ExadataInsightSummary.
        :rtype: str
        """
        return self._exadata_name

    @exadata_name.setter
    def exadata_name(self, exadata_name):
        """
        Sets the exadata_name of this ExadataInsightSummary.
        The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.


        :param exadata_name: The exadata_name of this ExadataInsightSummary.
        :type: str
        """
        self._exadata_name = exadata_name

    @property
    def exadata_display_name(self):
        """
        Gets the exadata_display_name of this ExadataInsightSummary.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :return: The exadata_display_name of this ExadataInsightSummary.
        :rtype: str
        """
        return self._exadata_display_name

    @exadata_display_name.setter
    def exadata_display_name(self, exadata_display_name):
        """
        Sets the exadata_display_name of this ExadataInsightSummary.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :param exadata_display_name: The exadata_display_name of this ExadataInsightSummary.
        :type: str
        """
        self._exadata_display_name = exadata_display_name

    @property
    def exadata_type(self):
        """
        Gets the exadata_type of this ExadataInsightSummary.
        Operations Insights internal representation of the the Exadata system type.

        Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_type of this ExadataInsightSummary.
        :rtype: str
        """
        return self._exadata_type

    @exadata_type.setter
    def exadata_type(self, exadata_type):
        """
        Sets the exadata_type of this ExadataInsightSummary.
        Operations Insights internal representation of the the Exadata system type.


        :param exadata_type: The exadata_type of this ExadataInsightSummary.
        :type: str
        """
        allowed_values = ["DBMACHINE", "EXACS", "EXACC"]
        if not value_allowed_none_or_none_sentinel(exadata_type, allowed_values):
            exadata_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_type = exadata_type

    @property
    def exadata_rack_type(self):
        """
        Gets the exadata_rack_type of this ExadataInsightSummary.
        Operations Insights internal representation of the the Exadata system rack type.

        Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_rack_type of this ExadataInsightSummary.
        :rtype: str
        """
        return self._exadata_rack_type

    @exadata_rack_type.setter
    def exadata_rack_type(self, exadata_rack_type):
        """
        Sets the exadata_rack_type of this ExadataInsightSummary.
        Operations Insights internal representation of the the Exadata system rack type.


        :param exadata_rack_type: The exadata_rack_type of this ExadataInsightSummary.
        :type: str
        """
        allowed_values = ["FULL", "HALF", "QUARTER", "EIGHTH"]
        if not value_allowed_none_or_none_sentinel(exadata_rack_type, allowed_values):
            exadata_rack_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_rack_type = exadata_rack_type

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ExadataInsightSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ExadataInsightSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExadataInsightSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ExadataInsightSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ExadataInsightSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ExadataInsightSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExadataInsightSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ExadataInsightSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ExadataInsightSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ExadataInsightSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ExadataInsightSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ExadataInsightSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ExadataInsightSummary.
        Indicates the status of an Exadata insight in Operations Insights

        Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ExadataInsightSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExadataInsightSummary.
        Indicates the status of an Exadata insight in Operations Insights


        :param status: The status of this ExadataInsightSummary.
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExadataInsightSummary.
        The time the the Exadata insight was first enabled. An RFC3339 formatted datetime string


        :return: The time_created of this ExadataInsightSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExadataInsightSummary.
        The time the the Exadata insight was first enabled. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ExadataInsightSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ExadataInsightSummary.
        The time the Exadata insight was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this ExadataInsightSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExadataInsightSummary.
        The time the Exadata insight was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this ExadataInsightSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExadataInsightSummary.
        The current state of the Exadata insight.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExadataInsightSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExadataInsightSummary.
        The current state of the Exadata insight.


        :param lifecycle_state: The lifecycle_state of this ExadataInsightSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExadataInsightSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ExadataInsightSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExadataInsightSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ExadataInsightSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other