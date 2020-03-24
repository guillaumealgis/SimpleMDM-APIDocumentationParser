// SimpleMDM API Version 1.21

# Authentication

```shell
$ curl https://a.simplemdm.com/api/v1/account
```


# Errors

```json
{
    "errors": [
        {
            "title": "object not found"
        }
    ]
}
```

# Pagination

```shell
$ curl https://a.simplemdm.com/api/v1/apps?limit=3&starting_after=33
```

```json
{
  "data": [
    {
      "type": "app",
      "id": 34,
      "attributes": {
        "name": "Afterlight",
        "bundle_identifier": "com.simonfilip.AfterGlow",
        "app_type": "app store",
        "itunes_store_id": 573116090
      }
    },
    {
      "type": "app",
      "id": 63,
      "attributes": {
        "name": "Surf Report",
        "bundle_identifier": "com.portlandsurfclub.ent.surfreport2.2",
        "app_type": "enterprise",
        "version": "2.2"
      }
    },
    {
      "type": "app",
      "id": 67,
      "attributes": {
        "name": "Scanner Pro",
        "app_type": "custom b2b",
        "itunes_store_id": 44827291
      }
    }
  ],
  "has_more": true
}
```

# Account / Show

```shell
$ curl https://a.simplemdm.com/api/v1/account
```

```json
{
  "data": {
    "type": "account",
    "attributes": {
      "name": "SimpleMDM",
      "apple_store_country_code": "US",
      "subscription": {
        "licenses": {
          "total": 500,
          "available": 123
        }
      }
    }
  }
}

```

# Account / Update

```shell
$ curl https://a.simplemdm.com/api/v1/account -F _method=PATCH -d apple_store_country_code=AU
```

```json
{
  "data": {
      "type": "account",
      "attributes": {
          "name": "SimpleMDM",
          "apple_store_country_code": "AU"
      }
  }
}
```

# Apps / List all

```shell
$ curl https://a.simplemdm.com/api/v1/apps
```

```json
{
  "data": [
    {
      "type": "app",
      "id": 34,
      "attributes": {
        "name": "Afterlight",
        "bundle_identifier": "com.simonfilip.AfterGlow",
        "app_type": "app store",
        "itunes_store_id": 573116090
      }
    },
    {
      "type": "app",
      "id": 63,
      "attributes": {
        "name": "Surf Report",
        "bundle_identifier": "com.portlandsurfclub.ent.surfreport2.2",
        "app_type": "enterprise",
        "version": "2.2"
      }
    },
    {
      "type": "app",
      "id": 67,
      "attributes": {
        "name": "Scanner Pro",
        "app_type": "custom b2b",
        "itunes_store_id": 44827291
      }
    }
  ],
  "has_more": false
}
```

# Apps / Retrieve one

```shell
$ curl https://a.simplemdm.com/api/v1/apps/34
```

```json
{
  "data": {
    "type": "app",
    "id": 34,
    "attributes": {
      "name": "Afterlight",
      "bundle_identifier": "com.simonfilip.AfterGlow",
      "app_type": "app store",
      "itunes_store_id": 573116090
    }
  }
}
```

# Apps / Create

```shell
$ curl https://a.simplemdm.com/api/v1/apps -F binary=@SurfReport.ipa
```

```json
{
  "data": {
    "type": "app",
    "id": 63,
    "attributes": {
      "name": "Surf Report",
      "app_type": "enterprise",
      "version": "2.2",
      "bundle_identifier": "com.portlandsurfclub.ent.surfreport2.2"
    }
  }
}
```

# Apps / Update

```shell
$ curl https://a.simplemdm.com/api/v1/apps/63 -F binary=@SurfReportUpdated.ipa -F _method=PATCH
```

```json
{
  "data": {
    "type": "app",
    "id": 63,
    "attributes": {
      "name": "Surf Report (Updated)",
      "app_type": "enterprise",
      "version": "2.3",
      "bundle_identifier": "com.portlandsurfclub.ent.surfreport2.3"
    }
  }
}
```

