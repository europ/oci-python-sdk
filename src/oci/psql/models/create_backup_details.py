# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBackupDetails(object):
    """
    The information to create a new Backup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateBackupDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateBackupDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBackupDetails.
        :type compartment_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateBackupDetails.
        :type db_system_id: str

        :param retention_period:
            The value to assign to the retention_period property of this CreateBackupDetails.
        :type retention_period: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBackupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'db_system_id': 'str',
            'retention_period': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'db_system_id': 'dbSystemId',
            'retention_period': 'retentionPeriod',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._db_system_id = None
        self._retention_period = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateBackupDetails.
        Backup display name.


        :return: The display_name of this CreateBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBackupDetails.
        Backup display name.


        :param display_name: The display_name of this CreateBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateBackupDetails.
        Backup description


        :return: The description of this CreateBackupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateBackupDetails.
        Backup description


        :param description: The description of this CreateBackupDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateBackupDetails.
        Compartment identifier


        :return: The compartment_id of this CreateBackupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateBackupDetails.
        Compartment identifier


        :param compartment_id: The compartment_id of this CreateBackupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this CreateBackupDetails.
        Posgresql DbSystem identifier


        :return: The db_system_id of this CreateBackupDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateBackupDetails.
        Posgresql DbSystem identifier


        :param db_system_id: The db_system_id of this CreateBackupDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def retention_period(self):
        """
        Gets the retention_period of this CreateBackupDetails.
        Backup retention period in days.


        :return: The retention_period of this CreateBackupDetails.
        :rtype: int
        """
        return self._retention_period

    @retention_period.setter
    def retention_period(self, retention_period):
        """
        Sets the retention_period of this CreateBackupDetails.
        Backup retention period in days.


        :param retention_period: The retention_period of this CreateBackupDetails.
        :type: int
        """
        self._retention_period = retention_period

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBackupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateBackupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBackupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateBackupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateBackupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateBackupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other