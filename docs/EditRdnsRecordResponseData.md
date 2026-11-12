# EditRdnsRecordResponseData

Response data for the edit-rdns-record operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | [**RdnsRecord**](RdnsRecord.md) |  | 

## Example

```python
from ha_sdk_python.models.edit_rdns_record_response_data import EditRdnsRecordResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EditRdnsRecordResponseData from a JSON string
edit_rdns_record_response_data_instance = EditRdnsRecordResponseData.from_json(json)
# print the JSON string representation of the object
print(EditRdnsRecordResponseData.to_json())

# convert the object into a dict
edit_rdns_record_response_data_dict = edit_rdns_record_response_data_instance.to_dict()
# create an instance of EditRdnsRecordResponseData from a dict
edit_rdns_record_response_data_from_dict = EditRdnsRecordResponseData.from_dict(edit_rdns_record_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


