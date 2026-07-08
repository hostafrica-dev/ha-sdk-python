# CreateSnapshotRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**name** | **str** | Name for the snapshot | 
**description** | **str** | Description for the snapshot | [optional] 
**include_ram** | **bool** | Whether to include RAM state in the snapshot. Defaults to false when omitted. | [optional] 

## Example

```python
from ha_sdk_python.models.create_snapshot_request_content import CreateSnapshotRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotRequestContent from a JSON string
create_snapshot_request_content_instance = CreateSnapshotRequestContent.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotRequestContent.to_json())

# convert the object into a dict
create_snapshot_request_content_dict = create_snapshot_request_content_instance.to_dict()
# create an instance of CreateSnapshotRequestContent from a dict
create_snapshot_request_content_from_dict = CreateSnapshotRequestContent.from_dict(create_snapshot_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


