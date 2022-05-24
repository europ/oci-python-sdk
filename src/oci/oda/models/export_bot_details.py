# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportBotDetails(object):
    """
    Properties to export a Bot to Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportBotDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target:
            The value to assign to the target property of this ExportBotDetails.
        :type target: oci.oda.models.StorageLocation

        """
        self.swagger_types = {
            'target': 'StorageLocation'
        }

        self.attribute_map = {
            'target': 'target'
        }

        self._target = None

    @property
    def target(self):
        """
        **[Required]** Gets the target of this ExportBotDetails.

        :return: The target of this ExportBotDetails.
        :rtype: oci.oda.models.StorageLocation
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this ExportBotDetails.

        :param target: The target of this ExportBotDetails.
        :type: oci.oda.models.StorageLocation
        """
        self._target = target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
