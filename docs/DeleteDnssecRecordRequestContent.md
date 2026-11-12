# DeleteDnssecRecordRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**key_tag** | **int** | DNSSEC key tag (0-65535) | 
**alg** | **int** | DNSSEC algorithm (1-255) | 
**digest_type** | **int** | DNSSEC digest type (1-255) | 
**digest** | **str** | Hex digest identifying the DS record to remove | 

## Example

```python
from ha_sdk_python.models.delete_dnssec_record_request_content import DeleteDnssecRecordRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDnssecRecordRequestContent from a JSON string
delete_dnssec_record_request_content_instance = DeleteDnssecRecordRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDnssecRecordRequestContent.to_json())

# convert the object into a dict
delete_dnssec_record_request_content_dict = delete_dnssec_record_request_content_instance.to_dict()
# create an instance of DeleteDnssecRecordRequestContent from a dict
delete_dnssec_record_request_content_from_dict = DeleteDnssecRecordRequestContent.from_dict(delete_dnssec_record_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