# Apps / Delete

```shell
$ curl https://a.simplemdm.com/api/v1/apps/63
-> HTTP/1.1 204 No Content
```


# Assignment Groups / List all

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups
```

```json
{
  "data": [
    {
      "type": "assignment_group",
      "id": 26,
      "attributes": {
        "name": "SimpleMDM",
        "auto_deploy": true
      },
      "relationships": {
        "apps": {
          "data": [
            {
              "type": "app",
              "id": 49
            }
          ]
        },
        "device_groups": {
          "data": [
            {
              "type": "device_group",
              "id": 37
            }
          ]
        },
        "devices": {
          "data": [
            {
              "type": "device",
              "id": 56
            }
          ]
        }
      }
    },
    {
      "type": "assignment_group",
      "id": 38,
      "attributes": {
        "name": "Productivity Apps",
        "auto_deploy": false
      },
      "relationships": {
        "apps": {
          "data": [
            {
              "type": "app",
              "id": 63
            },
            {
              "type": "app",
              "id": 67
            }
          ]
        },
        "device_groups": {
          "data": [
            {
              "type": "device_group",
              "id": 37
            },
            {
              "type": "device_group",
              "id": 38
            }
          ]
        },
        "devices": {
          "data": [
            {
              "type": "device",
              "id": 54
            }
          ]
        }
      }
    },

    ...

  ],
  "has_more": false
}
```

# Assignment Groups / Retrieve one

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/26
```

```json
{
  "data": {
    "type": "assignment_group",
    "id": 26,
    "attributes": {
      "name": "SimpleMDM",
      "auto_deploy": true
    },
    "relationships": {
      "apps": {
        "data": [
          {
            "type": "app",
            "id": 49
          },
          {
            "type": "app",
            "id": 67
          }
        ]
      },
      "device_groups": {
        "data": [
          {
            "type": "device_group",
            "id": 37
          },
          {
            "type": "device_group",
            "id": 38
          }
        ]
      },
      "devices": {
        "data": [
          {
            "type": "device",
            "id": 54
          }
        ]
      }
    }
  }
}
```

# Assignment Groups / Create

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups -d name="Communication Apps"
```

```json
{
  "data": {
    "type": "assignment_group",
    "id": 43,
    "attributes": {
      "name": "Communication Apps",
      "auto_deploy": true
    },
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
    }
  }
}
```

# Assignment Groups / Update

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43 -d auto_deploy=false
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Delete

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/{ASSIGNMENT_GROUP_ID}
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Assign app

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/apps/21
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Unassign app

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/apps/21
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Assign device group

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/device_groups/87
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Unassign device group

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/device_groups/87
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Assign device

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/devices/87
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Unassign device

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/device/87
-> HTTP/1.1 204 No Content
```


