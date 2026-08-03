# DnsCreateCandidateInfo

A domain or service eligible for DNS zone creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Domain name when the candidate is a domain | [optional] 
**domain_id** | **str** | Domain service id when the candidate is a domain | [optional] 
**relid** | **int** | Related service id when the candidate is a hosting or addon service | [optional] 
**type** | **int** | Zone type: 0&#x3D;OTHER, 1&#x3D;DOMAIN, 2&#x3D;HOSTING, 3&#x3D;ADDON | [optional] 
**name** | **str** | Display name for the candidate | [optional] 

## Example

```python
from ha_sdk_python.models.dns_create_candidate_info import DnsCreateCandidateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DnsCreateCandidateInfo from a JSON string
dns_create_candidate_info_instance = DnsCreateCandidateInfo.from_json(json)
# print the JSON string representation of the object
print(DnsCreateCandidateInfo.to_json())

# convert the object into a dict
dns_create_candidate_info_dict = dns_create_candidate_info_instance.to_dict()
# create an instance of DnsCreateCandidateInfo from a dict
dns_create_candidate_info_from_dict = DnsCreateCandidateInfo.from_dict(dns_create_candidate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


