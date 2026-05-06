# ListIsosResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListIsosResponseData**](ListIsosResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_isos_response_content import ListIsosResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListIsosResponseContent from a JSON string
list_isos_response_content_instance = ListIsosResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListIsosResponseContent.to_json())

# convert the object into a dict
list_isos_response_content_dict = list_isos_response_content_instance.to_dict()
# create an instance of ListIsosResponseContent from a dict
list_isos_response_content_from_dict = ListIsosResponseContent.from_dict(list_isos_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


