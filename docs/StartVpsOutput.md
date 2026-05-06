# StartVpsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.start_vps_output import StartVpsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StartVpsOutput from a JSON string
start_vps_output_instance = StartVpsOutput.from_json(json)
# print the JSON string representation of the object
print(StartVpsOutput.to_json())

# convert the object into a dict
start_vps_output_dict = start_vps_output_instance.to_dict()
# create an instance of StartVpsOutput from a dict
start_vps_output_from_dict = StartVpsOutput.from_dict(start_vps_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


