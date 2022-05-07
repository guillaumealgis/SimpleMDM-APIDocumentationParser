// SimpleMDM API Version 1.39

# Account / Show

```http
GET https://a.simplemdm.com/api/v1/account
```

```json
{
  "data": {
    "attributes": {
      "apple_store_country_code": "US",
      "name": "SimpleMDM",
      "subscription": {
        "licenses": {
          "available": 123,
          "total": 500
        }
      }
    },
    "type": "account"
  }
}
```

# Account / Update

```http
PATCH https://a.simplemdm.com/api/v1/account
```

| Argument                   | Description                                                |
|----------------------------|------------------------------------------------------------|
| `name`                     | The name of the account.                                   |
| `apple_store_country_code` | The app store country that SimpleMDM uses for the account. |


```json
{
  "data": {
    "attributes": {
      "apple_store_country_code": "AU",
      "name": "SimpleMDM"
    },
    "type": "account"
  }
}
```

# Apps / List all

```http
GET https://a.simplemdm.com/api/v1/apps
```

```json
{
  "data": [
    {
      "attributes": {
        "app_type": "app store",
        "bundle_identifier": "com.simonfilip.AfterGlow",
        "itunes_store_id": 573116090,
        "name": "Afterlight"
      },
      "id": 34,
      "type": "app"
    },
    {
      "attributes": {
        "app_type": "enterprise",
        "bundle_identifier": "com.portlandsurfclub.ent.surfreport2.2",
        "name": "Surf Report",
        "version": "2.2"
      },
      "id": 63,
      "type": "app"
    },
    {
      "attributes": {
        "app_type": "custom b2b",
        "itunes_store_id": 44827291,
        "name": "Scanner Pro"
      },
      "id": 67,
      "type": "app"
    }
  ],
  "has_more": false
}
```

# Apps / Retrieve one

```http
GET https://a.simplemdm.com/api/v1/apps/{APP_ID}
```

```json
{
  "data": {
    "attributes": {
      "app_type": "app store",
      "bundle_identifier": "com.simonfilip.AfterGlow",
      "itunes_store_id": 573116090,
      "name": "Afterlight"
    },
    "id": 34,
    "type": "app"
  }
}
```

# Apps / Create

```http
POST https://a.simplemdm.com/api/v1/apps
```

