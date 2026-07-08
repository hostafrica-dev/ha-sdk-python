# SnapshotJobMutationResponseData

Response data for snapshot job create operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**job** | [**SnapshotJob**](SnapshotJob.md) |  | 
**limits** | [**SnapshotJobLimits**](SnapshotJobLimits.md) |  | 

## Example

```python
from ha_sdk_python.models.snapshot_job_mutation_response_data import SnapshotJobMutationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotJobMutationResponseData from a JSON string
snapshot_job_mutation_response_data_instance = SnapshotJobMutationResponseData.from_json(json)
# print the JSON string representation of the object
print(SnapshotJobMutationResponseData.to_json())

# convert the object into a dict
snapshot_job_mutation_response_data_dict = snapshot_job_mutation_response_data_instance.to_dict()
# create an instance of SnapshotJobMutationResponseData from a dict
snapshot_job_mutation_response_data_from_dict = SnapshotJobMutationResponseData.from_dict(snapshot_job_mutation_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


