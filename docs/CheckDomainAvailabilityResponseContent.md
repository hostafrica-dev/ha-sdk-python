# CheckDomainAvailabilityResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DomainSearchResponseData**](DomainSearchResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.check_domain_availability_response_content import CheckDomainAvailabilityResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDomainAvailabilityResponseContent from a JSON string
check_domain_availability_response_content_instance = CheckDomainAvailabilityResponseContent.from_json(json)
# print the JSON string representation of the object
print(CheckDomainAvailabilityResponseContent.to_json())

# convert the object into a dict
check_domain_availability_response_content_dict = check_domain_availability_response_content_instance.to_dict()
# create an instance of CheckDomainAvailabilityResponseContent from a dict
check_domain_availability_response_content_from_dict = CheckDomainAvailabilityResponseContent.from_dict(check_domain_availability_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