| Argument       | Description                                                                                                                                           |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app_store_id` | The Apple App Store ID of the app to be added. Example: 1090161858.                                                                                   |
| `bundle_id`    | The bundle identifier of the Apple App Store app to be added. Example: com.myCompany.MyApp1                                                           |
| `binary`       | The binary file with an ipa or pkg extension. File should be provided as multipart/form-data.                                                         |
| `name`         | The name that SimpleMDM will use to reference this app. If left blank, SimpleMDM will automatically set this to the app name specified by the binary. |


```json
{
  "data": {
    "attributes": {
      "app_type": "enterprise",
      "bundle_identifier": "com.portlandsurfclub.ent.surfreport2.2",
      "name": "Surf Report",
      "version": "2.2"
    },
    "id": 63,
    "type": "app"
  }
}
```

# Apps / Update

```http
PATCH https://a.simplemdm.com/api/v1/apps/{APP_ID}
```

| Argument    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `binary`    | The binary file with an ipa or pkg extension. File should be provided as multipart/form-data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `name`      | The name that SimpleMDM will use to reference this app. If left blank, SimpleMDM will automatically set this to the app name specified by the binary.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `deploy_to` | Deploy the app to associated devices immediately after the app has been uploaded and processed. Possible values are none, outdated or all. When set to outdated, and a newer version of an app has been uploaded, SimpleMDM will deploy the app to all associated devices with an outdated version of the app installed. When set to all, SimpleMDM will deploy to all associated devices regardless of the version of the app currently installed. If set to none then the app will not be immediately deployed to any devices as a result of this API call. Defaults to none |


```json
{
  "data": {
    "attributes": {
      "app_type": "enterprise",
      "bundle_identifier": "com.portlandsurfclub.ent.surfreport2.3",
      "name": "Surf Report (Updated)",
      "version": "2.3"
    },
    "id": 63,
    "type": "app"
  }
}
```

# Apps / Delete

```http
DELETE https://a.simplemdm.com/api/v1/apps/{APP_ID}
```

```http
HTTP/1.1 204 No Content
```

# Apps / List installs

```http
GET https://a.simplemdm.com/api/v1/apps/{APP_ID}/installs
```

```json
{
  "data": [
    {
      "attributes": {
        "bundle_size": 56163003,
        "discovered_at": "2021-11-08T09:02:07.000-08:00",
        "dynamic_size": null,
        "identifier": "com.junecloud.Deliveries",
        "last_seen_at": "2021-12-22T13:01:58.000-08:00",
        "managed": false,
        "name": "Deliveries",
        "short_version": "9.2.1",
        "version": "9.2.1"
      },
      "id": 26409,
      "relationships": {
        "device": {
          "data": {
            "id": 7,
            "type": "device"
          }
        }
      },
      "type": "installed_app"
    },
    {
      "attributes": {
        "bundle_size": 21204992,
        "discovered_at": "2021-12-16T14:25:54.000-08:00",
        "dynamic_size": 139264,
        "identifier": "com.junecloud.Deliveries",
        "last_seen_at": "2021-12-22T13:00:57.000-08:00",
        "managed": true,
        "name": "Deliveries",
        "short_version": "9.2.1",
        "version": "1311"
      },
      "id": 34943,
      "relationships": {
        "device": {
          "data": {
            "id": 3,
            "type": "device"
          }
        }
      },
      "type": "installed_app"
    }
  ],
  "has_more": false
}
```

# Assignment Groups / List all

```http
GET https://a.simplemdm.com/api/v1/assignment_groups
```

```json
{
  "data": [
    {
      "attributes": {
        "auto_deploy": true,
        "name": "SimpleMDM"
      },
      "id": 26,
      "relationships": {
        "apps": {
          "data": [
            {
              "id": 49,
              "type": "app"
            }
          ]
        },
        "device_groups": {
          "data": [
            {
              "id": 37,
              "type": "device_group"
            }
          ]
        },
        "devices": {
          "data": [
            {
              "id": 56,
              "type": "device"
            }
          ]
        }
      },
      "type": "assignment_group"
    },
    {
      "attributes": {
        "auto_deploy": false,
        "name": "Productivity Apps"
      },
      "id": 38,
      "relationships": {
        "apps": {
          "data": [
            {
              "id": 63,
              "type": "app"
            },
            {
              "id": 67,
              "type": "app"
            }
          ]
        },
        "device_groups": {
          "data": [
            {
              "id": 37,
              "type": "device_group"
            },
            {
              "id": 38,
              "type": "device_group"
            }
          ]
        },
        "devices": {
          "data": [
            {
              "id": 54,
              "type": "device"
            }
          ]
        }
      },
      "type": "assignment_group"
    },
    ...
  ],
  "has_more": false
}
```

# Assignment Groups / Retrieve one

```http
GET https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}
```

```json
{
  "data": {
    "attributes": {
      "auto_deploy": true,
      "name": "SimpleMDM"
    },
    "id": 26,
    "relationships": {
      "apps": {
        "data": [
          {
            "id": 49,
            "type": "app"
          },
          {
            "id": 67,
            "type": "app"
          }
        ]
      },
      "device_groups": {
        "data": [
          {
            "id": 37,
            "type": "device_group"
          },
          {
            "id": 38,
            "type": "device_group"
          }
        ]
      },
      "devices": {
        "data": [
          {
            "id": 54,
            "type": "device"
          }
        ]
      }
    },
    "type": "assignment_group"
  }
}
```

# Assignment Groups / Create

```http
POST https://a.simplemdm.com/api/v1/assignment_groups
```

| Argument      | Description                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | The name of the assignment group.                                                                                                       |
| `auto_deploy` | Optional. Whether the apps should be automatically pushed to devices when they join any of the related device groups. Defaults to true. |


```json
{
  "data": {
    "attributes": {
      "auto_deploy": true,
      "name": "Communication Apps"
    },
    "id": 43,
    "relationships": {
      "apps": {
        "data": []
      },
      "device_groups": {
        "data": []
      },
      "devices": {
        "data": []
      }
    },
    "type": "assignment_group"
  }
}
```

# Assignment Groups / Update

```http
PATCH https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}
```

| Argument      | Description                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | The name of the assignment group.                                                                                                       |
| `auto_deploy` | Optional. Whether the apps should be automatically pushed to devices when they join any of the related device groups. Defaults to true. |


```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Delete

```http
DELETE https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}
```

```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Assign app

```http
POST https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/apps/{APP_ID}
```

```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Unassign app

```http
DELETE https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/apps/{APP_ID}
```

```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Assign device group

```http
POST https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/device_groups/{DEVICE_GROUP_ID}
```

```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Unassign device group

```http
DELETE https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/device_groups/{DEVICE_GROUP_ID}
```

```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Assign device

```http
POST https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/devices/{DEVICE_ID}
```

```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Unassign device

```http
DELETE https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/devices/{DEVICE_ID}
```

```http
HTTP/1.1 204 No Content
```

# Assignment Groups / Push apps

```http
POST https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/push_apps
```

```http
HTTP/1.1 202 Accepted
```

# Assignment Groups / Update apps

```http
POST https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}/update_apps
```

```http
HTTP/1.1 202 Accepted
```

# Custom Attributes / List all

```http
GET https://a.simplemdm.com/api/v1/custom_attributes
```

```json
{
  "data": [
    {
      "attributes": {
        "default_value": "user@example.org",
        "name": "email_address"
      },
      "id": "email_address",
      "type": "custom_attribute"
    },
    {
      "attributes": {
        "default_value": "not provided",
        "name": "full_name"
      },
      "id": "full_name",
      "type": "custom_attribute"
    }
  ],
  "has_more": false
}
```

# Custom Attributes / Retrieve one

```http
GET https://a.simplemdm.com/api/v1/custom_attributes/{CUSTOM_ATTRIBUTE_ID}
```

```json
{
  "data": {
    "attributes": {
      "default_value": "user@example.org",
      "name": "email_address"
    },
    "id": "email_address",
    "type": "custom_attribute"
  }
}
```

# Custom Attributes / Create

```http
POST https://a.simplemdm.com/api/v1/custom_attributes
```

