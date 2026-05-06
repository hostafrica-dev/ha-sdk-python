# GetOsTemplateDetailsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**GetOsTemplateDetailsResponseData**](GetOsTemplateDetailsResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_os_template_details_response_content import GetOsTemplateDetailsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetOsTemplateDetailsResponseContent from a JSON string
get_os_template_details_response_content_instance = GetOsTemplateDetailsResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetOsTemplateDetailsResponseContent.to_json())

# convert the object into a dict
get_os_template_details_response_content_dict = get_os_template_details_response_content_instance.to_dict()
# create an instance of GetOsTemplateDetailsResponseContent from a dict
get_os_template_details_response_content_from_dict = GetOsTemplateDetailsResponseContent.from_dict(get_os_template_details_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


