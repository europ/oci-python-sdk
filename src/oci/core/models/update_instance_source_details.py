# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInstanceSourceDetails(object):
    """
    The details for updating the instance source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInstanceSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.UpdateInstanceSourceViaBootVolumeDetails`
        * :class:`~oci.core.models.UpdateInstanceSourceViaImageDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this UpdateInstanceSourceDetails.
        :type source_type: str

        :param is_preserve_boot_volume_enabled:
            The value to assign to the is_preserve_boot_volume_enabled property of this UpdateInstanceSourceDetails.
        :type is_preserve_boot_volume_enabled: bool

        """
        self.swagger_types = {
            'source_type': 'str',
            'is_preserve_boot_volume_enabled': 'bool'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'is_preserve_boot_volume_enabled': 'isPreserveBootVolumeEnabled'
        }

        self._source_type = None
        self._is_preserve_boot_volume_enabled = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sourceType']

        if type == 'bootVolume':
            return 'UpdateInstanceSourceViaBootVolumeDetails'

        if type == 'image':
            return 'UpdateInstanceSourceViaImageDetails'
        else:
            return 'UpdateInstanceSourceDetails'

    @property
    def source_type(self):
        """
        **[Required]** Gets the source_type of this UpdateInstanceSourceDetails.
        The source type for the instance.
        Use `image` when specifying the image OCID. Use `bootVolume` when specifying
        the boot volume OCID.


        :return: The source_type of this UpdateInstanceSourceDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this UpdateInstanceSourceDetails.
        The source type for the instance.
        Use `image` when specifying the image OCID. Use `bootVolume` when specifying
        the boot volume OCID.


        :param source_type: The source_type of this UpdateInstanceSourceDetails.
        :type: str
        """
        self._source_type = source_type

    @property
    def is_preserve_boot_volume_enabled(self):
        """
        Gets the is_preserve_boot_volume_enabled of this UpdateInstanceSourceDetails.
        Whether to preserve the boot volume that was previously attached to the instance after a successful replacement of that boot volume.


        :return: The is_preserve_boot_volume_enabled of this UpdateInstanceSourceDetails.
        :rtype: bool
        """
        return self._is_preserve_boot_volume_enabled

    @is_preserve_boot_volume_enabled.setter
    def is_preserve_boot_volume_enabled(self, is_preserve_boot_volume_enabled):
        """
        Sets the is_preserve_boot_volume_enabled of this UpdateInstanceSourceDetails.
        Whether to preserve the boot volume that was previously attached to the instance after a successful replacement of that boot volume.


        :param is_preserve_boot_volume_enabled: The is_preserve_boot_volume_enabled of this UpdateInstanceSourceDetails.
        :type: bool
        """
        self._is_preserve_boot_volume_enabled = is_preserve_boot_volume_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other