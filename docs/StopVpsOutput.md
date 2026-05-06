# StopVpsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.stop_vps_output import StopVpsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StopVpsOutput from a JSON string
stop_vps_output_instance = StopVpsOutput.from_json(json)
# print the JSON string representation of the object
print(StopVpsOutput.to_json())

# convert the object into a dict
stop_vps_output_dict = stop_vps_output_instance.to_dict()
# create an instance of StopVpsOutput from a dict
stop_vps_output_from_dict = StopVpsOutput.from_dict(stop_vps_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


