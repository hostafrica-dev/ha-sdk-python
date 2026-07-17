# SuggestDomainsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DomainSearchResponseData**](DomainSearchResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.suggest_domains_response_content import SuggestDomainsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestDomainsResponseContent from a JSON string
suggest_domains_response_content_instance = SuggestDomainsResponseContent.from_json(json)
# print the JSON string representation of the object
print(SuggestDomainsResponseContent.to_json())

# convert the object into a dict
suggest_domains_response_content_dict = suggest_domains_response_content_instance.to_dict()
# create an instance of SuggestDomainsResponseContent from a dict
suggest_domains_response_content_from_dict = SuggestDomainsResponseContent.from_dict(suggest_domains_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


