# ListIsosResponseData

Response data for list ISOs operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**isos** | **List[str]** | List of available ISO images | 

## Example

```python
from hostafrica_sdk_python.models.list_isos_response_data import ListIsosResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListIsosResponseData from a JSON string
list_isos_response_data_instance = ListIsosResponseData.from_json(json)
# print the JSON string representation of the object
print(ListIsosResponseData.to_json())

# convert the object into a dict
list_isos_response_data_dict = list_isos_response_data_instance.to_dict()
# create an instance of ListIsosResponseData from a dict
list_isos_response_data_from_dict = ListIsosResponseData.from_dict(list_isos_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


