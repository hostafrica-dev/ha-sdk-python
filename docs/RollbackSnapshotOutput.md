# RollbackSnapshotOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.rollback_snapshot_output import RollbackSnapshotOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackSnapshotOutput from a JSON string
rollback_snapshot_output_instance = RollbackSnapshotOutput.from_json(json)
# print the JSON string representation of the object
print(RollbackSnapshotOutput.to_json())

# convert the object into a dict
rollback_snapshot_output_dict = rollback_snapshot_output_instance.to_dict()
# create an instance of RollbackSnapshotOutput from a dict
rollback_snapshot_output_from_dict = RollbackSnapshotOutput.from_dict(rollback_snapshot_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


