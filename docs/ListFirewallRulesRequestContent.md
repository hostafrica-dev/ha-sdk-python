# ListFirewallRulesRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_firewall_rules_request_content import ListFirewallRulesRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallRulesRequestContent from a JSON string
list_firewall_rules_request_content_instance = ListFirewallRulesRequestContent.from_json(json)
# print the JSON string representation of the object
print(ListFirewallRulesRequestContent.to_json())

# convert the object into a dict
list_firewall_rules_request_content_dict = list_firewall_rules_request_content_instance.to_dict()
# create an instance of ListFirewallRulesRequestContent from a dict
list_firewall_rules_request_content_from_dict = ListFirewallRulesRequestContent.from_dict(list_firewall_rules_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


