# peertube-api-client
## _Generated for API v5.1.0_
## Command for generation

```bash
java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \                                                                                                                                                                                                   4s 973ms
  -i ./openapi.json \
  -g python \
  -o . \
  --package-name peertube_api_client
```

The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite
HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with
[openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO)
which generates a client SDK in the language of your choice - we generate some client SDKs automatically:

- [Python](https://framagit.org/framasoft/peertube/clients/python)
- [Go](https://framagit.org/framasoft/peertube/clients/go)
- [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)

See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few
examples of using the PeerTube API.

# Authentication

When you sign up for an account on a PeerTube instance, you are given the possibility
to generate sessions on it, and authenticate there using an access token. Only __one
access token can currently be used at a time__.

## Roles

Accounts are given permissions based on their role. There are three roles on
PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.

# Errors

The API uses standard HTTP status codes to indicate the success or failure
of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.

```
HTTP 1.1 404 Not Found
Content-Type: application/problem+json; charset=utf-8

{
  \"detail\": \"Video not found\",
  \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",
  \"status\": 404,
  \"title\": \"Not Found\",
  \"type\": \"about:blank\"
}
```

We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts),
but it is still optional. Types are used to disambiguate errors that bear the same status code
and are non-obvious:

```
HTTP 1.1 403 Forbidden
Content-Type: application/problem+json; charset=utf-8

{
  \"detail\": \"Cannot get this video regarding follow constraints\",
  \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",
  \"status\": 403,
  \"title\": \"Forbidden\",
  \"type\": \"https://docs.joinpeertube.org/api-rest-reference.html#section/Errors/does_not_respect_follow_constraints\"
}
```

Here a 403 error could otherwise mean that the video is private or blocklisted.

### Validation errors

Each parameter is evaluated on its own against a set of rules before the route validator
proceeds with potential testing involving parameter combinations. Errors coming from validation
errors appear earlier and benefit from a more detailed error description:

```
HTTP 1.1 400 Bad Request
Content-Type: application/problem+json; charset=utf-8

{
  \"detail\": \"Incorrect request parameters: id\",
  \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",
  \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",
  \"invalid-params\": {
    \"id\": {
      \"location\": \"params\",
      \"msg\": \"Invalid value\",
      \"param\": \"id\",
      \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"
    }
  },
  \"status\": 400,
  \"title\": \"Bad Request\",
  \"type\": \"about:blank\"
}
```

Where `id` is the name of the field concerned by the error, within the route definition.
`invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and
`invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg`
is about.

### Deprecated error fields

Some fields could be included with previous versions. They are still included but their use is deprecated:
- `error`: superseded by `detail`
- `code`: superseded by `type` (which is now an URI)

# Rate limits

We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:

| Endpoint (prefix: `/api/v1`) | Calls         | Time frame   |
|------------------------------|---------------|--------------|
| `/*`                         | 50            | 10 seconds   |
| `POST /users/token`          | 15            | 5 minutes    |
| `POST /users/register`       | 2<sup>*</sup> | 5 minutes    |
| `POST /users/ask-send-verify-email` | 3      | 5 minutes    |

Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service
limit is announced by a `429 Too Many Requests` status code.

You can get details about the current state of your rate limit by reading the
following headers:

| Header                  | Description                                                |
|-------------------------|------------------------------------------------------------|
| `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  |
| `X-RateLimit-Remaining` | Number of remaining requests in the current time period    |
| `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  |
| `Retry-After`           | Seconds to delay after the first `429` is received         |

# CORS

This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/),
allowing cross-domain communication from the browser for some routes:

| Endpoint                    |
|------------------------- ---|
| `/api/*`                    |
| `/download/*`               |
| `/lazy-static/*`            |
| `/.well-known/webfinger`    |

In addition, all routes serving ActivityPub are CORS-enabled for all origins.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://joinpeertube.org](https://joinpeertube.org)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import peertube_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import peertube_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import peertube_api_client
from peertube_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://peertube2.cpy.re
# See configuration.py for a list of all supported configuration parameters.
configuration = peertube_api_client.Configuration(
    host = "https://peertube2.cpy.re"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.AbusesApi(api_client)
    abuse_id = 56 # int | Abuse id

    try:
        # Delete an abuse
        api_instance.api_v1_abuses_abuse_id_delete(abuse_id)
    except ApiException as e:
        print("Exception when calling AbusesApi->api_v1_abuses_abuse_id_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://peertube2.cpy.re*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AbusesApi* | [**api_v1_abuses_abuse_id_delete**](docs/AbusesApi.md#api_v1_abuses_abuse_id_delete) | **DELETE** /api/v1/abuses/{abuseId} | Delete an abuse
*AbusesApi* | [**api_v1_abuses_abuse_id_messages_abuse_message_id_delete**](docs/AbusesApi.md#api_v1_abuses_abuse_id_messages_abuse_message_id_delete) | **DELETE** /api/v1/abuses/{abuseId}/messages/{abuseMessageId} | Delete an abuse message
*AbusesApi* | [**api_v1_abuses_abuse_id_messages_get**](docs/AbusesApi.md#api_v1_abuses_abuse_id_messages_get) | **GET** /api/v1/abuses/{abuseId}/messages | List messages of an abuse
*AbusesApi* | [**api_v1_abuses_abuse_id_messages_post**](docs/AbusesApi.md#api_v1_abuses_abuse_id_messages_post) | **POST** /api/v1/abuses/{abuseId}/messages | Add message to an abuse
*AbusesApi* | [**api_v1_abuses_abuse_id_put**](docs/AbusesApi.md#api_v1_abuses_abuse_id_put) | **PUT** /api/v1/abuses/{abuseId} | Update an abuse
*AbusesApi* | [**api_v1_abuses_post**](docs/AbusesApi.md#api_v1_abuses_post) | **POST** /api/v1/abuses | Report an abuse
*AbusesApi* | [**get_abuses**](docs/AbusesApi.md#get_abuses) | **GET** /api/v1/abuses | List abuses
*AbusesApi* | [**get_my_abuses**](docs/AbusesApi.md#get_my_abuses) | **GET** /api/v1/users/me/abuses | List my abuses
*AccountBlocksApi* | [**api_v1_blocklist_status_get**](docs/AccountBlocksApi.md#api_v1_blocklist_status_get) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
*AccountBlocksApi* | [**api_v1_server_blocklist_accounts_account_name_delete**](docs/AccountBlocksApi.md#api_v1_server_blocklist_accounts_account_name_delete) | **DELETE** /api/v1/server/blocklist/accounts/{accountName} | Unblock an account by its handle
*AccountBlocksApi* | [**api_v1_server_blocklist_accounts_get**](docs/AccountBlocksApi.md#api_v1_server_blocklist_accounts_get) | **GET** /api/v1/server/blocklist/accounts | List account blocks
*AccountBlocksApi* | [**api_v1_server_blocklist_accounts_post**](docs/AccountBlocksApi.md#api_v1_server_blocklist_accounts_post) | **POST** /api/v1/server/blocklist/accounts | Block an account
*AccountsApi* | [**api_v1_accounts_name_ratings_get**](docs/AccountsApi.md#api_v1_accounts_name_ratings_get) | **GET** /api/v1/accounts/{name}/ratings | List ratings of an account
*AccountsApi* | [**api_v1_accounts_name_video_channel_syncs_get**](docs/AccountsApi.md#api_v1_accounts_name_video_channel_syncs_get) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*AccountsApi* | [**api_v1_accounts_name_video_channels_get**](docs/AccountsApi.md#api_v1_accounts_name_video_channels_get) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
*AccountsApi* | [**api_v1_accounts_name_video_playlists_get**](docs/AccountsApi.md#api_v1_accounts_name_video_playlists_get) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /api/v1/accounts/{name} | Get an account
*AccountsApi* | [**get_account_followers**](docs/AccountsApi.md#get_account_followers) | **GET** /api/v1/accounts/{name}/followers | List followers of an account
*AccountsApi* | [**get_account_videos**](docs/AccountsApi.md#get_account_videos) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
*AccountsApi* | [**get_accounts**](docs/AccountsApi.md#get_accounts) | **GET** /api/v1/accounts | List accounts
*ChannelsSyncApi* | [**add_video_channel_sync**](docs/ChannelsSyncApi.md#add_video_channel_sync) | **POST** /api/v1/video-channel-syncs | Create a synchronization for a video channel
*ChannelsSyncApi* | [**api_v1_accounts_name_video_channel_syncs_get**](docs/ChannelsSyncApi.md#api_v1_accounts_name_video_channel_syncs_get) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*ChannelsSyncApi* | [**api_v1_video_channels_channel_handle_import_videos_post**](docs/ChannelsSyncApi.md#api_v1_video_channels_channel_handle_import_videos_post) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
*ChannelsSyncApi* | [**del_video_channel_sync**](docs/ChannelsSyncApi.md#del_video_channel_sync) | **DELETE** /api/v1/video-channel-syncs/{channelSyncId} | Delete a video channel synchronization
*ChannelsSyncApi* | [**trigger_video_channel_sync**](docs/ChannelsSyncApi.md#trigger_video_channel_sync) | **POST** /api/v1/video-channel-syncs/{channelSyncId}/sync | Triggers the channel synchronization job, fetching all the videos from the remote channel
*ConfigApi* | [**del_custom_config**](docs/ConfigApi.md#del_custom_config) | **DELETE** /api/v1/config/custom | Delete instance runtime configuration
*ConfigApi* | [**get_about**](docs/ConfigApi.md#get_about) | **GET** /api/v1/config/about | Get instance \&quot;About\&quot; information
*ConfigApi* | [**get_config**](docs/ConfigApi.md#get_config) | **GET** /api/v1/config | Get instance public configuration
*ConfigApi* | [**get_custom_config**](docs/ConfigApi.md#get_custom_config) | **GET** /api/v1/config/custom | Get instance runtime configuration
*ConfigApi* | [**put_custom_config**](docs/ConfigApi.md#put_custom_config) | **PUT** /api/v1/config/custom | Set instance runtime configuration
*HomepageApi* | [**api_v1_custom_pages_homepage_instance_get**](docs/HomepageApi.md#api_v1_custom_pages_homepage_instance_get) | **GET** /api/v1/custom-pages/homepage/instance | Get instance custom homepage
*HomepageApi* | [**api_v1_custom_pages_homepage_instance_put**](docs/HomepageApi.md#api_v1_custom_pages_homepage_instance_put) | **PUT** /api/v1/custom-pages/homepage/instance | Set instance custom homepage
*InstanceFollowsApi* | [**api_v1_server_followers_get**](docs/InstanceFollowsApi.md#api_v1_server_followers_get) | **GET** /api/v1/server/followers | List instances following the server
*InstanceFollowsApi* | [**api_v1_server_followers_name_with_host_accept_post**](docs/InstanceFollowsApi.md#api_v1_server_followers_name_with_host_accept_post) | **POST** /api/v1/server/followers/{nameWithHost}/accept | Accept a pending follower to your server
*InstanceFollowsApi* | [**api_v1_server_followers_name_with_host_delete**](docs/InstanceFollowsApi.md#api_v1_server_followers_name_with_host_delete) | **DELETE** /api/v1/server/followers/{nameWithHost} | Remove or reject a follower to your server
*InstanceFollowsApi* | [**api_v1_server_followers_name_with_host_reject_post**](docs/InstanceFollowsApi.md#api_v1_server_followers_name_with_host_reject_post) | **POST** /api/v1/server/followers/{nameWithHost}/reject | Reject a pending follower to your server
*InstanceFollowsApi* | [**api_v1_server_following_get**](docs/InstanceFollowsApi.md#api_v1_server_following_get) | **GET** /api/v1/server/following | List instances followed by the server
*InstanceFollowsApi* | [**api_v1_server_following_host_or_handle_delete**](docs/InstanceFollowsApi.md#api_v1_server_following_host_or_handle_delete) | **DELETE** /api/v1/server/following/{hostOrHandle} | Unfollow an actor (PeerTube instance, channel or account)
*InstanceFollowsApi* | [**api_v1_server_following_post**](docs/InstanceFollowsApi.md#api_v1_server_following_post) | **POST** /api/v1/server/following | Follow a list of actors (PeerTube instance, channel or account)
*InstanceRedundancyApi* | [**api_v1_server_redundancy_host_put**](docs/InstanceRedundancyApi.md#api_v1_server_redundancy_host_put) | **PUT** /api/v1/server/redundancy/{host} | Update a server redundancy policy
*JobApi* | [**api_v1_jobs_pause_post**](docs/JobApi.md#api_v1_jobs_pause_post) | **POST** /api/v1/jobs/pause | Pause job queue
*JobApi* | [**api_v1_jobs_resume_post**](docs/JobApi.md#api_v1_jobs_resume_post) | **POST** /api/v1/jobs/resume | Resume job queue
*JobApi* | [**get_jobs**](docs/JobApi.md#get_jobs) | **GET** /api/v1/jobs/{state} | List instance jobs
*LiveVideosApi* | [**add_live**](docs/LiveVideosApi.md#add_live) | **POST** /api/v1/videos/live | Create a live
*LiveVideosApi* | [**api_v1_videos_id_live_session_get**](docs/LiveVideosApi.md#api_v1_videos_id_live_session_get) | **GET** /api/v1/videos/{id}/live-session | Get live session of a replay
*LiveVideosApi* | [**api_v1_videos_live_id_sessions_get**](docs/LiveVideosApi.md#api_v1_videos_live_id_sessions_get) | **GET** /api/v1/videos/live/{id}/sessions | List live sessions
*LiveVideosApi* | [**get_live_id**](docs/LiveVideosApi.md#get_live_id) | **GET** /api/v1/videos/live/{id} | Get information about a live
*LiveVideosApi* | [**update_live_id**](docs/LiveVideosApi.md#update_live_id) | **PUT** /api/v1/videos/live/{id} | Update information about a live
*LogsApi* | [**get_instance_audit_logs**](docs/LogsApi.md#get_instance_audit_logs) | **GET** /api/v1/server/audit-logs | Get instance audit logs
*LogsApi* | [**get_instance_logs**](docs/LogsApi.md#get_instance_logs) | **GET** /api/v1/server/logs | Get instance logs
*LogsApi* | [**send_client_log**](docs/LogsApi.md#send_client_log) | **POST** /api/v1/server/logs/client | Send client log
*MyHistoryApi* | [**api_v1_users_me_history_videos_get**](docs/MyHistoryApi.md#api_v1_users_me_history_videos_get) | **GET** /api/v1/users/me/history/videos | List watched videos history
*MyHistoryApi* | [**api_v1_users_me_history_videos_remove_post**](docs/MyHistoryApi.md#api_v1_users_me_history_videos_remove_post) | **POST** /api/v1/users/me/history/videos/remove | Clear video history
*MyHistoryApi* | [**api_v1_users_me_history_videos_video_id_delete**](docs/MyHistoryApi.md#api_v1_users_me_history_videos_video_id_delete) | **DELETE** /api/v1/users/me/history/videos/{videoId} | Delete history element
*MyNotificationsApi* | [**api_v1_users_me_notification_settings_put**](docs/MyNotificationsApi.md#api_v1_users_me_notification_settings_put) | **PUT** /api/v1/users/me/notification-settings | Update my notification settings
*MyNotificationsApi* | [**api_v1_users_me_notifications_get**](docs/MyNotificationsApi.md#api_v1_users_me_notifications_get) | **GET** /api/v1/users/me/notifications | List my notifications
*MyNotificationsApi* | [**api_v1_users_me_notifications_read_all_post**](docs/MyNotificationsApi.md#api_v1_users_me_notifications_read_all_post) | **POST** /api/v1/users/me/notifications/read-all | Mark all my notification as read
*MyNotificationsApi* | [**api_v1_users_me_notifications_read_post**](docs/MyNotificationsApi.md#api_v1_users_me_notifications_read_post) | **POST** /api/v1/users/me/notifications/read | Mark notifications as read by their id
*MySubscriptionsApi* | [**api_v1_users_me_subscriptions_exist_get**](docs/MySubscriptionsApi.md#api_v1_users_me_subscriptions_exist_get) | **GET** /api/v1/users/me/subscriptions/exist | Get if subscriptions exist for my user
*MySubscriptionsApi* | [**api_v1_users_me_subscriptions_get**](docs/MySubscriptionsApi.md#api_v1_users_me_subscriptions_get) | **GET** /api/v1/users/me/subscriptions | Get my user subscriptions
*MySubscriptionsApi* | [**api_v1_users_me_subscriptions_post**](docs/MySubscriptionsApi.md#api_v1_users_me_subscriptions_post) | **POST** /api/v1/users/me/subscriptions | Add subscription to my user
*MySubscriptionsApi* | [**api_v1_users_me_subscriptions_subscription_handle_delete**](docs/MySubscriptionsApi.md#api_v1_users_me_subscriptions_subscription_handle_delete) | **DELETE** /api/v1/users/me/subscriptions/{subscriptionHandle} | Delete subscription of my user
*MySubscriptionsApi* | [**api_v1_users_me_subscriptions_subscription_handle_get**](docs/MySubscriptionsApi.md#api_v1_users_me_subscriptions_subscription_handle_get) | **GET** /api/v1/users/me/subscriptions/{subscriptionHandle} | Get subscription of my user
*MySubscriptionsApi* | [**api_v1_users_me_subscriptions_videos_get**](docs/MySubscriptionsApi.md#api_v1_users_me_subscriptions_videos_get) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
*MyUserApi* | [**api_v1_users_me_avatar_delete**](docs/MyUserApi.md#api_v1_users_me_avatar_delete) | **DELETE** /api/v1/users/me/avatar | Delete my avatar
*MyUserApi* | [**api_v1_users_me_avatar_pick_post**](docs/MyUserApi.md#api_v1_users_me_avatar_pick_post) | **POST** /api/v1/users/me/avatar/pick | Update my user avatar
*MyUserApi* | [**api_v1_users_me_video_quota_used_get**](docs/MyUserApi.md#api_v1_users_me_video_quota_used_get) | **GET** /api/v1/users/me/video-quota-used | Get my user used quota
*MyUserApi* | [**api_v1_users_me_videos_get**](docs/MyUserApi.md#api_v1_users_me_videos_get) | **GET** /api/v1/users/me/videos | Get videos of my user
*MyUserApi* | [**api_v1_users_me_videos_imports_get**](docs/MyUserApi.md#api_v1_users_me_videos_imports_get) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
*MyUserApi* | [**api_v1_users_me_videos_video_id_rating_get**](docs/MyUserApi.md#api_v1_users_me_videos_video_id_rating_get) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
*MyUserApi* | [**get_my_abuses**](docs/MyUserApi.md#get_my_abuses) | **GET** /api/v1/users/me/abuses | List my abuses
*MyUserApi* | [**get_user_info**](docs/MyUserApi.md#get_user_info) | **GET** /api/v1/users/me | Get my user information
*MyUserApi* | [**put_user_info**](docs/MyUserApi.md#put_user_info) | **PUT** /api/v1/users/me | Update my user information
*PluginsApi* | [**add_plugin**](docs/PluginsApi.md#add_plugin) | **POST** /api/v1/plugins/install | Install a plugin
*PluginsApi* | [**api_v1_plugins_npm_name_public_settings_get**](docs/PluginsApi.md#api_v1_plugins_npm_name_public_settings_get) | **GET** /api/v1/plugins/{npmName}/public-settings | Get a plugin&#39;s public settings
*PluginsApi* | [**api_v1_plugins_npm_name_registered_settings_get**](docs/PluginsApi.md#api_v1_plugins_npm_name_registered_settings_get) | **GET** /api/v1/plugins/{npmName}/registered-settings | Get a plugin&#39;s registered settings
*PluginsApi* | [**api_v1_plugins_npm_name_settings_put**](docs/PluginsApi.md#api_v1_plugins_npm_name_settings_put) | **PUT** /api/v1/plugins/{npmName}/settings | Set a plugin&#39;s settings
*PluginsApi* | [**get_available_plugins**](docs/PluginsApi.md#get_available_plugins) | **GET** /api/v1/plugins/available | List available plugins
*PluginsApi* | [**get_plugin**](docs/PluginsApi.md#get_plugin) | **GET** /api/v1/plugins/{npmName} | Get a plugin
*PluginsApi* | [**get_plugins**](docs/PluginsApi.md#get_plugins) | **GET** /api/v1/plugins | List plugins
*PluginsApi* | [**uninstall_plugin**](docs/PluginsApi.md#uninstall_plugin) | **POST** /api/v1/plugins/uninstall | Uninstall a plugin
*PluginsApi* | [**update_plugin**](docs/PluginsApi.md#update_plugin) | **POST** /api/v1/plugins/update | Update a plugin
*RegisterApi* | [**accept_registration**](docs/RegisterApi.md#accept_registration) | **POST** /api/v1/users/registrations/{registrationId}/accept | Accept registration
*RegisterApi* | [**delete_registration**](docs/RegisterApi.md#delete_registration) | **DELETE** /api/v1/users/registrations/{registrationId} | Delete registration
*RegisterApi* | [**list_registrations**](docs/RegisterApi.md#list_registrations) | **GET** /api/v1/users/registrations | List registrations
*RegisterApi* | [**register_user**](docs/RegisterApi.md#register_user) | **POST** /api/v1/users/register | Register a user
*RegisterApi* | [**reject_registration**](docs/RegisterApi.md#reject_registration) | **POST** /api/v1/users/registrations/{registrationId}/reject | Reject registration
*RegisterApi* | [**request_registration**](docs/RegisterApi.md#request_registration) | **POST** /api/v1/users/registrations/request | Request registration
*RegisterApi* | [**resend_email_to_verify_registration**](docs/RegisterApi.md#resend_email_to_verify_registration) | **POST** /api/v1/users/registrations/ask-send-verify-email | Resend verification link to registration email
*RegisterApi* | [**resend_email_to_verify_user**](docs/RegisterApi.md#resend_email_to_verify_user) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
*RegisterApi* | [**verify_registration_email**](docs/RegisterApi.md#verify_registration_email) | **POST** /api/v1/users/registrations/{registrationId}/verify-email | Verify a registration email
*RegisterApi* | [**verify_user**](docs/RegisterApi.md#verify_user) | **POST** /api/v1/users/{id}/verify-email | Verify a user
*RunnerJobsApi* | [**api_v1_runners_jobs_get**](docs/RunnerJobsApi.md#api_v1_runners_jobs_get) | **GET** /api/v1/runners/jobs | List jobs
*RunnerJobsApi* | [**api_v1_runners_jobs_job_uuid_abort_post**](docs/RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_abort_post) | **POST** /api/v1/runners/jobs/{jobUUID}/abort | Abort job
*RunnerJobsApi* | [**api_v1_runners_jobs_job_uuid_accept_post**](docs/RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_accept_post) | **POST** /api/v1/runners/jobs/{jobUUID}/accept | Accept job
*RunnerJobsApi* | [**api_v1_runners_jobs_job_uuid_cancel_get**](docs/RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_cancel_get) | **GET** /api/v1/runners/jobs/{jobUUID}/cancel | Cancel a job
*RunnerJobsApi* | [**api_v1_runners_jobs_job_uuid_error_post**](docs/RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_error_post) | **POST** /api/v1/runners/jobs/{jobUUID}/error | Post job error
*RunnerJobsApi* | [**api_v1_runners_jobs_job_uuid_success_post**](docs/RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_success_post) | **POST** /api/v1/runners/jobs/{jobUUID}/success | Post job success
*RunnerJobsApi* | [**api_v1_runners_jobs_job_uuid_update_post**](docs/RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_update_post) | **POST** /api/v1/runners/jobs/{jobUUID}/update | Update job
*RunnerJobsApi* | [**api_v1_runners_jobs_request_post**](docs/RunnerJobsApi.md#api_v1_runners_jobs_request_post) | **POST** /api/v1/runners/jobs/request | Request a new job
*RunnerRegistrationTokenApi* | [**api_v1_runners_registration_tokens_generate_post**](docs/RunnerRegistrationTokenApi.md#api_v1_runners_registration_tokens_generate_post) | **POST** /api/v1/runners/registration-tokens/generate | Generate registration token
*RunnerRegistrationTokenApi* | [**api_v1_runners_registration_tokens_get**](docs/RunnerRegistrationTokenApi.md#api_v1_runners_registration_tokens_get) | **GET** /api/v1/runners/registration-tokens | List registration tokens
*RunnerRegistrationTokenApi* | [**api_v1_runners_registration_tokens_registration_token_id_delete**](docs/RunnerRegistrationTokenApi.md#api_v1_runners_registration_tokens_registration_token_id_delete) | **DELETE** /api/v1/runners/registration-tokens/{registrationTokenId} | Remove registration token
*RunnersApi* | [**api_v1_runners_get**](docs/RunnersApi.md#api_v1_runners_get) | **GET** /api/v1/runners | List runners
*RunnersApi* | [**api_v1_runners_register_post**](docs/RunnersApi.md#api_v1_runners_register_post) | **POST** /api/v1/runners/register | Register a new runner
*RunnersApi* | [**api_v1_runners_runner_id_delete**](docs/RunnersApi.md#api_v1_runners_runner_id_delete) | **DELETE** /api/v1/runners/{runnerId} | Delete a runner
*RunnersApi* | [**api_v1_runners_unregister_post**](docs/RunnersApi.md#api_v1_runners_unregister_post) | **POST** /api/v1/runners/unregister | Unregister a runner
*SearchApi* | [**search_channels**](docs/SearchApi.md#search_channels) | **GET** /api/v1/search/video-channels | Search channels
*SearchApi* | [**search_playlists**](docs/SearchApi.md#search_playlists) | **GET** /api/v1/search/video-playlists | Search playlists
*SearchApi* | [**search_videos**](docs/SearchApi.md#search_videos) | **GET** /api/v1/search/videos | Search videos
*ServerBlocksApi* | [**api_v1_blocklist_status_get**](docs/ServerBlocksApi.md#api_v1_blocklist_status_get) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
*ServerBlocksApi* | [**api_v1_server_blocklist_servers_get**](docs/ServerBlocksApi.md#api_v1_server_blocklist_servers_get) | **GET** /api/v1/server/blocklist/servers | List server blocks
*ServerBlocksApi* | [**api_v1_server_blocklist_servers_host_delete**](docs/ServerBlocksApi.md#api_v1_server_blocklist_servers_host_delete) | **DELETE** /api/v1/server/blocklist/servers/{host} | Unblock a server by its domain
*ServerBlocksApi* | [**api_v1_server_blocklist_servers_post**](docs/ServerBlocksApi.md#api_v1_server_blocklist_servers_post) | **POST** /api/v1/server/blocklist/servers | Block a server
*SessionApi* | [**get_o_auth_client**](docs/SessionApi.md#get_o_auth_client) | **GET** /api/v1/oauth-clients/local | Login prerequisite
*SessionApi* | [**get_o_auth_token**](docs/SessionApi.md#get_o_auth_token) | **POST** /api/v1/users/token | Login
*SessionApi* | [**revoke_o_auth_token**](docs/SessionApi.md#revoke_o_auth_token) | **POST** /api/v1/users/revoke-token | Logout
*StaticVideoFilesApi* | [**static_streaming_playlists_hls_filename_get**](docs/StaticVideoFilesApi.md#static_streaming_playlists_hls_filename_get) | **GET** /static/streaming-playlists/hls/{filename} | Get public HLS video file
*StaticVideoFilesApi* | [**static_streaming_playlists_hls_private_filename_get**](docs/StaticVideoFilesApi.md#static_streaming_playlists_hls_private_filename_get) | **GET** /static/streaming-playlists/hls/private/{filename} | Get private HLS video file
*StaticVideoFilesApi* | [**static_webseed_filename_get**](docs/StaticVideoFilesApi.md#static_webseed_filename_get) | **GET** /static/webseed/{filename} | Get public WebTorrent video file
*StaticVideoFilesApi* | [**static_webseed_private_filename_get**](docs/StaticVideoFilesApi.md#static_webseed_private_filename_get) | **GET** /static/webseed/private/{filename} | Get private WebTorrent video file
*StatsApi* | [**api_v1_metrics_playback_post**](docs/StatsApi.md#api_v1_metrics_playback_post) | **POST** /api/v1/metrics/playback | Create playback metrics
*StatsApi* | [**get_instance_stats**](docs/StatsApi.md#get_instance_stats) | **GET** /api/v1/server/stats | Get instance stats
*UsersApi* | [**add_user**](docs/UsersApi.md#add_user) | **POST** /api/v1/users | Create a user
*UsersApi* | [**confirm_two_factor_request**](docs/UsersApi.md#confirm_two_factor_request) | **POST** /api/v1/users/{id}/two-factor/confirm-request | Confirm two factor auth
*UsersApi* | [**del_user**](docs/UsersApi.md#del_user) | **DELETE** /api/v1/users/{id} | Delete a user
*UsersApi* | [**disable_two_factor**](docs/UsersApi.md#disable_two_factor) | **POST** /api/v1/users/{id}/two-factor/disable | Disable two factor auth
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /api/v1/users/{id} | Get a user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /api/v1/users | List users
*UsersApi* | [**put_user**](docs/UsersApi.md#put_user) | **PUT** /api/v1/users/{id} | Update a user
*UsersApi* | [**request_two_factor**](docs/UsersApi.md#request_two_factor) | **POST** /api/v1/users/{id}/two-factor/request | Request two factor auth
*UsersApi* | [**resend_email_to_verify_user**](docs/UsersApi.md#resend_email_to_verify_user) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
*UsersApi* | [**verify_user**](docs/UsersApi.md#verify_user) | **POST** /api/v1/users/{id}/verify-email | Verify a user
*VideoApi* | [**add_live**](docs/VideoApi.md#add_live) | **POST** /api/v1/videos/live | Create a live
*VideoApi* | [**add_view**](docs/VideoApi.md#add_view) | **POST** /api/v1/videos/{id}/views | Notify user is watching a video
*VideoApi* | [**api_v1_videos_id_studio_edit_post**](docs/VideoApi.md#api_v1_videos_id_studio_edit_post) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
*VideoApi* | [**api_v1_videos_id_watching_put**](docs/VideoApi.md#api_v1_videos_id_watching_put) | **PUT** /api/v1/videos/{id}/watching | Set watching progress of a video
*VideoApi* | [**del_video**](docs/VideoApi.md#del_video) | **DELETE** /api/v1/videos/{id} | Delete a video
*VideoApi* | [**get_account_videos**](docs/VideoApi.md#get_account_videos) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
*VideoApi* | [**get_categories**](docs/VideoApi.md#get_categories) | **GET** /api/v1/videos/categories | List available video categories
*VideoApi* | [**get_languages**](docs/VideoApi.md#get_languages) | **GET** /api/v1/videos/languages | List available video languages
*VideoApi* | [**get_licences**](docs/VideoApi.md#get_licences) | **GET** /api/v1/videos/licences | List available video licences
*VideoApi* | [**get_live_id**](docs/VideoApi.md#get_live_id) | **GET** /api/v1/videos/live/{id} | Get information about a live
*VideoApi* | [**get_video**](docs/VideoApi.md#get_video) | **GET** /api/v1/videos/{id} | Get a video
*VideoApi* | [**get_video_channel_videos**](docs/VideoApi.md#get_video_channel_videos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
*VideoApi* | [**get_video_desc**](docs/VideoApi.md#get_video_desc) | **GET** /api/v1/videos/{id}/description | Get complete video description
*VideoApi* | [**get_video_privacy_policies**](docs/VideoApi.md#get_video_privacy_policies) | **GET** /api/v1/videos/privacies | List available video privacy policies
*VideoApi* | [**get_video_source**](docs/VideoApi.md#get_video_source) | **POST** /api/v1/videos/{id}/source | Get video source file metadata
*VideoApi* | [**get_videos**](docs/VideoApi.md#get_videos) | **GET** /api/v1/videos | List videos
*VideoApi* | [**put_video**](docs/VideoApi.md#put_video) | **PUT** /api/v1/videos/{id} | Update a video
*VideoApi* | [**request_video_token**](docs/VideoApi.md#request_video_token) | **POST** /api/v1/videos/{id}/token | Request video token
*VideoApi* | [**update_live_id**](docs/VideoApi.md#update_live_id) | **PUT** /api/v1/videos/live/{id} | Update information about a live
*VideoApi* | [**upload_legacy**](docs/VideoApi.md#upload_legacy) | **POST** /api/v1/videos/upload | Upload a video
*VideoApi* | [**upload_resumable**](docs/VideoApi.md#upload_resumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
*VideoApi* | [**upload_resumable_cancel**](docs/VideoApi.md#upload_resumable_cancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
*VideoApi* | [**upload_resumable_init**](docs/VideoApi.md#upload_resumable_init) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video
*VideoBlocksApi* | [**add_video_block**](docs/VideoBlocksApi.md#add_video_block) | **POST** /api/v1/videos/{id}/blacklist | Block a video
*VideoBlocksApi* | [**del_video_block**](docs/VideoBlocksApi.md#del_video_block) | **DELETE** /api/v1/videos/{id}/blacklist | Unblock a video by its id
*VideoBlocksApi* | [**get_video_blocks**](docs/VideoBlocksApi.md#get_video_blocks) | **GET** /api/v1/videos/blacklist | List video blocks
*VideoCaptionsApi* | [**add_video_caption**](docs/VideoCaptionsApi.md#add_video_caption) | **PUT** /api/v1/videos/{id}/captions/{captionLanguage} | Add or replace a video caption
*VideoCaptionsApi* | [**del_video_caption**](docs/VideoCaptionsApi.md#del_video_caption) | **DELETE** /api/v1/videos/{id}/captions/{captionLanguage} | Delete a video caption
*VideoCaptionsApi* | [**get_video_captions**](docs/VideoCaptionsApi.md#get_video_captions) | **GET** /api/v1/videos/{id}/captions | List captions of a video
*VideoChannelsApi* | [**add_video_channel**](docs/VideoChannelsApi.md#add_video_channel) | **POST** /api/v1/video-channels | Create a video channel
*VideoChannelsApi* | [**api_v1_accounts_name_video_channel_syncs_get**](docs/VideoChannelsApi.md#api_v1_accounts_name_video_channel_syncs_get) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*VideoChannelsApi* | [**api_v1_accounts_name_video_channels_get**](docs/VideoChannelsApi.md#api_v1_accounts_name_video_channels_get) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
*VideoChannelsApi* | [**api_v1_video_channels_channel_handle_avatar_delete**](docs/VideoChannelsApi.md#api_v1_video_channels_channel_handle_avatar_delete) | **DELETE** /api/v1/video-channels/{channelHandle}/avatar | Delete channel avatar
*VideoChannelsApi* | [**api_v1_video_channels_channel_handle_avatar_pick_post**](docs/VideoChannelsApi.md#api_v1_video_channels_channel_handle_avatar_pick_post) | **POST** /api/v1/video-channels/{channelHandle}/avatar/pick | Update channel avatar
*VideoChannelsApi* | [**api_v1_video_channels_channel_handle_banner_delete**](docs/VideoChannelsApi.md#api_v1_video_channels_channel_handle_banner_delete) | **DELETE** /api/v1/video-channels/{channelHandle}/banner | Delete channel banner
*VideoChannelsApi* | [**api_v1_video_channels_channel_handle_banner_pick_post**](docs/VideoChannelsApi.md#api_v1_video_channels_channel_handle_banner_pick_post) | **POST** /api/v1/video-channels/{channelHandle}/banner/pick | Update channel banner
*VideoChannelsApi* | [**api_v1_video_channels_channel_handle_import_videos_post**](docs/VideoChannelsApi.md#api_v1_video_channels_channel_handle_import_videos_post) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
*VideoChannelsApi* | [**api_v1_video_channels_channel_handle_video_playlists_get**](docs/VideoChannelsApi.md#api_v1_video_channels_channel_handle_video_playlists_get) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
*VideoChannelsApi* | [**del_video_channel**](docs/VideoChannelsApi.md#del_video_channel) | **DELETE** /api/v1/video-channels/{channelHandle} | Delete a video channel
*VideoChannelsApi* | [**get_video_channel**](docs/VideoChannelsApi.md#get_video_channel) | **GET** /api/v1/video-channels/{channelHandle} | Get a video channel
*VideoChannelsApi* | [**get_video_channel_followers**](docs/VideoChannelsApi.md#get_video_channel_followers) | **GET** /api/v1/video-channels/{channelHandle}/followers | List followers of a video channel
*VideoChannelsApi* | [**get_video_channel_videos**](docs/VideoChannelsApi.md#get_video_channel_videos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
*VideoChannelsApi* | [**get_video_channels**](docs/VideoChannelsApi.md#get_video_channels) | **GET** /api/v1/video-channels | List video channels
*VideoChannelsApi* | [**put_video_channel**](docs/VideoChannelsApi.md#put_video_channel) | **PUT** /api/v1/video-channels/{channelHandle} | Update a video channel
*VideoCommentsApi* | [**api_v1_videos_id_comment_threads_get**](docs/VideoCommentsApi.md#api_v1_videos_id_comment_threads_get) | **GET** /api/v1/videos/{id}/comment-threads | List threads of a video
*VideoCommentsApi* | [**api_v1_videos_id_comment_threads_post**](docs/VideoCommentsApi.md#api_v1_videos_id_comment_threads_post) | **POST** /api/v1/videos/{id}/comment-threads | Create a thread
*VideoCommentsApi* | [**api_v1_videos_id_comment_threads_thread_id_get**](docs/VideoCommentsApi.md#api_v1_videos_id_comment_threads_thread_id_get) | **GET** /api/v1/videos/{id}/comment-threads/{threadId} | Get a thread
*VideoCommentsApi* | [**api_v1_videos_id_comments_comment_id_delete**](docs/VideoCommentsApi.md#api_v1_videos_id_comments_comment_id_delete) | **DELETE** /api/v1/videos/{id}/comments/{commentId} | Delete a comment or a reply
*VideoCommentsApi* | [**api_v1_videos_id_comments_comment_id_post**](docs/VideoCommentsApi.md#api_v1_videos_id_comments_comment_id_post) | **POST** /api/v1/videos/{id}/comments/{commentId} | Reply to a thread of a video
*VideoFeedsApi* | [**get_syndicated_comments**](docs/VideoFeedsApi.md#get_syndicated_comments) | **GET** /feeds/video-comments.{format} | Comments on videos feeds
*VideoFeedsApi* | [**get_syndicated_subscription_videos**](docs/VideoFeedsApi.md#get_syndicated_subscription_videos) | **GET** /feeds/subscriptions.{format} | Videos of subscriptions feeds
*VideoFeedsApi* | [**get_syndicated_videos**](docs/VideoFeedsApi.md#get_syndicated_videos) | **GET** /feeds/videos.{format} | Common videos feeds
*VideoFeedsApi* | [**get_videos_podcast_feed**](docs/VideoFeedsApi.md#get_videos_podcast_feed) | **GET** /feeds/podcast/videos.xml | Videos podcast feed
*VideoFilesApi* | [**del_video_hls**](docs/VideoFilesApi.md#del_video_hls) | **DELETE** /api/v1/videos/{id}/hls | Delete video HLS files
*VideoFilesApi* | [**del_video_web_torrent**](docs/VideoFilesApi.md#del_video_web_torrent) | **DELETE** /api/v1/videos/{id}/webtorrent | Delete video WebTorrent files
*VideoImportsApi* | [**api_v1_videos_imports_id_cancel_post**](docs/VideoImportsApi.md#api_v1_videos_imports_id_cancel_post) | **POST** /api/v1/videos/imports/{id}/cancel | Cancel video import
*VideoImportsApi* | [**api_v1_videos_imports_id_delete**](docs/VideoImportsApi.md#api_v1_videos_imports_id_delete) | **DELETE** /api/v1/videos/imports/{id} | Delete video import
*VideoImportsApi* | [**import_video**](docs/VideoImportsApi.md#import_video) | **POST** /api/v1/videos/imports | Import a video
*VideoMirroringApi* | [**del_mirrored_video**](docs/VideoMirroringApi.md#del_mirrored_video) | **DELETE** /api/v1/server/redundancy/videos/{redundancyId} | Delete a mirror done on a video
*VideoMirroringApi* | [**get_mirrored_videos**](docs/VideoMirroringApi.md#get_mirrored_videos) | **GET** /api/v1/server/redundancy/videos | List videos being mirrored
*VideoMirroringApi* | [**put_mirrored_video**](docs/VideoMirroringApi.md#put_mirrored_video) | **POST** /api/v1/server/redundancy/videos | Mirror a video
*VideoOwnershipChangeApi* | [**api_v1_videos_id_give_ownership_post**](docs/VideoOwnershipChangeApi.md#api_v1_videos_id_give_ownership_post) | **POST** /api/v1/videos/{id}/give-ownership | Request ownership change
*VideoOwnershipChangeApi* | [**api_v1_videos_ownership_get**](docs/VideoOwnershipChangeApi.md#api_v1_videos_ownership_get) | **GET** /api/v1/videos/ownership | List video ownership changes
*VideoOwnershipChangeApi* | [**api_v1_videos_ownership_id_accept_post**](docs/VideoOwnershipChangeApi.md#api_v1_videos_ownership_id_accept_post) | **POST** /api/v1/videos/ownership/{id}/accept | Accept ownership change request
*VideoOwnershipChangeApi* | [**api_v1_videos_ownership_id_refuse_post**](docs/VideoOwnershipChangeApi.md#api_v1_videos_ownership_id_refuse_post) | **POST** /api/v1/videos/ownership/{id}/refuse | Refuse ownership change request
*VideoPlaylistsApi* | [**add_playlist**](docs/VideoPlaylistsApi.md#add_playlist) | **POST** /api/v1/video-playlists | Create a video playlist
*VideoPlaylistsApi* | [**add_video_playlist_video**](docs/VideoPlaylistsApi.md#add_video_playlist_video) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
*VideoPlaylistsApi* | [**api_v1_accounts_name_video_playlists_get**](docs/VideoPlaylistsApi.md#api_v1_accounts_name_video_playlists_get) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
*VideoPlaylistsApi* | [**api_v1_users_me_video_playlists_videos_exist_get**](docs/VideoPlaylistsApi.md#api_v1_users_me_video_playlists_videos_exist_get) | **GET** /api/v1/users/me/video-playlists/videos-exist | Check video exists in my playlists
*VideoPlaylistsApi* | [**api_v1_video_channels_channel_handle_video_playlists_get**](docs/VideoPlaylistsApi.md#api_v1_video_channels_channel_handle_video_playlists_get) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
*VideoPlaylistsApi* | [**api_v1_video_playlists_playlist_id_delete**](docs/VideoPlaylistsApi.md#api_v1_video_playlists_playlist_id_delete) | **DELETE** /api/v1/video-playlists/{playlistId} | Delete a video playlist
*VideoPlaylistsApi* | [**api_v1_video_playlists_playlist_id_get**](docs/VideoPlaylistsApi.md#api_v1_video_playlists_playlist_id_get) | **GET** /api/v1/video-playlists/{playlistId} | Get a video playlist
*VideoPlaylistsApi* | [**api_v1_video_playlists_playlist_id_put**](docs/VideoPlaylistsApi.md#api_v1_video_playlists_playlist_id_put) | **PUT** /api/v1/video-playlists/{playlistId} | Update a video playlist
*VideoPlaylistsApi* | [**del_video_playlist_video**](docs/VideoPlaylistsApi.md#del_video_playlist_video) | **DELETE** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Delete an element from a playlist
*VideoPlaylistsApi* | [**get_playlist_privacy_policies**](docs/VideoPlaylistsApi.md#get_playlist_privacy_policies) | **GET** /api/v1/video-playlists/privacies | List available playlist privacy policies
*VideoPlaylistsApi* | [**get_playlists**](docs/VideoPlaylistsApi.md#get_playlists) | **GET** /api/v1/video-playlists | List video playlists
*VideoPlaylistsApi* | [**get_video_playlist_videos**](docs/VideoPlaylistsApi.md#get_video_playlist_videos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist
*VideoPlaylistsApi* | [**put_video_playlist_video**](docs/VideoPlaylistsApi.md#put_video_playlist_video) | **PUT** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Update a playlist element
*VideoPlaylistsApi* | [**reorder_video_playlist**](docs/VideoPlaylistsApi.md#reorder_video_playlist) | **POST** /api/v1/video-playlists/{playlistId}/videos/reorder | Reorder a playlist
*VideoRatesApi* | [**api_v1_users_me_videos_video_id_rating_get**](docs/VideoRatesApi.md#api_v1_users_me_videos_video_id_rating_get) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
*VideoRatesApi* | [**api_v1_videos_id_rate_put**](docs/VideoRatesApi.md#api_v1_videos_id_rate_put) | **PUT** /api/v1/videos/{id}/rate | Like/dislike a video
*VideoStatsApi* | [**api_v1_videos_id_stats_overall_get**](docs/VideoStatsApi.md#api_v1_videos_id_stats_overall_get) | **GET** /api/v1/videos/{id}/stats/overall | Get overall stats of a video
*VideoStatsApi* | [**api_v1_videos_id_stats_retention_get**](docs/VideoStatsApi.md#api_v1_videos_id_stats_retention_get) | **GET** /api/v1/videos/{id}/stats/retention | Get retention stats of a video
*VideoStatsApi* | [**api_v1_videos_id_stats_timeseries_metric_get**](docs/VideoStatsApi.md#api_v1_videos_id_stats_timeseries_metric_get) | **GET** /api/v1/videos/{id}/stats/timeseries/{metric} | Get timeserie stats of a video
*VideoTranscodingApi* | [**api_v1_videos_id_studio_edit_post**](docs/VideoTranscodingApi.md#api_v1_videos_id_studio_edit_post) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
*VideoTranscodingApi* | [**create_video_transcoding**](docs/VideoTranscodingApi.md#create_video_transcoding) | **POST** /api/v1/videos/{id}/transcoding | Create a transcoding job
*VideoUploadApi* | [**import_video**](docs/VideoUploadApi.md#import_video) | **POST** /api/v1/videos/imports | Import a video
*VideoUploadApi* | [**upload_legacy**](docs/VideoUploadApi.md#upload_legacy) | **POST** /api/v1/videos/upload | Upload a video
*VideoUploadApi* | [**upload_resumable**](docs/VideoUploadApi.md#upload_resumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
*VideoUploadApi* | [**upload_resumable_cancel**](docs/VideoUploadApi.md#upload_resumable_cancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
*VideoUploadApi* | [**upload_resumable_init**](docs/VideoUploadApi.md#upload_resumable_init) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video
*VideosApi* | [**add_video_playlist_video**](docs/VideosApi.md#add_video_playlist_video) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
*VideosApi* | [**api_v1_users_me_subscriptions_videos_get**](docs/VideosApi.md#api_v1_users_me_subscriptions_videos_get) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
*VideosApi* | [**api_v1_users_me_videos_get**](docs/VideosApi.md#api_v1_users_me_videos_get) | **GET** /api/v1/users/me/videos | Get videos of my user
*VideosApi* | [**api_v1_users_me_videos_imports_get**](docs/VideosApi.md#api_v1_users_me_videos_imports_get) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
*VideosApi* | [**get_video_playlist_videos**](docs/VideosApi.md#get_video_playlist_videos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist


## Documentation For Models

 - [Abuse](docs/Abuse.md)
 - [AbuseMessage](docs/AbuseMessage.md)
 - [AbuseStateConstant](docs/AbuseStateConstant.md)
 - [AbuseStateSet](docs/AbuseStateSet.md)
 - [Account](docs/Account.md)
 - [AccountSummary](docs/AccountSummary.md)
 - [Actor](docs/Actor.md)
 - [ActorImage](docs/ActorImage.md)
 - [ActorInfo](docs/ActorInfo.md)
 - [AddPlaylist200Response](docs/AddPlaylist200Response.md)
 - [AddPlaylist200ResponseVideoPlaylist](docs/AddPlaylist200ResponseVideoPlaylist.md)
 - [AddPluginRequest](docs/AddPluginRequest.md)
 - [AddPluginRequestOneOf](docs/AddPluginRequestOneOf.md)
 - [AddPluginRequestOneOf1](docs/AddPluginRequestOneOf1.md)
 - [AddUser](docs/AddUser.md)
 - [AddUserResponse](docs/AddUserResponse.md)
 - [AddUserResponseUser](docs/AddUserResponseUser.md)
 - [AddVideoChannel200Response](docs/AddVideoChannel200Response.md)
 - [AddVideoChannelSync200Response](docs/AddVideoChannelSync200Response.md)
 - [AddVideoPlaylistVideo200Response](docs/AddVideoPlaylistVideo200Response.md)
 - [AddVideoPlaylistVideo200ResponseVideoPlaylistElement](docs/AddVideoPlaylistVideo200ResponseVideoPlaylistElement.md)
 - [AddVideoPlaylistVideoRequest](docs/AddVideoPlaylistVideoRequest.md)
 - [AddVideoPlaylistVideoRequestVideoId](docs/AddVideoPlaylistVideoRequestVideoId.md)
 - [ApiV1AbusesAbuseIdMessagesGet200Response](docs/ApiV1AbusesAbuseIdMessagesGet200Response.md)
 - [ApiV1AbusesAbuseIdMessagesPostRequest](docs/ApiV1AbusesAbuseIdMessagesPostRequest.md)
 - [ApiV1AbusesAbuseIdPutRequest](docs/ApiV1AbusesAbuseIdPutRequest.md)
 - [ApiV1AbusesPost200Response](docs/ApiV1AbusesPost200Response.md)
 - [ApiV1AbusesPost200ResponseAbuse](docs/ApiV1AbusesPost200ResponseAbuse.md)
 - [ApiV1AbusesPostRequest](docs/ApiV1AbusesPostRequest.md)
 - [ApiV1AbusesPostRequestAccount](docs/ApiV1AbusesPostRequestAccount.md)
 - [ApiV1AbusesPostRequestComment](docs/ApiV1AbusesPostRequestComment.md)
 - [ApiV1AbusesPostRequestVideo](docs/ApiV1AbusesPostRequestVideo.md)
 - [ApiV1CustomPagesHomepageInstancePutRequest](docs/ApiV1CustomPagesHomepageInstancePutRequest.md)
 - [ApiV1PluginsNpmNameSettingsPutRequest](docs/ApiV1PluginsNpmNameSettingsPutRequest.md)
 - [ApiV1RunnersGet200Response](docs/ApiV1RunnersGet200Response.md)
 - [ApiV1RunnersJobsGet200Response](docs/ApiV1RunnersJobsGet200Response.md)
 - [ApiV1RunnersJobsJobUUIDAbortPostRequest](docs/ApiV1RunnersJobsJobUUIDAbortPostRequest.md)
 - [ApiV1RunnersJobsJobUUIDAcceptPost200Response](docs/ApiV1RunnersJobsJobUUIDAcceptPost200Response.md)
 - [ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob](docs/ApiV1RunnersJobsJobUUIDAcceptPost200ResponseJob.md)
 - [ApiV1RunnersJobsJobUUIDErrorPostRequest](docs/ApiV1RunnersJobsJobUUIDErrorPostRequest.md)
 - [ApiV1RunnersJobsJobUUIDSuccessPostRequest](docs/ApiV1RunnersJobsJobUUIDSuccessPostRequest.md)
 - [ApiV1RunnersJobsJobUUIDSuccessPostRequestPayload](docs/ApiV1RunnersJobsJobUUIDSuccessPostRequestPayload.md)
 - [ApiV1RunnersJobsJobUUIDUpdatePostRequest](docs/ApiV1RunnersJobsJobUUIDUpdatePostRequest.md)
 - [ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload](docs/ApiV1RunnersJobsJobUUIDUpdatePostRequestPayload.md)
 - [ApiV1RunnersJobsRequestPost200Response](docs/ApiV1RunnersJobsRequestPost200Response.md)
 - [ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner](docs/ApiV1RunnersJobsRequestPost200ResponseAvailableJobsInner.md)
 - [ApiV1RunnersRegisterPost200Response](docs/ApiV1RunnersRegisterPost200Response.md)
 - [ApiV1RunnersRegisterPostRequest](docs/ApiV1RunnersRegisterPostRequest.md)
 - [ApiV1RunnersRegistrationTokensGet200Response](docs/ApiV1RunnersRegistrationTokensGet200Response.md)
 - [ApiV1RunnersUnregisterPostRequest](docs/ApiV1RunnersUnregisterPostRequest.md)
 - [ApiV1ServerBlocklistAccountsPostRequest](docs/ApiV1ServerBlocklistAccountsPostRequest.md)
 - [ApiV1ServerBlocklistServersPostRequest](docs/ApiV1ServerBlocklistServersPostRequest.md)
 - [ApiV1ServerFollowingPostRequest](docs/ApiV1ServerFollowingPostRequest.md)
 - [ApiV1ServerRedundancyHostPutRequest](docs/ApiV1ServerRedundancyHostPutRequest.md)
 - [ApiV1UsersMeAvatarPickPost200Response](docs/ApiV1UsersMeAvatarPickPost200Response.md)
 - [ApiV1UsersMeNotificationSettingsPutRequest](docs/ApiV1UsersMeNotificationSettingsPutRequest.md)
 - [ApiV1UsersMeNotificationsReadPostRequest](docs/ApiV1UsersMeNotificationsReadPostRequest.md)
 - [ApiV1UsersMeSubscriptionsPostRequest](docs/ApiV1UsersMeSubscriptionsPostRequest.md)
 - [ApiV1UsersMeVideoPlaylistsVideosExistGet200Response](docs/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response.md)
 - [ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner](docs/ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner.md)
 - [ApiV1UsersMeVideoQuotaUsedGet200Response](docs/ApiV1UsersMeVideoQuotaUsedGet200Response.md)
 - [ApiV1VideoChannelsChannelHandleBannerPickPost200Response](docs/ApiV1VideoChannelsChannelHandleBannerPickPost200Response.md)
 - [ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response](docs/ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response.md)
 - [ApiV1VideosIdCommentThreadsPostRequest](docs/ApiV1VideosIdCommentThreadsPostRequest.md)
 - [ApiV1VideosIdRatePutRequest](docs/ApiV1VideosIdRatePutRequest.md)
 - [ApiV1VideosLiveIdSessionsGet200Response](docs/ApiV1VideosLiveIdSessionsGet200Response.md)
 - [ApiV1VideosOwnershipIdAcceptPostIdParameter](docs/ApiV1VideosOwnershipIdAcceptPostIdParameter.md)
 - [BlockStatus](docs/BlockStatus.md)
 - [BlockStatusAccountsValue](docs/BlockStatusAccountsValue.md)
 - [BlockStatusHostsValue](docs/BlockStatusHostsValue.md)
 - [CommentThreadPostResponse](docs/CommentThreadPostResponse.md)
 - [CommentThreadResponse](docs/CommentThreadResponse.md)
 - [ConfirmTwoFactorRequestRequest](docs/ConfirmTwoFactorRequestRequest.md)
 - [CreateVideoTranscodingRequest](docs/CreateVideoTranscodingRequest.md)
 - [CustomHomepage](docs/CustomHomepage.md)
 - [FileRedundancyInformation](docs/FileRedundancyInformation.md)
 - [Follow](docs/Follow.md)
 - [GetAccountFollowers200Response](docs/GetAccountFollowers200Response.md)
 - [GetAccountVideosCategoryOneOfParameter](docs/GetAccountVideosCategoryOneOfParameter.md)
 - [GetAccountVideosLanguageOneOfParameter](docs/GetAccountVideosLanguageOneOfParameter.md)
 - [GetAccountVideosLicenceOneOfParameter](docs/GetAccountVideosLicenceOneOfParameter.md)
 - [GetAccountVideosTagsAllOfParameter](docs/GetAccountVideosTagsAllOfParameter.md)
 - [GetAccountVideosTagsOneOfParameter](docs/GetAccountVideosTagsOneOfParameter.md)
 - [GetAccounts200Response](docs/GetAccounts200Response.md)
 - [GetJobs200Response](docs/GetJobs200Response.md)
 - [GetMeVideoRating](docs/GetMeVideoRating.md)
 - [GetMyAbuses200Response](docs/GetMyAbuses200Response.md)
 - [GetOAuthToken200Response](docs/GetOAuthToken200Response.md)
 - [GetUser200Response](docs/GetUser200Response.md)
 - [GetUsers200Response](docs/GetUsers200Response.md)
 - [GetVideoBlocks200Response](docs/GetVideoBlocks200Response.md)
 - [GetVideoCaptions200Response](docs/GetVideoCaptions200Response.md)
 - [ImportVideosInChannelCreate](docs/ImportVideosInChannelCreate.md)
 - [Job](docs/Job.md)
 - [ListRegistrations200Response](docs/ListRegistrations200Response.md)
 - [LiveVideoLatencyMode](docs/LiveVideoLatencyMode.md)
 - [LiveVideoReplaySettings](docs/LiveVideoReplaySettings.md)
 - [LiveVideoResponse](docs/LiveVideoResponse.md)
 - [LiveVideoSessionResponse](docs/LiveVideoSessionResponse.md)
 - [LiveVideoSessionResponseReplayVideo](docs/LiveVideoSessionResponseReplayVideo.md)
 - [LiveVideoUpdate](docs/LiveVideoUpdate.md)
 - [MRSSGroupContent](docs/MRSSGroupContent.md)
 - [MRSSPeerLink](docs/MRSSPeerLink.md)
 - [NSFWPolicy](docs/NSFWPolicy.md)
 - [Notification](docs/Notification.md)
 - [NotificationActorFollow](docs/NotificationActorFollow.md)
 - [NotificationActorFollowFollowing](docs/NotificationActorFollowFollowing.md)
 - [NotificationComment](docs/NotificationComment.md)
 - [NotificationListResponse](docs/NotificationListResponse.md)
 - [NotificationVideo](docs/NotificationVideo.md)
 - [NotificationVideoAbuse](docs/NotificationVideoAbuse.md)
 - [NotificationVideoAbuseVideo](docs/NotificationVideoAbuseVideo.md)
 - [NotificationVideoImport](docs/NotificationVideoImport.md)
 - [OAuthClient](docs/OAuthClient.md)
 - [PlaybackMetricCreate](docs/PlaybackMetricCreate.md)
 - [PlaylistElement](docs/PlaylistElement.md)
 - [Plugin](docs/Plugin.md)
 - [PluginResponse](docs/PluginResponse.md)
 - [PutMirroredVideoRequest](docs/PutMirroredVideoRequest.md)
 - [PutVideoPlaylistVideoRequest](docs/PutVideoPlaylistVideoRequest.md)
 - [RegisterUser](docs/RegisterUser.md)
 - [RegisterUserChannel](docs/RegisterUserChannel.md)
 - [ReorderVideoPlaylistRequest](docs/ReorderVideoPlaylistRequest.md)
 - [RequestTwoFactorRequest](docs/RequestTwoFactorRequest.md)
 - [RequestTwoFactorResponse](docs/RequestTwoFactorResponse.md)
 - [RequestTwoFactorResponseOtpRequest](docs/RequestTwoFactorResponseOtpRequest.md)
 - [ResendEmailToVerifyRegistrationRequest](docs/ResendEmailToVerifyRegistrationRequest.md)
 - [ResendEmailToVerifyUserRequest](docs/ResendEmailToVerifyUserRequest.md)
 - [Runner](docs/Runner.md)
 - [RunnerJob](docs/RunnerJob.md)
 - [RunnerJobAdmin](docs/RunnerJobAdmin.md)
 - [RunnerJobParent](docs/RunnerJobParent.md)
 - [RunnerJobPayload](docs/RunnerJobPayload.md)
 - [RunnerJobRunner](docs/RunnerJobRunner.md)
 - [RunnerJobState](docs/RunnerJobState.md)
 - [RunnerJobStateConstant](docs/RunnerJobStateConstant.md)
 - [RunnerJobType](docs/RunnerJobType.md)
 - [RunnerRegistrationToken](docs/RunnerRegistrationToken.md)
 - [SendClientLog](docs/SendClientLog.md)
 - [ServerConfig](docs/ServerConfig.md)
 - [ServerConfigAbout](docs/ServerConfigAbout.md)
 - [ServerConfigAboutInstance](docs/ServerConfigAboutInstance.md)
 - [ServerConfigAutoBlacklist](docs/ServerConfigAutoBlacklist.md)
 - [ServerConfigAutoBlacklistVideos](docs/ServerConfigAutoBlacklistVideos.md)
 - [ServerConfigAvatar](docs/ServerConfigAvatar.md)
 - [ServerConfigAvatarFile](docs/ServerConfigAvatarFile.md)
 - [ServerConfigAvatarFileSize](docs/ServerConfigAvatarFileSize.md)
 - [ServerConfigCustom](docs/ServerConfigCustom.md)
 - [ServerConfigCustomAdmin](docs/ServerConfigCustomAdmin.md)
 - [ServerConfigCustomCache](docs/ServerConfigCustomCache.md)
 - [ServerConfigCustomCachePreviews](docs/ServerConfigCustomCachePreviews.md)
 - [ServerConfigCustomFollowers](docs/ServerConfigCustomFollowers.md)
 - [ServerConfigCustomFollowersInstance](docs/ServerConfigCustomFollowersInstance.md)
 - [ServerConfigCustomImport](docs/ServerConfigCustomImport.md)
 - [ServerConfigCustomInstance](docs/ServerConfigCustomInstance.md)
 - [ServerConfigCustomServices](docs/ServerConfigCustomServices.md)
 - [ServerConfigCustomServicesTwitter](docs/ServerConfigCustomServicesTwitter.md)
 - [ServerConfigCustomSignup](docs/ServerConfigCustomSignup.md)
 - [ServerConfigCustomTheme](docs/ServerConfigCustomTheme.md)
 - [ServerConfigCustomTranscoding](docs/ServerConfigCustomTranscoding.md)
 - [ServerConfigCustomTranscodingHls](docs/ServerConfigCustomTranscodingHls.md)
 - [ServerConfigCustomTranscodingResolutions](docs/ServerConfigCustomTranscodingResolutions.md)
 - [ServerConfigCustomTranscodingWebtorrent](docs/ServerConfigCustomTranscodingWebtorrent.md)
 - [ServerConfigCustomUser](docs/ServerConfigCustomUser.md)
 - [ServerConfigEmail](docs/ServerConfigEmail.md)
 - [ServerConfigFollowings](docs/ServerConfigFollowings.md)
 - [ServerConfigFollowingsInstance](docs/ServerConfigFollowingsInstance.md)
 - [ServerConfigFollowingsInstanceAutoFollowIndex](docs/ServerConfigFollowingsInstanceAutoFollowIndex.md)
 - [ServerConfigImport](docs/ServerConfigImport.md)
 - [ServerConfigImportVideos](docs/ServerConfigImportVideos.md)
 - [ServerConfigInstance](docs/ServerConfigInstance.md)
 - [ServerConfigInstanceCustomizations](docs/ServerConfigInstanceCustomizations.md)
 - [ServerConfigPlugin](docs/ServerConfigPlugin.md)
 - [ServerConfigSearch](docs/ServerConfigSearch.md)
 - [ServerConfigSearchRemoteUri](docs/ServerConfigSearchRemoteUri.md)
 - [ServerConfigSignup](docs/ServerConfigSignup.md)
 - [ServerConfigTranscoding](docs/ServerConfigTranscoding.md)
 - [ServerConfigTrending](docs/ServerConfigTrending.md)
 - [ServerConfigTrendingVideos](docs/ServerConfigTrendingVideos.md)
 - [ServerConfigUser](docs/ServerConfigUser.md)
 - [ServerConfigVideo](docs/ServerConfigVideo.md)
 - [ServerConfigVideoCaption](docs/ServerConfigVideoCaption.md)
 - [ServerConfigVideoCaptionFile](docs/ServerConfigVideoCaptionFile.md)
 - [ServerConfigVideoFile](docs/ServerConfigVideoFile.md)
 - [ServerConfigVideoImage](docs/ServerConfigVideoImage.md)
 - [ServerStats](docs/ServerStats.md)
 - [ServerStatsVideosRedundancyInner](docs/ServerStatsVideosRedundancyInner.md)
 - [UninstallPluginRequest](docs/UninstallPluginRequest.md)
 - [UpdateMe](docs/UpdateMe.md)
 - [UpdateUser](docs/UpdateUser.md)
 - [User](docs/User.md)
 - [UserAdminFlags](docs/UserAdminFlags.md)
 - [UserRegistration](docs/UserRegistration.md)
 - [UserRegistrationAcceptOrReject](docs/UserRegistrationAcceptOrReject.md)
 - [UserRegistrationRequest](docs/UserRegistrationRequest.md)
 - [UserRegistrationState](docs/UserRegistrationState.md)
 - [UserRegistrationUser](docs/UserRegistrationUser.md)
 - [UserRole](docs/UserRole.md)
 - [UserViewingVideo](docs/UserViewingVideo.md)
 - [UserWithStats](docs/UserWithStats.md)
 - [VODAudioMergeTranscoding](docs/VODAudioMergeTranscoding.md)
 - [VODAudioMergeTranscoding1](docs/VODAudioMergeTranscoding1.md)
 - [VODAudioMergeTranscoding1Input](docs/VODAudioMergeTranscoding1Input.md)
 - [VODHLSTranscoding](docs/VODHLSTranscoding.md)
 - [VODHLSTranscoding1](docs/VODHLSTranscoding1.md)
 - [VODWebVideoTranscoding](docs/VODWebVideoTranscoding.md)
 - [VODWebVideoTranscoding1](docs/VODWebVideoTranscoding1.md)
 - [VODWebVideoTranscoding1Input](docs/VODWebVideoTranscoding1Input.md)
 - [VODWebVideoTranscoding1Output](docs/VODWebVideoTranscoding1Output.md)
 - [VerifyRegistrationEmailRequest](docs/VerifyRegistrationEmailRequest.md)
 - [VerifyUserRequest](docs/VerifyUserRequest.md)
 - [Video](docs/Video.md)
 - [VideoBlacklist](docs/VideoBlacklist.md)
 - [VideoCaption](docs/VideoCaption.md)
 - [VideoCategory](docs/VideoCategory.md)
 - [VideoChannel](docs/VideoChannel.md)
 - [VideoChannelAllOfOwnerAccount](docs/VideoChannelAllOfOwnerAccount.md)
 - [VideoChannelCreate](docs/VideoChannelCreate.md)
 - [VideoChannelEdit](docs/VideoChannelEdit.md)
 - [VideoChannelList](docs/VideoChannelList.md)
 - [VideoChannelListDataInner](docs/VideoChannelListDataInner.md)
 - [VideoChannelSummary](docs/VideoChannelSummary.md)
 - [VideoChannelSync](docs/VideoChannelSync.md)
 - [VideoChannelSyncCreate](docs/VideoChannelSyncCreate.md)
 - [VideoChannelSyncList](docs/VideoChannelSyncList.md)
 - [VideoChannelSyncListDataInner](docs/VideoChannelSyncListDataInner.md)
 - [VideoChannelSyncState](docs/VideoChannelSyncState.md)
 - [VideoChannelUpdate](docs/VideoChannelUpdate.md)
 - [VideoComment](docs/VideoComment.md)
 - [VideoCommentThreadTree](docs/VideoCommentThreadTree.md)
 - [VideoCommentsForXMLInner](docs/VideoCommentsForXMLInner.md)
 - [VideoConstantNumberCategory](docs/VideoConstantNumberCategory.md)
 - [VideoConstantNumberLicence](docs/VideoConstantNumberLicence.md)
 - [VideoConstantStringLanguage](docs/VideoConstantStringLanguage.md)
 - [VideoDetails](docs/VideoDetails.md)
 - [VideoFile](docs/VideoFile.md)
 - [VideoImport](docs/VideoImport.md)
 - [VideoImportStateConstant](docs/VideoImportStateConstant.md)
 - [VideoImportsList](docs/VideoImportsList.md)
 - [VideoInfo](docs/VideoInfo.md)
 - [VideoLanguage](docs/VideoLanguage.md)
 - [VideoLicence](docs/VideoLicence.md)
 - [VideoListResponse](docs/VideoListResponse.md)
 - [VideoPlaylist](docs/VideoPlaylist.md)
 - [VideoPlaylistPrivacyConstant](docs/VideoPlaylistPrivacyConstant.md)
 - [VideoPlaylistPrivacySet](docs/VideoPlaylistPrivacySet.md)
 - [VideoPlaylistTypeConstant](docs/VideoPlaylistTypeConstant.md)
 - [VideoPlaylistTypeSet](docs/VideoPlaylistTypeSet.md)
 - [VideoPrivacy](docs/VideoPrivacy.md)
 - [VideoPrivacyConstant](docs/VideoPrivacyConstant.md)
 - [VideoPrivacySet](docs/VideoPrivacySet.md)
 - [VideoRating](docs/VideoRating.md)
 - [VideoRedundancy](docs/VideoRedundancy.md)
 - [VideoRedundancyRedundancies](docs/VideoRedundancyRedundancies.md)
 - [VideoResolutionConstant](docs/VideoResolutionConstant.md)
 - [VideoScheduledUpdate](docs/VideoScheduledUpdate.md)
 - [VideoSource](docs/VideoSource.md)
 - [VideoState](docs/VideoState.md)
 - [VideoStateConstant](docs/VideoStateConstant.md)
 - [VideoStatsOverall](docs/VideoStatsOverall.md)
 - [VideoStatsOverallCountriesInner](docs/VideoStatsOverallCountriesInner.md)
 - [VideoStatsRetention](docs/VideoStatsRetention.md)
 - [VideoStatsRetentionDataInner](docs/VideoStatsRetentionDataInner.md)
 - [VideoStatsTimeserie](docs/VideoStatsTimeserie.md)
 - [VideoStatsTimeserieDataInner](docs/VideoStatsTimeserieDataInner.md)
 - [VideoStreamingPlaylists](docs/VideoStreamingPlaylists.md)
 - [VideoStreamingPlaylistsHLS](docs/VideoStreamingPlaylistsHLS.md)
 - [VideoStreamingPlaylistsHLSRedundanciesInner](docs/VideoStreamingPlaylistsHLSRedundanciesInner.md)
 - [VideoTokenResponse](docs/VideoTokenResponse.md)
 - [VideoTokenResponseFiles](docs/VideoTokenResponseFiles.md)
 - [VideoUploadRequestCommon](docs/VideoUploadRequestCommon.md)
 - [VideoUploadRequestResumable](docs/VideoUploadRequestResumable.md)
 - [VideoUploadResponse](docs/VideoUploadResponse.md)
 - [VideoUploadResponseVideo](docs/VideoUploadResponseVideo.md)
 - [VideoUserHistory](docs/VideoUserHistory.md)
 - [VideosForXMLInner](docs/VideosForXMLInner.md)
 - [VideosForXMLInnerEnclosure](docs/VideosForXMLInnerEnclosure.md)
 - [VideosForXMLInnerMediaCommunity](docs/VideosForXMLInnerMediaCommunity.md)
 - [VideosForXMLInnerMediaCommunityMediaStatistics](docs/VideosForXMLInnerMediaCommunityMediaStatistics.md)
 - [VideosForXMLInnerMediaEmbed](docs/VideosForXMLInnerMediaEmbed.md)
 - [VideosForXMLInnerMediaGroupInner](docs/VideosForXMLInnerMediaGroupInner.md)
 - [VideosForXMLInnerMediaPlayer](docs/VideosForXMLInnerMediaPlayer.md)
 - [VideosForXMLInnerMediaThumbnail](docs/VideosForXMLInnerMediaThumbnail.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="OAuth2"></a>
### OAuth2

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - **admin**: Admin scope
 - **moderator**: Moderator scope
 - **user**: User scope


## Author




