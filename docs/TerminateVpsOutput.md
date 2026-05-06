# TerminateVpsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.terminate_vps_output import TerminateVpsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateVpsOutput from a JSON string
terminate_vps_output_instance = TerminateVpsOutput.from_json(json)
# print the JSON string representation of the object
print(TerminateVpsOutput.to_json())

# convert the object into a dict
terminate_vps_output_dict = terminate_vps_output_instance.to_dict()
# create an instance of TerminateVpsOutput from a dict
terminate_vps_output_from_dict = TerminateVpsOutput.from_dict(terminate_vps_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


