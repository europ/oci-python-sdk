# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GroupExtDomainLevelSchemaNames(object):
    """
    DBCS Domain-level schema-names. Each value is specific to a DB Domain.

    **Added In:** 18.2.4

    **SCIM++ Properties:**
    - idcsCompositeKey: [domainName, schemaName]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readOnly
    - required: false
    - returned: request
    - type: complex
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GroupExtDomainLevelSchemaNames object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param domain_name:
            The value to assign to the domain_name property of this GroupExtDomainLevelSchemaNames.
        :type domain_name: str

        :param schema_name:
            The value to assign to the schema_name property of this GroupExtDomainLevelSchemaNames.
        :type schema_name: str

        """
        self.swagger_types = {
            'domain_name': 'str',
            'schema_name': 'str'
        }

        self.attribute_map = {
            'domain_name': 'domainName',
            'schema_name': 'schemaName'
        }

        self._domain_name = None
        self._schema_name = None

    @property
    def domain_name(self):
        """
        **[Required]** Gets the domain_name of this GroupExtDomainLevelSchemaNames.
        DBCS Domain Name

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_name of this GroupExtDomainLevelSchemaNames.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this GroupExtDomainLevelSchemaNames.
        DBCS Domain Name

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_name: The domain_name of this GroupExtDomainLevelSchemaNames.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this GroupExtDomainLevelSchemaNames.
        The DBCS schema-name granted to this group in the DB domain that 'domainName' specifies.

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schema_name of this GroupExtDomainLevelSchemaNames.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this GroupExtDomainLevelSchemaNames.
        The DBCS schema-name granted to this group in the DB domain that 'domainName' specifies.

        **Added In:** 18.2.4

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schema_name: The schema_name of this GroupExtDomainLevelSchemaNames.
        :type: str
        """
        self._schema_name = schema_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other