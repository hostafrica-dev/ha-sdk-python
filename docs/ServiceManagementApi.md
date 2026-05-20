# ha_sdk_python.ServiceManagementApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_vps**](ServiceManagementApi.md#cancel_vps) | **POST** /vps/cancel | 
[**create_order**](ServiceManagementApi.md#create_order) | **POST** /vps/create-order | 
[**get_catalogue**](ServiceManagementApi.md#get_catalogue) | **POST** /vps/get-catalogue | 
[**list_orders**](ServiceManagementApi.md#list_orders) | **POST** /vps/list-orders | 
[**retry_payment**](ServiceManagementApi.md#retry_payment) | **POST** /vps/retry-payment | 
[**validate_pricing**](ServiceManagementApi.md#validate_pricing) | **POST** /vps/validate-pricing | 


# **cancel_vps**
> CancelVpsResponseContent cancel_vps(cancel_vps_request_content)

Cancels a VPS service through WHMCS. This action is irreversible

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.cancel_vps_request_content import CancelVpsRequestContent
from ha_sdk_python.models.cancel_vps_response_content import CancelVpsResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.ServiceManagementApi(api_client)
    cancel_vps_request_content = ha_sdk_python.CancelVpsRequestContent() # CancelVpsRequestContent | 

    try:
        api_response = api_instance.cancel_vps(cancel_vps_request_content)
        print("The response of ServiceManagementApi->cancel_vps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagementApi->cancel_vps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_vps_request_content** | [**CancelVpsRequestContent**](CancelVpsRequestContent.md)|  | 

### Return type

[**CancelVpsResponseContent**](CancelVpsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CancelVps 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> CreateOrderResponseContent create_order(create_order_request_content)

Creates an order through checkout. Returns payment status; on failure also includes payment_error with code and message.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.create_order_request_content import CreateOrderRequestContent
from ha_sdk_python.models.create_order_response_content import CreateOrderResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.ServiceManagementApi(api_client)
    create_order_request_content = ha_sdk_python.CreateOrderRequestContent() # CreateOrderRequestContent | 

    try:
        api_response = api_instance.create_order(create_order_request_content)
        print("The response of ServiceManagementApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagementApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_request_content** | [**CreateOrderRequestContent**](CreateOrderRequestContent.md)|  | 

### Return type

[**CreateOrderResponseContent**](CreateOrderResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateOrder 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogue**
> GetCatalogueResponseContent get_catalogue(get_catalogue_request_content=get_catalogue_request_content)

Retrieves the product catalogue, optionally filtered by group or product

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_catalogue_request_content import GetCatalogueRequestContent
from ha_sdk_python.models.get_catalogue_response_content import GetCatalogueResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.ServiceManagementApi(api_client)
    get_catalogue_request_content = ha_sdk_python.GetCatalogueRequestContent() # GetCatalogueRequestContent |  (optional)

    try:
        api_response = api_instance.get_catalogue(get_catalogue_request_content=get_catalogue_request_content)
        print("The response of ServiceManagementApi->get_catalogue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagementApi->get_catalogue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_catalogue_request_content** | [**GetCatalogueRequestContent**](GetCatalogueRequestContent.md)|  | [optional] 

### Return type

[**GetCatalogueResponseContent**](GetCatalogueResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetCatalogue 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> ListOrdersResponseContent list_orders()

Lists all orders for the authenticated user, including payment and invoice status

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_orders_response_content import ListOrdersResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.ServiceManagementApi(api_client)

    try:
        api_response = api_instance.list_orders()
        print("The response of ServiceManagementApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagementApi->list_orders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListOrdersResponseContent**](ListOrdersResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListOrders 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_payment**
> RetryPaymentResponseContent retry_payment(retry_payment_request_content)

Retries a failed or pending payment for an existing order

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.retry_payment_request_content import RetryPaymentRequestContent
from ha_sdk_python.models.retry_payment_response_content import RetryPaymentResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.ServiceManagementApi(api_client)
    retry_payment_request_content = ha_sdk_python.RetryPaymentRequestContent() # RetryPaymentRequestContent | 

    try:
        api_response = api_instance.retry_payment(retry_payment_request_content)
        print("The response of ServiceManagementApi->retry_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagementApi->retry_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retry_payment_request_content** | [**RetryPaymentRequestContent**](RetryPaymentRequestContent.md)|  | 

### Return type

[**RetryPaymentResponseContent**](RetryPaymentResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RetryPayment 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_pricing**
> ValidatePricingResponseContent validate_pricing(validate_pricing_request_content)

Validates pricing for one or more products, returning per-product breakdown and order summary

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.validate_pricing_request_content import ValidatePricingRequestContent
from ha_sdk_python.models.validate_pricing_response_content import ValidatePricingResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.ServiceManagementApi(api_client)
    validate_pricing_request_content = ha_sdk_python.ValidatePricingRequestContent() # ValidatePricingRequestContent | 

    try:
        api_response = api_instance.validate_pricing(validate_pricing_request_content)
        print("The response of ServiceManagementApi->validate_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceManagementApi->validate_pricing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_pricing_request_content** | [**ValidatePricingRequestContent**](ValidatePricingRequestContent.md)|  | 

### Return type

[**ValidatePricingResponseContent**](ValidatePricingResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ValidatePricing 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