| Argument        | Description                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`          | Required. The name of the custom attribute. This name will be used when referencing the custom attribute throughout the app. Alphanumeric characters and underscores only. Case insensitive. |
| `default_value` | Optional. The value that will be used if a value is not provided elsewhere.                                                                                                                  |


# Custom Attributes / Update

```http
PATCH https://a.simplemdm.com/api/v1/custom_attributes/{CUSTOM_ATTRIBUTE_ID}
```

| Argument        | Description                                                       |
|-----------------|-------------------------------------------------------------------|
| `default_value` | The value that will be used if a value is not provided elsewhere. |


# Custom Attributes / Delete

```http
DELETE https://a.simplemdm.com/api/v1/custom_attributes/{CUSTOM_ATTRIBUTE_ID}
```

# Custom Attributes / Get values for device

```http
GET https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/custom_attribute_values
```

```json
{
  "data": [
    {
      "attributes": {
        "value": "hello"
      },
      "id": "my_first_custom_attribute",
      "type": "custom_attribute_value"
    },
    {
      "attributes": {
        "value": ""
      },
      "id": "my_other_custom_attribute",
      "type": "custom_attribute_value"
    }
  ]
}
```

# Custom Attributes / Set value for device

```http
PUT https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/custom_attribute_values/{CUSTOM_ATTRIBUTE_NAME}
```

| Argument | Description                                                                      |
|---------|----------------------------------------------------------------------------------|
| `value` | Required. The value to be assigned for the provided device and custom attribute. |


```json
{
  "data": {
    "attributes": {
      "value": "test"
    },
    "id": "my_other_custom_attribute",
    "type": "custom_attribute_value"
  }
}
```

# Custom Attributes / Get values for group

```http
GET https://a.simplemdm.com/api/v1/device_groups/{DEVICE_GROUP_ID}/custom_attribute_values
```

```json
{
  "data": [
    {
      "attributes": {
        "value": "hello"
      },
      "id": "my_first_custom_attribute",
      "type": "custom_attribute_value"
    },
    {
      "attributes": {
        "value": ""
      },
      "id": "my_other_custom_attribute",
      "type": "custom_attribute_value"
    }
  ]
}
```

# Custom Attributes / Set value for group

```http
PUT https://a.simplemdm.com/api/v1/device_groups/{DEVICE_GROUP_ID}/custom_attribute_values/{CUSTOM_ATTRIBUTE_NAME}
```

| Argument | Description                                                                     |
|---------|---------------------------------------------------------------------------------|
| `value` | Required. The value to be assigned for the provided group and custom attribute. |


```json
{
  "data": {
    "attributes": {
      "value": "test"
    },
    "id": "my_other_custom_attribute",
    "type": "custom_attribute_value"
  }
}
```

# Custom Configuration Profiles / List all

```http
GET https://a.simplemdm.com/api/v1/custom_configuration_profiles
```

```json
{
  "data": [
    {
      "attributes": {
        "attribute_support": false,
        "name": "Munki Configuration",
        "profile_identifier": "com.unwiredmdm.aabc717175a3467b93af177aa5f1992d",
        "user_scope": true
      },
      "id": 293814,
      "relationships": {
        "device_groups": {
          "data": [
            {
              "id": 732444,
              "type": "device group"
            }
          ]
        }
      },
      "type": "custom_configuration_profile"
    }
  ],
  "has_more": false
}
```

# Custom Configuration Profiles / Create

```http
POST https://a.simplemdm.com/api/v1/custom_configuration_profiles/
```

| Argument            | Description                                                                                                                            |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `name`              | Required. A name for the profile.                                                                                                      |
| `mobileconfig`      | Required. The mobileconfig file. Send as multipart/form-data.                                                                          |
| `user_scope`        | Optional. A boolean true or false. If false, deploy as a device profile instead of a user profile for macOS devices. Defaults to true. |
| `attribute_support` | Optional. A boolean true or false. When enabled, SimpleMDM will process variables in the uploaded profile. Defaults to false.          |


# Custom Configuration Profiles / Update

```http
PATCH https://a.simplemdm.com/api/v1/custom_configuration_profiles/{PROFILE_ID}
```

| Argument            | Description                                                                                                          |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| `name`              | Optional. Change the name of the profile.                                                                            |
| `mobileconfig`      | Optional. Update the mobileconfig file. Send as multipart/form-data.                                                 |
| `user_scope`        | Optional. A boolean true or false. If false, deploy as a device profile instead of a user profile for macOS devices. |
| `attribute_support` | Optional. A boolean true or false. When enabled, SimpleMDM will process variables in the uploaded profile.           |


# Custom Configuration Profiles / Download

```http
GET https://a.simplemdm.com/api/v1/custom_configuration_profiles/{PROFILE_ID}/download
```

# Custom Configuration Profiles / Delete

```http
DELETE https://a.simplemdm.com/api/v1/custom_configuration_profiles/{PROFILE_ID}
```

# Custom Configuration Profiles / Assign to device group

```http
POST https://a.simplemdm.com/api/v1/custom_configuration_profiles/{PROFILE_ID}/device_groups/{DEVICE_GROUP_ID}
```

# Custom Configuration Profiles / Unassign from device group

```http
DELETE https://a.simplemdm.com/api/v1/custom_configuration_profiles/{PROFILE_ID}/device_groups/{DEVICE_GROUP_ID}
```

# Custom Configuration Profiles / Assign to device

```http
POST https://a.simplemdm.com/api/v1/custom_configuration_profiles/{PROFILE_ID}/devices/{DEVICE_ID}
```

# Custom Configuration Profiles / Unassign from device

```http
DELETE https://a.simplemdm.com/api/v1/custom_configuration_profiles/{PROFILE_ID}/devices/{DEVICE_ID}
```

# DEP Servers / List all

```http
GET https://a.simplemdm.com/api/v1/dep_servers
```

```json
{
  "data": [
    {
      "attributes": {
        "last_synced_at": "2022-02-05T06:00:05.000-08:00",
        "organization_name": "SimpleMDM",
        "server_name": "My DEP MDM Server",
        "token_expires_at": "2023-02-03T10:57:07.000-08:00"
      },
      "id": 1,
      "type": "dep_server"
    },
    {
      "attributes": {
        "last_synced_at": "2022-02-05T06:00:05.000-08:00",
        "organization_name": "Acme Corp",
        "server_name": "Another MDM Server",
        "token_expires_at": "2023-02-03T10:57:07.000-08:00"
      },
      "id": 2,
      "type": "dep_server"
    }
  ],
  "has_more": false
}
```

# DEP Servers / Retrieve one

```http
GET https://a.simplemdm.com/api/v1/dep_servers/{DEP_SERVER_ID}
```

# DEP Servers / Sync with Apple

```http
POST https://a.simplemdm.com/api/v1/dep_servers/{DEP_SERVER_ID}/sync
```

# DEP Servers / List DEP devices

```http
GET https://a.simplemdm.com/api/v1/dep_servers/{DEP_SERVER_ID}/dep_devices
```

# DEP Servers / Retrieve one DEP device

```http
GET https://a.simplemdm.com/api/v1/dep_servers/{DEP_SERVER_ID}/dep_devices/{DEP_DEVICE_ID}
```

# Devices / List all

```http
GET https://a.simplemdm.com/api/v1/devices
```

| Argument                      | Description                                                                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `search`                      | Limit response to devices with matching name, UDID, serial number, IMEI, MAC address, or phone number.                                                                    |
| `include_awaiting_enrollment` | When true, returns all devices including those in the awaiting_enrollment state. When false, does not return devices in the awaiting_enrollment state. Defaults to false. |


```json
{
  "data": [
    {
      "attributes": {
        "available_device_capacity": 119.07,
        "battery_level": "100%",
        "bluetooth_mac": "f0:db:e2:df:e9:11",
        "build_version": "18G5042c",
        "carrier_settings_version": "46.0.1",
        "cellular_technology": 3,
        "current_carrier_network": "Verizon",
        "current_mcc": "310",
        "current_mnc": "00",
        "data_roaming_enabled": false,
        "device_capacity": 128.0,
        "device_name": "Mike's iPhone",
        "enrollment_channels": [
          "device"
        ],
        "ethernet_macs": [],
        "filevault_enabled": false,
        "filevault_recovery_key": null,
        "firewall": {
          "block_all_incoming": null,
          "enabled": null,
          "stealth_mode": null
        },
        "firmware_password": null,
        "firmware_password_enabled": false,
        "hardware_encryption_caps": 3,
        "iccid": "8914 8110 0002 8094 4264",
        "imei": "35 445506 652132 5",
        "is_activation_lock_enabled": false,
        "is_cloud_backup_enabled": false,
        "is_dep_enrollment": false,
        "is_device_locator_service_enabled": false,
        "is_do_not_disturb_in_effect": false,
        "is_roaming": false,
        "is_supervised": true,
        "is_user_approved_enrollment": null,
        "itunes_store_account_is_active": false,
        "last_cloud_backup_date": null,
        "last_seen_at": "2021-07-13T16:00:54.000-07:00",
        "last_seen_ip": "203.0.113.0",
        "location_accuracy": null,
        "location_latitude": null,
        "location_longitude": null,
        "location_updated_at": null,
        "meid": "35404596608032",
        "model": "NG4W2LL",
        "model_name": "iPhone 7",
        "modem_firmware_version": "8.80.00",
        "name": "Mike's iPhone",
        "os_update": {
          "automatic_app_installation_enabled": null,
          "automatic_check_enabled": null,
          "automatic_os_installation_enabled": null,
          "automatic_security_updates_enabled": null,
          "background_download_enabled": null,
          "catalog_url": null,
          "default_catalog": null,
          "perform_periodic_check": null,
          "previous_scan_date": null,
          "previous_scan_result": null
        },
        "os_version": "14.7",
        "passcode_compliant": true,
        "passcode_compliant_with_profiles": true,
        "passcode_present": false,
        "personal_hotspot_enabled": false,
        "phone_number": "+15555555555",
        "processor_architecture": null,
        "product_name": "iPhone9,1",
        "recovery_lock_password": null,
        "recovery_lock_password_enabled": false,
        "remote_desktop_enabled": false,
        "serial_number": "DNFJE9DNG5MG",
        "sim_carrier_network": null,
        "simmnc": null,
        "status": "enrolled",
        "subscriber_carrier_network": "Verizon",
        "subscriber_mcc": "311",
        "subscriber_mnc": "480",
        "system_integrity_protection_enabled": null,
        "unique_identifier": "4A08359C-1D3A-5D3E-939E-FFA6A561321D",
        "voice_roaming_enabled": true,
        "wifi_mac": "f0:db:e2:df:e9:2f"
      },
      "id": 121,
      "relationships": {
        "device_group": {
          "data": {
            "id": 1,
            "type": "device_group"
          }
        }
      },
      "type": "device"
    },
    ...
  ],
  "has_more": false
}
```

# Devices / Retrieve one

```http
GET https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}
```

```json
{
  "data": {
    "attributes": {
      "available_device_capacity": 119.07,
      "battery_level": "100%",
      "bluetooth_mac": "f0:db:e2:df:e9:11",
      "build_version": "18G5042c",
      "carrier_settings_version": "46.0.1",
      "cellular_technology": 3,
      "current_carrier_network": "Verizon",
      "current_mcc": "310",
      "current_mnc": "00",
      "data_roaming_enabled": false,
      "device_capacity": 128.0,
      "device_name": "Mike's iPhone",
      "enrollment_channels": [
        "device"
      ],
      "ethernet_macs": [],
      "filevault_enabled": false,
      "filevault_recovery_key": null,
      "firewall": {
        "block_all_incoming": null,
        "enabled": null,
        "stealth_mode": null
      },
      "firmware_password": null,
      "firmware_password_enabled": false,
      "hardware_encryption_caps": 3,
      "iccid": "8914 8110 0002 8094 4264",
      "imei": "35 445506 652132 5",
      "is_activation_lock_enabled": false,
      "is_cloud_backup_enabled": false,
      "is_dep_enrollment": false,
      "is_device_locator_service_enabled": false,
      "is_do_not_disturb_in_effect": false,
      "is_roaming": false,
      "is_supervised": true,
      "is_user_approved_enrollment": null,
      "itunes_store_account_is_active": false,
      "last_cloud_backup_date": null,
      "last_seen_at": "2021-07-13T16:00:54.000-07:00",
      "last_seen_ip": "203.0.113.0",
      "location_accuracy": null,
      "location_latitude": null,
      "location_longitude": null,
      "location_updated_at": null,
      "meid": "35404596608032",
      "model": "NG4W2LL",
      "model_name": "iPhone 7",
      "modem_firmware_version": "8.80.00",
      "name": "Mike's iPhone",
      "os_update": {
        "automatic_app_installation_enabled": null,
        "automatic_check_enabled": null,
        "automatic_os_installation_enabled": null,
        "automatic_security_updates_enabled": null,
        "background_download_enabled": null,
        "catalog_url": null,
        "default_catalog": null,
        "perform_periodic_check": null,
        "previous_scan_date": null,
        "previous_scan_result": null
      },
      "os_version": "14.7",
      "passcode_compliant": true,
      "passcode_compliant_with_profiles": true,
      "passcode_present": false,
      "personal_hotspot_enabled": false,
      "phone_number": "+15555555555",
      "processor_architecture": null,
      "product_name": "iPhone9,1",
      "recovery_lock_password": null,
      "recovery_lock_password_enabled": false,
      "remote_desktop_enabled": false,
      "serial_number": "DNFJE9DNG5MG",
      "sim_carrier_network": null,
      "simmnc": null,
      "status": "enrolled",
      "subscriber_carrier_network": "Verizon",
      "subscriber_mcc": "311",
      "subscriber_mnc": "480",
      "system_integrity_protection_enabled": null,
      "unique_identifier": "4A08359C-1D3A-5D3E-939E-FFA6A561321D",
      "voice_roaming_enabled": true,
      "wifi_mac": "f0:db:e2:df:e9:2f"
    },
    "id": 121,
    "relationships": {
      "device_group": {
        "data": {
          "id": 1,
          "type": "device_group"
        }
      }
    },
    "type": "device"
  }
}
```

# Devices / Create

```http
POST https://a.simplemdm.com/api/v1/devices
```

| Argument   | Description                                         |
|------------|-----------------------------------------------------|
| `name`     | The name the device will show within SimpleMDM.     |
| `group_id` | The device group to assign the device to initially. |


```json
{
  "data": {
    "attributes": {
      "available_device_capacity": null,
      "battery_level": null,
      "bluetooth_mac": null,
      "build_version": null,
      "carrier_settings_version": null,
      "cellular_technology": null,
      "current_carrier_network": null,
      "current_mcc": null,
      "current_mnc": null,
      "data_roaming_enabled": null,
      "device_capacity": null,
      "device_name": null,
      "enrollment_url": "https://a.simplemdm.com/e/?c=63154796",
      "hardware_encryption_caps": null,
      "iccid": null,
      "imei": null,
      "is_activation_lock_enabled": null,
      "is_cloud_backup_enabled": null,
      "is_device_locator_service_enabled": null,
      "is_do_not_disturb_in_effect": null,
      "is_roaming": null,
      "is_supervised": null,
      "itunes_store_account_is_active": null,
      "last_cloud_backup_date": null,
      "last_seen_at": null,
      "last_seen_ip": null,
      "location_accuracy": null,
      "location_latitude": null,
      "location_longitude": null,
      "location_updated_at": null,
      "meid": null,
      "model": null,
      "model_name": "Unknown",
      "modem_firmware_version": null,
      "name": "Sara's iPad",
      "os_version": null,
      "passcode_compliant": null,
      "passcode_compliant_with_profiles": null,
      "passcode_present": null,
      "personal_hotspot_enabled": null,
      "phone_number": null,
      "product_name": null,
      "serial_number": null,
      "sim_carrier_network": null,
      "simmnc": null,
      "status": "awaiting enrollment",
      "subscriber_carrier_network": null,
      "subscriber_mcc": null,
      "unique_identifier": null,
      "voice_roaming_enabled": null,
      "wifi_mac": null
    },
    "id": 980190963,
    "relationships": {
      "device_group": {
        "data": {
          "id": 41,
          "type": "device_group"
        }
      }
    },
    "type": "device"
  }
}
```

# Devices / Update

```http
PATCH https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}
```

| Argument      | Description                                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | The name of the device within SimpleMDM.                                                                                               |
| `device_name` | The name that appears on the device itself. Requires supervision. This operation is asynchronous and occurs when the device is online. |


```json
{
  "data": {
    "attributes": {
      "available_device_capacity": 15.19466781616211,
      "battery_level": "93%",
      "bluetooth_mac": "f0:db:e2:df:e9:11",
      "build_version": "13A452",
      "carrier_settings_version": "21.1",
      "cellular_technology": 3,
      "current_carrier_network": "Verizon",
      "current_mcc": "311",
      "current_mnc": "480",
      "data_roaming_enabled": false,
      "device_capacity": 55.62955093383789,
      "device_name": "iPhone",
      "hardware_encryption_caps": 3,
      "iccid": "8914 8110 0002 8094 4264",
      "imei": "35 445506 652132 5",
      "is_activation_lock_enabled": true,
      "is_cloud_backup_enabled": true,
      "is_device_locator_service_enabled": true,
      "is_do_not_disturb_in_effect": false,
      "is_roaming": false,
      "is_supervised": false,
      "itunes_store_account_is_active": true,
      "last_cloud_backup_date": "2015-10-01T15:09:12.000-07:00",
      "last_seen_at": "2015-10-01T18:38:47.277-07:00",
      "last_seen_ip": "203.0.113.0",
      "location_accuracy": "60",
      "location_latitude": "75.13421212355",
      "location_longitude": "-14.313565422",
      "location_updated_at": "2015-10-01T15:09:12.000-07:00",
      "meid": "35404596608032",
      "model": "NG4W2LL",
      "model_name": "iPhone 6",
      "modem_firmware_version": "4.02.00",
      "name": "Ashley's iPad",
      "os_version": "9.3.2",
      "passcode_compliant": true,
      "passcode_compliant_with_profiles": true,
      "passcode_present": true,
      "personal_hotspot_enabled": true,
      "phone_number": "5035551234",
      "product_name": "iPhone7,2",
      "serial_number": "DNFJE9DNG5MG",
      "sim_carrier_network": "Verizon",
      "simmcc": "311",
      "simmnc": "480",
      "status": "enrolled",
      "subscriber_carrier_network": "Verizon",
      "subscriber_mcc": "311",
      "subscriber_mnc": "480",
      "voice_roaming_enabled": true,
      "wifi_mac": "f0:db:e2:df:e9:2f"
    },
    "id": 121,
    "relationships": {
      "device_group": {
        "data": {
          "id": 37,
          "type": "device_group"
        }
      }
    },
    "type": "device"
  }
}
```

# Devices / Delete

```http
DELETE https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}
```

```http
HTTP/1.1 204
```

# Devices / List profiles

```http
GET https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/profiles
```

```json
{
  "data": [
    {
      "attributes": {
        "attribute_support": false,
        "name": "Disable AFP",
        "profile_identifier": "com.unwiredmdm.aabc717175a3467b93af177aa5f1992b",
        "user_scope": false
      },
      "id": 13,
      "type": "custom_configuration_profile"
    }
  ],
  "has_more": false
}
```

# Devices / List installed apps

```http
GET https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/installed_apps
```

```json
{
  "data": [
    {
      "attributes": {
        "bundle_size": 93097984,
        "discovered_at": "2015-10-01T18:02:13.611-07:00",
        "dynamic_size": 1056768,
        "identifier": "com.agilebits.onepassword-ios",
        "last_seen_at": "2021-12-22T13:00:57.000-08:00",
        "managed": true,
        "name": "1Password",
        "short_version": "6.0.1",
        "version": "601004"
      },
      "id": 578,
      "type": "installed_app"
    },
    {
      "attributes": {
        "bundle_size": 120823808,
        "discovered_at": "2015-10-01T18:02:13.858-07:00",
        "dynamic_size": 27934720,
        "identifier": "com.airbnb.app",
        "last_seen_at": "2021-12-22T13:00:57.000-08:00",
        "managed": false,
        "name": "Airbnb",
        "short_version": "15.39",
        "version": "485"
      },
      "id": 618,
      "type": "installed_app"
    },
    {
      "attributes": {
        "bundle_size": 24756224,
        "discovered_at": "2015-10-01T18:02:13.659-07:00",
        "dynamic_size": 18677760,
        "identifier": "com.bandsintown.bit",
        "last_seen_at": "2021-12-22T13:00:57.000-08:00",
        "managed": false,
        "name": "Bandsintown",
        "short_version": "4.13.1",
        "version": "160"
      },
      "id": 587,
      "type": "installed_app"
    },
    ...
  ],
  "has_more": false
}
```

# Devices / List Users

```http
GET https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/users
```

```json
{
  "data": [
    {
      "attributes": {
        "data_quota": null,
        "data_to_sync": false,
        "data_used": null,
        "full_name": "User One",
        "logged_in": true,
        "mobile_account": false,
        "secure_token": true,
        "uid": 501,
        "user_guid": "2DEE464E-0C21-4D0C-8B5B-0F74655ED54E",
        "username": "userone"
      },
      "id": 5,
      "type": "device_user"
    },
    {
      "attributes": {
        "data_quota": null,
        "data_to_sync": false,
        "data_used": null,
        "full_name": "User Two",
        "logged_in": false,
        "mobile_account": false,
        "secure_token": true,
        "uid": 502,
        "user_guid": "AABBA42B-8078-48BA-9DA7-2CB6B0BC7272",
        "username": "usertwo"
      },
      "id": 6,
      "type": "device_user"
    }
  ],
  "has_more": false
}
```

# Devices / Delete User

```http
DELETE https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/users/{USER_ID}
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Push assigned apps

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/push_apps
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Refresh

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/refresh
```

```http
HTTP/1.1 202
```

# Devices / Restart

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/restart
```

