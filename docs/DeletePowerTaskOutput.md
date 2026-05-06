# DeletePowerTaskOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.delete_power_task_output import DeletePowerTaskOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePowerTaskOutput from a JSON string
delete_power_task_output_instance = DeletePowerTaskOutput.from_json(json)
# print the JSON string representation of the object
print(DeletePowerTaskOutput.to_json())

# convert the object into a dict
delete_power_task_output_dict = delete_power_task_output_instance.to_dict()
# create an instance of DeletePowerTaskOutput from a dict
delete_power_task_output_from_dict = DeletePowerTaskOutput.from_dict(delete_power_task_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


