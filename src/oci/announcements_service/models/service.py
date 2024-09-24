# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 0.0.1

from .base_service import BaseService
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Service(BaseService):
    """
    Summary of the service object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Service object with values from keyword arguments. The default value of the :py:attr:`~oci.announcements_service.models.Service.type` attribute
        of this class is ``Service`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Service.
        :type type: str

        :param id:
            The value to assign to the id property of this Service.
        :type id: str

        :param service_name:
            The value to assign to the service_name property of this Service.
        :type service_name: str

        :param short_name:
            The value to assign to the short_name property of this Service.
        :type short_name: str

        :param team_name:
            The value to assign to the team_name property of this Service.
        :type team_name: str

        :param platform_type:
            The value to assign to the platform_type property of this Service.
            Allowed values for this property are: "IAAS", "SAAS", "PAAS"
        :type platform_type: str

        :param comms_manager_name:
            The value to assign to the comms_manager_name property of this Service.
            Allowed values for this property are: "CN", "FUSION", "AS", "ERF"
        :type comms_manager_name: str

        :param excluded_realms:
            The value to assign to the excluded_realms property of this Service.
        :type excluded_realms: list[str]

        :param previous_service_names:
            The value to assign to the previous_service_names property of this Service.
        :type previous_service_names: list[str]

        :param time_created:
            The value to assign to the time_created property of this Service.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Service.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Service.
            Allowed values for this property are: "ACTIVE", "DELETED"
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'service_name': 'str',
            'short_name': 'str',
            'team_name': 'str',
            'platform_type': 'str',
            'comms_manager_name': 'str',
            'excluded_realms': 'list[str]',
            'previous_service_names': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'service_name': 'serviceName',
            'short_name': 'shortName',
            'team_name': 'teamName',
            'platform_type': 'platformType',
            'comms_manager_name': 'commsManagerName',
            'excluded_realms': 'excludedRealms',
            'previous_service_names': 'previousServiceNames',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState'
        }

        self._type = None
        self._id = None
        self._service_name = None
        self._short_name = None
        self._team_name = None
        self._platform_type = None
        self._comms_manager_name = None
        self._excluded_realms = None
        self._previous_service_names = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._type = 'Service'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other