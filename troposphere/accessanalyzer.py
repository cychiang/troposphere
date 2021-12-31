# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class Filter(AWSProperty):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html>`__
    """

    props: PropsDictType = {
        "Contains": ([str], False),
        "Eq": ([str], False),
        "Exists": (boolean, False),
        "Neq": ([str], False),
        "Property": (str, True),
    }


class ArchiveRule(AWSProperty):
    """
    `ArchiveRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html>`__
    """

    props: PropsDictType = {
        "Filter": ([Filter], True),
        "RuleName": (str, True),
    }


class Analyzer(AWSObject):
    """
    `Analyzer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html>`__
    """

    resource_type = "AWS::AccessAnalyzer::Analyzer"

    props: PropsDictType = {
        "AnalyzerName": (str, False),
        "ArchiveRules": ([ArchiveRule], False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }
