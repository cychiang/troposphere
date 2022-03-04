# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.eks import VALID_TAINT_EFFECT  # noqa: F401
from .validators.eks import (
    validate_cluster_logging,
    validate_taint_effect,
    validate_taint_key,
    validate_taint_value,
)


class Addon(AWSObject):
    """
    `Addon <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html>`__
    """

    resource_type = "AWS::EKS::Addon"

    props: PropsDictType = {
        "AddonName": (str, True),
        "AddonVersion": (str, False),
        "ClusterName": (str, True),
        "ResolveConflicts": (str, False),
        "ServiceAccountRoleArn": (str, False),
        "Tags": (Tags, False),
    }


class EncryptionConfig(AWSProperty):
    """
    `EncryptionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html>`__
    """

    props: PropsDictType = {
        "Provider": (dict, False),
        "Resources": ([str], False),
    }


class KubernetesNetworkConfig(AWSProperty):
    """
    `KubernetesNetworkConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html>`__
    """

    props: PropsDictType = {
        "IpFamily": (str, False),
        "ServiceIpv4Cidr": (str, False),
        "ServiceIpv6Cidr": (str, False),
    }


class LoggingTypeConfig(AWSProperty):
    """
    `LoggingTypeConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
    }


class ClusterLogging(AWSProperty):
    """
    `ClusterLogging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html>`__
    """

    props: PropsDictType = {
        "EnabledTypes": ([LoggingTypeConfig], False),
    }

    def validate(self):
        validate_cluster_logging(self)


class Logging(AWSProperty):
    """
    `Logging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html>`__
    """

    props: PropsDictType = {
        "ClusterLogging": (ClusterLogging, False),
    }


class ResourcesVpcConfig(AWSProperty):
    """
    `ResourcesVpcConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html>`__
    """

    props: PropsDictType = {
        "EndpointPrivateAccess": (boolean, False),
        "EndpointPublicAccess": (boolean, False),
        "PublicAccessCidrs": ([str], False),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], True),
    }


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html>`__
    """

    resource_type = "AWS::EKS::Cluster"

    props: PropsDictType = {
        "EncryptionConfig": ([EncryptionConfig], False),
        "KubernetesNetworkConfig": (KubernetesNetworkConfig, False),
        "Logging": (Logging, False),
        "Name": (str, False),
        "ResourcesVpcConfig": (ResourcesVpcConfig, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
        "Version": (str, False),
    }


class Label(AWSProperty):
    """
    `Label <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class Selector(AWSProperty):
    """
    `Selector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html>`__
    """

    props: PropsDictType = {
        "Labels": ([Label], False),
        "Namespace": (str, True),
    }


class FargateProfile(AWSObject):
    """
    `FargateProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html>`__
    """

    resource_type = "AWS::EKS::FargateProfile"

    props: PropsDictType = {
        "ClusterName": (str, True),
        "FargateProfileName": (str, False),
        "PodExecutionRoleArn": (str, True),
        "Selectors": ([Selector], True),
        "Subnets": ([str], False),
        "Tags": (Tags, False),
    }


class RequiredClaim(AWSProperty):
    """
    `RequiredClaim <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-requiredclaim.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class OidcIdentityProviderConfig(AWSProperty):
    """
    `OidcIdentityProviderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html>`__
    """

    props: PropsDictType = {
        "ClientId": (str, True),
        "GroupsClaim": (str, False),
        "GroupsPrefix": (str, False),
        "IssuerUrl": (str, True),
        "RequiredClaims": ([RequiredClaim], False),
        "UsernameClaim": (str, False),
        "UsernamePrefix": (str, False),
    }


class IdentityProviderConfig(AWSObject):
    """
    `IdentityProviderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html>`__
    """

    resource_type = "AWS::EKS::IdentityProviderConfig"

    props: PropsDictType = {
        "ClusterName": (str, True),
        "IdentityProviderConfigName": (str, False),
        "Oidc": (OidcIdentityProviderConfig, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class LaunchTemplateSpecification(AWSProperty):
    """
    `LaunchTemplateSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html>`__
    """

    props: PropsDictType = {
        "Id": (str, False),
        "Name": (str, False),
        "Version": (str, False),
    }


class RemoteAccess(AWSProperty):
    """
    `RemoteAccess <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html>`__
    """

    props: PropsDictType = {
        "Ec2SshKey": (str, True),
        "SourceSecurityGroups": ([str], False),
    }


class ScalingConfig(AWSProperty):
    """
    `ScalingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html>`__
    """

    props: PropsDictType = {
        "DesiredSize": (integer, False),
        "MaxSize": (integer, False),
        "MinSize": (integer, False),
    }


class Taint(AWSProperty):
    """
    `Taint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html>`__
    """

    props: PropsDictType = {
        "Effect": (validate_taint_effect, False),
        "Key": (validate_taint_key, False),
        "Value": (validate_taint_value, False),
    }


class UpdateConfig(AWSProperty):
    """
    `UpdateConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html>`__
    """

    props: PropsDictType = {
        "MaxUnavailable": (double, False),
        "MaxUnavailablePercentage": (double, False),
    }


class Nodegroup(AWSObject):
    """
    `Nodegroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html>`__
    """

    resource_type = "AWS::EKS::Nodegroup"

    props: PropsDictType = {
        "AmiType": (str, False),
        "CapacityType": (str, False),
        "ClusterName": (str, True),
        "DiskSize": (integer, False),
        "ForceUpdateEnabled": (boolean, False),
        "InstanceTypes": ([str], False),
        "Labels": (dict, False),
        "LaunchTemplate": (LaunchTemplateSpecification, False),
        "NodeRole": (str, True),
        "NodegroupName": (str, False),
        "ReleaseVersion": (str, False),
        "RemoteAccess": (RemoteAccess, False),
        "ScalingConfig": (ScalingConfig, False),
        "Subnets": ([str], True),
        "Tags": (dict, False),
        "Taints": ([Taint], False),
        "UpdateConfig": (UpdateConfig, False),
        "Version": (str, False),
    }
