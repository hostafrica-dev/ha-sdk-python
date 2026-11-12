# EditRdnsRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**EditRdnsRecordResponseData**](EditRdnsRecordResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.edit_rdns_record_response_content import EditRdnsRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of EditRdnsRecordResponseContent from a JSON string
edit_rdns_record_response_content_instance = EditRdnsRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(EditRdnsRecordResponseContent.to_json())

# convert the object into a dict
edit_rdns_record_response_content_dict = edit_rdns_record_response_content_instance.to_dict()
# create an instance of EditRdnsRecordResponseContent from a dict
edit_rdns_record_response_content_from_dict = EditRdnsRecordResponseContent.from_dict(edit_rdns_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


