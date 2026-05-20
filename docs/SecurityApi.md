# ha_sdk_python.SecurityApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](SecurityApi.md#change_password) | **POST** /vps/change-password | 
[**get_private_ssh_key**](SecurityApi.md#get_private_ssh_key) | **POST** /vps/get-private-ssh-keys | 
[**get_public_ssh_key**](SecurityApi.md#get_public_ssh_key) | **POST** /vps/get-public-ssh-keys | 
[**update_ssh_keys**](SecurityApi.md#update_ssh_keys) | **POST** /vps/update-ssh-keys | 


# **change_password**
> ChangePasswordResponseContent change_password(change_password_request_content)

Change the root password for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.change_password_request_content import ChangePasswordRequestContent
from ha_sdk_python.models.change_password_response_content import ChangePasswordResponseContent
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
    api_instance = ha_sdk_python.SecurityApi(api_client)
    change_password_request_content = ha_sdk_python.ChangePasswordRequestContent() # ChangePasswordRequestContent | 

    try:
        api_response = api_instance.change_password(change_password_request_content)
        print("The response of SecurityApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request_content** | [**ChangePasswordRequestContent**](ChangePasswordRequestContent.md)|  | 

### Return type

[**ChangePasswordResponseContent**](ChangePasswordResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChangePassword 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_ssh_key**
> GetPrivateSshKeyResponseContent get_private_ssh_key(get_private_ssh_key_request_content)

Retrieves the private SSH key configured for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_private_ssh_key_request_content import GetPrivateSshKeyRequestContent
from ha_sdk_python.models.get_private_ssh_key_response_content import GetPrivateSshKeyResponseContent
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
    api_instance = ha_sdk_python.SecurityApi(api_client)
    get_private_ssh_key_request_content = ha_sdk_python.GetPrivateSshKeyRequestContent() # GetPrivateSshKeyRequestContent | 

    try:
        api_response = api_instance.get_private_ssh_key(get_private_ssh_key_request_content)
        print("The response of SecurityApi->get_private_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_private_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_private_ssh_key_request_content** | [**GetPrivateSshKeyRequestContent**](GetPrivateSshKeyRequestContent.md)|  | 

### Return type

[**GetPrivateSshKeyResponseContent**](GetPrivateSshKeyResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetPrivateSshKey 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_ssh_key**
> GetPublicSshKeyResponseContent get_public_ssh_key(get_public_ssh_key_request_content)

Retrieves the public SSH key configured for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_public_ssh_key_request_content import GetPublicSshKeyRequestContent
from ha_sdk_python.models.get_public_ssh_key_response_content import GetPublicSshKeyResponseContent
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
    api_instance = ha_sdk_python.SecurityApi(api_client)
    get_public_ssh_key_request_content = ha_sdk_python.GetPublicSshKeyRequestContent() # GetPublicSshKeyRequestContent | 

    try:
        api_response = api_instance.get_public_ssh_key(get_public_ssh_key_request_content)
        print("The response of SecurityApi->get_public_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_public_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_public_ssh_key_request_content** | [**GetPublicSshKeyRequestContent**](GetPublicSshKeyRequestContent.md)|  | 

### Return type

[**GetPublicSshKeyResponseContent**](GetPublicSshKeyResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetPublicSshKey 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssh_keys**
> UpdateSshKeysResponseContent update_ssh_keys(update_ssh_keys_request_content)

Updates SSH public keys for a VPS service for root access.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_ssh_keys_request_content import UpdateSshKeysRequestContent
from ha_sdk_python.models.update_ssh_keys_response_content import UpdateSshKeysResponseContent
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
    api_instance = ha_sdk_python.SecurityApi(api_client)
    update_ssh_keys_request_content = ha_sdk_python.UpdateSshKeysRequestContent() # UpdateSshKeysRequestContent | 

    try:
        api_response = api_instance.update_ssh_keys(update_ssh_keys_request_content)
        print("The response of SecurityApi->update_ssh_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->update_ssh_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_ssh_keys_request_content** | [**UpdateSshKeysRequestContent**](UpdateSshKeysRequestContent.md)|  | 

### Return type

[**UpdateSshKeysResponseContent**](UpdateSshKeysResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateSshKeys 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