| Argument               | Description                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `rebuild_kernel_cache` | Optional. Rebuild the kernel cache during restart. Requires macOS 11 or later. Defaults to false                                 |
| `notify_user`          | Optional. If a user is signed in, prompt them to optionally restart the device. Requires macOS 11.3 or later. Defaults to false. |


```http
HTTP/1.1 202 Accepted
```

# Devices / Shut down

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/shutdown
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Lock

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/lock
```

| Argument       | Description                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| `message`      | Optional. The message to display on the lock screen. Supported on iOS 7.0+ and macOS 10.14+.                    |
| `phone_number` | Optional. The phone number to display on the lock screen.                                                       |
| `pin`          | Required for macOS devices. Not supported by iOS. A 6-digit number that the device will require to be unlocked. |


```http
HTTP/1.1 202 Accepted
```

# Devices / Clear passcode

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/clear_passcode
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Clear firmware password

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/clear_firmware_password
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Rotate FileVault recovery key

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/rotate_filevault_key
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Wipe

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/wipe
```

| Argument | Description                                                                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pin` | Required for macOS devices that do not have the T2 chip. Not supported by iOS or macOS devices with a T2 chip. A 6-digit number that the device will require to be unlocked. |


```http
HTTP/1.1 202 Accepted
```

# Devices / Update OS

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/update_os
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Enable Remote Desktop

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/remote_desktop
```

