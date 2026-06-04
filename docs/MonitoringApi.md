# ha_sdk_python.MonitoringApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](MonitoringApi.md#create_notification) | **POST** /vps/create-notification | 
[**delete_notification**](MonitoringApi.md#delete_notification) | **POST** /vps/delete-notification | 
[**list_notifications**](MonitoringApi.md#list_notifications) | **POST** /vps/list-notifications | 
[**update_notification**](MonitoringApi.md#update_notification) | **POST** /vps/update-notification | 


# **create_notification**
> CreateNotificationResponseContent create_notification(create_notification_request_content)

Creates a new notification for a VPS service with customizable thresholds for CPU, memory, network, and disk metrics

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.create_notification_request_content import CreateNotificationRequestContent
from ha_sdk_python.models.create_notification_response_content import CreateNotificationResponseContent
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
    api_instance = ha_sdk_python.MonitoringApi(api_client)
    create_notification_request_content = ha_sdk_python.CreateNotificationRequestContent() # CreateNotificationRequestContent | 

    try:
        api_response = api_instance.create_notification(create_notification_request_content)
        print("The response of MonitoringApi->create_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->create_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_notification_request_content** | [**CreateNotificationRequestContent**](CreateNotificationRequestContent.md)|  | 

### Return type

[**CreateNotificationResponseContent**](CreateNotificationResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateNotification 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> DeleteNotificationResponseContent delete_notification(delete_notification_request_content)

Deletes a notification from a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_notification_request_content import DeleteNotificationRequestContent
from ha_sdk_python.models.delete_notification_response_content import DeleteNotificationResponseContent
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
    api_instance = ha_sdk_python.MonitoringApi(api_client)
    delete_notification_request_content = ha_sdk_python.DeleteNotificationRequestContent() # DeleteNotificationRequestContent | 

    try:
        api_response = api_instance.delete_notification(delete_notification_request_content)
        print("The response of MonitoringApi->delete_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->delete_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_notification_request_content** | [**DeleteNotificationRequestContent**](DeleteNotificationRequestContent.md)|  | 

### Return type

[**DeleteNotificationResponseContent**](DeleteNotificationResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteNotification 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> ListNotificationsResponseContent list_notifications(list_notifications_request_content)

Retrieves the list of notifications for a VPS service along with dialog rules for creating notifications

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_notifications_request_content import ListNotificationsRequestContent
from ha_sdk_python.models.list_notifications_response_content import ListNotificationsResponseContent
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
    api_instance = ha_sdk_python.MonitoringApi(api_client)
    list_notifications_request_content = ha_sdk_python.ListNotificationsRequestContent() # ListNotificationsRequestContent | 

    try:
        api_response = api_instance.list_notifications(list_notifications_request_content)
        print("The response of MonitoringApi->list_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->list_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_notifications_request_content** | [**ListNotificationsRequestContent**](ListNotificationsRequestContent.md)|  | 

### Return type

[**ListNotificationsResponseContent**](ListNotificationsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListNotifications 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> UpdateNotificationResponseContent update_notification(update_notification_request_content)

Updates an existing notification for a VPS service with customizable thresholds for CPU, memory, network, and disk metrics

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_notification_request_content import UpdateNotificationRequestContent
from ha_sdk_python.models.update_notification_response_content import UpdateNotificationResponseContent
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
    api_instance = ha_sdk_python.MonitoringApi(api_client)
    update_notification_request_content = ha_sdk_python.UpdateNotificationRequestContent() # UpdateNotificationRequestContent | 

    try:
        api_response = api_instance.update_notification(update_notification_request_content)
        print("The response of MonitoringApi->update_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->update_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_notification_request_content** | [**UpdateNotificationRequestContent**](UpdateNotificationRequestContent.md)|  | 

### Return type

[**UpdateNotificationResponseContent**](UpdateNotificationResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateNotification 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

