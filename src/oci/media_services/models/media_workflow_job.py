# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MediaWorkflowJob(object):
    """
    A MediaWorkflowJob represents a run of a MediaWorkflow for a specific set of parameters and configurations.
    """

    #: A constant which can be used with the lifecycle_state property of a MediaWorkflowJob.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a MediaWorkflowJob.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a MediaWorkflowJob.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a MediaWorkflowJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a MediaWorkflowJob.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a MediaWorkflowJob.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a MediaWorkflowJob.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new MediaWorkflowJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param media_workflow_configuration_ids:
            The value to assign to the media_workflow_configuration_ids property of this MediaWorkflowJob.
        :type media_workflow_configuration_ids: list[str]

        :param media_workflow_id:
            The value to assign to the media_workflow_id property of this MediaWorkflowJob.
        :type media_workflow_id: str

        :param id:
            The value to assign to the id property of this MediaWorkflowJob.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MediaWorkflowJob.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MediaWorkflowJob.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MediaWorkflowJob.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MediaWorkflowJob.
        :type lifecycle_details: str

        :param task_lifecycle_state:
            The value to assign to the task_lifecycle_state property of this MediaWorkflowJob.
        :type task_lifecycle_state: list[oci.media_services.models.MediaWorkflowTaskState]

        :param parameters:
            The value to assign to the parameters property of this MediaWorkflowJob.
        :type parameters: dict(str, object)

        :param time_created:
            The value to assign to the time_created property of this MediaWorkflowJob.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MediaWorkflowJob.
        :type time_updated: datetime

        :param runnable:
            The value to assign to the runnable property of this MediaWorkflowJob.
        :type runnable: dict(str, object)

        :param outputs:
            The value to assign to the outputs property of this MediaWorkflowJob.
        :type outputs: list[oci.media_services.models.JobOutput]

        :param time_started:
            The value to assign to the time_started property of this MediaWorkflowJob.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this MediaWorkflowJob.
        :type time_ended: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MediaWorkflowJob.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MediaWorkflowJob.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MediaWorkflowJob.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'media_workflow_configuration_ids': 'list[str]',
            'media_workflow_id': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'task_lifecycle_state': 'list[MediaWorkflowTaskState]',
            'parameters': 'dict(str, object)',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'runnable': 'dict(str, object)',
            'outputs': 'list[JobOutput]',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'media_workflow_configuration_ids': 'mediaWorkflowConfigurationIds',
            'media_workflow_id': 'mediaWorkflowId',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'task_lifecycle_state': 'taskLifecycleState',
            'parameters': 'parameters',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'runnable': 'runnable',
            'outputs': 'outputs',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._media_workflow_configuration_ids = None
        self._media_workflow_id = None
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._task_lifecycle_state = None
        self._parameters = None
        self._time_created = None
        self._time_updated = None
        self._runnable = None
        self._outputs = None
        self._time_started = None
        self._time_ended = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def media_workflow_configuration_ids(self):
        """
        Gets the media_workflow_configuration_ids of this MediaWorkflowJob.
        Configurations to be applied to this run of the workflow.


        :return: The media_workflow_configuration_ids of this MediaWorkflowJob.
        :rtype: list[str]
        """
        return self._media_workflow_configuration_ids

    @media_workflow_configuration_ids.setter
    def media_workflow_configuration_ids(self, media_workflow_configuration_ids):
        """
        Sets the media_workflow_configuration_ids of this MediaWorkflowJob.
        Configurations to be applied to this run of the workflow.


        :param media_workflow_configuration_ids: The media_workflow_configuration_ids of this MediaWorkflowJob.
        :type: list[str]
        """
        self._media_workflow_configuration_ids = media_workflow_configuration_ids

    @property
    def media_workflow_id(self):
        """
        **[Required]** Gets the media_workflow_id of this MediaWorkflowJob.
        The workflow to execute.


        :return: The media_workflow_id of this MediaWorkflowJob.
        :rtype: str
        """
        return self._media_workflow_id

    @media_workflow_id.setter
    def media_workflow_id(self, media_workflow_id):
        """
        Sets the media_workflow_id of this MediaWorkflowJob.
        The workflow to execute.


        :param media_workflow_id: The media_workflow_id of this MediaWorkflowJob.
        :type: str
        """
        self._media_workflow_id = media_workflow_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MediaWorkflowJob.
        Unique identifier for this run of the workflow.


        :return: The id of this MediaWorkflowJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MediaWorkflowJob.
        Unique identifier for this run of the workflow.


        :param id: The id of this MediaWorkflowJob.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MediaWorkflowJob.
        Compartment Identifier.


        :return: The compartment_id of this MediaWorkflowJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MediaWorkflowJob.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this MediaWorkflowJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this MediaWorkflowJob.
        Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.


        :return: The display_name of this MediaWorkflowJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MediaWorkflowJob.
        Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this MediaWorkflowJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MediaWorkflowJob.
        The current state of the MediaWorkflowJob.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MediaWorkflowJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MediaWorkflowJob.
        The current state of the MediaWorkflowJob.


        :param lifecycle_state: The lifecycle_state of this MediaWorkflowJob.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MediaWorkflowJob.
        The lifecyle details.


        :return: The lifecycle_details of this MediaWorkflowJob.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MediaWorkflowJob.
        The lifecyle details.


        :param lifecycle_details: The lifecycle_details of this MediaWorkflowJob.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def task_lifecycle_state(self):
        """
        Gets the task_lifecycle_state of this MediaWorkflowJob.
        Status of each task.


        :return: The task_lifecycle_state of this MediaWorkflowJob.
        :rtype: list[oci.media_services.models.MediaWorkflowTaskState]
        """
        return self._task_lifecycle_state

    @task_lifecycle_state.setter
    def task_lifecycle_state(self, task_lifecycle_state):
        """
        Sets the task_lifecycle_state of this MediaWorkflowJob.
        Status of each task.


        :param task_lifecycle_state: The task_lifecycle_state of this MediaWorkflowJob.
        :type: list[oci.media_services.models.MediaWorkflowTaskState]
        """
        self._task_lifecycle_state = task_lifecycle_state

    @property
    def parameters(self):
        """
        Gets the parameters of this MediaWorkflowJob.
        Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow,
        the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this
        MediaWorkflowJob. The parameters are given as JSON.  The top level and 2nd level elements must be
        JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level
        keys refer to a parameter's name.


        :return: The parameters of this MediaWorkflowJob.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this MediaWorkflowJob.
        Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow,
        the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this
        MediaWorkflowJob. The parameters are given as JSON.  The top level and 2nd level elements must be
        JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level
        keys refer to a parameter's name.


        :param parameters: The parameters of this MediaWorkflowJob.
        :type: dict(str, object)
        """
        self._parameters = parameters

    @property
    def time_created(self):
        """
        Gets the time_created of this MediaWorkflowJob.
        Creation time of the job. An RFC3339 formatted datetime string.


        :return: The time_created of this MediaWorkflowJob.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MediaWorkflowJob.
        Creation time of the job. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MediaWorkflowJob.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MediaWorkflowJob.
        Updated time of the job. An RFC3339 formatted datetime string.


        :return: The time_updated of this MediaWorkflowJob.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MediaWorkflowJob.
        Updated time of the job. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MediaWorkflowJob.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def runnable(self):
        """
        Gets the runnable of this MediaWorkflowJob.
        A JSON representation of the job as it will be run by the system. All the task declarations, configurations
        and parameters are merged. Parameter values are all fully resolved.


        :return: The runnable of this MediaWorkflowJob.
        :rtype: dict(str, object)
        """
        return self._runnable

    @runnable.setter
    def runnable(self, runnable):
        """
        Sets the runnable of this MediaWorkflowJob.
        A JSON representation of the job as it will be run by the system. All the task declarations, configurations
        and parameters are merged. Parameter values are all fully resolved.


        :param runnable: The runnable of this MediaWorkflowJob.
        :type: dict(str, object)
        """
        self._runnable = runnable

    @property
    def outputs(self):
        """
        Gets the outputs of this MediaWorkflowJob.
        A list of JobOutput for the workflowJob.


        :return: The outputs of this MediaWorkflowJob.
        :rtype: list[oci.media_services.models.JobOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Sets the outputs of this MediaWorkflowJob.
        A list of JobOutput for the workflowJob.


        :param outputs: The outputs of this MediaWorkflowJob.
        :type: list[oci.media_services.models.JobOutput]
        """
        self._outputs = outputs

    @property
    def time_started(self):
        """
        Gets the time_started of this MediaWorkflowJob.
        Time when the job started to execute. An RFC3339 formatted datetime string.


        :return: The time_started of this MediaWorkflowJob.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this MediaWorkflowJob.
        Time when the job started to execute. An RFC3339 formatted datetime string.


        :param time_started: The time_started of this MediaWorkflowJob.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this MediaWorkflowJob.
        Time when the job finished. An RFC3339 formatted datetime string.


        :return: The time_ended of this MediaWorkflowJob.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this MediaWorkflowJob.
        Time when the job finished. An RFC3339 formatted datetime string.


        :param time_ended: The time_ended of this MediaWorkflowJob.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MediaWorkflowJob.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MediaWorkflowJob.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MediaWorkflowJob.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MediaWorkflowJob.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MediaWorkflowJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MediaWorkflowJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MediaWorkflowJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MediaWorkflowJob.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MediaWorkflowJob.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MediaWorkflowJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MediaWorkflowJob.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MediaWorkflowJob.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other