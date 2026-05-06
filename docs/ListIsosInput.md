# ListIsosInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_isos_input import ListIsosInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListIsosInput from a JSON string
list_isos_input_instance = ListIsosInput.from_json(json)
# print the JSON string representation of the object
print(ListIsosInput.to_json())

# convert the object into a dict
list_isos_input_dict = list_isos_input_instance.to_dict()
# create an instance of ListIsosInput from a dict
list_isos_input_from_dict = ListIsosInput.from_dict(list_isos_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


