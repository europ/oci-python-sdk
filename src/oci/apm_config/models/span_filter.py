# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config import Config
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SpanFilter(Config):
    """
    A named setting that specifies the filter criteria to match a subset of the spans.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SpanFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_config.models.SpanFilter.config_type` attribute
        of this class is ``SPAN_FILTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SpanFilter.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this SpanFilter.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"
        :type config_type: str

        :param time_created:
            The value to assign to the time_created property of this SpanFilter.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SpanFilter.
        :type time_updated: datetime

        :param created_by:
            The value to assign to the created_by property of this SpanFilter.
        :type created_by: str

        :param updated_by:
            The value to assign to the updated_by property of this SpanFilter.
        :type updated_by: str

        :param etag:
            The value to assign to the etag property of this SpanFilter.
        :type etag: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SpanFilter.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SpanFilter.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this SpanFilter.
        :type display_name: str

        :param filter_text:
            The value to assign to the filter_text property of this SpanFilter.
        :type filter_text: str

        :param in_use_by:
            The value to assign to the in_use_by property of this SpanFilter.
        :type in_use_by: list[oci.apm_config.models.SpanFilterReference]

        :param description:
            The value to assign to the description property of this SpanFilter.
        :type description: str

        """
        self.swagger_types = {
            'id': 'str',
            'config_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by': 'str',
            'updated_by': 'str',
            'etag': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'filter_text': 'str',
            'in_use_by': 'list[SpanFilterReference]',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'config_type': 'configType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by': 'createdBy',
            'updated_by': 'updatedBy',
            'etag': 'etag',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'filter_text': 'filterText',
            'in_use_by': 'inUseBy',
            'description': 'description'
        }

        self._id = None
        self._config_type = None
        self._time_created = None
        self._time_updated = None
        self._created_by = None
        self._updated_by = None
        self._etag = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._filter_text = None
        self._in_use_by = None
        self._description = None
        self._config_type = 'SPAN_FILTER'

    @property
    def display_name(self):
        """
        Gets the display_name of this SpanFilter.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this SpanFilter.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SpanFilter.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this SpanFilter.
        :type: str
        """
        self._display_name = display_name

    @property
    def filter_text(self):
        """
        Gets the filter_text of this SpanFilter.
        The string that defines the Span Filter expression.


        :return: The filter_text of this SpanFilter.
        :rtype: str
        """
        return self._filter_text

    @filter_text.setter
    def filter_text(self, filter_text):
        """
        Sets the filter_text of this SpanFilter.
        The string that defines the Span Filter expression.


        :param filter_text: The filter_text of this SpanFilter.
        :type: str
        """
        self._filter_text = filter_text

    @property
    def in_use_by(self):
        """
        Gets the in_use_by of this SpanFilter.
        The list of configuration items that reference the span filter.


        :return: The in_use_by of this SpanFilter.
        :rtype: list[oci.apm_config.models.SpanFilterReference]
        """
        return self._in_use_by

    @in_use_by.setter
    def in_use_by(self, in_use_by):
        """
        Sets the in_use_by of this SpanFilter.
        The list of configuration items that reference the span filter.


        :param in_use_by: The in_use_by of this SpanFilter.
        :type: list[oci.apm_config.models.SpanFilterReference]
        """
        self._in_use_by = in_use_by

    @property
    def description(self):
        """
        Gets the description of this SpanFilter.
        An optional string that describes what the span filter is intended or used for.


        :return: The description of this SpanFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SpanFilter.
        An optional string that describes what the span filter is intended or used for.


        :param description: The description of this SpanFilter.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
