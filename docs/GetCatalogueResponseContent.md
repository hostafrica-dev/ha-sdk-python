# GetCatalogueResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**CatalogueData**](CatalogueData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_catalogue_response_content import GetCatalogueResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogueResponseContent from a JSON string
get_catalogue_response_content_instance = GetCatalogueResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetCatalogueResponseContent.to_json())

# convert the object into a dict
get_catalogue_response_content_dict = get_catalogue_response_content_instance.to_dict()
# create an instance of GetCatalogueResponseContent from a dict
get_catalogue_response_content_from_dict = GetCatalogueResponseContent.from_dict(get_catalogue_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


