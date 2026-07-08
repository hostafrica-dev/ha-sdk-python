# CreateSnapshotJobResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**SnapshotJobMutationResponseData**](SnapshotJobMutationResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.create_snapshot_job_response_content import CreateSnapshotJobResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotJobResponseContent from a JSON string
create_snapshot_job_response_content_instance = CreateSnapshotJobResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotJobResponseContent.to_json())

# convert the object into a dict
create_snapshot_job_response_content_dict = create_snapshot_job_response_content_instance.to_dict()
# create an instance of CreateSnapshotJobResponseContent from a dict
create_snapshot_job_response_content_from_dict = CreateSnapshotJobResponseContent.from_dict(create_snapshot_job_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


