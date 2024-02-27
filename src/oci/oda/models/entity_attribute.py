# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityAttribute(object):
    """
    Attribute of an entity
    """

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "TEXT"
    TYPE_TEXT = "TEXT"

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "NUMBER"
    TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "DATE_TIME"
    TYPE_DATE_TIME = "DATE_TIME"

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "DATE"
    TYPE_DATE = "DATE"

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "ENTITY"
    TYPE_ENTITY = "ENTITY"

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "COMPOSITE_ENTITY"
    TYPE_COMPOSITE_ENTITY = "COMPOSITE_ENTITY"

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "ATTRIBUTE_REFERENCE"
    TYPE_ATTRIBUTE_REFERENCE = "ATTRIBUTE_REFERENCE"

    #: A constant which can be used with the type property of a EntityAttribute.
    #: This constant has a value of "BOOLEAN"
    TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the temporal_preference property of a EntityAttribute.
    #: This constant has a value of "PAST"
    TEMPORAL_PREFERENCE_PAST = "PAST"

    #: A constant which can be used with the temporal_preference property of a EntityAttribute.
    #: This constant has a value of "FUTURE"
    TEMPORAL_PREFERENCE_FUTURE = "FUTURE"

    #: A constant which can be used with the temporal_preference property of a EntityAttribute.
    #: This constant has a value of "NEAREST"
    TEMPORAL_PREFERENCE_NEAREST = "NEAREST"

    def __init__(self, **kwargs):
        """
        Initializes a new EntityAttribute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this EntityAttribute.
        :type name: str

        :param type:
            The value to assign to the type property of this EntityAttribute.
            Allowed values for this property are: "TEXT", "NUMBER", "DATE_TIME", "DATE", "ENTITY", "COMPOSITE_ENTITY", "ATTRIBUTE_REFERENCE", "BOOLEAN"
        :type type: str

        :param natural_language_mapping:
            The value to assign to the natural_language_mapping property of this EntityAttribute.
        :type natural_language_mapping: oci.oda.models.EntityAttributeNaturalLanguageMapping

        :param is_multi_value:
            The value to assign to the is_multi_value property of this EntityAttribute.
        :type is_multi_value: bool

        :param is_fuzzy_match:
            The value to assign to the is_fuzzy_match property of this EntityAttribute.
        :type is_fuzzy_match: bool

        :param is_invert_comparisons:
            The value to assign to the is_invert_comparisons property of this EntityAttribute.
        :type is_invert_comparisons: bool

        :param temporal_preference:
            The value to assign to the temporal_preference property of this EntityAttribute.
            Allowed values for this property are: "PAST", "FUTURE", "NEAREST"
        :type temporal_preference: str

        :param entity_name:
            The value to assign to the entity_name property of this EntityAttribute.
        :type entity_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'natural_language_mapping': 'EntityAttributeNaturalLanguageMapping',
            'is_multi_value': 'bool',
            'is_fuzzy_match': 'bool',
            'is_invert_comparisons': 'bool',
            'temporal_preference': 'str',
            'entity_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'natural_language_mapping': 'naturalLanguageMapping',
            'is_multi_value': 'isMultiValue',
            'is_fuzzy_match': 'isFuzzyMatch',
            'is_invert_comparisons': 'isInvertComparisons',
            'temporal_preference': 'temporalPreference',
            'entity_name': 'entityName'
        }

        self._name = None
        self._type = None
        self._natural_language_mapping = None
        self._is_multi_value = None
        self._is_fuzzy_match = None
        self._is_invert_comparisons = None
        self._temporal_preference = None
        self._entity_name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this EntityAttribute.
        The name of an entity attribute


        :return: The name of this EntityAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EntityAttribute.
        The name of an entity attribute


        :param name: The name of this EntityAttribute.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this EntityAttribute.
        The type of an entity attribute

        Allowed values for this property are: "TEXT", "NUMBER", "DATE_TIME", "DATE", "ENTITY", "COMPOSITE_ENTITY", "ATTRIBUTE_REFERENCE", "BOOLEAN"


        :return: The type of this EntityAttribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EntityAttribute.
        The type of an entity attribute


        :param type: The type of this EntityAttribute.
        :type: str
        """
        allowed_values = ["TEXT", "NUMBER", "DATE_TIME", "DATE", "ENTITY", "COMPOSITE_ENTITY", "ATTRIBUTE_REFERENCE", "BOOLEAN"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def natural_language_mapping(self):
        """
        Gets the natural_language_mapping of this EntityAttribute.

        :return: The natural_language_mapping of this EntityAttribute.
        :rtype: oci.oda.models.EntityAttributeNaturalLanguageMapping
        """
        return self._natural_language_mapping

    @natural_language_mapping.setter
    def natural_language_mapping(self, natural_language_mapping):
        """
        Sets the natural_language_mapping of this EntityAttribute.

        :param natural_language_mapping: The natural_language_mapping of this EntityAttribute.
        :type: oci.oda.models.EntityAttributeNaturalLanguageMapping
        """
        self._natural_language_mapping = natural_language_mapping

    @property
    def is_multi_value(self):
        """
        Gets the is_multi_value of this EntityAttribute.
        Is the entity attribute multi-value


        :return: The is_multi_value of this EntityAttribute.
        :rtype: bool
        """
        return self._is_multi_value

    @is_multi_value.setter
    def is_multi_value(self, is_multi_value):
        """
        Sets the is_multi_value of this EntityAttribute.
        Is the entity attribute multi-value


        :param is_multi_value: The is_multi_value of this EntityAttribute.
        :type: bool
        """
        self._is_multi_value = is_multi_value

    @property
    def is_fuzzy_match(self):
        """
        Gets the is_fuzzy_match of this EntityAttribute.
        Is the entity attribute a fuzzy match


        :return: The is_fuzzy_match of this EntityAttribute.
        :rtype: bool
        """
        return self._is_fuzzy_match

    @is_fuzzy_match.setter
    def is_fuzzy_match(self, is_fuzzy_match):
        """
        Sets the is_fuzzy_match of this EntityAttribute.
        Is the entity attribute a fuzzy match


        :param is_fuzzy_match: The is_fuzzy_match of this EntityAttribute.
        :type: bool
        """
        self._is_fuzzy_match = is_fuzzy_match

    @property
    def is_invert_comparisons(self):
        """
        Gets the is_invert_comparisons of this EntityAttribute.
        Are comparisons inverted in the entity attribute


        :return: The is_invert_comparisons of this EntityAttribute.
        :rtype: bool
        """
        return self._is_invert_comparisons

    @is_invert_comparisons.setter
    def is_invert_comparisons(self, is_invert_comparisons):
        """
        Sets the is_invert_comparisons of this EntityAttribute.
        Are comparisons inverted in the entity attribute


        :param is_invert_comparisons: The is_invert_comparisons of this EntityAttribute.
        :type: bool
        """
        self._is_invert_comparisons = is_invert_comparisons

    @property
    def temporal_preference(self):
        """
        Gets the temporal_preference of this EntityAttribute.
        Temporal preference of an attribute

        Allowed values for this property are: "PAST", "FUTURE", "NEAREST"


        :return: The temporal_preference of this EntityAttribute.
        :rtype: str
        """
        return self._temporal_preference

    @temporal_preference.setter
    def temporal_preference(self, temporal_preference):
        """
        Sets the temporal_preference of this EntityAttribute.
        Temporal preference of an attribute


        :param temporal_preference: The temporal_preference of this EntityAttribute.
        :type: str
        """
        allowed_values = ["PAST", "FUTURE", "NEAREST"]
        if not value_allowed_none_or_none_sentinel(temporal_preference, allowed_values):
            raise ValueError(
                f"Invalid value for `temporal_preference`, must be None or one of {allowed_values}"
            )
        self._temporal_preference = temporal_preference

    @property
    def entity_name(self):
        """
        Gets the entity_name of this EntityAttribute.
        Name of referenced entity.


        :return: The entity_name of this EntityAttribute.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this EntityAttribute.
        Name of referenced entity.


        :param entity_name: The entity_name of this EntityAttribute.
        :type: str
        """
        self._entity_name = entity_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
