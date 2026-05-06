# RollbackSnapshotInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**snapshot_name** | **str** | Snapshot name to rollback to | 

## Example

```python
from hostafrica_sdk_python.models.rollback_snapshot_input import RollbackSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackSnapshotInput from a JSON string
rollback_snapshot_input_instance = RollbackSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(RollbackSnapshotInput.to_json())

# convert the object into a dict
rollback_snapshot_input_dict = rollback_snapshot_input_instance.to_dict()
# create an instance of RollbackSnapshotInput from a dict
rollback_snapshot_input_from_dict = RollbackSnapshotInput.from_dict(rollback_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


