# ListOsTemplatesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListOsTemplatesResponseData**](ListOsTemplatesResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_os_templates_output import ListOsTemplatesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListOsTemplatesOutput from a JSON string
list_os_templates_output_instance = ListOsTemplatesOutput.from_json(json)
# print the JSON string representation of the object
print(ListOsTemplatesOutput.to_json())

# convert the object into a dict
list_os_templates_output_dict = list_os_templates_output_instance.to_dict()
# create an instance of ListOsTemplatesOutput from a dict
list_os_templates_output_from_dict = ListOsTemplatesOutput.from_dict(list_os_templates_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


