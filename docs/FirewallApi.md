# ha_sdk_python.FirewallApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firewall_rule**](FirewallApi.md#create_firewall_rule) | **POST** /vps/create-firewall-rule | 
[**delete_firewall_rule**](FirewallApi.md#delete_firewall_rule) | **POST** /vps/delete-firewall-rule | 
[**list_firewall_rules**](FirewallApi.md#list_firewall_rules) | **POST** /vps/list-firewall-rules | 
[**move_firewall_rule**](FirewallApi.md#move_firewall_rule) | **POST** /vps/move-firewall-rule | 
[**update_firewall_rule**](FirewallApi.md#update_firewall_rule) | **POST** /vps/update-firewall-rule | 


# **create_firewall_rule**
> CreateFirewallRuleResponseContent create_firewall_rule(create_firewall_rule_request_content)

Creates a new firewall rule for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.create_firewall_rule_request_content import CreateFirewallRuleRequestContent
from ha_sdk_python.models.create_firewall_rule_response_content import CreateFirewallRuleResponseContent
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
    api_instance = ha_sdk_python.FirewallApi(api_client)
    create_firewall_rule_request_content = ha_sdk_python.CreateFirewallRuleRequestContent() # CreateFirewallRuleRequestContent | 

    try:
        api_response = api_instance.create_firewall_rule(create_firewall_rule_request_content)
        print("The response of FirewallApi->create_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->create_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_firewall_rule_request_content** | [**CreateFirewallRuleRequestContent**](CreateFirewallRuleRequestContent.md)|  | 

### Return type

[**CreateFirewallRuleResponseContent**](CreateFirewallRuleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateFirewallRule 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_rule**
> DeleteFirewallRuleResponseContent delete_firewall_rule(delete_firewall_rule_request_content)

Deletes a firewall rule from a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_firewall_rule_request_content import DeleteFirewallRuleRequestContent
from ha_sdk_python.models.delete_firewall_rule_response_content import DeleteFirewallRuleResponseContent
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
    api_instance = ha_sdk_python.FirewallApi(api_client)
    delete_firewall_rule_request_content = ha_sdk_python.DeleteFirewallRuleRequestContent() # DeleteFirewallRuleRequestContent | 

    try:
        api_response = api_instance.delete_firewall_rule(delete_firewall_rule_request_content)
        print("The response of FirewallApi->delete_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->delete_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_firewall_rule_request_content** | [**DeleteFirewallRuleRequestContent**](DeleteFirewallRuleRequestContent.md)|  | 

### Return type

[**DeleteFirewallRuleResponseContent**](DeleteFirewallRuleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteFirewallRule 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_rules**
> ListFirewallRulesResponseContent list_firewall_rules(list_firewall_rules_request_content)

Retrieves the list of firewall rules and available options for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_firewall_rules_request_content import ListFirewallRulesRequestContent
from ha_sdk_python.models.list_firewall_rules_response_content import ListFirewallRulesResponseContent
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
    api_instance = ha_sdk_python.FirewallApi(api_client)
    list_firewall_rules_request_content = ha_sdk_python.ListFirewallRulesRequestContent() # ListFirewallRulesRequestContent | 

    try:
        api_response = api_instance.list_firewall_rules(list_firewall_rules_request_content)
        print("The response of FirewallApi->list_firewall_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->list_firewall_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_firewall_rules_request_content** | [**ListFirewallRulesRequestContent**](ListFirewallRulesRequestContent.md)|  | 

### Return type

[**ListFirewallRulesResponseContent**](ListFirewallRulesResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListFirewallRules 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_firewall_rule**
> MoveFirewallRuleResponseContent move_firewall_rule(move_firewall_rule_request_content)

Moves a firewall rule to a different position in the rule list. Supports both absolute positioning (target_pos) and relative movement (direction). Exactly one of target_pos or direction must be provided.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.move_firewall_rule_request_content import MoveFirewallRuleRequestContent
from ha_sdk_python.models.move_firewall_rule_response_content import MoveFirewallRuleResponseContent
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
    api_instance = ha_sdk_python.FirewallApi(api_client)
    move_firewall_rule_request_content = ha_sdk_python.MoveFirewallRuleRequestContent() # MoveFirewallRuleRequestContent | 

    try:
        api_response = api_instance.move_firewall_rule(move_firewall_rule_request_content)
        print("The response of FirewallApi->move_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->move_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_firewall_rule_request_content** | [**MoveFirewallRuleRequestContent**](MoveFirewallRuleRequestContent.md)|  | 

### Return type

[**MoveFirewallRuleResponseContent**](MoveFirewallRuleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MoveFirewallRule 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_rule**
> UpdateFirewallRuleResponseContent update_firewall_rule(update_firewall_rule_request_content)

Updates an existing firewall rule for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_firewall_rule_request_content import UpdateFirewallRuleRequestContent
from ha_sdk_python.models.update_firewall_rule_response_content import UpdateFirewallRuleResponseContent
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
    api_instance = ha_sdk_python.FirewallApi(api_client)
    update_firewall_rule_request_content = ha_sdk_python.UpdateFirewallRuleRequestContent() # UpdateFirewallRuleRequestContent | 

    try:
        api_response = api_instance.update_firewall_rule(update_firewall_rule_request_content)
        print("The response of FirewallApi->update_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->update_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_firewall_rule_request_content** | [**UpdateFirewallRuleRequestContent**](UpdateFirewallRuleRequestContent.md)|  | 

### Return type

[**UpdateFirewallRuleResponseContent**](UpdateFirewallRuleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateFirewallRule 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

