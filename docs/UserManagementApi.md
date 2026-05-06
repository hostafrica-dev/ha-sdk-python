# hostafrica_sdk_python.UserManagementApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_change_password**](UserManagementApi.md#user_change_password) | **POST** /user/change-password | 


# **user_change_password**
> UserChangePasswordResponseContent user_change_password(user_change_password_request_content)

Changes the authenticated user's password. All active sessions will be revoked and the user must login again.

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.user_change_password_request_content import UserChangePasswordRequestContent
from hostafrica_sdk_python.models.user_change_password_response_content import UserChangePasswordResponseContent
from hostafrica_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostafrica_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: smithy.api.httpBearerAuth
configuration = hostafrica_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostafrica_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostafrica_sdk_python.UserManagementApi(api_client)
    user_change_password_request_content = hostafrica_sdk_python.UserChangePasswordRequestContent() # UserChangePasswordRequestContent | 

    try:
        api_response = api_instance.user_change_password(user_change_password_request_content)
        print("The response of UserManagementApi->user_change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->user_change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_change_password_request_content** | [**UserChangePasswordRequestContent**](UserChangePasswordRequestContent.md)|  | 

### Return type

[**UserChangePasswordResponseContent**](UserChangePasswordResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserChangePassword 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

