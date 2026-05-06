# UpdateSnapshotOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_snapshot_output import UpdateSnapshotOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotOutput from a JSON string
update_snapshot_output_instance = UpdateSnapshotOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotOutput.to_json())

# convert the object into a dict
update_snapshot_output_dict = update_snapshot_output_instance.to_dict()
# create an instance of UpdateSnapshotOutput from a dict
update_snapshot_output_from_dict = UpdateSnapshotOutput.from_dict(update_snapshot_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


