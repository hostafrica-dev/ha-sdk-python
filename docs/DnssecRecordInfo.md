# DnssecRecordInfo

A DNSSEC DS record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_tag** | **int** | DNSSEC key tag (0-65535) | 
**alg** | **int** | DNSSEC algorithm (1-255) | 
**digest_type** | **int** | DNSSEC digest type (1-255) | 
**digest** | **str** | Hex digest | 

## Example

```python
from ha_sdk_python.models.dnssec_record_info import DnssecRecordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecRecordInfo from a JSON string
dnssec_record_info_instance = DnssecRecordInfo.from_json(json)
# print the JSON string representation of the object
print(DnssecRecordInfo.to_json())

# convert the object into a dict
dnssec_record_info_dict = dnssec_record_info_instance.to_dict()
# create an instance of DnssecRecordInfo from a dict
dnssec_record_info_from_dict = DnssecRecordInfo.from_dict(dnssec_record_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


