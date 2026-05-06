# CreateRdnsRecordResponseData

Response data for the create-rdns-record operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | [**RdnsRecord**](RdnsRecord.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_rdns_record_response_data import CreateRdnsRecordResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRdnsRecordResponseData from a JSON string
create_rdns_record_response_data_instance = CreateRdnsRecordResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateRdnsRecordResponseData.to_json())

# convert the object into a dict
create_rdns_record_response_data_dict = create_rdns_record_response_data_instance.to_dict()
# create an instance of CreateRdnsRecordResponseData from a dict
create_rdns_record_response_data_from_dict = CreateRdnsRecordResponseData.from_dict(create_rdns_record_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


