# CreateOrderDomainItem

A domain line item returned in the order response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **int** | Line item identifier | 
**domain_id** | **str** | Domain identifier | 
**domain** | **str** | Domain name | 
**type** | **str** | Domain operation type (e.g. register, transfer) | 
**period** | **int** | Registration period in years | 
**domain_warranty** | **bool** | Whether domain warranty is included | 
**autorenew** | **bool** | Whether auto-renewal is enabled | 
**amount** | **str** | Line item amount charged (decimal string, e.g. \&quot;2333.33\&quot;) | 

## Example

```python
from ha_sdk_python.models.create_order_domain_item import CreateOrderDomainItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderDomainItem from a JSON string
create_order_domain_item_instance = CreateOrderDomainItem.from_json(json)
# print the JSON string representation of the object
print(CreateOrderDomainItem.to_json())

# convert the object into a dict
create_order_domain_item_dict = create_order_domain_item_instance.to_dict()
# create an instance of CreateOrderDomainItem from a dict
create_order_domain_item_from_dict = CreateOrderDomainItem.from_dict(create_order_domain_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