# Assignment Groups / Push apps

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/push_apps
-> HTTP/1.1 202 Accepted
```


# Assignment Groups / Update apps

```shell
$ curl https://a.simplemdm.com/api/v1/assignment_groups/43/update_apps
-> HTTP/1.1 202 Accepted
```


# Custom Attributes / List all

```shell
$ curl https://a.simplemdm.com/api/v1/custom_attributes
```

```json
{
    "data": [
        {
            "type": "custom_attribute",
            "id": "email_address",
            "attributes": {
                "name": "email_address"
            }
        },
        {
            "type": "custom_attribute",
            "id": "full_name",
            "attributes": {
                "name": "full_name"
            }
        }
    ],
    "has_more": false
}
```

# Custom Configuration Profiles / List all

```shell
$ curl https://a.simplemdm.com/api/v1/custom_configuration_profiles
```

```json
{
    "data": [
        {
            "type": "custom_configuration_profile",
            "id": 293814,
            "attributes": {
                "name": "Munki Configuration",
                "user_scope": true,
                "attribute_support": false
            },
            "relationships": {
                "device_groups": {
                    "data": [
                        {
                            "type": "device group",
                            "id": 732444
                        }
                    ]
                }
            }
        }
    ],
    "has_more": false
}
```

# Devices / List all

```shell
$ curl https://a.simplemdm.com/api/v1/devices
```

```json
{
  "data": [
    {
      "type": "device",
      "id": 121,
      "attributes": {
        "name": "Mike's iPhone",
        "last_seen_at": "2015-10-01T18:38:47.277-07:00",
        "status": "enrolled",
        "device_name": "Mike's iPhone",
        "os_version": "9.0.2",
        "build_version": "13A452",
        "model_name": "iPhone 6",
        "model": "NG4W2LL",
        "product_name": "iPhone7,2",
        "unique_identifier": "4A08359C-1D3A-5D3E-939E-FFA6A561321D",
        "serial_number": "DNFJE9DNG5MG",
        "imei": "35 445506 652132 5",
        "meid": "35404596608032",
        "device_capacity": 55.62955093383789,
        "available_device_capacity": 15.19466781616211,
        "battery_level": "93%",
        "modem_firmware_version": "4.02.00",
        "iccid": "8914 8110 0002 8094 4264",
        "bluetooth_mac": "f0:db:e2:df:e9:11",
        "wifi_mac": "f0:db:e2:df:e9:2f",
        "current_carrier_network": "Verizon",
        "sim_carrier_network": "Verizon",
        "subscriber_carrier_network": "Verizon",
        "carrier_settings_version": "21.1",
        "phone_number": "5035551234",
        "voice_roaming_enabled": true,
        "data_roaming_enabled": false,
        "is_roaming": false,
        "subscriber_mcc": "311",
        "simmnc": "480",
        "current_mcc": "311",
        "current_mnc": "480",
        "hardware_encryption_caps": 3,
        "passcode_present": true,
        "passcode_compliant": true,
        "passcode_compliant_with_profiles": true,
        "subscriber_mnc": "480",
        "simmcc": "311",
        "is_supervised": false,
        "is_device_locator_service_enabled": true,
        "is_do_not_disturb_in_effect": false,
        "personal_hotspot_enabled": true,
        "itunes_store_account_is_active": true,
        "cellular_technology": 3,
        "last_cloud_backup_date": "2015-10-01T15:09:12.000-07:00",
        "is_activation_lock_enabled": true,
        "is_cloud_backup_enabled": true,
        "location_latitude": "75.13421212355",
        "location_longitude": "-14.313565422",
        "location_accuracy": "60",
        "location_updated_at": "2015-10-01T15:09:12.000-07:00"
      },
      "relationships": {
        "device_group": {
          "data": {
            "type": "device_group",
            "id": 37
          }
        }
      }
    },

    ...

  ],
  "has_more": false
}
```

# Devices / Retrieve one

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121
```

```json
{
  "data": {
    "type": "device",
    "id": 121,
    "attributes": {
      "name": "Mike's iPhone",
      "last_seen_at": "2015-10-01T18:38:47.277-07:00",
      "status": "enrolled",
      "device_name": "Mike's iPhone",
      "os_version": "9.0.2",
      "build_version": "13A452",
      "model_name": "iPhone 6",
      "model": "NG4W2LL",
      "product_name": "iPhone7,2",
      "serial_number": "DNFJE9DNG5MG",
      "imei": "35 445506 652132 5",
      "meid": "35404596608032",
      "device_capacity": 55.62955093383789,
      "available_device_capacity": 15.19466781616211,
      "battery_level": "93%",
      "modem_firmware_version": "4.02.00",
      "iccid": "8914 8110 0002 8094 4264",
      "bluetooth_mac": "f0:db:e2:df:e9:11",
      "wifi_mac": "f0:db:e2:df:e9:2f",
      "current_carrier_network": "Verizon",
      "sim_carrier_network": "Verizon",
      "subscriber_carrier_network": "Verizon",
      "carrier_settings_version": "21.1",
      "phone_number": "5035551234",
      "voice_roaming_enabled": true,
      "data_roaming_enabled": false,
      "is_roaming": false,
      "subscriber_mcc": "311",
      "simmnc": "480",
      "current_mcc": "311",
      "current_mnc": "480",
      "hardware_encryption_caps": 3,
      "passcode_present": true,
      "passcode_compliant": true,
      "passcode_compliant_with_profiles": true,
      "subscriber_mnc": "480",
      "simmcc": "311",
      "is_supervised": false,
      "is_device_locator_service_enabled": true,
      "is_do_not_disturb_in_effect": false,
      "personal_hotspot_enabled": true,
      "itunes_store_account_is_active": true,
      "cellular_technology": 3,
      "last_cloud_backup_date": "2015-10-01T15:09:12.000-07:00",
      "is_activation_lock_enabled": true,
      "is_cloud_backup_enabled": true,
      "location_latitude": "75.13421212355",
      "location_longitude": "-14.313565422",
      "location_accuracy": "60",
      "location_updated_at": "2015-10-01T15:09:12.000-07:00"
    },
    "relationships": {
      "device_group": {
        "data": {
          "type": "device_group",
          "id": 37
        }
      }
    }
  }
}
```

