# lusid_scheduler.ApplicationMetadataApi

All URIs are relative to *https://fbn-ci.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_access_controlled_resources**](ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | [EXPERIMENTAL] ListAccessControlledResources: Get resources available for access control


# **list_access_controlled_resources**
> ResourceListOfAccessControlledResource list_access_controlled_resources()

[EXPERIMENTAL] ListAccessControlledResources: Get resources available for access control

Get the comprehensive set of resources that are available for access control

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.ApplicationMetadataApi(api_client)
    
    try:
        # [EXPERIMENTAL] ListAccessControlledResources: Get resources available for access control
        api_response = api_instance.list_access_controlled_resources()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationMetadataApi->list_access_controlled_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