```http
HTTP/1.1 202 Accepted
```

# Devices / Disable Remote Desktop

```http
DELETE https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/remote_desktop
```

```http
HTTP/1.1 202 Accepted
```

# Device Groups / List all

```http
GET https://a.simplemdm.com/api/v1/device_groups
```

```json
{
  "data": [
    {
      "attributes": {
        "name": "Remote Employees"
      },
      "id": 37,
      "type": "device_group"
    },
    {
      "attributes": {
        "name": "Executives"
      },
      "id": 38,
      "type": "device_group"
    }
  ],
  "has_more": false
}
```

# Device Groups / Retrieve one

```http
GET https://a.simplemdm.com/api/v1/device_groups/{DEVICE_GROUP_ID}
```

```json
{
  "data": {
    "attributes": {
      "name": "Remote Employees"
    },
    "id": 37,
    "type": "device_group"
  }
}
```

# Device Groups / Assign device

```http
POST https://a.simplemdm.com/api/v1/device_groups/{DEVICE_GROUP_ID}/devices/{DEVICE_ID}
```

```http
HTTP/1.1 202 No Content
```

# Device Groups / Clone

```http
POST https://a.simplemdm.com/api/v1/device_groups/{DEVICE_GROUP_ID}/clone
```

```json
{
  "data": {
    "attributes": {
      "name": "Remote Employees (1)"
    },
    "id": 38,
    "relationships": {
      "devices": {
        "data": []
      }
    },
    "type": "device_group"
  }
}
```