# Devices / Create

```shell
$ curl https://a.simplemdm.com/api/v1/devices/ -d name="Sara's iPad" -d group_id="41"
```

```json
{
    "data" => {
                 "type" => "device",
                   "id" => 980190963,
           "attributes" => {
                                         "name" => "Sara's iPad",
                                 "last_seen_at" => nil,
                                       "status" => "awaiting enrollment",
                               "enrollment_url" => "https://a.simplemdm.com/e/?c=63154796",
                                  "device_name" => nil,
                                   "os_version" => nil,
                                "build_version" => nil,
                                   "model_name" => "Unknown",
                                        "model" => nil,
                                 "product_name" => nil,
                            "unique_identifier" => nil,
                                "serial_number" => nil,
                                         "imei" => nil,
                                         "meid" => nil,
                              "device_capacity" => nil,
                    "available_device_capacity" => nil,
                                "battery_level" => nil,
                       "modem_firmware_version" => nil,
                                        "iccid" => nil,
                                "bluetooth_mac" => nil,
                                     "wifi_mac" => nil,
                      "current_carrier_network" => nil,
                          "sim_carrier_network" => nil,
                   "subscriber_carrier_network" => nil,
                     "carrier_settings_version" => nil,
                                 "phone_number" => nil,
                        "voice_roaming_enabled" => nil,
                         "data_roaming_enabled" => nil,
                                   "is_roaming" => nil,
                               "subscriber_mcc" => nil,
                                       "simmnc" => nil,
                                  "current_mcc" => nil,
                                  "current_mnc" => nil,
                     "hardware_encryption_caps" => nil,
                             "passcode_present" => nil,
                           "passcode_compliant" => nil,
             "passcode_compliant_with_profiles" => nil,
                                "is_supervised" => nil,
            "is_device_locator_service_enabled" => nil,
                  "is_do_not_disturb_in_effect" => nil,
                     "personal_hotspot_enabled" => nil,
               "itunes_store_account_is_active" => nil,
                          "cellular_technology" => nil,
                       "last_cloud_backup_date" => nil,
                   "is_activation_lock_enabled" => nil,
                      "is_cloud_backup_enabled" => nil,
                            "location_latitude" => nil,
                           "location_longitude" => nil,
                            "location_accuracy" => nil,
                          "location_updated_at" => nil
        },
        "relationships" => {
            "device_group" => {
                "data" => {
                    "type" => "device_group",
                      "id" => 41
                }
            }
        }
    }
}
```

