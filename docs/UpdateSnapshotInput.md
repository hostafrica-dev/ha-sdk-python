# UpdateSnapshotInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**snapshot_name** | **str** | Snapshot name to update | 
**description** | **str** | New description for the snapshot | [optional] 

## Example

```python
from hostafrica_sdk_python.models.update_snapshot_input import UpdateSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotInput from a JSON string
update_snapshot_input_instance = UpdateSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotInput.to_json())

# convert the object into a dict
update_snapshot_input_dict = update_snapshot_input_instance.to_dict()
# create an instance of UpdateSnapshotInput from a dict
update_snapshot_input_from_dict = UpdateSnapshotInput.from_dict(update_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


