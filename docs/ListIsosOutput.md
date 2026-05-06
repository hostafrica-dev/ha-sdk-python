# ListIsosOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListIsosResponseData**](ListIsosResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_isos_output import ListIsosOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListIsosOutput from a JSON string
list_isos_output_instance = ListIsosOutput.from_json(json)
# print the JSON string representation of the object
print(ListIsosOutput.to_json())

# convert the object into a dict
list_isos_output_dict = list_isos_output_instance.to_dict()
# create an instance of ListIsosOutput from a dict
list_isos_output_from_dict = ListIsosOutput.from_dict(list_isos_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


