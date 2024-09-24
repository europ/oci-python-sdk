# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkCreateSqlFirewallAllowedSqlsDetails(object):
    """
    The details used to append the violation logs as allowed SQLs
    """

    #: A constant which can be used with the log_type property of a BulkCreateSqlFirewallAllowedSqlsDetails.
    #: This constant has a value of "VIOLATION_LOG"
    LOG_TYPE_VIOLATION_LOG = "VIOLATION_LOG"

    def __init__(self, **kwargs):
        """
        Initializes a new BulkCreateSqlFirewallAllowedSqlsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_firewall_policy_id:
            The value to assign to the sql_firewall_policy_id property of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :type sql_firewall_policy_id: str

        :param log_type:
            The value to assign to the log_type property of this BulkCreateSqlFirewallAllowedSqlsDetails.
            Allowed values for this property are: "VIOLATION_LOG"
        :type log_type: str

        :param selection:
            The value to assign to the selection property of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :type selection: oci.data_safe.models.SelectionDetails

        """
        self.swagger_types = {
            'sql_firewall_policy_id': 'str',
            'log_type': 'str',
            'selection': 'SelectionDetails'
        }

        self.attribute_map = {
            'sql_firewall_policy_id': 'sqlFirewallPolicyId',
            'log_type': 'logType',
            'selection': 'selection'
        }

        self._sql_firewall_policy_id = None
        self._log_type = None
        self._selection = None

    @property
    def sql_firewall_policy_id(self):
        """
        **[Required]** Gets the sql_firewall_policy_id of this BulkCreateSqlFirewallAllowedSqlsDetails.
        The OCID of the SQL firewall policy where new allowed SQLs needs to be added.


        :return: The sql_firewall_policy_id of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :rtype: str
        """
        return self._sql_firewall_policy_id

    @sql_firewall_policy_id.setter
    def sql_firewall_policy_id(self, sql_firewall_policy_id):
        """
        Sets the sql_firewall_policy_id of this BulkCreateSqlFirewallAllowedSqlsDetails.
        The OCID of the SQL firewall policy where new allowed SQLs needs to be added.


        :param sql_firewall_policy_id: The sql_firewall_policy_id of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :type: str
        """
        self._sql_firewall_policy_id = sql_firewall_policy_id

    @property
    def log_type(self):
        """
        **[Required]** Gets the log_type of this BulkCreateSqlFirewallAllowedSqlsDetails.
        The type of log to be added as an allowed sql.

        Allowed values for this property are: "VIOLATION_LOG"


        :return: The log_type of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """
        Sets the log_type of this BulkCreateSqlFirewallAllowedSqlsDetails.
        The type of log to be added as an allowed sql.


        :param log_type: The log_type of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :type: str
        """
        allowed_values = ["VIOLATION_LOG"]
        if not value_allowed_none_or_none_sentinel(log_type, allowed_values):
            raise ValueError(
                f"Invalid value for `log_type`, must be None or one of {allowed_values}"
            )
        self._log_type = log_type

    @property
    def selection(self):
        """
        **[Required]** Gets the selection of this BulkCreateSqlFirewallAllowedSqlsDetails.

        :return: The selection of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :rtype: oci.data_safe.models.SelectionDetails
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """
        Sets the selection of this BulkCreateSqlFirewallAllowedSqlsDetails.

        :param selection: The selection of this BulkCreateSqlFirewallAllowedSqlsDetails.
        :type: oci.data_safe.models.SelectionDetails
        """
        self._selection = selection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
