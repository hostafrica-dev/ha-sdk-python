# GetDomainRedirectDetailsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**GetDomainRedirectDetailsData**](GetDomainRedirectDetailsData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_domain_redirect_details_response_content import GetDomainRedirectDetailsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainRedirectDetailsResponseContent from a JSON string
get_domain_redirect_details_response_content_instance = GetDomainRedirectDetailsResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetDomainRedirectDetailsResponseContent.to_json())

# convert the object into a dict
get_domain_redirect_details_response_content_dict = get_domain_redirect_details_response_content_instance.to_dict()
# create an instance of GetDomainRedirectDetailsResponseContent from a dict
get_domain_redirect_details_response_content_from_dict = GetDomainRedirectDetailsResponseContent.from_dict(get_domain_redirect_details_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