# Devices / Update

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121 -X PATCH -d name="Ashley's iPad"
```

```json
{
  "data": {
    "type": "device",
    "id": 121,
    "attributes": {
      "name": "Ashley's iPad",
      "last_seen_at": "2015-10-01T18:38:47.277-07:00",
      "status": "enrolled",
      "device_name": "iPhone",
      "os_version": "9.3.2",
      "build_version": "13A452",
      "model_name": "iPhone 6",
      "model": "NG4W2LL",
      "product_name": "iPhone7,2",
      "serial_number": "DNFJE9DNG5MG",
      "imei": "35 445506 652132 5",
      "meid": "35404596608032",
      "device_capacity": 55.62955093383789,
      "available_device_capacity": 15.19466781616211,
      "battery_level": "93%",
      "modem_firmware_version": "4.02.00",
      "iccid": "8914 8110 0002 8094 4264",
      "bluetooth_mac": "f0:db:e2:df:e9:11",
      "wifi_mac": "f0:db:e2:df:e9:2f",
      "current_carrier_network": "Verizon",
      "sim_carrier_network": "Verizon",
      "subscriber_carrier_network": "Verizon",
      "carrier_settings_version": "21.1",
      "phone_number": "5035551234",
      "voice_roaming_enabled": true,
      "data_roaming_enabled": false,
      "is_roaming": false,
      "subscriber_mcc": "311",
      "simmnc": "480",
      "current_mcc": "311",
      "current_mnc": "480",
      "hardware_encryption_caps": 3,
      "passcode_present": true,
      "passcode_compliant": true,
      "passcode_compliant_with_profiles": true,
      "subscriber_mnc": "480",
      "simmcc": "311",
      "is_supervised": false,
      "is_device_locator_service_enabled": true,
      "is_do_not_disturb_in_effect": false,
      "personal_hotspot_enabled": true,
      "itunes_store_account_is_active": true,
      "cellular_technology": 3,
      "last_cloud_backup_date": "2015-10-01T15:09:12.000-07:00",
      "is_activation_lock_enabled": true,
      "is_cloud_backup_enabled": true,
      "location_latitude": "75.13421212355",
      "location_longitude": "-14.313565422",
      "location_accuracy": "60",
      "location_updated_at": "2015-10-01T15:09:12.000-07:00"
    },
    "relationships": {
      "device_group": {
        "data": {
          "type": "device_group",
          "id": 37
        }
      }
    }
  }
}
```

# Devices / Delete

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121
-> HTTP/1.1 204
```


# Devices / List installed apps

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/installed_apps
```

```json
{
  "data": [
    {
      "type": "installed_app",
      "id": 578,
      "attributes": {
        "name": "1Password",
        "identifier": "com.agilebits.onepassword-ios",
        "version": "601004",
        "short_version": "6.0.1",
        "bundle_size": 93097984,
        "dynamic_size": 1056768,
        "managed": true,
        "discovered_at": "2015-10-01T18:02:13.611-07:00"
      }
    },
    {
      "type": "installed_app",
      "id": 618,
      "attributes": {
        "name": "Airbnb",
        "identifier": "com.airbnb.app",
        "version": "485",
        "short_version": "15.39",
        "bundle_size": 120823808,
        "dynamic_size": 27934720,
        "managed": false,
        "discovered_at": "2015-10-01T18:02:13.858-07:00"
      }
    },
    {
      "type": "installed_app",
      "id": 587,
      "attributes": {
        "name": "Bandsintown",
        "identifier": "com.bandsintown.bit",
        "version": "160",
        "short_version": "4.13.1",
        "bundle_size": 24756224,
        "dynamic_size": 18677760,
        "managed": false,
        "discovered_at": "2015-10-01T18:02:13.659-07:00"
      }
    },

    ...

  ],
  "has_more": false
}
```

# Devices / Push assigned apps

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/push_apps
-> HTTP/1.1 202 Accepted
```


# Devices / Restart

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/restart
-> HTTP/1.1 202 Accepted
```


# Devices / Shutdown

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/shutdown
-> HTTP/1.1 202 Accepted
```


# Devices / Lock

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/lock -d message="Please call the number provided" -d phone_number="5035551212"
-> HTTP/1.1 202 Accepted
```


# Devices / Clear passcode

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/clear_passcode
-> HTTP/1.1 202 Accepted
```


