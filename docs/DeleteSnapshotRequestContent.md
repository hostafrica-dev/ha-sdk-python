# DeleteSnapshotRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**snapshot_name** | **str** | Snapshot name to delete | 

## Example

```python
from ha_sdk_python.models.delete_snapshot_request_content import DeleteSnapshotRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnapshotRequestContent from a JSON string
delete_snapshot_request_content_instance = DeleteSnapshotRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteSnapshotRequestContent.to_json())

# convert the object into a dict
delete_snapshot_request_content_dict = delete_snapshot_request_content_instance.to_dict()
# create an instance of DeleteSnapshotRequestContent from a dict
delete_snapshot_request_content_from_dict = DeleteSnapshotRequestContent.from_dict(delete_snapshot_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


