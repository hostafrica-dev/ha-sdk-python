# RollbackSnapshotRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**snapshot_name** | **str** | Snapshot name to rollback to | 

## Example

```python
from ha_sdk_python.models.rollback_snapshot_request_content import RollbackSnapshotRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackSnapshotRequestContent from a JSON string
rollback_snapshot_request_content_instance = RollbackSnapshotRequestContent.from_json(json)
# print the JSON string representation of the object
print(RollbackSnapshotRequestContent.to_json())

# convert the object into a dict
rollback_snapshot_request_content_dict = rollback_snapshot_request_content_instance.to_dict()
# create an instance of RollbackSnapshotRequestContent from a dict
rollback_snapshot_request_content_from_dict = RollbackSnapshotRequestContent.from_dict(rollback_snapshot_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


