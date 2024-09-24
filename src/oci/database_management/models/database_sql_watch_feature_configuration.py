# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .database_feature_configuration import DatabaseFeatureConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseSqlWatchFeatureConfiguration(DatabaseFeatureConfiguration):
    """
    The details required to enable the SQL Watch feature.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseSqlWatchFeatureConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DatabaseSqlWatchFeatureConfiguration.feature` attribute
        of this class is ``SQLWATCH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature:
            The value to assign to the feature property of this DatabaseSqlWatchFeatureConfiguration.
            Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT", "DB_LIFECYCLE_MANAGEMENT", "SQLWATCH"
        :type feature: str

        :param feature_status:
            The value to assign to the feature_status property of this DatabaseSqlWatchFeatureConfiguration.
            Allowed values for this property are: "ENABLED", "NOT_ENABLED", "UNSUPPORTED", "FAILED_ENABLING", "FAILED_DISABLING", "FAILED", "ENABLED_WITH_WARNINGS", "PENDING_DISABLE", "ENABLING", "DISABLING"
        :type feature_status: str

        :param connector_details:
            The value to assign to the connector_details property of this DatabaseSqlWatchFeatureConfiguration.
        :type connector_details: oci.database_management.models.ConnectorDetails

        :param database_connection_details:
            The value to assign to the database_connection_details property of this DatabaseSqlWatchFeatureConfiguration.
        :type database_connection_details: oci.database_management.models.DatabaseConnectionDetails

        """
        self.swagger_types = {
            'feature': 'str',
            'feature_status': 'str',
            'connector_details': 'ConnectorDetails',
            'database_connection_details': 'DatabaseConnectionDetails'
        }

        self.attribute_map = {
            'feature': 'feature',
            'feature_status': 'featureStatus',
            'connector_details': 'connectorDetails',
            'database_connection_details': 'databaseConnectionDetails'
        }

        self._feature = None
        self._feature_status = None
        self._connector_details = None
        self._database_connection_details = None
        self._feature = 'SQLWATCH'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other