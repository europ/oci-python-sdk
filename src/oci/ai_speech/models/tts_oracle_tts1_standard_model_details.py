# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101

from .tts_oracle_model_details import TtsOracleModelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TtsOracleTts1StandardModelDetails(TtsOracleModelDetails):
    """
    Use this schema for specifying properties of TTS_1_STANDARD model from Oracle model family.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TtsOracleTts1StandardModelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_speech.models.TtsOracleTts1StandardModelDetails.model_name` attribute
        of this class is ``TTS_1_STANDARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_name:
            The value to assign to the model_name property of this TtsOracleTts1StandardModelDetails.
            Allowed values for this property are: "TTS_1_STANDARD", "TTS_2_NATURAL"
        :type model_name: str

        :param voice_id:
            The value to assign to the voice_id property of this TtsOracleTts1StandardModelDetails.
        :type voice_id: str

        """
        self.swagger_types = {
            'model_name': 'str',
            'voice_id': 'str'
        }

        self.attribute_map = {
            'model_name': 'modelName',
            'voice_id': 'voiceId'
        }

        self._model_name = None
        self._voice_id = None
        self._model_name = 'TTS_1_STANDARD'

    @property
    def voice_id(self):
        """
        Gets the voice_id of this TtsOracleTts1StandardModelDetails.
        Speaker in whose voice the user wants the output speech to be in.
        The possible values for `voiceId` can be obtained by calling :func:`list_voices` api.


        :return: The voice_id of this TtsOracleTts1StandardModelDetails.
        :rtype: str
        """
        return self._voice_id

    @voice_id.setter
    def voice_id(self, voice_id):
        """
        Sets the voice_id of this TtsOracleTts1StandardModelDetails.
        Speaker in whose voice the user wants the output speech to be in.
        The possible values for `voiceId` can be obtained by calling :func:`list_voices` api.


        :param voice_id: The voice_id of this TtsOracleTts1StandardModelDetails.
        :type: str
        """
        self._voice_id = voice_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other