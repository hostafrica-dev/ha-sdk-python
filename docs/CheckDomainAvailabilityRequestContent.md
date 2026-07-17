# CheckDomainAvailabilityRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | A single domain name to look up, e.g. \&quot;example.co.za\&quot;. Required unless domains is provided. | [optional] 
**domains** | **str** | Comma-separated list of domain names for a batch check. Required unless domain is provided. | [optional] 
**currency** | **str** | Currency for pricing. Accepts ISO code, symbol, country name, or numeric ID. Defaults to ZAR. | [optional] 

## Example

```python
from ha_sdk_python.models.check_domain_availability_request_content import CheckDomainAvailabilityRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDomainAvailabilityRequestContent from a JSON string
check_domain_availability_request_content_instance = CheckDomainAvailabilityRequestContent.from_json(json)
# print the JSON string representation of the object
print(CheckDomainAvailabilityRequestContent.to_json())

# convert the object into a dict
check_domain_availability_request_content_dict = check_domain_availability_request_content_instance.to_dict()
# create an instance of CheckDomainAvailabilityRequestContent from a dict
check_domain_availability_request_content_from_dict = CheckDomainAvailabilityRequestContent.from_dict(check_domain_availability_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


