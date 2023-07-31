# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.814
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_scheduler.configuration import Configuration


class UploadImageInstructions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'docker_login_command': 'str',
        'build_versioned_docker_image_command': 'str',
        'tag_versioned_docker_image_command': 'str',
        'push_versioned_docker_image_command': 'str',
        'tag_latest_docker_image_command': 'str',
        'push_latest_docker_image_command': 'str',
        'expiry_time': 'datetime'
    }

    attribute_map = {
        'docker_login_command': 'dockerLoginCommand',
        'build_versioned_docker_image_command': 'buildVersionedDockerImageCommand',
        'tag_versioned_docker_image_command': 'tagVersionedDockerImageCommand',
        'push_versioned_docker_image_command': 'pushVersionedDockerImageCommand',
        'tag_latest_docker_image_command': 'tagLatestDockerImageCommand',
        'push_latest_docker_image_command': 'pushLatestDockerImageCommand',
        'expiry_time': 'expiryTime'
    }

    required_map = {
        'docker_login_command': 'required',
        'build_versioned_docker_image_command': 'required',
        'tag_versioned_docker_image_command': 'required',
        'push_versioned_docker_image_command': 'required',
        'tag_latest_docker_image_command': 'optional',
        'push_latest_docker_image_command': 'optional',
        'expiry_time': 'optional'
    }

    def __init__(self, docker_login_command=None, build_versioned_docker_image_command=None, tag_versioned_docker_image_command=None, push_versioned_docker_image_command=None, tag_latest_docker_image_command=None, push_latest_docker_image_command=None, expiry_time=None, local_vars_configuration=None):  # noqa: E501
        """UploadImageInstructions - a model defined in OpenAPI"
        
        :param docker_login_command:  (required)
        :type docker_login_command: str
        :param build_versioned_docker_image_command:  (required)
        :type build_versioned_docker_image_command: str
        :param tag_versioned_docker_image_command:  (required)
        :type tag_versioned_docker_image_command: str
        :param push_versioned_docker_image_command:  (required)
        :type push_versioned_docker_image_command: str
        :param tag_latest_docker_image_command: 
        :type tag_latest_docker_image_command: str
        :param push_latest_docker_image_command: 
        :type push_latest_docker_image_command: str
        :param expiry_time: 
        :type expiry_time: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._docker_login_command = None
        self._build_versioned_docker_image_command = None
        self._tag_versioned_docker_image_command = None
        self._push_versioned_docker_image_command = None
        self._tag_latest_docker_image_command = None
        self._push_latest_docker_image_command = None
        self._expiry_time = None
        self.discriminator = None

        self.docker_login_command = docker_login_command
        self.build_versioned_docker_image_command = build_versioned_docker_image_command
        self.tag_versioned_docker_image_command = tag_versioned_docker_image_command
        self.push_versioned_docker_image_command = push_versioned_docker_image_command
        self.tag_latest_docker_image_command = tag_latest_docker_image_command
        self.push_latest_docker_image_command = push_latest_docker_image_command
        if expiry_time is not None:
            self.expiry_time = expiry_time

    @property
    def docker_login_command(self):
        """Gets the docker_login_command of this UploadImageInstructions.  # noqa: E501


        :return: The docker_login_command of this UploadImageInstructions.  # noqa: E501
        :rtype: str
        """
        return self._docker_login_command

    @docker_login_command.setter
    def docker_login_command(self, docker_login_command):
        """Sets the docker_login_command of this UploadImageInstructions.


        :param docker_login_command: The docker_login_command of this UploadImageInstructions.  # noqa: E501
        :type docker_login_command: str
        """
        if self.local_vars_configuration.client_side_validation and docker_login_command is None:  # noqa: E501
            raise ValueError("Invalid value for `docker_login_command`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                docker_login_command is not None and len(docker_login_command) < 1):
            raise ValueError("Invalid value for `docker_login_command`, length must be greater than or equal to `1`")  # noqa: E501

        self._docker_login_command = docker_login_command

    @property
    def build_versioned_docker_image_command(self):
        """Gets the build_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501


        :return: The build_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :rtype: str
        """
        return self._build_versioned_docker_image_command

    @build_versioned_docker_image_command.setter
    def build_versioned_docker_image_command(self, build_versioned_docker_image_command):
        """Sets the build_versioned_docker_image_command of this UploadImageInstructions.


        :param build_versioned_docker_image_command: The build_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :type build_versioned_docker_image_command: str
        """
        if self.local_vars_configuration.client_side_validation and build_versioned_docker_image_command is None:  # noqa: E501
            raise ValueError("Invalid value for `build_versioned_docker_image_command`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                build_versioned_docker_image_command is not None and len(build_versioned_docker_image_command) < 1):
            raise ValueError("Invalid value for `build_versioned_docker_image_command`, length must be greater than or equal to `1`")  # noqa: E501

        self._build_versioned_docker_image_command = build_versioned_docker_image_command

    @property
    def tag_versioned_docker_image_command(self):
        """Gets the tag_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501


        :return: The tag_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :rtype: str
        """
        return self._tag_versioned_docker_image_command

    @tag_versioned_docker_image_command.setter
    def tag_versioned_docker_image_command(self, tag_versioned_docker_image_command):
        """Sets the tag_versioned_docker_image_command of this UploadImageInstructions.


        :param tag_versioned_docker_image_command: The tag_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :type tag_versioned_docker_image_command: str
        """
        if self.local_vars_configuration.client_side_validation and tag_versioned_docker_image_command is None:  # noqa: E501
            raise ValueError("Invalid value for `tag_versioned_docker_image_command`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tag_versioned_docker_image_command is not None and len(tag_versioned_docker_image_command) < 1):
            raise ValueError("Invalid value for `tag_versioned_docker_image_command`, length must be greater than or equal to `1`")  # noqa: E501

        self._tag_versioned_docker_image_command = tag_versioned_docker_image_command

    @property
    def push_versioned_docker_image_command(self):
        """Gets the push_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501


        :return: The push_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :rtype: str
        """
        return self._push_versioned_docker_image_command

    @push_versioned_docker_image_command.setter
    def push_versioned_docker_image_command(self, push_versioned_docker_image_command):
        """Sets the push_versioned_docker_image_command of this UploadImageInstructions.


        :param push_versioned_docker_image_command: The push_versioned_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :type push_versioned_docker_image_command: str
        """
        if self.local_vars_configuration.client_side_validation and push_versioned_docker_image_command is None:  # noqa: E501
            raise ValueError("Invalid value for `push_versioned_docker_image_command`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                push_versioned_docker_image_command is not None and len(push_versioned_docker_image_command) < 1):
            raise ValueError("Invalid value for `push_versioned_docker_image_command`, length must be greater than or equal to `1`")  # noqa: E501

        self._push_versioned_docker_image_command = push_versioned_docker_image_command

    @property
    def tag_latest_docker_image_command(self):
        """Gets the tag_latest_docker_image_command of this UploadImageInstructions.  # noqa: E501


        :return: The tag_latest_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :rtype: str
        """
        return self._tag_latest_docker_image_command

    @tag_latest_docker_image_command.setter
    def tag_latest_docker_image_command(self, tag_latest_docker_image_command):
        """Sets the tag_latest_docker_image_command of this UploadImageInstructions.


        :param tag_latest_docker_image_command: The tag_latest_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :type tag_latest_docker_image_command: str
        """

        self._tag_latest_docker_image_command = tag_latest_docker_image_command

    @property
    def push_latest_docker_image_command(self):
        """Gets the push_latest_docker_image_command of this UploadImageInstructions.  # noqa: E501


        :return: The push_latest_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :rtype: str
        """
        return self._push_latest_docker_image_command

    @push_latest_docker_image_command.setter
    def push_latest_docker_image_command(self, push_latest_docker_image_command):
        """Sets the push_latest_docker_image_command of this UploadImageInstructions.


        :param push_latest_docker_image_command: The push_latest_docker_image_command of this UploadImageInstructions.  # noqa: E501
        :type push_latest_docker_image_command: str
        """

        self._push_latest_docker_image_command = push_latest_docker_image_command

    @property
    def expiry_time(self):
        """Gets the expiry_time of this UploadImageInstructions.  # noqa: E501


        :return: The expiry_time of this UploadImageInstructions.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """Sets the expiry_time of this UploadImageInstructions.


        :param expiry_time: The expiry_time of this UploadImageInstructions.  # noqa: E501
        :type expiry_time: datetime
        """

        self._expiry_time = expiry_time

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UploadImageInstructions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadImageInstructions):
            return True

        return self.to_dict() != other.to_dict()
