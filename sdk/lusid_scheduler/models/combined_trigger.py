# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.493
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


class CombinedTrigger(object):
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
        'start_time': 'str',
        'end_time': 'str',
        'file': 'str',
        'poll_period': 'int',
        'bucket': 'str',
        'trigger_every_file': 'bool',
        'end_of_time_window_option': 'str',
        'days_available': 'DaysOfWeek'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'file': 'file',
        'poll_period': 'pollPeriod',
        'bucket': 'bucket',
        'trigger_every_file': 'triggerEveryFile',
        'end_of_time_window_option': 'endOfTimeWindowOption',
        'days_available': 'daysAvailable'
    }

    required_map = {
        'start_time': 'required',
        'end_time': 'required',
        'file': 'required',
        'poll_period': 'optional',
        'bucket': 'required',
        'trigger_every_file': 'optional',
        'end_of_time_window_option': 'required',
        'days_available': 'required'
    }

    def __init__(self, start_time=None, end_time=None, file=None, poll_period=None, bucket=None, trigger_every_file=None, end_of_time_window_option=None, days_available=None, local_vars_configuration=None):  # noqa: E501
        """CombinedTrigger - a model defined in OpenAPI"
        
        :param start_time:  The start of the time window when a file can arrive to trigger the schedule  Cannot exceed 24 hours (required)
        :type start_time: str
        :param end_time:  The end of the time window when a file can arrive to trigger the schedule  Must be after the Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime and cannot exceed 24 hours (required)
        :type end_time: str
        :param file:  The file name or partial path of the file that will trigger the job  E.G: `fileName` or `folder1/folder2/someFileName` (required)
        :type file: str
        :param poll_period:  The frequency, in seconds, at which to poll the S3 bucket for the file.  Must be lower than the difference in seconds between Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndTime and Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime  Defaults to 5.
        :type poll_period: int
        :param bucket:  The S3 bucket where to watch for the trigger file (required)
        :type bucket: str
        :param trigger_every_file:  Specify whether to trigger every time the file is updated
        :type trigger_every_file: bool
        :param end_of_time_window_option:  Specifies the behaviour of the trigger when the time window ends  Available options are \"Always\", \"NoFile\", \"FileReceived\", \"Never\"  Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndOfTimeWindowOption (required)
        :type end_of_time_window_option: str
        :param days_available:  (required)
        :type days_available: lusid_scheduler.DaysOfWeek

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_time = None
        self._end_time = None
        self._file = None
        self._poll_period = None
        self._bucket = None
        self._trigger_every_file = None
        self._end_of_time_window_option = None
        self._days_available = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.file = file
        if poll_period is not None:
            self.poll_period = poll_period
        self.bucket = bucket
        if trigger_every_file is not None:
            self.trigger_every_file = trigger_every_file
        self.end_of_time_window_option = end_of_time_window_option
        self.days_available = days_available

    @property
    def start_time(self):
        """Gets the start_time of this CombinedTrigger.  # noqa: E501

        The start of the time window when a file can arrive to trigger the schedule  Cannot exceed 24 hours  # noqa: E501

        :return: The start_time of this CombinedTrigger.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CombinedTrigger.

        The start of the time window when a file can arrive to trigger the schedule  Cannot exceed 24 hours  # noqa: E501

        :param start_time: The start_time of this CombinedTrigger.  # noqa: E501
        :type start_time: str
        """
        if self.local_vars_configuration.client_side_validation and start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CombinedTrigger.  # noqa: E501

        The end of the time window when a file can arrive to trigger the schedule  Must be after the Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime and cannot exceed 24 hours  # noqa: E501

        :return: The end_time of this CombinedTrigger.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CombinedTrigger.

        The end of the time window when a file can arrive to trigger the schedule  Must be after the Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime and cannot exceed 24 hours  # noqa: E501

        :param end_time: The end_time of this CombinedTrigger.  # noqa: E501
        :type end_time: str
        """
        if self.local_vars_configuration.client_side_validation and end_time is None:  # noqa: E501
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def file(self):
        """Gets the file of this CombinedTrigger.  # noqa: E501

        The file name or partial path of the file that will trigger the job  E.G: `fileName` or `folder1/folder2/someFileName`  # noqa: E501

        :return: The file of this CombinedTrigger.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CombinedTrigger.

        The file name or partial path of the file that will trigger the job  E.G: `fileName` or `folder1/folder2/someFileName`  # noqa: E501

        :param file: The file of this CombinedTrigger.  # noqa: E501
        :type file: str
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file is not None and len(file) > 256):
            raise ValueError("Invalid value for `file`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file is not None and len(file) < 1):
            raise ValueError("Invalid value for `file`, length must be greater than or equal to `1`")  # noqa: E501

        self._file = file

    @property
    def poll_period(self):
        """Gets the poll_period of this CombinedTrigger.  # noqa: E501

        The frequency, in seconds, at which to poll the S3 bucket for the file.  Must be lower than the difference in seconds between Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndTime and Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime  Defaults to 5.  # noqa: E501

        :return: The poll_period of this CombinedTrigger.  # noqa: E501
        :rtype: int
        """
        return self._poll_period

    @poll_period.setter
    def poll_period(self, poll_period):
        """Sets the poll_period of this CombinedTrigger.

        The frequency, in seconds, at which to poll the S3 bucket for the file.  Must be lower than the difference in seconds between Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndTime and Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime  Defaults to 5.  # noqa: E501

        :param poll_period: The poll_period of this CombinedTrigger.  # noqa: E501
        :type poll_period: int
        """
        if (self.local_vars_configuration.client_side_validation and
                poll_period is not None and poll_period > 86400):  # noqa: E501
            raise ValueError("Invalid value for `poll_period`, must be a value less than or equal to `86400`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                poll_period is not None and poll_period < 1):  # noqa: E501
            raise ValueError("Invalid value for `poll_period`, must be a value greater than or equal to `1`")  # noqa: E501

        self._poll_period = poll_period

    @property
    def bucket(self):
        """Gets the bucket of this CombinedTrigger.  # noqa: E501

        The S3 bucket where to watch for the trigger file  # noqa: E501

        :return: The bucket of this CombinedTrigger.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this CombinedTrigger.

        The S3 bucket where to watch for the trigger file  # noqa: E501

        :param bucket: The bucket of this CombinedTrigger.  # noqa: E501
        :type bucket: str
        """
        if self.local_vars_configuration.client_side_validation and bucket is None:  # noqa: E501
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

    @property
    def trigger_every_file(self):
        """Gets the trigger_every_file of this CombinedTrigger.  # noqa: E501

        Specify whether to trigger every time the file is updated  # noqa: E501

        :return: The trigger_every_file of this CombinedTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._trigger_every_file

    @trigger_every_file.setter
    def trigger_every_file(self, trigger_every_file):
        """Sets the trigger_every_file of this CombinedTrigger.

        Specify whether to trigger every time the file is updated  # noqa: E501

        :param trigger_every_file: The trigger_every_file of this CombinedTrigger.  # noqa: E501
        :type trigger_every_file: bool
        """

        self._trigger_every_file = trigger_every_file

    @property
    def end_of_time_window_option(self):
        """Gets the end_of_time_window_option of this CombinedTrigger.  # noqa: E501

        Specifies the behaviour of the trigger when the time window ends  Available options are \"Always\", \"NoFile\", \"FileReceived\", \"Never\"  Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndOfTimeWindowOption  # noqa: E501

        :return: The end_of_time_window_option of this CombinedTrigger.  # noqa: E501
        :rtype: str
        """
        return self._end_of_time_window_option

    @end_of_time_window_option.setter
    def end_of_time_window_option(self, end_of_time_window_option):
        """Sets the end_of_time_window_option of this CombinedTrigger.

        Specifies the behaviour of the trigger when the time window ends  Available options are \"Always\", \"NoFile\", \"FileReceived\", \"Never\"  Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndOfTimeWindowOption  # noqa: E501

        :param end_of_time_window_option: The end_of_time_window_option of this CombinedTrigger.  # noqa: E501
        :type end_of_time_window_option: str
        """
        if self.local_vars_configuration.client_side_validation and end_of_time_window_option is None:  # noqa: E501
            raise ValueError("Invalid value for `end_of_time_window_option`, must not be `None`")  # noqa: E501

        self._end_of_time_window_option = end_of_time_window_option

    @property
    def days_available(self):
        """Gets the days_available of this CombinedTrigger.  # noqa: E501


        :return: The days_available of this CombinedTrigger.  # noqa: E501
        :rtype: lusid_scheduler.DaysOfWeek
        """
        return self._days_available

    @days_available.setter
    def days_available(self, days_available):
        """Sets the days_available of this CombinedTrigger.


        :param days_available: The days_available of this CombinedTrigger.  # noqa: E501
        :type days_available: lusid_scheduler.DaysOfWeek
        """
        if self.local_vars_configuration.client_side_validation and days_available is None:  # noqa: E501
            raise ValueError("Invalid value for `days_available`, must not be `None`")  # noqa: E501

        self._days_available = days_available

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
        if not isinstance(other, CombinedTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CombinedTrigger):
            return True

        return self.to_dict() != other.to_dict()
