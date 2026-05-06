# UnsuspendVpsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.unsuspend_vps_output import UnsuspendVpsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UnsuspendVpsOutput from a JSON string
unsuspend_vps_output_instance = UnsuspendVpsOutput.from_json(json)
# print the JSON string representation of the object
print(UnsuspendVpsOutput.to_json())

# convert the object into a dict
unsuspend_vps_output_dict = unsuspend_vps_output_instance.to_dict()
# create an instance of UnsuspendVpsOutput from a dict
unsuspend_vps_output_from_dict = UnsuspendVpsOutput.from_dict(unsuspend_vps_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


