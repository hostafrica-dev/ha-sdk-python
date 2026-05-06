# ShutdownVpsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.shutdown_vps_output import ShutdownVpsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ShutdownVpsOutput from a JSON string
shutdown_vps_output_instance = ShutdownVpsOutput.from_json(json)
# print the JSON string representation of the object
print(ShutdownVpsOutput.to_json())

# convert the object into a dict
shutdown_vps_output_dict = shutdown_vps_output_instance.to_dict()
# create an instance of ShutdownVpsOutput from a dict
shutdown_vps_output_from_dict = ShutdownVpsOutput.from_dict(shutdown_vps_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


