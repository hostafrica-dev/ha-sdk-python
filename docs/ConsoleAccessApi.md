# ha_sdk_python.ConsoleAccessApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_no_vnc_console**](ConsoleAccessApi.md#get_no_vnc_console) | **POST** /vps/novnc-console | 


# **get_no_vnc_console**
> GetNoVncConsoleResponseContent get_no_vnc_console(get_no_vnc_console_request_content)

Retrieves noVNC console access credentials and connection details for a VPS

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_no_vnc_console_request_content import GetNoVncConsoleRequestContent
from ha_sdk_python.models.get_no_vnc_console_response_content import GetNoVncConsoleResponseContent
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
    api_instance = ha_sdk_python.ConsoleAccessApi(api_client)
    get_no_vnc_console_request_content = ha_sdk_python.GetNoVncConsoleRequestContent() # GetNoVncConsoleRequestContent | 

    try:
        api_response = api_instance.get_no_vnc_console(get_no_vnc_console_request_content)
        print("The response of ConsoleAccessApi->get_no_vnc_console:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsoleAccessApi->get_no_vnc_console: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_no_vnc_console_request_content** | [**GetNoVncConsoleRequestContent**](GetNoVncConsoleRequestContent.md)|  | 

### Return type

[**GetNoVncConsoleResponseContent**](GetNoVncConsoleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetNoVncConsole 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

