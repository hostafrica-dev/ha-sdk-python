# GetInvoiceDetailsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**GetInvoiceDetailsResponseData**](GetInvoiceDetailsResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_invoice_details_response_content import GetInvoiceDetailsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceDetailsResponseContent from a JSON string
get_invoice_details_response_content_instance = GetInvoiceDetailsResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceDetailsResponseContent.to_json())

# convert the object into a dict
get_invoice_details_response_content_dict = get_invoice_details_response_content_instance.to_dict()
# create an instance of GetInvoiceDetailsResponseContent from a dict
get_invoice_details_response_content_from_dict = GetInvoiceDetailsResponseContent.from_dict(get_invoice_details_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