# Enrollments / List All

```http
GET https://a.simplemdm.com/api/v1/enrollments
```

```json
{
  "data": [
    {
      "attributes": {
        "url": "https://a.simplemdm.com/e/?c=31970277"
      },
      "id": 3,
      "relationships": {
        "device_group": {
          "data": {
            "id": 3,
            "type": "device_group"
          }
        }
      },
      "type": "enrollment"
    },
    {
      "attributes": {
        "url": "https://a.simplemdm.com/e/?c=30486333"
      },
      "id": 4,
      "relationships": {
        "device_group": {
          "data": {
            "id": 1,
            "type": "device_group"
          }
        }
      },
      "type": "enrollment"
    },
    {
      "attributes": {
        "url": "https://a.simplemdm.com/e/?c=86534893"
      },
      "id": 5,
      "relationships": {
        "device": {
          "data": {
            "id": 11,
            "type": "device"
          }
        }
      },
      "type": "enrollment"
    }
  ],
  "has_more": false
}
```

# Enrollments / Show

```http
GET https://a.simplemdm.com/api/v1/enrollments/{ENROLLMENT_ID}
```

```json
{
  "data": {
    "attributes": {
      "url": "https://a.simplemdm.com/e/?c=86534893"
    },
    "id": 5,
    "relationships": {
      "device": {
        "data": {
          "id": 11,
          "type": "device"
        }
      }
    },
    "type": "enrollment"
  }
}
```

