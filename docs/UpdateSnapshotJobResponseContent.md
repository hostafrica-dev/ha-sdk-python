# UpdateSnapshotJobResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**SnapshotJobUpdateResponseData**](SnapshotJobUpdateResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.update_snapshot_job_response_content import UpdateSnapshotJobResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotJobResponseContent from a JSON string
update_snapshot_job_response_content_instance = UpdateSnapshotJobResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotJobResponseContent.to_json())

# convert the object into a dict
update_snapshot_job_response_content_dict = update_snapshot_job_response_content_instance.to_dict()
# create an instance of UpdateSnapshotJobResponseContent from a dict
update_snapshot_job_response_content_from_dict = UpdateSnapshotJobResponseContent.from_dict(update_snapshot_job_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


