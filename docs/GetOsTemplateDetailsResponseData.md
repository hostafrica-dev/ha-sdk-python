# GetOsTemplateDetailsResponseData

Response data for get OS template details operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**image** | [**OsImage**](OsImage.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_os_template_details_response_data import GetOsTemplateDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetOsTemplateDetailsResponseData from a JSON string
get_os_template_details_response_data_instance = GetOsTemplateDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetOsTemplateDetailsResponseData.to_json())

# convert the object into a dict
get_os_template_details_response_data_dict = get_os_template_details_response_data_instance.to_dict()
# create an instance of GetOsTemplateDetailsResponseData from a dict
get_os_template_details_response_data_from_dict = GetOsTemplateDetailsResponseData.from_dict(get_os_template_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


