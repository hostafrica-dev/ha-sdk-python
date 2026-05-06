# ListOsTemplatesResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListOsTemplatesResponseData**](ListOsTemplatesResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_os_templates_response_content import ListOsTemplatesResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListOsTemplatesResponseContent from a JSON string
list_os_templates_response_content_instance = ListOsTemplatesResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListOsTemplatesResponseContent.to_json())

# convert the object into a dict
list_os_templates_response_content_dict = list_os_templates_response_content_instance.to_dict()
# create an instance of ListOsTemplatesResponseContent from a dict
list_os_templates_response_content_from_dict = ListOsTemplatesResponseContent.from_dict(list_os_templates_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


