# SuggestDomainsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | Natural-language description of the business or idea, e.g. \&quot;my coffee shop\&quot; | 
**currency** | **str** | Currency for pricing. Accepts ISO code, symbol, country name, or numeric ID. Defaults to ZAR. | [optional] 

## Example

```python
from ha_sdk_python.models.suggest_domains_request_content import SuggestDomainsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestDomainsRequestContent from a JSON string
suggest_domains_request_content_instance = SuggestDomainsRequestContent.from_json(json)
# print the JSON string representation of the object
print(SuggestDomainsRequestContent.to_json())

# convert the object into a dict
suggest_domains_request_content_dict = suggest_domains_request_content_instance.to_dict()
# create an instance of SuggestDomainsRequestContent from a dict
suggest_domains_request_content_from_dict = SuggestDomainsRequestContent.from_dict(suggest_domains_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


