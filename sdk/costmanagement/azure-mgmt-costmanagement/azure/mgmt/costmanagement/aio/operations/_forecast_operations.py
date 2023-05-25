# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._forecast_operations import build_external_cloud_provider_usage_request, build_usage_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ForecastOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.costmanagement.aio.CostManagementClient`'s
        :attr:`forecast` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def usage(
        self,
        scope: str,
        parameters: _models.ForecastDefinition,
        filter: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.ForecastResult]:
        """Lists the forecast charges for scope defined.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param scope: The scope associated with forecast operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation.
         Required.
        :type parameters: ~azure.mgmt.costmanagement.models.ForecastDefinition
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'. Default value is None.
        :type filter: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForecastResult or None or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.ForecastResult or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def usage(
        self,
        scope: str,
        parameters: IO,
        filter: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.ForecastResult]:
        """Lists the forecast charges for scope defined.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param scope: The scope associated with forecast operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation.
         Required.
        :type parameters: IO
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'. Default value is None.
        :type filter: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForecastResult or None or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.ForecastResult or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def usage(
        self, scope: str, parameters: Union[_models.ForecastDefinition, IO], filter: Optional[str] = None, **kwargs: Any
    ) -> Optional[_models.ForecastResult]:
        """Lists the forecast charges for scope defined.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param scope: The scope associated with forecast operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation. Is
         either a ForecastDefinition type or a IO type. Required.
        :type parameters: ~azure.mgmt.costmanagement.models.ForecastDefinition or IO
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'. Default value is None.
        :type filter: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForecastResult or None or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.ForecastResult or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.ForecastResult]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ForecastDefinition")

        request = build_usage_request(
            scope=scope,
            filter=filter,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.usage.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("ForecastResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    usage.metadata = {"url": "/{scope}/providers/Microsoft.CostManagement/forecast"}

    @overload
    async def external_cloud_provider_usage(
        self,
        external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
        external_cloud_provider_id: str,
        parameters: _models.ForecastDefinition,
        filter: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ForecastResult:
        """Lists the forecast charges for external cloud provider type defined.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions"
         and "externalBillingAccounts". Required.
        :type external_cloud_provider_type: str or
         ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
         Required.
        :type external_cloud_provider_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation.
         Required.
        :type parameters: ~azure.mgmt.costmanagement.models.ForecastDefinition
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'. Default value is None.
        :type filter: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForecastResult or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.ForecastResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def external_cloud_provider_usage(
        self,
        external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
        external_cloud_provider_id: str,
        parameters: IO,
        filter: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ForecastResult:
        """Lists the forecast charges for external cloud provider type defined.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions"
         and "externalBillingAccounts". Required.
        :type external_cloud_provider_type: str or
         ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
         Required.
        :type external_cloud_provider_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation.
         Required.
        :type parameters: IO
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'. Default value is None.
        :type filter: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForecastResult or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.ForecastResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def external_cloud_provider_usage(
        self,
        external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
        external_cloud_provider_id: str,
        parameters: Union[_models.ForecastDefinition, IO],
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ForecastResult:
        """Lists the forecast charges for external cloud provider type defined.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions"
         and "externalBillingAccounts". Required.
        :type external_cloud_provider_type: str or
         ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
         Required.
        :type external_cloud_provider_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation. Is
         either a ForecastDefinition type or a IO type. Required.
        :type parameters: ~azure.mgmt.costmanagement.models.ForecastDefinition or IO
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'. Default value is None.
        :type filter: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ForecastResult or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.ForecastResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ForecastResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ForecastDefinition")

        request = build_external_cloud_provider_usage_request(
            external_cloud_provider_type=external_cloud_provider_type,
            external_cloud_provider_id=external_cloud_provider_id,
            filter=filter,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.external_cloud_provider_usage.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ForecastResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    external_cloud_provider_usage.metadata = {
        "url": "/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/forecast"
    }
