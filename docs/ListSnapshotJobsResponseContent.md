# ListSnapshotJobsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**SnapshotJobListResponseData**](SnapshotJobListResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_snapshot_jobs_response_content import ListSnapshotJobsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshotJobsResponseContent from a JSON string
list_snapshot_jobs_response_content_instance = ListSnapshotJobsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListSnapshotJobsResponseContent.to_json())

# convert the object into a dict
list_snapshot_jobs_response_content_dict = list_snapshot_jobs_response_content_instance.to_dict()
# create an instance of ListSnapshotJobsResponseContent from a dict
list_snapshot_jobs_response_content_from_dict = ListSnapshotJobsResponseContent.from_dict(list_snapshot_jobs_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


