# ListOsTemplatesResponseData

Response data for list OS templates operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**images** | [**List[OsImage]**](OsImage.md) | List of available OS images | 

## Example

```python
from hostafrica_sdk_python.models.list_os_templates_response_data import ListOsTemplatesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListOsTemplatesResponseData from a JSON string
list_os_templates_response_data_instance = ListOsTemplatesResponseData.from_json(json)
# print the JSON string representation of the object
print(ListOsTemplatesResponseData.to_json())

# convert the object into a dict
list_os_templates_response_data_dict = list_os_templates_response_data_instance.to_dict()
# create an instance of ListOsTemplatesResponseData from a dict
list_os_templates_response_data_from_dict = ListOsTemplatesResponseData.from_dict(list_os_templates_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


