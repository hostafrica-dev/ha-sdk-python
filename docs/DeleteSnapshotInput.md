# DeleteSnapshotInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**snapshot_name** | **str** | Snapshot name to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_snapshot_input import DeleteSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnapshotInput from a JSON string
delete_snapshot_input_instance = DeleteSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(DeleteSnapshotInput.to_json())

# convert the object into a dict
delete_snapshot_input_dict = delete_snapshot_input_instance.to_dict()
# create an instance of DeleteSnapshotInput from a dict
delete_snapshot_input_from_dict = DeleteSnapshotInput.from_dict(delete_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


