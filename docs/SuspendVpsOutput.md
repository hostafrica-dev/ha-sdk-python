# SuspendVpsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.suspend_vps_output import SuspendVpsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SuspendVpsOutput from a JSON string
suspend_vps_output_instance = SuspendVpsOutput.from_json(json)
# print the JSON string representation of the object
print(SuspendVpsOutput.to_json())

# convert the object into a dict
suspend_vps_output_dict = suspend_vps_output_instance.to_dict()
# create an instance of SuspendVpsOutput from a dict
suspend_vps_output_from_dict = SuspendVpsOutput.from_dict(suspend_vps_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