# Enrollments / Send Invitation

```http
POST https://a.simplemdm.com/api/v1/enrollments/{ENROLLMENT_ID}/invitations
```

| Argument  | Description                                                                        |
|-----------|------------------------------------------------------------------------------------|
| `contact` | Required. An email address or phone number. Prefix international numbers with a +. |


# Enrollments / Delete

```http
GET https://a.simplemdm.com/api/v1/enrollments
```

```shell
curl https://a.simplemdm.com/api/v1/enrollments \
  -u {API_KEY}:
```

# Installed Apps / Retrieve one

```http
GET https://a.simplemdm.com/api/v1/installed_apps/{INSTALLED_APP_ID}
```

```json
{
  "data": {
    "attributes": {
      "bundle_size": 15720448,
      "discovered_at": "2016-10-12T15:54:16.116-07:00",
      "dynamic_size": 16384,
      "identifier": "com.fuilana.SunsetRun",
      "last_seen_at": "2021-12-22T13:00:57.000-08:00",
      "managed": true,
      "name": "Sunset Run",
      "short_version": "2.2.1",
      "version": "2.2.1.1"
    },
    "id": 6632,
    "type": "installed_app"
  }
}
```

# Installed Apps / Request management of app

```http
POST https://a.simplemdm.com/api/v1/installed_apps/{INSTALLED_APP_ID}/request_management
```

