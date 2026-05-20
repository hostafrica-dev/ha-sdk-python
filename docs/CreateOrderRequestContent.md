# CreateOrderRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo** | **str** | Promotional code to apply to the order | [optional] 
**products** | [**List[CreateOrderProduct]**](CreateOrderProduct.md) | List of products to order | 

## Example

```python
from ha_sdk_python.models.create_order_request_content import CreateOrderRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequestContent from a JSON string
create_order_request_content_instance = CreateOrderRequestContent.from_json(json)
# print the JSON string representation of the object
print(CreateOrderRequestContent.to_json())

# convert the object into a dict
create_order_request_content_dict = create_order_request_content_instance.to_dict()
# create an instance of CreateOrderRequestContent from a dict
create_order_request_content_from_dict = CreateOrderRequestContent.from_dict(create_order_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


