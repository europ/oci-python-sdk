# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateProductLicenseDetails(object):
    """
    Details for creating a new product license.
    """

    #: A constant which can be used with the license_unit property of a CreateProductLicenseDetails.
    #: This constant has a value of "OCPU"
    LICENSE_UNIT_OCPU = "OCPU"

    #: A constant which can be used with the license_unit property of a CreateProductLicenseDetails.
    #: This constant has a value of "NAMED_USER_PLUS"
    LICENSE_UNIT_NAMED_USER_PLUS = "NAMED_USER_PLUS"

    #: A constant which can be used with the license_unit property of a CreateProductLicenseDetails.
    #: This constant has a value of "PROCESSORS"
    LICENSE_UNIT_PROCESSORS = "PROCESSORS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateProductLicenseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateProductLicenseDetails.
        :type compartment_id: str

        :param is_vendor_oracle:
            The value to assign to the is_vendor_oracle property of this CreateProductLicenseDetails.
        :type is_vendor_oracle: bool

        :param display_name:
            The value to assign to the display_name property of this CreateProductLicenseDetails.
        :type display_name: str

        :param license_unit:
            The value to assign to the license_unit property of this CreateProductLicenseDetails.
            Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS"
        :type license_unit: str

        :param vendor_name:
            The value to assign to the vendor_name property of this CreateProductLicenseDetails.
        :type vendor_name: str

        :param images:
            The value to assign to the images property of this CreateProductLicenseDetails.
        :type images: list[oci.license_manager.models.ImageDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateProductLicenseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateProductLicenseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'is_vendor_oracle': 'bool',
            'display_name': 'str',
            'license_unit': 'str',
            'vendor_name': 'str',
            'images': 'list[ImageDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'is_vendor_oracle': 'isVendorOracle',
            'display_name': 'displayName',
            'license_unit': 'licenseUnit',
            'vendor_name': 'vendorName',
            'images': 'images',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._is_vendor_oracle = None
        self._display_name = None
        self._license_unit = None
        self._vendor_name = None
        self._images = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateProductLicenseDetails.
        The compartment `OCID`__ where product licenses are created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateProductLicenseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateProductLicenseDetails.
        The compartment `OCID`__ where product licenses are created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateProductLicenseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_vendor_oracle(self):
        """
        **[Required]** Gets the is_vendor_oracle of this CreateProductLicenseDetails.
        Specifies if the product license vendor is Oracle or a third party.


        :return: The is_vendor_oracle of this CreateProductLicenseDetails.
        :rtype: bool
        """
        return self._is_vendor_oracle

    @is_vendor_oracle.setter
    def is_vendor_oracle(self, is_vendor_oracle):
        """
        Sets the is_vendor_oracle of this CreateProductLicenseDetails.
        Specifies if the product license vendor is Oracle or a third party.


        :param is_vendor_oracle: The is_vendor_oracle of this CreateProductLicenseDetails.
        :type: bool
        """
        self._is_vendor_oracle = is_vendor_oracle

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateProductLicenseDetails.
        Name of the product license.


        :return: The display_name of this CreateProductLicenseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateProductLicenseDetails.
        Name of the product license.


        :param display_name: The display_name of this CreateProductLicenseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def license_unit(self):
        """
        **[Required]** Gets the license_unit of this CreateProductLicenseDetails.
        The product license unit.

        Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS"


        :return: The license_unit of this CreateProductLicenseDetails.
        :rtype: str
        """
        return self._license_unit

    @license_unit.setter
    def license_unit(self, license_unit):
        """
        Sets the license_unit of this CreateProductLicenseDetails.
        The product license unit.


        :param license_unit: The license_unit of this CreateProductLicenseDetails.
        :type: str
        """
        allowed_values = ["OCPU", "NAMED_USER_PLUS", "PROCESSORS"]
        if not value_allowed_none_or_none_sentinel(license_unit, allowed_values):
            raise ValueError(
                "Invalid value for `license_unit`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_unit = license_unit

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this CreateProductLicenseDetails.
        The product license vendor name, for example: Microsoft, RHEL, and so on.


        :return: The vendor_name of this CreateProductLicenseDetails.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this CreateProductLicenseDetails.
        The product license vendor name, for example: Microsoft, RHEL, and so on.


        :param vendor_name: The vendor_name of this CreateProductLicenseDetails.
        :type: str
        """
        self._vendor_name = vendor_name

    @property
    def images(self):
        """
        Gets the images of this CreateProductLicenseDetails.
        The image details associated with the product license.


        :return: The images of this CreateProductLicenseDetails.
        :rtype: list[oci.license_manager.models.ImageDetails]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this CreateProductLicenseDetails.
        The image details associated with the product license.


        :param images: The images of this CreateProductLicenseDetails.
        :type: list[oci.license_manager.models.ImageDetails]
        """
        self._images = images

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateProductLicenseDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateProductLicenseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateProductLicenseDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateProductLicenseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateProductLicenseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateProductLicenseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateProductLicenseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateProductLicenseDetails.
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
