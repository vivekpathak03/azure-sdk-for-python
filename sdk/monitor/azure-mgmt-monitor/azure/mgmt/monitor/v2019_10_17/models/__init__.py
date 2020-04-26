# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AzureMonitorPrivateLinkScope
    from ._models_py3 import AzureMonitorPrivateLinkScopeListResult
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ErrorResponseCommon
    from ._models_py3 import OperationStatus
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateEndpointProperty
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkScopesResource
    from ._models_py3 import PrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ProxyResource
    from ._models_py3 import ScopedResource
    from ._models_py3 import ScopedResourceListResult
    from ._models_py3 import TagsResource
except (SyntaxError, ImportError):
    from ._models import AzureMonitorPrivateLinkScope  # type: ignore
    from ._models import AzureMonitorPrivateLinkScopeListResult  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ErrorResponseCommon  # type: ignore
    from ._models import OperationStatus  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateEndpointProperty  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkScopesResource  # type: ignore
    from ._models import PrivateLinkServiceConnectionStateProperty  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import ScopedResource  # type: ignore
    from ._models import ScopedResourceListResult  # type: ignore
    from ._models import TagsResource  # type: ignore

__all__ = [
    'AzureMonitorPrivateLinkScope',
    'AzureMonitorPrivateLinkScopeListResult',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'ErrorResponseCommon',
    'OperationStatus',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkScopesResource',
    'PrivateLinkServiceConnectionStateProperty',
    'ProxyResource',
    'ScopedResource',
    'ScopedResourceListResult',
    'TagsResource',
]