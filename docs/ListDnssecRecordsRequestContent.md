# ListDnssecRecordsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.list_dnssec_records_request_content import ListDnssecRecordsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnssecRecordsRequestContent from a JSON string
list_dnssec_records_request_content_instance = ListDnssecRecordsRequestContent.from_json(json)
# print the JSON string representation of the object
print(ListDnssecRecordsRequestContent.to_json())

# convert the object into a dict
list_dnssec_records_request_content_dict = list_dnssec_records_request_content_instance.to_dict()
# create an instance of ListDnssecRecordsRequestContent from a dict
list_dnssec_records_request_content_from_dict = ListDnssecRecordsRequestContent.from_dict(list_dnssec_records_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