```http
HTTP/1.1 202 Accepted
```

# Installed Apps / Install update

```http
POST https://a.simplemdm.com/api/v1/installed_apps/{INSTALLED_APP_ID}/update
```

```http
HTTP/1.1 202 Accepted
```

# Installed Apps / Uninstall

```http
DELETE https://a.simplemdm.com/api/v1/installed_apps/{INSTALLED_APP_ID}
```

```http
HTTP/1.1 202 Accepted
```

# Logs / List All

```http
GET https://a.simplemdm.com/api/v1/logs
```

```json
{
  "data": [
    {
      "attributes": {
        "at": "11/06/19 18:27:41",
        "event_type": "user.signed_in",
        "level": 0,
        "metadata": {},
        "namespace": "admin",
        "relationships": {
          "account": {
            "data": {
              "id": 123456,
              "type": "account"
            }
          },
          "user": {
            "data": {
              "email": "support@simplemdm.com",
              "id": 123456,
              "type": "user"
            }
          }
        },
        "source": "admin ui"
      },
      "id": "abcde123456",
      "type": "log"
    }
  ],
  "has_more": true
}
```

# Lost Mode / Enable

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/lost_mode
```

| Argument       | Description                                                        |
|----------------|--------------------------------------------------------------------|
| `message`      | A message to be delivered to the user of the device.               |
| `phone_number` | A contact number to reach the device's administrator.              |
| `footnote`     | An additional message to be displayed at the bottom of the device. |


# Lost Mode / Disable

```http
DELETE https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/lost_mode
```

# Lost Mode / Play a sound

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/lost_mode/play_sound
```

# Lost Mode / Update location

```http
POST https://a.simplemdm.com/api/v1/devices/{DEVICE_ID}/lost_mode/update_location
```

# Managed App Configs / Get

```http
GET https://a.simplemdm.com/api/v1/apps/{APP_ID}/managed_configs
```

```json
{
  "data": [
    {
      "attributes": {
        "key": "customer_name",
        "value": "ACME Inc.",
        "value_type": "string"
      },
      "id": 14,
      "type": "managed_config"
    },
    {
      "attributes": {
        "key": "User IDs",
        "value": "1,53,3",
        "value_type": "integer array"
      },
      "id": 32,
      "type": "managed_config"
    },
    {
      "attributes": {
        "key": "Device values",
        "value": "\"$imei\",\"$udid\"",
        "value_type": "string array"
      },
      "id": 13,
      "type": "managed_config"
    }
  ],
  "has_more": false
}
```

# Managed App Configs / Create

| Argument     | Description                                                          |
|--------------|----------------------------------------------------------------------|
| `key`        | Required.                                                            |
| `value`      | Valid values are based on the value_type specified. See table below. |
| `value_type` | The type of the value. See valid options below.                      |


# Managed App Configs / Delete

```http
DELETE https://a.simplemdm.com/api/v1/apps/{APP_ID}/managed_configs/{MANAGED_CONFIG_ID}
```

# Managed App Configs / Push Updates

```http
POST https://a.simplemdm.com/api/v1/apps/{APP_ID}/managed_configs/push
```

# Push Certificate / Show

```http
GET https://a.simplemdm.com/api/v1/push_certificate
```

```json
{
  "data": {
    "attributes": {
      "apple_id": "devops@example.org",
      "expires_at": "2017-09-21T15:28:34.000+00:00"
    },
    "type": "push_certificate"
  }
}
```

# Push Certificate / Update

```http
PUT https://a.simplemdm.com/api/v1/push_certificate
```

| Argument   | Description                                                                          |
|------------|--------------------------------------------------------------------------------------|
| `file`     | Required. The push certificate as provided by Apple. Send as multipart/form-data.    |
| `apple_id` | Optional. The email address of the apple ID the push certificate was generated with. |


```json
{
  "data": {
    "attributes": {
      "apple_id": "admin@example.org",
      "expires_at": "2020-09-21T15:28:34.000+00:00"
    },
    "type": "push_certificate"
  }
}
```

# Push Certificate / Get Signed CSR

```http
GET https://a.simplemdm.com/api/v1/push_certificate/scsr
```

```json
{
  "type": "event.type",
  "at": "2000-01-01T12:00:00.000-07:00",
  "data": {}
}
```

