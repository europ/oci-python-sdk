# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PullRequestAttachment(object):
    """
    Pull Request attachment created by users.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PullRequestAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PullRequestAttachment.
        :type id: str

        :param pull_request_id:
            The value to assign to the pull_request_id property of this PullRequestAttachment.
        :type pull_request_id: str

        :param file_name:
            The value to assign to the file_name property of this PullRequestAttachment.
        :type file_name: str

        :param time_created:
            The value to assign to the time_created property of this PullRequestAttachment.
        :type time_created: datetime

        :param created_by:
            The value to assign to the created_by property of this PullRequestAttachment.
        :type created_by: oci.devops.models.PrincipalDetails

        """
        self.swagger_types = {
            'id': 'str',
            'pull_request_id': 'str',
            'file_name': 'str',
            'time_created': 'datetime',
            'created_by': 'PrincipalDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'pull_request_id': 'pullRequestId',
            'file_name': 'fileName',
            'time_created': 'timeCreated',
            'created_by': 'createdBy'
        }

        self._id = None
        self._pull_request_id = None
        self._file_name = None
        self._time_created = None
        self._created_by = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PullRequestAttachment.
        Unique identifier that is immutable on creation


        :return: The id of this PullRequestAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PullRequestAttachment.
        Unique identifier that is immutable on creation


        :param id: The id of this PullRequestAttachment.
        :type: str
        """
        self._id = id

    @property
    def pull_request_id(self):
        """
        **[Required]** Gets the pull_request_id of this PullRequestAttachment.
        OCID of the pull request that this attachment belongs to


        :return: The pull_request_id of this PullRequestAttachment.
        :rtype: str
        """
        return self._pull_request_id

    @pull_request_id.setter
    def pull_request_id(self, pull_request_id):
        """
        Sets the pull_request_id of this PullRequestAttachment.
        OCID of the pull request that this attachment belongs to


        :param pull_request_id: The pull_request_id of this PullRequestAttachment.
        :type: str
        """
        self._pull_request_id = pull_request_id

    @property
    def file_name(self):
        """
        **[Required]** Gets the file_name of this PullRequestAttachment.
        name to display in description or comment


        :return: The file_name of this PullRequestAttachment.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this PullRequestAttachment.
        name to display in description or comment


        :param file_name: The file_name of this PullRequestAttachment.
        :type: str
        """
        self._file_name = file_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PullRequestAttachment.
        Creation timestamp. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this PullRequestAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PullRequestAttachment.
        Creation timestamp. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this PullRequestAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this PullRequestAttachment.

        :return: The created_by of this PullRequestAttachment.
        :rtype: oci.devops.models.PrincipalDetails
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this PullRequestAttachment.

        :param created_by: The created_by of this PullRequestAttachment.
        :type: oci.devops.models.PrincipalDetails
        """
        self._created_by = created_by

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other