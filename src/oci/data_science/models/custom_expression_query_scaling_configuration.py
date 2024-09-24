# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .scaling_configuration import ScalingConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomExpressionQueryScalingConfiguration(ScalingConfiguration):
    """
    The scaling configuration for the custom metric expression rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomExpressionQueryScalingConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.CustomExpressionQueryScalingConfiguration.scaling_configuration_type` attribute
        of this class is ``QUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scaling_configuration_type:
            The value to assign to the scaling_configuration_type property of this CustomExpressionQueryScalingConfiguration.
            Allowed values for this property are: "THRESHOLD", "QUERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scaling_configuration_type: str

        :param pending_duration:
            The value to assign to the pending_duration property of this CustomExpressionQueryScalingConfiguration.
        :type pending_duration: str

        :param instance_count_adjustment:
            The value to assign to the instance_count_adjustment property of this CustomExpressionQueryScalingConfiguration.
        :type instance_count_adjustment: int

        :param query:
            The value to assign to the query property of this CustomExpressionQueryScalingConfiguration.
        :type query: str

        """
        self.swagger_types = {
            'scaling_configuration_type': 'str',
            'pending_duration': 'str',
            'instance_count_adjustment': 'int',
            'query': 'str'
        }

        self.attribute_map = {
            'scaling_configuration_type': 'scalingConfigurationType',
            'pending_duration': 'pendingDuration',
            'instance_count_adjustment': 'instanceCountAdjustment',
            'query': 'query'
        }

        self._scaling_configuration_type = None
        self._pending_duration = None
        self._instance_count_adjustment = None
        self._query = None
        self._scaling_configuration_type = 'QUERY'

    @property
    def query(self):
        """
        **[Required]** Gets the query of this CustomExpressionQueryScalingConfiguration.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally
        specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`.

        Example of threshold alarm:

          -----

            CPUUtilization[1m]{resourceId = \"MODEL_DEPLOYMENT_OCID\"}.grouping().mean() < 25
            CPUUtilization[1m]{resourceId = \"MODEL_DEPLOYMENT_OCID\"}.grouping().mean() > 75

          -----


        :return: The query of this CustomExpressionQueryScalingConfiguration.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this CustomExpressionQueryScalingConfiguration.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally
        specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`.

        Example of threshold alarm:

          -----

            CPUUtilization[1m]{resourceId = \"MODEL_DEPLOYMENT_OCID\"}.grouping().mean() < 25
            CPUUtilization[1m]{resourceId = \"MODEL_DEPLOYMENT_OCID\"}.grouping().mean() > 75

          -----


        :param query: The query of this CustomExpressionQueryScalingConfiguration.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
