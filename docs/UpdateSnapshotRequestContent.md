# UpdateSnapshotRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**snapshot_name** | **str** | Snapshot name to update | 
**description** | **str** | New description for the snapshot | [optional] 

## Example

```python
from ha_sdk_python.models.update_snapshot_request_content import UpdateSnapshotRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotRequestContent from a JSON string
update_snapshot_request_content_instance = UpdateSnapshotRequestContent.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotRequestContent.to_json())

# convert the object into a dict
update_snapshot_request_content_dict = update_snapshot_request_content_instance.to_dict()
# create an instance of UpdateSnapshotRequestContent from a dict
update_snapshot_request_content_from_dict = UpdateSnapshotRequestContent.from_dict(update_snapshot_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