# Devices / Clear firmware password

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/clear_firmware_password
-> HTTP/1.1 202 Accepted
```


# Devices / Wipe

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/wipe
-> HTTP/1.1 202 Accepted
```


# Devices / Update OS

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/update_os
-> HTTP/1.1 202 Accepted
```


# Devices / Refresh

```shell
$ curl https://a.simplemdm.com/api/v1/devices/121/refresh
-> HTTP/1.1 202
```


# Device Groups / List all

```shell
$ curl https://a.simplemdm.com/api/v1/device_groups
```

```json
{
  "data": [
    {
      "type": "device_group",
      "id": 37,
      "attributes": {
        "name": "Remote Employees"
      }
    },
    {
      "type": "device_group",
      "id": 38,
      "attributes": {
        "name": "Executives"
      }
    }
  ],
  "has_more": false
}
```

# Device Groups / Retrieve one

```shell
$ curl https://a.simplemdm.com/api/v1/device_groups/37
```

```json
{
  "data": {
    "type": "device_group",
    "id": 37,
    "attributes": {
      "name": "Remote Employees"
    }
  }
}
```

# Device Groups / Assign device

```shell
$ curl https://a.simplemdm.com/api/v1/device_groups/37/devices/121
-> HTTP/1.1 202 No Content
```


# Device Groups / Clone

```shell
$ curl https://a.simplemdm.com/api/v1/device_groups/37/clone
```

```json
{
  "data": {
    "type": "device_group",
    "id": 38,
    "attributes": {
      "name": "Remote Employees (1)"
    },
    "relationships": {
      "devices": {
        "data": []
      }
    }
  }
}
```

# Enrollments / List All

```shell
$ curl https://a.simplemdm.com/api/v1/enrollments
```

```json
{  
  "data":[  
    {  
      "type":"enrollment",
      "id":3,
      "attributes":{  
        "url":"https://a.simplemdm.com/e/?c=31970277"
      },
      "relationships":{  
        "device_group":{  
          "data":{  
            "type":"device_group",
            "id":3
          }
        }
      }
    },
    {  
      "type":"enrollment",
      "id":4,
      "attributes":{  
        "url":"https://a.simplemdm.com/e/?c=30486333"
      },
      "relationships":{  
        "device_group":{  
          "data":{  
            "type":"device_group",
            "id":1
          }
        }
      }
    },
    {  
      "type":"enrollment",
      "id":5,
      "attributes":{  
        "url":"https://a.simplemdm.com/e/?c=86534893"
      },
      "relationships":{  
        "device":{  
          "data":{  
            "type":"device",
            "id":11
          }
        }
      }
    }
  ],
  "has_more":false
}
```

# Enrollments / Show

```shell
$ curl https://a.simplemdm.com/api/v1/enrollments/5
```

```json
{  
  "data":{  
    "type":"enrollment",
    "id":5,
    "attributes":{  
      "url":"https://a.simplemdm.com/e/?c=86534893"
    },
    "relationships":{  
      "device":{  
        "data":{  
          "type":"device",
          "id":11
        }
      }
    }
  }
}
```

# Enrollments / Delete

```shell
$ curl https://a.simplemdm.com/api/v1/enrollments
```


# Installed Apps / Retrieve one

```shell
$ curl https://a.simplemdm.com/api/v1/installed_apps/6632
```

```json
{
    "data": {
        "type": "installed_app",
        "id": 6632,
        "attributes": {
            "name": "Sunset Run",
            "identifier": "com.fuilana.SunsetRun",
            "version": "2.2.1.1",
            "short_version": "2.2.1",
            "bundle_size": 15720448,
            "dynamic_size": 16384,
            "managed": true,
            "discovered_at": "2016-10-12T15:54:16.116-07:00"
        }
    }
}
```

# Installed Apps / Install update

```shell
$ curl https://a.simplemdm.com/api/v1/installed_apps/{INSTALLED_APP_ID}/update
-> HTTP/1.1 202 Accepted
```


# Installed Apps / Uninstall

```shell
$ curl https://a.simplemdm.com/api/v1/installed_apps/{INSTALLED_APP_ID}
-> HTTP/1.1 202 Accepted
```


# Logs / List All

```shell
$ curl https://a.simplemdm.com/api/v1/logs
```

```json
  {
  "data": [
    {
      "type": "log",
      "id": "abcde123456",
      "attributes": {
        "namespace": "admin",
        "event_type": "user.signed_in",
        "level": 0,
        "source": "admin ui",
        "at": "11/06/19 18:27:41",
        "metadata": {},
        "relationships": {
          "account": {
            "data": {
              "type": "account",
              "id": 123456
            }
          },
          "user": {
            "data": {
              "type": "user",
              "id": 123456,
              "email": "support@simplemdm.com"
            }
          }
        }
      }
    }
  ],
  "has_more": true
}
```

# Managed App Configs / Get

```shell
$ curl https://a.simplemdm.com/api/v1/apps/{APP_ID}/managed_configs
```

```json
{
    "data": [
        {
            "type": "managed_config",
            "id": 14,
            "attributes": {
                "key": "customer_name",
                "value": "ACME Inc.",
                "value_type": "string"
            }
        },
        {
            "type": "managed_config",
            "id": 32,
            "attributes": {
                "key": "User IDs",
                "value": "1,53,3",
                "value_type": "integer array"
            }
        },
        {
            "type": "managed_config",
            "id": 13,
            "attributes": {
                "key": "Device values",
                "value": "\"$imei\",\"$udid\"",
                "value_type": "string array"
            }
        }
    ],
    "has_more": false
}
```

# Push Certificate / Show

```shell
$ curl https://a.simplemdm.com/api/v1/push_certificate
```

```json
{
    "data": {
        "type": "push_certificate",
        "attributes": {
            "apple_id": "devops@example.org",
            "expires_at": "2017-09-21T15:28:34.000+00:00"
        }
    }
}
```

# Push Certificate / Update

```shell
$ curl https://a.simplemdm.com/api/v1/push_certificate/scsr -F file@apns.cert -F apple_id=admin@example.org
```

```json
{
    "data": {
        "type": "push_certificate",
        "attributes": {
            "apple_id": "admin@example.org",
            "expires_at": "2020-09-21T15:28:34.000+00:00"
        }
    }
}
```

# Push Certificate / Get Signed CSR

```shell
$ curl https://a.simplemdm.com/api/v1/push_certificate/scsr
```

```json
{
    "data": "VUVRVZ5HSlhkMmRrYlZaNVl6SnNkbUpxTUdsTlV6UjNTV2xDYkdKdFRuWmFS\nMngxV25vd2FWWldVa2RNClZHZHBVSG8wUzFCRFJrVlVNRTVWQ2xkV1FrWkpT\nRUp6WVZoT01FbEdRbFpSYTNoS1VYbEJhVXhUT0haUgpXRUozWWtkVloxRXlP\nWFJaU0ZZd1dsaEpka3d3QmtSa3BwVGxWb2VWWkgKYkRKa01V\nSkVXakJzYjFWclJYWmlhMFpUVGxWNFdWSkdVWGRsYkUxTFdsVTRjbU5FU1RB\nSUlRSM1VWVTFid3BSCmFscDBUVVpz\nUWsxWGFGUlRWMWw2VFcweFlXTlZkRVpVUjFaSlZuazVlVmx0VW5WT01VVTVV\nRkZ2T0V3egpUakJqYld4MVdubzBTMUJET1dzS1lWZE9NRkJuYnpoTU0wSnpZ\nVmhPTUZCbmJ6MEsT\n"
}
```

# Webhooks

```json
{
  "type": "event.type",
  "at": "2000-01-01T12:00:00.000-07:00",
  "data": {}
}
```

# Webhooks / Events

- device.changed_group
- device.enrolled
- device.unenrolled

