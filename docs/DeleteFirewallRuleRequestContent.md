# DeleteFirewallRuleRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**pos** | **int** | Position/index of the rule to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_firewall_rule_request_content import DeleteFirewallRuleRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFirewallRuleRequestContent from a JSON string
delete_firewall_rule_request_content_instance = DeleteFirewallRuleRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteFirewallRuleRequestContent.to_json())

# convert the object into a dict
delete_firewall_rule_request_content_dict = delete_firewall_rule_request_content_instance.to_dict()
# create an instance of DeleteFirewallRuleRequestContent from a dict
delete_firewall_rule_request_content_from_dict = DeleteFirewallRuleRequestContent.from_dict(delete_firewall_rule_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


