---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/uuid.html
original_path: connectivity/bluetooth/api/uuid.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Universal Unique Identifiers (UUIDs)

## API Reference

*group* UUIDs
:   UUIDs.

    Defines

    BT\_UUID\_SIZE\_16
    :   Size in octets of a 16-bit UUID.

    BT\_UUID\_SIZE\_32
    :   Size in octets of a 32-bit UUID.

    BT\_UUID\_SIZE\_128
    :   Size in octets of a 128-bit UUID.

    BT\_UUID\_INIT\_16(value)
    :   Initialize a 16-bit UUID.

        Parameters:
        :   - **value** – 16-bit UUID value in host endianness.

    BT\_UUID\_INIT\_32(value)
    :   Initialize a 32-bit UUID.

        Parameters:
        :   - **value** – 32-bit UUID value in host endianness.

    BT\_UUID\_INIT\_128(value...)
    :   Initialize a 128-bit UUID.

        Parameters:
        :   - **value** – 128-bit UUID array values in little-endian format. Can be combined with [BT\_UUID\_128\_ENCODE](#group__bt__uuid_1gac3973b66e992cbc0940752b77b378f43) to initialize a UUID from the readable form of UUIDs.

    BT\_UUID\_DECLARE\_16(value)
    :   Helper to declare a 16-bit UUID inline.

        Parameters:
        :   - **value** – 16-bit UUID value in host endianness.

        Returns:
        :   Pointer to a generic UUID.

    BT\_UUID\_DECLARE\_32(value)
    :   Helper to declare a 32-bit UUID inline.

        Parameters:
        :   - **value** – 32-bit UUID value in host endianness.

        Returns:
        :   Pointer to a generic UUID.

    BT\_UUID\_DECLARE\_128(value...)
    :   Helper to declare a 128-bit UUID inline.

        Parameters:
        :   - **value** – 128-bit UUID array values in little-endian format. Can be combined with [BT\_UUID\_128\_ENCODE](#group__bt__uuid_1gac3973b66e992cbc0940752b77b378f43) to declare a UUID from the readable form of UUIDs.

        Returns:
        :   Pointer to a generic UUID.

    BT\_UUID\_16(\_\_u)
    :   Helper macro to access the 16-bit UUID from a generic UUID.

    BT\_UUID\_32(\_\_u)
    :   Helper macro to access the 32-bit UUID from a generic UUID.

    BT\_UUID\_128(\_\_u)
    :   Helper macro to access the 128-bit UUID from a generic UUID.

    BT\_UUID\_128\_ENCODE(w32, w1, w2, w3, w48)
    :   Encode 128 bit UUID into array values in little-endian format.

        Helper macro to initialize a 128-bit UUID array value from the readable form of UUIDs, or encode 128-bit UUID values into advertising data Can be combined with BT\_UUID\_DECLARE\_128 to declare a 128-bit UUID.

        Example of how to declare the UUID `6E400001-B5A3-F393-E0A9-E50E24DCCA9E`

        ```text
        BT_UUID_DECLARE_128(
             BT_UUID_128_ENCODE(0x6E400001, 0xB5A3, 0xF393, 0xE0A9, 0xE50E24DCCA9E))
        ```

        Example of how to encode the UUID `6E400001-B5A3-F393-E0A9-E50E24DCCA9E` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_UUID128_ALL,
             BT_UUID_128_ENCODE(0x6E400001, 0xB5A3, 0xF393, 0xE0A9, 0xE50E24DCCA9E))
        ```

        Just replace the hyphen by the comma and add `0x` prefixes.

        Parameters:
        :   - **w32** – First part of the UUID (32 bits)
            - **w1** – Second part of the UUID (16 bits)
            - **w2** – Third part of the UUID (16 bits)
            - **w3** – Fourth part of the UUID (16 bits)
            - **w48** – Fifth part of the UUID (48 bits)

        Returns:
        :   The comma separated values for UUID 128 initializer that may be used directly as an argument for [BT\_UUID\_INIT\_128](#group__bt__uuid_1ga1a840adf4bc06cf2cd5dbeb0c868374b) or [BT\_UUID\_DECLARE\_128](#group__bt__uuid_1gadece715e13e2a529aa55c298ff760bf0)

    BT\_UUID\_16\_ENCODE(w16)
    :   Encode 16-bit UUID into array values in little-endian format.

        Helper macro to encode 16-bit UUID values into advertising data.

        Example of how to encode the UUID `0x180a` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_UUID16_ALL, BT_UUID_16_ENCODE(0x180a))
        ```

        Parameters:
        :   - **w16** – UUID value (16-bits)

        Returns:
        :   The comma separated values for UUID 16 value that may be used directly as an argument for [BT\_DATA\_BYTES](gap.md#group__bt__gap_1ga4c51f9b7a3a4e84abb4df3f1f714c6e2).

    BT\_UUID\_32\_ENCODE(w32)
    :   Encode 32-bit UUID into array values in little-endian format.

        Helper macro to encode 32-bit UUID values into advertising data.

        Example of how to encode the UUID `0x180a01af` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_UUID32_ALL, BT_UUID_32_ENCODE(0x180a01af))
        ```

        Parameters:
        :   - **w32** – UUID value (32-bits)

        Returns:
        :   The comma separated values for UUID 32 value that may be used directly as an argument for [BT\_DATA\_BYTES](gap.md#group__bt__gap_1ga4c51f9b7a3a4e84abb4df3f1f714c6e2).

    BT\_UUID\_STR\_LEN
    :   Recommended length of user string buffer for Bluetooth UUID.

        The recommended length guarantee the output of UUID conversion will not lose valuable information about the UUID being processed. If the length of the UUID is known the string can be shorter.

    BT\_UUID\_GAP\_VAL
    :   Generic Access UUID value.

    BT\_UUID\_GAP
    :   Generic Access.

    BT\_UUID\_GATT\_VAL
    :   Generic attribute UUID value.

    BT\_UUID\_GATT
    :   Generic Attribute.

    BT\_UUID\_IAS\_VAL
    :   Immediate Alert Service UUID value.

    BT\_UUID\_IAS
    :   Immediate Alert Service.

    BT\_UUID\_LLS\_VAL
    :   Link Loss Service UUID value.

    BT\_UUID\_LLS
    :   Link Loss Service.

    BT\_UUID\_TPS\_VAL
    :   Tx Power Service UUID value.

    BT\_UUID\_TPS
    :   Tx Power Service.

    BT\_UUID\_CTS\_VAL
    :   Current Time Service UUID value.

    BT\_UUID\_CTS
    :   Current Time Service.

    BT\_UUID\_RTUS\_VAL
    :   Reference Time Update Service UUID value.

    BT\_UUID\_RTUS
    :   Reference Time Update Service.

    BT\_UUID\_NDSTS\_VAL
    :   Next DST Change Service UUID value.

    BT\_UUID\_NDSTS
    :   Next DST Change Service.

    BT\_UUID\_GS\_VAL
    :   Glucose Service UUID value.

    BT\_UUID\_GS
    :   Glucose Service.

    BT\_UUID\_HTS\_VAL
    :   Health Thermometer Service UUID value.

    BT\_UUID\_HTS
    :   Health Thermometer Service.

    BT\_UUID\_DIS\_VAL
    :   Device Information Service UUID value.

    BT\_UUID\_DIS
    :   Device Information Service.

    BT\_UUID\_NAS\_VAL
    :   Network Availability Service UUID value.

    BT\_UUID\_NAS
    :   Network Availability Service.

    BT\_UUID\_WDS\_VAL
    :   Watchdog Service UUID value.

    BT\_UUID\_WDS
    :   Watchdog Service.

    BT\_UUID\_HRS\_VAL
    :   Heart Rate Service UUID value.

    BT\_UUID\_HRS
    :   Heart Rate Service.

    BT\_UUID\_PAS\_VAL
    :   Phone Alert Service UUID value.

    BT\_UUID\_PAS
    :   Phone Alert Service.

    BT\_UUID\_BAS\_VAL
    :   Battery Service UUID value.

    BT\_UUID\_BAS
    :   Battery Service.

    BT\_UUID\_BPS\_VAL
    :   Blood Pressure Service UUID value.

    BT\_UUID\_BPS
    :   Blood Pressure Service.

    BT\_UUID\_ANS\_VAL
    :   Alert Notification Service UUID value.

    BT\_UUID\_ANS
    :   Alert Notification Service.

    BT\_UUID\_HIDS\_VAL
    :   HID Service UUID value.

    BT\_UUID\_HIDS
    :   HID Service.

    BT\_UUID\_SPS\_VAL
    :   Scan Parameters Service UUID value.

    BT\_UUID\_SPS
    :   Scan Parameters Service.

    BT\_UUID\_RSCS\_VAL
    :   Running Speed and Cadence Service UUID value.

    BT\_UUID\_RSCS
    :   Running Speed and Cadence Service.

    BT\_UUID\_AIOS\_VAL
    :   Automation IO Service UUID value.

    BT\_UUID\_AIOS
    :   Automation IO Service.

    BT\_UUID\_CSC\_VAL
    :   Cycling Speed and Cadence Service UUID value.

    BT\_UUID\_CSC
    :   Cycling Speed and Cadence Service.

    BT\_UUID\_CPS\_VAL
    :   Cycling Power Service UUID value.

    BT\_UUID\_CPS
    :   Cycling Power Service.

    BT\_UUID\_LNS\_VAL
    :   Location and Navigation Service UUID value.

    BT\_UUID\_LNS
    :   Location and Navigation Service.

    BT\_UUID\_ESS\_VAL
    :   Environmental Sensing Service UUID value.

    BT\_UUID\_ESS
    :   Environmental Sensing Service.

    BT\_UUID\_BCS\_VAL
    :   Body Composition Service UUID value.

    BT\_UUID\_BCS
    :   Body Composition Service.

    BT\_UUID\_UDS\_VAL
    :   User Data Service UUID value.

    BT\_UUID\_UDS
    :   User Data Service.

    BT\_UUID\_WSS\_VAL
    :   Weight Scale Service UUID value.

    BT\_UUID\_WSS
    :   Weight Scale Service.

    BT\_UUID\_BMS\_VAL
    :   Bond Management Service UUID value.

    BT\_UUID\_BMS
    :   Bond Management Service.

    BT\_UUID\_CGMS\_VAL
    :   Continuous Glucose Monitoring Service UUID value.

    BT\_UUID\_CGMS
    :   Continuous Glucose Monitoring Service.

    BT\_UUID\_IPSS\_VAL
    :   IP Support Service UUID value.

    BT\_UUID\_IPSS
    :   IP Support Service.

    BT\_UUID\_IPS\_VAL
    :   Indoor Positioning Service UUID value.

    BT\_UUID\_IPS
    :   Indoor Positioning Service.

    BT\_UUID\_POS\_VAL
    :   Pulse Oximeter Service UUID value.

    BT\_UUID\_POS
    :   Pulse Oximeter Service.

    BT\_UUID\_HPS\_VAL
    :   HTTP Proxy Service UUID value.

    BT\_UUID\_HPS
    :   HTTP Proxy Service.

    BT\_UUID\_TDS\_VAL
    :   Transport Discovery Service UUID value.

    BT\_UUID\_TDS
    :   Transport Discovery Service.

    BT\_UUID\_OTS\_VAL
    :   Object Transfer Service UUID value.

    BT\_UUID\_OTS
    :   Object Transfer Service.

    BT\_UUID\_FMS\_VAL
    :   Fitness Machine Service UUID value.

    BT\_UUID\_FMS
    :   Fitness Machine Service.

    BT\_UUID\_MESH\_PROV\_VAL
    :   Mesh Provisioning Service UUID value.

    BT\_UUID\_MESH\_PROV
    :   Mesh Provisioning Service.

    BT\_UUID\_MESH\_PROXY\_VAL
    :   Mesh Proxy Service UUID value.

    BT\_UUID\_MESH\_PROXY
    :   Mesh Proxy Service.

    BT\_UUID\_MESH\_PROXY\_SOLICITATION\_VAL
    :   Proxy Solicitation UUID value.

    BT\_UUID\_RCSRV\_VAL
    :   Reconnection Configuration Service UUID value.

    BT\_UUID\_RCSRV
    :   Reconnection Configuration Service.

    BT\_UUID\_IDS\_VAL
    :   Insulin Delivery Service UUID value.

    BT\_UUID\_IDS
    :   Insulin Delivery Service.

    BT\_UUID\_BSS\_VAL
    :   Binary Sensor Service UUID value.

    BT\_UUID\_BSS
    :   Binary Sensor Service.

    BT\_UUID\_ECS\_VAL
    :   Emergency Configuration Service UUID value.

    BT\_UUID\_ECS
    :   Emergency Configuration Service.

    BT\_UUID\_ACLS\_VAL
    :   Authorization Control Service UUID value.

    BT\_UUID\_ACLS
    :   Authorization Control Service.

    BT\_UUID\_PAMS\_VAL
    :   Physical Activity Monitor Service UUID value.

    BT\_UUID\_PAMS
    :   Physical Activity Monitor Service.

    BT\_UUID\_AICS\_VAL
    :   Audio Input Control Service UUID value.

    BT\_UUID\_AICS
    :   Audio Input Control Service.

    BT\_UUID\_VCS\_VAL
    :   Volume Control Service UUID value.

    BT\_UUID\_VCS
    :   Volume Control Service.

    BT\_UUID\_VOCS\_VAL
    :   Volume Offset Control Service UUID value.

    BT\_UUID\_VOCS
    :   Volume Offset Control Service.

    BT\_UUID\_CSIS\_VAL
    :   Coordinated Set Identification Service UUID value.

    BT\_UUID\_CSIS
    :   Coordinated Set Identification Service.

    BT\_UUID\_DTS\_VAL
    :   Device Time Service UUID value.

    BT\_UUID\_DTS
    :   Device Time Service.

    BT\_UUID\_MCS\_VAL
    :   Media Control Service UUID value.

    BT\_UUID\_MCS
    :   Media Control Service.

    BT\_UUID\_GMCS\_VAL
    :   Generic Media Control Service UUID value.

    BT\_UUID\_GMCS
    :   Generic Media Control Service.

    BT\_UUID\_CTES\_VAL
    :   Constant Tone Extension Service UUID value.

    BT\_UUID\_CTES
    :   Constant Tone Extension Service.

    BT\_UUID\_TBS\_VAL
    :   Telephone Bearer Service UUID value.

    BT\_UUID\_TBS
    :   Telephone Bearer Service.

    BT\_UUID\_GTBS\_VAL
    :   Generic Telephone Bearer Service UUID value.

    BT\_UUID\_GTBS
    :   Generic Telephone Bearer Service.

    BT\_UUID\_MICS\_VAL
    :   Microphone Control Service UUID value.

    BT\_UUID\_MICS
    :   Microphone Control Service.

    BT\_UUID\_ASCS\_VAL
    :   Audio Stream Control Service UUID value.

    BT\_UUID\_ASCS
    :   Audio Stream Control Service.

    BT\_UUID\_BASS\_VAL
    :   Broadcast Audio Scan Service UUID value.

    BT\_UUID\_BASS
    :   Broadcast Audio Scan Service.

    BT\_UUID\_PACS\_VAL
    :   Published Audio Capabilities Service UUID value.

    BT\_UUID\_PACS
    :   Published Audio Capabilities Service.

    BT\_UUID\_BASIC\_AUDIO\_VAL
    :   Basic Audio Announcement Service UUID value.

    BT\_UUID\_BASIC\_AUDIO
    :   Basic Audio Announcement Service.

    BT\_UUID\_BROADCAST\_AUDIO\_VAL
    :   Broadcast Audio Announcement Service UUID value.

    BT\_UUID\_BROADCAST\_AUDIO
    :   Broadcast Audio Announcement Service.

    BT\_UUID\_CAS\_VAL
    :   Common Audio Service UUID value.

    BT\_UUID\_CAS
    :   Common Audio Service.

    BT\_UUID\_HAS\_VAL
    :   Hearing Access Service UUID value.

    BT\_UUID\_HAS
    :   Hearing Access Service.

    BT\_UUID\_TMAS\_VAL
    :   Telephony and Media Audio Service UUID value.

    BT\_UUID\_TMAS
    :   Telephony and Media Audio Service.

    BT\_UUID\_PBA\_VAL
    :   Public Broadcast Announcement Service UUID value.

    BT\_UUID\_PBA
    :   Public Broadcast Announcement Service.

    BT\_UUID\_GATT\_PRIMARY\_VAL
    :   GATT Primary Service UUID value.

    BT\_UUID\_GATT\_PRIMARY
    :   GATT Primary Service.

    BT\_UUID\_GATT\_SECONDARY\_VAL
    :   GATT Secondary Service UUID value.

    BT\_UUID\_GATT\_SECONDARY
    :   GATT Secondary Service.

    BT\_UUID\_GATT\_INCLUDE\_VAL
    :   GATT Include Service UUID value.

    BT\_UUID\_GATT\_INCLUDE
    :   GATT Include Service.

    BT\_UUID\_GATT\_CHRC\_VAL
    :   GATT Characteristic UUID value.

    BT\_UUID\_GATT\_CHRC
    :   GATT Characteristic.

    BT\_UUID\_GATT\_CEP\_VAL
    :   GATT Characteristic Extended Properties UUID value.

    BT\_UUID\_GATT\_CEP
    :   GATT Characteristic Extended Properties.

    BT\_UUID\_GATT\_CUD\_VAL
    :   GATT Characteristic User Description UUID value.

    BT\_UUID\_GATT\_CUD
    :   GATT Characteristic User Description.

    BT\_UUID\_GATT\_CCC\_VAL
    :   GATT Client Characteristic Configuration UUID value.

    BT\_UUID\_GATT\_CCC
    :   GATT Client Characteristic Configuration.

    BT\_UUID\_GATT\_SCC\_VAL
    :   GATT Server Characteristic Configuration UUID value.

    BT\_UUID\_GATT\_SCC
    :   GATT Server Characteristic Configuration.

    BT\_UUID\_GATT\_CPF\_VAL
    :   GATT Characteristic Presentation Format UUID value.

    BT\_UUID\_GATT\_CPF
    :   GATT Characteristic Presentation Format.

    BT\_UUID\_GATT\_CAF\_VAL
    :   GATT Characteristic Aggregated Format UUID value.

    BT\_UUID\_GATT\_CAF
    :   GATT Characteristic Aggregated Format.

    BT\_UUID\_VALID\_RANGE\_VAL
    :   Valid Range Descriptor UUID value.

    BT\_UUID\_VALID\_RANGE
    :   Valid Range Descriptor.

    BT\_UUID\_HIDS\_EXT\_REPORT\_VAL
    :   HID External Report Descriptor UUID value.

    BT\_UUID\_HIDS\_EXT\_REPORT
    :   HID External Report Descriptor.

    BT\_UUID\_HIDS\_REPORT\_REF\_VAL
    :   HID Report Reference Descriptor UUID value.

    BT\_UUID\_HIDS\_REPORT\_REF
    :   HID Report Reference Descriptor.

    BT\_UUID\_VAL\_TRIGGER\_SETTING\_VAL
    :   Value Trigger Setting Descriptor UUID value.

    BT\_UUID\_VAL\_TRIGGER\_SETTING
    :   Value Trigger Setting Descriptor.

    BT\_UUID\_ES\_CONFIGURATION\_VAL
    :   Environmental Sensing Configuration Descriptor UUID value.

    BT\_UUID\_ES\_CONFIGURATION
    :   Environmental Sensing Configuration Descriptor.

    BT\_UUID\_ES\_MEASUREMENT\_VAL
    :   Environmental Sensing Measurement Descriptor UUID value.

    BT\_UUID\_ES\_MEASUREMENT
    :   Environmental Sensing Measurement Descriptor.

    BT\_UUID\_ES\_TRIGGER\_SETTING\_VAL
    :   Environmental Sensing Trigger Setting Descriptor UUID value.

    BT\_UUID\_ES\_TRIGGER\_SETTING
    :   Environmental Sensing Trigger Setting Descriptor.

    BT\_UUID\_TM\_TRIGGER\_SETTING\_VAL
    :   Time Trigger Setting Descriptor UUID value.

    BT\_UUID\_TM\_TRIGGER\_SETTING
    :   Time Trigger Setting Descriptor.

    BT\_UUID\_GAP\_DEVICE\_NAME\_VAL
    :   GAP Characteristic Device Name UUID value.

    BT\_UUID\_GAP\_DEVICE\_NAME
    :   GAP Characteristic Device Name.

    BT\_UUID\_GAP\_APPEARANCE\_VAL
    :   GAP Characteristic Appearance UUID value.

    BT\_UUID\_GAP\_APPEARANCE
    :   GAP Characteristic Appearance.

    BT\_UUID\_GAP\_PPF\_VAL
    :   GAP Characteristic Peripheral Privacy Flag UUID value.

    BT\_UUID\_GAP\_PPF
    :   GAP Characteristic Peripheral Privacy Flag.

    BT\_UUID\_GAP\_RA\_VAL
    :   GAP Characteristic Reconnection Address UUID value.

    BT\_UUID\_GAP\_RA
    :   GAP Characteristic Reconnection Address.

    BT\_UUID\_GAP\_PPCP\_VAL
    :   GAP Characteristic Peripheral Preferred Connection Parameters UUID value.

    BT\_UUID\_GAP\_PPCP
    :   GAP Characteristic Peripheral Preferred Connection Parameters.

    BT\_UUID\_GATT\_SC\_VAL
    :   GATT Characteristic Service Changed UUID value.

    BT\_UUID\_GATT\_SC
    :   GATT Characteristic Service Changed.

    BT\_UUID\_ALERT\_LEVEL\_VAL
    :   GATT Characteristic Alert Level UUID value.

    BT\_UUID\_ALERT\_LEVEL
    :   GATT Characteristic Alert Level.

    BT\_UUID\_TPS\_TX\_POWER\_LEVEL\_VAL
    :   TPS Characteristic Tx Power Level UUID value.

    BT\_UUID\_TPS\_TX\_POWER\_LEVEL
    :   TPS Characteristic Tx Power Level.

    BT\_UUID\_GATT\_DT\_VAL
    :   GATT Characteristic Date Time UUID value.

    BT\_UUID\_GATT\_DT
    :   GATT Characteristic Date Time.

    BT\_UUID\_GATT\_DW\_VAL
    :   GATT Characteristic Day of Week UUID value.

    BT\_UUID\_GATT\_DW
    :   GATT Characteristic Day of Week.

    BT\_UUID\_GATT\_DDT\_VAL
    :   GATT Characteristic Day Date Time UUID value.

    BT\_UUID\_GATT\_DDT
    :   GATT Characteristic Day Date Time.

    BT\_UUID\_GATT\_ET256\_VAL
    :   GATT Characteristic Exact Time 256 UUID value.

    BT\_UUID\_GATT\_ET256
    :   GATT Characteristic Exact Time 256.

    BT\_UUID\_GATT\_DST\_VAL
    :   GATT Characteristic DST Offset UUID value.

    BT\_UUID\_GATT\_DST
    :   GATT Characteristic DST Offset.

    BT\_UUID\_GATT\_TZ\_VAL
    :   GATT Characteristic Time Zone UUID value.

    BT\_UUID\_GATT\_TZ
    :   GATT Characteristic Time Zone.

    BT\_UUID\_GATT\_LTI\_VAL
    :   GATT Characteristic Local Time Information UUID value.

    BT\_UUID\_GATT\_LTI
    :   GATT Characteristic Local Time Information.

    BT\_UUID\_GATT\_TDST\_VAL
    :   GATT Characteristic Time with DST UUID value.

    BT\_UUID\_GATT\_TDST
    :   GATT Characteristic Time with DST.

    BT\_UUID\_GATT\_TA\_VAL
    :   GATT Characteristic Time Accuracy UUID value.

    BT\_UUID\_GATT\_TA
    :   GATT Characteristic Time Accuracy.

    BT\_UUID\_GATT\_TS\_VAL
    :   GATT Characteristic Time Source UUID value.

    BT\_UUID\_GATT\_TS
    :   GATT Characteristic Time Source.

    BT\_UUID\_GATT\_RTI\_VAL
    :   GATT Characteristic Reference Time Information UUID value.

    BT\_UUID\_GATT\_RTI
    :   GATT Characteristic Reference Time Information.

    BT\_UUID\_GATT\_TUCP\_VAL
    :   GATT Characteristic Time Update Control Point UUID value.

    BT\_UUID\_GATT\_TUCP
    :   GATT Characteristic Time Update Control Point.

    BT\_UUID\_GATT\_TUS\_VAL
    :   GATT Characteristic Time Update State UUID value.

    BT\_UUID\_GATT\_TUS
    :   GATT Characteristic Time Update State.

    BT\_UUID\_GATT\_GM\_VAL
    :   GATT Characteristic Glucose Measurement UUID value.

    BT\_UUID\_GATT\_GM
    :   GATT Characteristic Glucose Measurement.

    BT\_UUID\_BAS\_BATTERY\_LEVEL\_VAL
    :   BAS Characteristic Battery Level UUID value.

    BT\_UUID\_BAS\_BATTERY\_LEVEL
    :   BAS Characteristic Battery Level.

    BT\_UUID\_BAS\_BATTERY\_POWER\_STATE\_VAL
    :   BAS Characteristic Battery Power State UUID value.

    BT\_UUID\_BAS\_BATTERY\_POWER\_STATE
    :   BAS Characteristic Battery Power State.

    BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE\_VAL
    :   BAS Characteristic Battery Level StateUUID value.

    BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE
    :   BAS Characteristic Battery Level State.

    BT\_UUID\_HTS\_MEASUREMENT\_VAL
    :   HTS Characteristic Temperature Measurement UUID value.

    BT\_UUID\_HTS\_MEASUREMENT
    :   HTS Characteristic Temperature Measurement Value.

    BT\_UUID\_HTS\_TEMP\_TYP\_VAL
    :   HTS Characteristic Temperature Type UUID value.

    BT\_UUID\_HTS\_TEMP\_TYP
    :   HTS Characteristic Temperature Type.

    BT\_UUID\_HTS\_TEMP\_INT\_VAL
    :   HTS Characteristic Intermediate Temperature UUID value.

    BT\_UUID\_HTS\_TEMP\_INT
    :   HTS Characteristic Intermediate Temperature.

    BT\_UUID\_HTS\_TEMP\_C\_VAL
    :   HTS Characteristic Temperature Celsius UUID value.

    BT\_UUID\_HTS\_TEMP\_C
    :   HTS Characteristic Temperature Celsius.

    BT\_UUID\_HTS\_TEMP\_F\_VAL
    :   HTS Characteristic Temperature Fahrenheit UUID value.

    BT\_UUID\_HTS\_TEMP\_F
    :   HTS Characteristic Temperature Fahrenheit.

    BT\_UUID\_HTS\_INTERVAL\_VAL
    :   HTS Characteristic Measurement Interval UUID value.

    BT\_UUID\_HTS\_INTERVAL
    :   HTS Characteristic Measurement Interval.

    BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT\_VAL
    :   HID Characteristic Boot Keyboard Input Report UUID value.

    BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT
    :   HID Characteristic Boot Keyboard Input Report.

    BT\_UUID\_DIS\_SYSTEM\_ID\_VAL
    :   DIS Characteristic System ID UUID value.

    BT\_UUID\_DIS\_SYSTEM\_ID
    :   DIS Characteristic System ID.

    BT\_UUID\_DIS\_MODEL\_NUMBER\_VAL
    :   DIS Characteristic Model Number String UUID value.

    BT\_UUID\_DIS\_MODEL\_NUMBER
    :   DIS Characteristic Model Number String.

    BT\_UUID\_DIS\_SERIAL\_NUMBER\_VAL
    :   DIS Characteristic Serial Number String UUID value.

    BT\_UUID\_DIS\_SERIAL\_NUMBER
    :   DIS Characteristic Serial Number String.

    BT\_UUID\_DIS\_FIRMWARE\_REVISION\_VAL
    :   DIS Characteristic Firmware Revision String UUID value.

    BT\_UUID\_DIS\_FIRMWARE\_REVISION
    :   DIS Characteristic Firmware Revision String.

    BT\_UUID\_DIS\_HARDWARE\_REVISION\_VAL
    :   DIS Characteristic Hardware Revision String UUID value.

    BT\_UUID\_DIS\_HARDWARE\_REVISION
    :   DIS Characteristic Hardware Revision String.

    BT\_UUID\_DIS\_SOFTWARE\_REVISION\_VAL
    :   DIS Characteristic Software Revision String UUID value.

    BT\_UUID\_DIS\_SOFTWARE\_REVISION
    :   DIS Characteristic Software Revision String.

    BT\_UUID\_DIS\_MANUFACTURER\_NAME\_VAL
    :   DIS Characteristic Manufacturer Name String UUID Value.

    BT\_UUID\_DIS\_MANUFACTURER\_NAME
    :   DIS Characteristic Manufacturer Name String.

    BT\_UUID\_GATT\_IEEE\_RCDL\_VAL
    :   GATT Characteristic IEEE Regulatory Certification Data List UUID Value.

    BT\_UUID\_GATT\_IEEE\_RCDL
    :   GATT Characteristic IEEE Regulatory Certification Data List.

    BT\_UUID\_CTS\_CURRENT\_TIME\_VAL
    :   CTS Characteristic Current Time UUID value.

    BT\_UUID\_CTS\_CURRENT\_TIME
    :   CTS Characteristic Current Time.

    BT\_UUID\_MAGN\_DECLINATION\_VAL
    :   Magnetic Declination Characteristic UUID value.

    BT\_UUID\_MAGN\_DECLINATION
    :   Magnetic Declination Characteristic.

    BT\_UUID\_GATT\_LLAT\_VAL
    :   GATT Characteristic Legacy Latitude UUID Value.

    BT\_UUID\_GATT\_LLAT
    :   GATT Characteristic Legacy Latitude.

    BT\_UUID\_GATT\_LLON\_VAL
    :   GATT Characteristic Legacy Longitude UUID Value.

    BT\_UUID\_GATT\_LLON
    :   GATT Characteristic Legacy Longitude.

    BT\_UUID\_GATT\_POS\_2D\_VAL
    :   GATT Characteristic Position 2D UUID Value.

    BT\_UUID\_GATT\_POS\_2D
    :   GATT Characteristic Position 2D.

    BT\_UUID\_GATT\_POS\_3D\_VAL
    :   GATT Characteristic Position 3D UUID Value.

    BT\_UUID\_GATT\_POS\_3D
    :   GATT Characteristic Position 3D.

    BT\_UUID\_GATT\_SR\_VAL
    :   GATT Characteristic Scan Refresh UUID Value.

    BT\_UUID\_GATT\_SR
    :   GATT Characteristic Scan Refresh.

    BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT\_VAL
    :   HID Boot Keyboard Output Report Characteristic UUID value.

    BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT
    :   HID Boot Keyboard Output Report Characteristic.

    BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT\_VAL
    :   HID Boot Mouse Input Report Characteristic UUID value.

    BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT
    :   HID Boot Mouse Input Report Characteristic.

    BT\_UUID\_GATT\_GMC\_VAL
    :   GATT Characteristic Glucose Measurement Context UUID Value.

    BT\_UUID\_GATT\_GMC
    :   GATT Characteristic Glucose Measurement Context.

    BT\_UUID\_GATT\_BPM\_VAL
    :   GATT Characteristic Blood Pressure Measurement UUID Value.

    BT\_UUID\_GATT\_BPM
    :   GATT Characteristic Blood Pressure Measurement.

    BT\_UUID\_GATT\_ICP\_VAL
    :   GATT Characteristic Intermediate Cuff Pressure UUID Value.

    BT\_UUID\_GATT\_ICP
    :   GATT Characteristic Intermediate Cuff Pressure.

    BT\_UUID\_HRS\_MEASUREMENT\_VAL
    :   HRS Characteristic Measurement Interval UUID value.

    BT\_UUID\_HRS\_MEASUREMENT
    :   HRS Characteristic Measurement Interval.

    BT\_UUID\_HRS\_BODY\_SENSOR\_VAL
    :   HRS Characteristic Body Sensor Location.

    BT\_UUID\_HRS\_BODY\_SENSOR
    :   HRS Characteristic Control Point.

    BT\_UUID\_HRS\_CONTROL\_POINT\_VAL
    :   HRS Characteristic Control Point UUID value.

    BT\_UUID\_HRS\_CONTROL\_POINT
    :   HRS Characteristic Control Point.

    BT\_UUID\_GATT\_REM\_VAL
    :   GATT Characteristic Removable UUID Value.

    BT\_UUID\_GATT\_REM
    :   GATT Characteristic Removable.

    BT\_UUID\_GATT\_SRVREQ\_VAL
    :   GATT Characteristic Service Required UUID Value.

    BT\_UUID\_GATT\_SRVREQ
    :   GATT Characteristic Service Required.

    BT\_UUID\_GATT\_SC\_TEMP\_C\_VAL
    :   GATT Characteristic Scientific Temperature in Celsius UUID Value.

    BT\_UUID\_GATT\_SC\_TEMP\_C
    :   GATT Characteristic Scientific Temperature in Celsius.

    BT\_UUID\_GATT\_STRING\_VAL
    :   GATT Characteristic String UUID Value.

    BT\_UUID\_GATT\_STRING
    :   GATT Characteristic String.

    BT\_UUID\_GATT\_NETA\_VAL
    :   GATT Characteristic Network Availability UUID Value.

    BT\_UUID\_GATT\_NETA
    :   GATT Characteristic Network Availability.

    BT\_UUID\_GATT\_ALRTS\_VAL
    :   GATT Characteristic Alert Status UUID Value.

    BT\_UUID\_GATT\_ALRTS
    :   GATT Characteristic Alert Status.

    BT\_UUID\_GATT\_RCP\_VAL
    :   GATT Characteristic Ringer Control Point UUID Value.

    BT\_UUID\_GATT\_RCP
    :   GATT Characteristic Ringer Control Point.

    BT\_UUID\_GATT\_RS\_VAL
    :   GATT Characteristic Ringer Setting UUID Value.

    BT\_UUID\_GATT\_RS
    :   GATT Characteristic Ringer Setting.

    BT\_UUID\_GATT\_ALRTCID\_MASK\_VAL
    :   GATT Characteristic Alert Category ID Bit Mask UUID Value.

    BT\_UUID\_GATT\_ALRTCID\_MASK
    :   GATT Characteristic Alert Category ID Bit Mask.

    BT\_UUID\_GATT\_ALRTCID\_VAL
    :   GATT Characteristic Alert Category ID UUID Value.

    BT\_UUID\_GATT\_ALRTCID
    :   GATT Characteristic Alert Category ID.

    BT\_UUID\_GATT\_ALRTNCP\_VAL
    :   GATT Characteristic Alert Notification Control Point Value.

    BT\_UUID\_GATT\_ALRTNCP
    :   GATT Characteristic Alert Notification Control Point.

    BT\_UUID\_GATT\_UALRTS\_VAL
    :   GATT Characteristic Unread Alert Status UUID Value.

    BT\_UUID\_GATT\_UALRTS
    :   GATT Characteristic Unread Alert Status.

    BT\_UUID\_GATT\_NALRT\_VAL
    :   GATT Characteristic New Alert UUID Value.

    BT\_UUID\_GATT\_NALRT
    :   GATT Characteristic New Alert.

    BT\_UUID\_GATT\_SNALRTC\_VAL
    :   GATT Characteristic Supported New Alert Category UUID Value.

    BT\_UUID\_GATT\_SNALRTC
    :   GATT Characteristic Supported New Alert Category.

    BT\_UUID\_GATT\_SUALRTC\_VAL
    :   GATT Characteristic Supported Unread Alert Category UUID Value.

    BT\_UUID\_GATT\_SUALRTC
    :   GATT Characteristic Supported Unread Alert Category.

    BT\_UUID\_GATT\_BPF\_VAL
    :   GATT Characteristic Blood Pressure Feature UUID Value.

    BT\_UUID\_GATT\_BPF
    :   GATT Characteristic Blood Pressure Feature.

    BT\_UUID\_HIDS\_INFO\_VAL
    :   HID Information Characteristic UUID value.

    BT\_UUID\_HIDS\_INFO
    :   HID Information Characteristic.

    BT\_UUID\_HIDS\_REPORT\_MAP\_VAL
    :   HID Report Map Characteristic UUID value.

    BT\_UUID\_HIDS\_REPORT\_MAP
    :   HID Report Map Characteristic.

    BT\_UUID\_HIDS\_CTRL\_POINT\_VAL
    :   HID Control Point Characteristic UUID value.

    BT\_UUID\_HIDS\_CTRL\_POINT
    :   HID Control Point Characteristic.

    BT\_UUID\_HIDS\_REPORT\_VAL
    :   HID Report Characteristic UUID value.

    BT\_UUID\_HIDS\_REPORT
    :   HID Report Characteristic.

    BT\_UUID\_HIDS\_PROTOCOL\_MODE\_VAL
    :   HID Protocol Mode Characteristic UUID value.

    BT\_UUID\_HIDS\_PROTOCOL\_MODE
    :   HID Protocol Mode Characteristic.

    BT\_UUID\_GATT\_SIW\_VAL
    :   GATT Characteristic Scan Interval Windows UUID Value.

    BT\_UUID\_GATT\_SIW
    :   GATT Characteristic Scan Interval Windows.

    BT\_UUID\_DIS\_PNP\_ID\_VAL
    :   DIS Characteristic PnP ID UUID value.

    BT\_UUID\_DIS\_PNP\_ID
    :   DIS Characteristic PnP ID.

    BT\_UUID\_GATT\_GF\_VAL
    :   GATT Characteristic Glucose Feature UUID Value.

    BT\_UUID\_GATT\_GF
    :   GATT Characteristic Glucose Feature.

    BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT\_VAL
    :   Record Access Control Point Characteristic value.

    BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT
    :   Record Access Control Point.

    BT\_UUID\_RSC\_MEASUREMENT\_VAL
    :   RSC Measurement Characteristic UUID value.

    BT\_UUID\_RSC\_MEASUREMENT
    :   RSC Measurement Characteristic.

    BT\_UUID\_RSC\_FEATURE\_VAL
    :   RSC Feature Characteristic UUID value.

    BT\_UUID\_RSC\_FEATURE
    :   RSC Feature Characteristic.

    BT\_UUID\_SC\_CONTROL\_POINT\_VAL
    :   SC Control Point Characteristic UUID value.

    BT\_UUID\_SC\_CONTROL\_POINT
    :   SC Control Point Characteristic.

    BT\_UUID\_GATT\_DI\_VAL
    :   GATT Characteristic Digital Input UUID Value.

    BT\_UUID\_GATT\_DI
    :   GATT Characteristic Digital Input.

    BT\_UUID\_GATT\_DO\_VAL
    :   GATT Characteristic Digital Output UUID Value.

    BT\_UUID\_GATT\_DO
    :   GATT Characteristic Digital Output.

    BT\_UUID\_GATT\_AI\_VAL
    :   GATT Characteristic Analog Input UUID Value.

    BT\_UUID\_GATT\_AI
    :   GATT Characteristic Analog Input.

    BT\_UUID\_GATT\_AO\_VAL
    :   GATT Characteristic Analog Output UUID Value.

    BT\_UUID\_GATT\_AO
    :   GATT Characteristic Analog Output.

    BT\_UUID\_GATT\_AGGR\_VAL
    :   GATT Characteristic Aggregate UUID Value.

    BT\_UUID\_GATT\_AGGR
    :   GATT Characteristic Aggregate.

    BT\_UUID\_CSC\_MEASUREMENT\_VAL
    :   CSC Measurement Characteristic UUID value.

    BT\_UUID\_CSC\_MEASUREMENT
    :   CSC Measurement Characteristic.

    BT\_UUID\_CSC\_FEATURE\_VAL
    :   CSC Feature Characteristic UUID value.

    BT\_UUID\_CSC\_FEATURE
    :   CSC Feature Characteristic.

    BT\_UUID\_SENSOR\_LOCATION\_VAL
    :   Sensor Location Characteristic UUID value.

    BT\_UUID\_SENSOR\_LOCATION
    :   Sensor Location Characteristic.

    BT\_UUID\_GATT\_PLX\_SCM\_VAL
    :   GATT Characteristic PLX Spot-Check Measurement UUID Value.

    BT\_UUID\_GATT\_PLX\_SCM
    :   GATT Characteristic PLX Spot-Check Measurement.

    BT\_UUID\_GATT\_PLX\_CM\_VAL
    :   GATT Characteristic PLX Continuous Measurement UUID Value.

    BT\_UUID\_GATT\_PLX\_CM
    :   GATT Characteristic PLX Continuous Measurement.

    BT\_UUID\_GATT\_PLX\_F\_VAL
    :   GATT Characteristic PLX Features UUID Value.

    BT\_UUID\_GATT\_PLX\_F
    :   GATT Characteristic PLX Features.

    BT\_UUID\_GATT\_POPE\_VAL
    :   GATT Characteristic Pulse Oximetry Pulastile Event UUID Value.

    BT\_UUID\_GATT\_POPE
    :   GATT Characteristic Pulse Oximetry Pulsatile Event.

    BT\_UUID\_GATT\_POCP\_VAL
    :   GATT Characteristic Pulse Oximetry Control Point UUID Value.

    BT\_UUID\_GATT\_POCP
    :   GATT Characteristic Pulse Oximetry Control Point.

    BT\_UUID\_GATT\_CPS\_CPM\_VAL
    :   GATT Characteristic Cycling Power Measurement UUID Value.

    BT\_UUID\_GATT\_CPS\_CPM
    :   GATT Characteristic Cycling Power Measurement.

    BT\_UUID\_GATT\_CPS\_CPV\_VAL
    :   GATT Characteristic Cycling Power Vector UUID Value.

    BT\_UUID\_GATT\_CPS\_CPV
    :   GATT Characteristic Cycling Power Vector.

    BT\_UUID\_GATT\_CPS\_CPF\_VAL
    :   GATT Characteristic Cycling Power Feature UUID Value.

    BT\_UUID\_GATT\_CPS\_CPF
    :   GATT Characteristic Cycling Power Feature.

    BT\_UUID\_GATT\_CPS\_CPCP\_VAL
    :   GATT Characteristic Cycling Power Control Point UUID Value.

    BT\_UUID\_GATT\_CPS\_CPCP
    :   GATT Characteristic Cycling Power Control Point.

    BT\_UUID\_GATT\_LOC\_SPD\_VAL
    :   GATT Characteristic Location and Speed UUID Value.

    BT\_UUID\_GATT\_LOC\_SPD
    :   GATT Characteristic Location and Speed.

    BT\_UUID\_GATT\_NAV\_VAL
    :   GATT Characteristic Navigation UUID Value.

    BT\_UUID\_GATT\_NAV
    :   GATT Characteristic Navigation.

    BT\_UUID\_GATT\_PQ\_VAL
    :   GATT Characteristic Position Quality UUID Value.

    BT\_UUID\_GATT\_PQ
    :   GATT Characteristic Position Quality.

    BT\_UUID\_GATT\_LNF\_VAL
    :   GATT Characteristic LN Feature UUID Value.

    BT\_UUID\_GATT\_LNF
    :   GATT Characteristic LN Feature.

    BT\_UUID\_GATT\_LNCP\_VAL
    :   GATT Characteristic LN Control Point UUID Value.

    BT\_UUID\_GATT\_LNCP
    :   GATT Characteristic LN Control Point.

    BT\_UUID\_ELEVATION\_VAL
    :   Elevation Characteristic UUID value.

    BT\_UUID\_ELEVATION
    :   Elevation Characteristic.

    BT\_UUID\_PRESSURE\_VAL
    :   Pressure Characteristic UUID value.

    BT\_UUID\_PRESSURE
    :   Pressure Characteristic.

    BT\_UUID\_TEMPERATURE\_VAL
    :   Temperature Characteristic UUID value.

    BT\_UUID\_TEMPERATURE
    :   Temperature Characteristic.

    BT\_UUID\_HUMIDITY\_VAL
    :   Humidity Characteristic UUID value.

    BT\_UUID\_HUMIDITY
    :   Humidity Characteristic.

    BT\_UUID\_TRUE\_WIND\_SPEED\_VAL
    :   True Wind Speed Characteristic UUID value.

    BT\_UUID\_TRUE\_WIND\_SPEED
    :   True Wind Speed Characteristic.

    BT\_UUID\_TRUE\_WIND\_DIR\_VAL
    :   True Wind Direction Characteristic UUID value.

    BT\_UUID\_TRUE\_WIND\_DIR
    :   True Wind Direction Characteristic.

    BT\_UUID\_APPARENT\_WIND\_SPEED\_VAL
    :   Apparent Wind Speed Characteristic UUID value.

    BT\_UUID\_APPARENT\_WIND\_SPEED
    :   Apparent Wind Speed Characteristic.

    BT\_UUID\_APPARENT\_WIND\_DIR\_VAL
    :   Apparent Wind Direction Characteristic UUID value.

    BT\_UUID\_APPARENT\_WIND\_DIR
    :   Apparent Wind Direction Characteristic.

    BT\_UUID\_GUST\_FACTOR\_VAL
    :   Gust Factor Characteristic UUID value.

    BT\_UUID\_GUST\_FACTOR
    :   Gust Factor Characteristic.

    BT\_UUID\_POLLEN\_CONCENTRATION\_VAL
    :   Pollen Concentration Characteristic UUID value.

    BT\_UUID\_POLLEN\_CONCENTRATION
    :   Pollen Concentration Characteristic.

    BT\_UUID\_UV\_INDEX\_VAL
    :   UV Index Characteristic UUID value.

    BT\_UUID\_UV\_INDEX
    :   UV Index Characteristic.

    BT\_UUID\_IRRADIANCE\_VAL
    :   Irradiance Characteristic UUID value.

    BT\_UUID\_IRRADIANCE
    :   Irradiance Characteristic.

    BT\_UUID\_RAINFALL\_VAL
    :   Rainfall Characteristic UUID value.

    BT\_UUID\_RAINFALL
    :   Rainfall Characteristic.

    BT\_UUID\_WIND\_CHILL\_VAL
    :   Wind Chill Characteristic UUID value.

    BT\_UUID\_WIND\_CHILL
    :   Wind Chill Characteristic.

    BT\_UUID\_HEAT\_INDEX\_VAL
    :   Heat Index Characteristic UUID value.

    BT\_UUID\_HEAT\_INDEX
    :   Heat Index Characteristic.

    BT\_UUID\_DEW\_POINT\_VAL
    :   Dew Point Characteristic UUID value.

    BT\_UUID\_DEW\_POINT
    :   Dew Point Characteristic.

    BT\_UUID\_GATT\_TREND\_VAL
    :   GATT Characteristic Trend UUID Value.

    BT\_UUID\_GATT\_TREND
    :   GATT Characteristic Trend.

    BT\_UUID\_DESC\_VALUE\_CHANGED\_VAL
    :   Descriptor Value Changed Characteristic UUID value.

    BT\_UUID\_DESC\_VALUE\_CHANGED
    :   Descriptor Value Changed Characteristic.

    BT\_UUID\_GATT\_AEHRLL\_VAL
    :   GATT Characteristic Aerobic Heart Rate Low Limit UUID Value.

    BT\_UUID\_GATT\_AEHRLL
    :   GATT Characteristic Aerobic Heart Rate Lower Limit.

    BT\_UUID\_GATT\_AETHR\_VAL
    :   GATT Characteristic Aerobic Threshold UUID Value.

    BT\_UUID\_GATT\_AETHR
    :   GATT Characteristic Aerobic Threshold.

    BT\_UUID\_GATT\_AGE\_VAL
    :   GATT Characteristic Age UUID Value.

    BT\_UUID\_GATT\_AGE
    :   GATT Characteristic Age.

    BT\_UUID\_GATT\_ANHRLL\_VAL
    :   GATT Characteristic Anaerobic Heart Rate Lower Limit UUID Value.

    BT\_UUID\_GATT\_ANHRLL
    :   GATT Characteristic Anaerobic Heart Rate Lower Limit.

    BT\_UUID\_GATT\_ANHRUL\_VAL
    :   GATT Characteristic Anaerobic Heart Rate Upper Limit UUID Value.

    BT\_UUID\_GATT\_ANHRUL
    :   GATT Characteristic Anaerobic Heart Rate Upper Limit.

    BT\_UUID\_GATT\_ANTHR\_VAL
    :   GATT Characteristic Anaerobic Threshold UUID Value.

    BT\_UUID\_GATT\_ANTHR
    :   GATT Characteristic Anaerobic Threshold.

    BT\_UUID\_GATT\_AEHRUL\_VAL
    :   GATT Characteristic Aerobic Heart Rate Upper Limit UUID Value.

    BT\_UUID\_GATT\_AEHRUL
    :   GATT Characteristic Aerobic Heart Rate Upper Limit.

    BT\_UUID\_GATT\_DATE\_BIRTH\_VAL
    :   GATT Characteristic Date of Birth UUID Value.

    BT\_UUID\_GATT\_DATE\_BIRTH
    :   GATT Characteristic Date of Birth.

    BT\_UUID\_GATT\_DATE\_THRASS\_VAL
    :   GATT Characteristic Date of Threshold Assessment UUID Value.

    BT\_UUID\_GATT\_DATE\_THRASS
    :   GATT Characteristic Date of Threshold Assessment.

    BT\_UUID\_GATT\_EMAIL\_VAL
    :   GATT Characteristic Email Address UUID Value.

    BT\_UUID\_GATT\_EMAIL
    :   GATT Characteristic Email Address.

    BT\_UUID\_GATT\_FBHRLL\_VAL
    :   GATT Characteristic Fat Burn Heart Rate Lower Limit UUID Value.

    BT\_UUID\_GATT\_FBHRLL
    :   GATT Characteristic Fat Burn Heart Rate Lower Limit.

    BT\_UUID\_GATT\_FBHRUL\_VAL
    :   GATT Characteristic Fat Burn Heart Rate Upper Limit UUID Value.

    BT\_UUID\_GATT\_FBHRUL
    :   GATT Characteristic Fat Burn Heart Rate Upper Limit.

    BT\_UUID\_GATT\_FIRST\_NAME\_VAL
    :   GATT Characteristic First Name UUID Value.

    BT\_UUID\_GATT\_FIRST\_NAME
    :   GATT Characteristic First Name.

    BT\_UUID\_GATT\_5ZHRL\_VAL
    :   GATT Characteristic Five Zone Heart Rate Limits UUID Value.

    BT\_UUID\_GATT\_5ZHRL
    :   GATT Characteristic Five Zone Heart Rate Limits.

    BT\_UUID\_GATT\_GENDER\_VAL
    :   GATT Characteristic Gender UUID Value.

    BT\_UUID\_GATT\_GENDER
    :   GATT Characteristic Gender.

    BT\_UUID\_GATT\_HR\_MAX\_VAL
    :   GATT Characteristic Heart Rate Max UUID Value.

    BT\_UUID\_GATT\_HR\_MAX
    :   GATT Characteristic Heart Rate Max.

    BT\_UUID\_GATT\_HEIGHT\_VAL
    :   GATT Characteristic Height UUID Value.

    BT\_UUID\_GATT\_HEIGHT
    :   GATT Characteristic Height.

    BT\_UUID\_GATT\_HC\_VAL
    :   GATT Characteristic Hip Circumference UUID Value.

    BT\_UUID\_GATT\_HC
    :   GATT Characteristic Hip Circumference.

    BT\_UUID\_GATT\_LAST\_NAME\_VAL
    :   GATT Characteristic Last Name UUID Value.

    BT\_UUID\_GATT\_LAST\_NAME
    :   GATT Characteristic Last Name.

    BT\_UUID\_GATT\_MRHR\_VAL
    :   GATT Characteristic Maximum Recommended Heart Rate> UUID Value.

    BT\_UUID\_GATT\_MRHR
    :   GATT Characteristic Maximum Recommended Heart Rate.

    BT\_UUID\_GATT\_RHR\_VAL
    :   GATT Characteristic Resting Heart Rate UUID Value.

    BT\_UUID\_GATT\_RHR
    :   GATT Characteristic Resting Heart Rate.

    BT\_UUID\_GATT\_AEANTHR\_VAL
    :   GATT Characteristic Sport Type for Aerobic and Anaerobic Thresholds UUID Value.

    BT\_UUID\_GATT\_AEANTHR
    :   GATT Characteristic Sport Type for Aerobic and Anaerobic Threshold.

    BT\_UUID\_GATT\_3ZHRL\_VAL
    :   GATT Characteristic Three Zone Heart Rate Limits UUID Value.

    BT\_UUID\_GATT\_3ZHRL
    :   GATT Characteristic Three Zone Heart Rate Limits.

    BT\_UUID\_GATT\_2ZHRL\_VAL
    :   GATT Characteristic Two Zone Heart Rate Limits UUID Value.

    BT\_UUID\_GATT\_2ZHRL
    :   GATT Characteristic Two Zone Heart Rate Limits.

    BT\_UUID\_GATT\_VO2\_MAX\_VAL
    :   GATT Characteristic VO2 Max UUID Value.

    BT\_UUID\_GATT\_VO2\_MAX
    :   GATT Characteristic VO2 Max.

    BT\_UUID\_GATT\_WC\_VAL
    :   GATT Characteristic Waist Circumference UUID Value.

    BT\_UUID\_GATT\_WC
    :   GATT Characteristic Waist Circumference.

    BT\_UUID\_GATT\_WEIGHT\_VAL
    :   GATT Characteristic Weight UUID Value.

    BT\_UUID\_GATT\_WEIGHT
    :   GATT Characteristic Weight.

    BT\_UUID\_GATT\_DBCHINC\_VAL
    :   GATT Characteristic Database Change Increment UUID Value.

    BT\_UUID\_GATT\_DBCHINC
    :   GATT Characteristic Database Change Increment.

    BT\_UUID\_GATT\_USRIDX\_VAL
    :   GATT Characteristic User Index UUID Value.

    BT\_UUID\_GATT\_USRIDX
    :   GATT Characteristic User Index.

    BT\_UUID\_GATT\_BCF\_VAL
    :   GATT Characteristic Body Composition Feature UUID Value.

    BT\_UUID\_GATT\_BCF
    :   GATT Characteristic Body Composition Feature.

    BT\_UUID\_GATT\_BCM\_VAL
    :   GATT Characteristic Body Composition Measurement UUID Value.

    BT\_UUID\_GATT\_BCM
    :   GATT Characteristic Body Composition Measurement.

    BT\_UUID\_GATT\_WM\_VAL
    :   GATT Characteristic Weight Measurement UUID Value.

    BT\_UUID\_GATT\_WM
    :   GATT Characteristic Weight Measurement.

    BT\_UUID\_GATT\_WSF\_VAL
    :   GATT Characteristic Weight Scale Feature UUID Value.

    BT\_UUID\_GATT\_WSF
    :   GATT Characteristic Weight Scale Feature.

    BT\_UUID\_GATT\_USRCP\_VAL
    :   GATT Characteristic User Control Point UUID Value.

    BT\_UUID\_GATT\_USRCP
    :   GATT Characteristic User Control Point.

    BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D\_VAL
    :   Magnetic Flux Density - 2D Characteristic UUID value.

    BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D
    :   Magnetic Flux Density - 2D Characteristic.

    BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D\_VAL
    :   Magnetic Flux Density - 3D Characteristic UUID value.

    BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D
    :   Magnetic Flux Density - 3D Characteristic.

    BT\_UUID\_GATT\_LANG\_VAL
    :   GATT Characteristic Language UUID Value.

    BT\_UUID\_GATT\_LANG
    :   GATT Characteristic Language.

    BT\_UUID\_BAR\_PRESSURE\_TREND\_VAL
    :   Barometric Pressure Trend Characteristic UUID value.

    BT\_UUID\_BAR\_PRESSURE\_TREND
    :   Barometric Pressure Trend Characteristic.

    BT\_UUID\_BMS\_CONTROL\_POINT\_VAL
    :   Bond Management Control Point UUID value.

    BT\_UUID\_BMS\_CONTROL\_POINT
    :   Bond Management Control Point.

    BT\_UUID\_BMS\_FEATURE\_VAL
    :   Bond Management Feature UUID value.

    BT\_UUID\_BMS\_FEATURE
    :   Bond Management Feature.

    BT\_UUID\_CENTRAL\_ADDR\_RES\_VAL
    :   Central Address Resolution Characteristic UUID value.

    BT\_UUID\_CENTRAL\_ADDR\_RES
    :   Central Address Resolution Characteristic.

    BT\_UUID\_CGM\_MEASUREMENT\_VAL
    :   CGM Measurement Characteristic value.

    BT\_UUID\_CGM\_MEASUREMENT
    :   CGM Measurement Characteristic.

    BT\_UUID\_CGM\_FEATURE\_VAL
    :   CGM Feature Characteristic value.

    BT\_UUID\_CGM\_FEATURE
    :   CGM Feature Characteristic.

    BT\_UUID\_CGM\_STATUS\_VAL
    :   CGM Status Characteristic value.

    BT\_UUID\_CGM\_STATUS
    :   CGM Status Characteristic.

    BT\_UUID\_CGM\_SESSION\_START\_TIME\_VAL
    :   CGM Session Start Time Characteristic value.

    BT\_UUID\_CGM\_SESSION\_START\_TIME
    :   CGM Session Start Time.

    BT\_UUID\_CGM\_SESSION\_RUN\_TIME\_VAL
    :   CGM Session Run Time Characteristic value.

    BT\_UUID\_CGM\_SESSION\_RUN\_TIME
    :   CGM Session Run Time.

    BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT\_VAL
    :   CGM Specific Ops Control Point Characteristic value.

    BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT
    :   CGM Specific Ops Control Point.

    BT\_UUID\_GATT\_IPC\_VAL
    :   GATT Characteristic Indoor Positioning Configuration UUID Value.

    BT\_UUID\_GATT\_IPC
    :   GATT Characteristic Indoor Positioning Configuration.

    BT\_UUID\_GATT\_LAT\_VAL
    :   GATT Characteristic Latitude UUID Value.

    BT\_UUID\_GATT\_LAT
    :   GATT Characteristic Latitude.

    BT\_UUID\_GATT\_LON\_VAL
    :   GATT Characteristic Longitude UUID Value.

    BT\_UUID\_GATT\_LON
    :   GATT Characteristic Longitude.

    BT\_UUID\_GATT\_LNCOORD\_VAL
    :   GATT Characteristic Local North Coordinate UUID Value.

    BT\_UUID\_GATT\_LNCOORD
    :   GATT Characteristic Local North Coordinate.

    BT\_UUID\_GATT\_LECOORD\_VAL
    :   GATT Characteristic Local East Coordinate UUID Value.

    BT\_UUID\_GATT\_LECOORD
    :   GATT Characteristic Local East Coordinate.

    BT\_UUID\_GATT\_FN\_VAL
    :   GATT Characteristic Floor Number UUID Value.

    BT\_UUID\_GATT\_FN
    :   GATT Characteristic Floor Number.

    BT\_UUID\_GATT\_ALT\_VAL
    :   GATT Characteristic Altitude UUID Value.

    BT\_UUID\_GATT\_ALT
    :   GATT Characteristic Altitude.

    BT\_UUID\_GATT\_UNCERTAINTY\_VAL
    :   GATT Characteristic Uncertainty UUID Value.

    BT\_UUID\_GATT\_UNCERTAINTY
    :   GATT Characteristic Uncertainty.

    BT\_UUID\_GATT\_LOC\_NAME\_VAL
    :   GATT Characteristic Location Name UUID Value.

    BT\_UUID\_GATT\_LOC\_NAME
    :   GATT Characteristic Location Name.

    BT\_UUID\_URI\_VAL
    :   URI UUID value.

    BT\_UUID\_URI
    :   URI.

    BT\_UUID\_HTTP\_HEADERS\_VAL
    :   HTTP Headers UUID value.

    BT\_UUID\_HTTP\_HEADERS
    :   HTTP Headers.

    BT\_UUID\_HTTP\_STATUS\_CODE\_VAL
    :   HTTP Status Code UUID value.

    BT\_UUID\_HTTP\_STATUS\_CODE
    :   HTTP Status Code.

    BT\_UUID\_HTTP\_ENTITY\_BODY\_VAL
    :   HTTP Entity Body UUID value.

    BT\_UUID\_HTTP\_ENTITY\_BODY
    :   HTTP Entity Body.

    BT\_UUID\_HTTP\_CONTROL\_POINT\_VAL
    :   HTTP Control Point UUID value.

    BT\_UUID\_HTTP\_CONTROL\_POINT
    :   HTTP Control Point.

    BT\_UUID\_HTTPS\_SECURITY\_VAL
    :   HTTPS Security UUID value.

    BT\_UUID\_HTTPS\_SECURITY
    :   HTTPS Security.

    BT\_UUID\_GATT\_TDS\_CP\_VAL
    :   GATT Characteristic TDS Control Point UUID Value.

    BT\_UUID\_GATT\_TDS\_CP
    :   GATT Characteristic TDS Control Point.

    BT\_UUID\_OTS\_FEATURE\_VAL
    :   OTS Feature Characteristic UUID value.

    BT\_UUID\_OTS\_FEATURE
    :   OTS Feature Characteristic.

    BT\_UUID\_OTS\_NAME\_VAL
    :   OTS Object Name Characteristic UUID value.

    BT\_UUID\_OTS\_NAME
    :   OTS Object Name Characteristic.

    BT\_UUID\_OTS\_TYPE\_VAL
    :   OTS Object Type Characteristic UUID value.

    BT\_UUID\_OTS\_TYPE
    :   OTS Object Type Characteristic.

    BT\_UUID\_OTS\_SIZE\_VAL
    :   OTS Object Size Characteristic UUID value.

    BT\_UUID\_OTS\_SIZE
    :   OTS Object Size Characteristic.

    BT\_UUID\_OTS\_FIRST\_CREATED\_VAL
    :   OTS Object First-Created Characteristic UUID value.

    BT\_UUID\_OTS\_FIRST\_CREATED
    :   OTS Object First-Created Characteristic.

    BT\_UUID\_OTS\_LAST\_MODIFIED\_VAL
    :   OTS Object Last-Modified Characteristic UUI value.

    BT\_UUID\_OTS\_LAST\_MODIFIED
    :   OTS Object Last-Modified Characteristic.

    BT\_UUID\_OTS\_ID\_VAL
    :   OTS Object ID Characteristic UUID value.

    BT\_UUID\_OTS\_ID
    :   OTS Object ID Characteristic.

    BT\_UUID\_OTS\_PROPERTIES\_VAL
    :   OTS Object Properties Characteristic UUID value.

    BT\_UUID\_OTS\_PROPERTIES
    :   OTS Object Properties Characteristic.

    BT\_UUID\_OTS\_ACTION\_CP\_VAL
    :   OTS Object Action Control Point Characteristic UUID value.

    BT\_UUID\_OTS\_ACTION\_CP
    :   OTS Object Action Control Point Characteristic.

    BT\_UUID\_OTS\_LIST\_CP\_VAL
    :   OTS Object List Control Point Characteristic UUID value.

    BT\_UUID\_OTS\_LIST\_CP
    :   OTS Object List Control Point Characteristic.

    BT\_UUID\_OTS\_LIST\_FILTER\_VAL
    :   OTS Object List Filter Characteristic UUID value.

    BT\_UUID\_OTS\_LIST\_FILTER
    :   OTS Object List Filter Characteristic.

    BT\_UUID\_OTS\_CHANGED\_VAL
    :   OTS Object Changed Characteristic UUID value.

    BT\_UUID\_OTS\_CHANGED
    :   OTS Object Changed Characteristic.

    BT\_UUID\_GATT\_RPAO\_VAL
    :   GATT Characteristic Resolvable Private Address Only UUID Value.

    BT\_UUID\_GATT\_RPAO
    :   GATT Characteristic Resolvable Private Address Only.

    BT\_UUID\_OTS\_TYPE\_UNSPECIFIED\_VAL
    :   OTS Unspecified Object Type UUID value.

    BT\_UUID\_OTS\_TYPE\_UNSPECIFIED
    :   OTS Unspecified Object Type.

    BT\_UUID\_OTS\_DIRECTORY\_LISTING\_VAL
    :   OTS Directory Listing UUID value.

    BT\_UUID\_OTS\_DIRECTORY\_LISTING
    :   OTS Directory Listing.

    BT\_UUID\_GATT\_FMF\_VAL
    :   GATT Characteristic Fitness Machine Feature UUID Value.

    BT\_UUID\_GATT\_FMF
    :   GATT Characteristic Fitness Machine Feature.

    BT\_UUID\_GATT\_TD\_VAL
    :   GATT Characteristic Treadmill Data UUID Value.

    BT\_UUID\_GATT\_TD
    :   GATT Characteristic Treadmill Data.

    BT\_UUID\_GATT\_CTD\_VAL
    :   GATT Characteristic Cross Trainer Data UUID Value.

    BT\_UUID\_GATT\_CTD
    :   GATT Characteristic Cross Trainer Data.

    BT\_UUID\_GATT\_STPCD\_VAL
    :   GATT Characteristic Step Climber Data UUID Value.

    BT\_UUID\_GATT\_STPCD
    :   GATT Characteristic Step Climber Data.

    BT\_UUID\_GATT\_STRCD\_VAL
    :   GATT Characteristic Stair Climber Data UUID Value.

    BT\_UUID\_GATT\_STRCD
    :   GATT Characteristic Stair Climber Data.

    BT\_UUID\_GATT\_RD\_VAL
    :   GATT Characteristic Rower Data UUID Value.

    BT\_UUID\_GATT\_RD
    :   GATT Characteristic Rower Data.

    BT\_UUID\_GATT\_IBD\_VAL
    :   GATT Characteristic Indoor Bike Data UUID Value.

    BT\_UUID\_GATT\_IBD
    :   GATT Characteristic Indoor Bike Data.

    BT\_UUID\_GATT\_TRSTAT\_VAL
    :   GATT Characteristic Training Status UUID Value.

    BT\_UUID\_GATT\_TRSTAT
    :   GATT Characteristic Training Status.

    BT\_UUID\_GATT\_SSR\_VAL
    :   GATT Characteristic Supported Speed Range UUID Value.

    BT\_UUID\_GATT\_SSR
    :   GATT Characteristic Supported Speed Range.

    BT\_UUID\_GATT\_SIR\_VAL
    :   GATT Characteristic Supported Inclination Range UUID Value.

    BT\_UUID\_GATT\_SIR
    :   GATT Characteristic Supported Inclination Range.

    BT\_UUID\_GATT\_SRLR\_VAL
    :   GATT Characteristic Supported Resistance Level Range UUID Value.

    BT\_UUID\_GATT\_SRLR
    :   GATT Characteristic Supported Resistance Level Range.

    BT\_UUID\_GATT\_SHRR\_VAL
    :   GATT Characteristic Supported Heart Rate Range UUID Value.

    BT\_UUID\_GATT\_SHRR
    :   GATT Characteristic Supported Heart Rate Range.

    BT\_UUID\_GATT\_SPR\_VAL
    :   GATT Characteristic Supported Power Range UUID Value.

    BT\_UUID\_GATT\_SPR
    :   GATT Characteristic Supported Power Range.

    BT\_UUID\_GATT\_FMCP\_VAL
    :   GATT Characteristic Fitness Machine Control Point UUID Value.

    BT\_UUID\_GATT\_FMCP
    :   GATT Characteristic Fitness Machine Control Point.

    BT\_UUID\_GATT\_FMS\_VAL
    :   GATT Characteristic Fitness Machine Status UUID Value.

    BT\_UUID\_GATT\_FMS
    :   GATT Characteristic Fitness Machine Status.

    BT\_UUID\_MESH\_PROV\_DATA\_IN\_VAL
    :   Mesh Provisioning Data In UUID value.

    BT\_UUID\_MESH\_PROV\_DATA\_IN
    :   Mesh Provisioning Data In.

    BT\_UUID\_MESH\_PROV\_DATA\_OUT\_VAL
    :   Mesh Provisioning Data Out UUID value.

    BT\_UUID\_MESH\_PROV\_DATA\_OUT
    :   Mesh Provisioning Data Out.

    BT\_UUID\_MESH\_PROXY\_DATA\_IN\_VAL
    :   Mesh Proxy Data In UUID value.

    BT\_UUID\_MESH\_PROXY\_DATA\_IN
    :   Mesh Proxy Data In.

    BT\_UUID\_MESH\_PROXY\_DATA\_OUT\_VAL
    :   Mesh Proxy Data Out UUID value.

    BT\_UUID\_MESH\_PROXY\_DATA\_OUT
    :   Mesh Proxy Data Out.

    BT\_UUID\_GATT\_NNN\_VAL
    :   GATT Characteristic New Number Needed UUID Value.

    BT\_UUID\_GATT\_NNN
    :   GATT Characteristic New Number Needed.

    BT\_UUID\_GATT\_AC\_VAL
    :   GATT Characteristic Average Current UUID Value.

    BT\_UUID\_GATT\_AC
    :   GATT Characteristic Average Current.

    BT\_UUID\_GATT\_AV\_VAL
    :   GATT Characteristic Average Voltage UUID Value.

    BT\_UUID\_GATT\_AV
    :   GATT Characteristic Average Voltage.

    BT\_UUID\_GATT\_BOOLEAN\_VAL
    :   GATT Characteristic Boolean UUID Value.

    BT\_UUID\_GATT\_BOOLEAN
    :   GATT Characteristic Boolean.

    BT\_UUID\_GATT\_CRDFP\_VAL
    :   GATT Characteristic Chromatic Distance From Planckian UUID Value.

    BT\_UUID\_GATT\_CRDFP
    :   GATT Characteristic Chromatic Distance From Planckian.

    BT\_UUID\_GATT\_CRCOORDS\_VAL
    :   GATT Characteristic Chromaticity Coordinates UUID Value.

    BT\_UUID\_GATT\_CRCOORDS
    :   GATT Characteristic Chromaticity Coordinates.

    BT\_UUID\_GATT\_CRCCT\_VAL
    :   GATT Characteristic Chromaticity In CCT And Duv Values UUID Value.

    BT\_UUID\_GATT\_CRCCT
    :   GATT Characteristic Chromaticity In CCT And Duv Values.

    BT\_UUID\_GATT\_CRT\_VAL
    :   GATT Characteristic Chromaticity Tolerance UUID Value.

    BT\_UUID\_GATT\_CRT
    :   GATT Characteristic Chromaticity Tolerance.

    BT\_UUID\_GATT\_CIEIDX\_VAL
    :   GATT Characteristic CIE 13.3-1995 Color Rendering Index UUID Value.

    BT\_UUID\_GATT\_CIEIDX
    :   GATT Characteristic CIE 13.3-1995 Color Rendering Index.

    BT\_UUID\_GATT\_COEFFICIENT\_VAL
    :   GATT Characteristic Coefficient UUID Value.

    BT\_UUID\_GATT\_COEFFICIENT
    :   GATT Characteristic Coefficient.

    BT\_UUID\_GATT\_CCTEMP\_VAL
    :   GATT Characteristic Correlated Color Temperature UUID Value.

    BT\_UUID\_GATT\_CCTEMP
    :   GATT Characteristic Correlated Color Temperature.

    BT\_UUID\_GATT\_COUNT16\_VAL
    :   GATT Characteristic Count 16 UUID Value.

    BT\_UUID\_GATT\_COUNT16
    :   GATT Characteristic Count 16.

    BT\_UUID\_GATT\_COUNT24\_VAL
    :   GATT Characteristic Count 24 UUID Value.

    BT\_UUID\_GATT\_COUNT24
    :   GATT Characteristic Count 24.

    BT\_UUID\_GATT\_CNTRCODE\_VAL
    :   GATT Characteristic Country Code UUID Value.

    BT\_UUID\_GATT\_CNTRCODE
    :   GATT Characteristic Country Code.

    BT\_UUID\_GATT\_DATEUTC\_VAL
    :   GATT Characteristic Date UTC UUID Value.

    BT\_UUID\_GATT\_DATEUTC
    :   GATT Characteristic Date UTC.

    BT\_UUID\_GATT\_EC\_VAL
    :   GATT Characteristic Electric Current UUID Value.

    BT\_UUID\_GATT\_EC
    :   GATT Characteristic Electric Current.

    BT\_UUID\_GATT\_ECR\_VAL
    :   GATT Characteristic Electric Current Range UUID Value.

    BT\_UUID\_GATT\_ECR
    :   GATT Characteristic Electric Current Range.

    BT\_UUID\_GATT\_ECSPEC\_VAL
    :   GATT Characteristic Electric Current Specification UUID Value.

    BT\_UUID\_GATT\_ECSPEC
    :   GATT Characteristic Electric Current Specification.

    BT\_UUID\_GATT\_ECSTAT\_VAL
    :   GATT Characteristic Electric Current Statistics UUID Value.

    BT\_UUID\_GATT\_ECSTAT
    :   GATT Characteristic Electric Current Statistics.

    BT\_UUID\_GATT\_ENERGY\_VAL
    :   GATT Characteristic Energy UUID Value.

    BT\_UUID\_GATT\_ENERGY
    :   GATT Characteristic Energy.

    BT\_UUID\_GATT\_EPOD\_VAL
    :   GATT Characteristic Energy In A Period Of Day UUID Value.

    BT\_UUID\_GATT\_EPOD
    :   GATT Characteristic Energy In A Period Of Day.

    BT\_UUID\_GATT\_EVTSTAT\_VAL
    :   GATT Characteristic Event Statistics UUID Value.

    BT\_UUID\_GATT\_EVTSTAT
    :   GATT Characteristic Event Statistics.

    BT\_UUID\_GATT\_FSTR16\_VAL
    :   GATT Characteristic Fixed String 16 UUID Value.

    BT\_UUID\_GATT\_FSTR16
    :   GATT Characteristic Fixed String 16.

    BT\_UUID\_GATT\_FSTR24\_VAL
    :   GATT Characteristic Fixed String 24 UUID Value.

    BT\_UUID\_GATT\_FSTR24
    :   GATT Characteristic Fixed String 24.

    BT\_UUID\_GATT\_FSTR36\_VAL
    :   GATT Characteristic Fixed String 36 UUID Value.

    BT\_UUID\_GATT\_FSTR36
    :   GATT Characteristic Fixed String 36.

    BT\_UUID\_GATT\_FSTR8\_VAL
    :   GATT Characteristic Fixed String 8 UUID Value.

    BT\_UUID\_GATT\_FSTR8
    :   GATT Characteristic Fixed String 8.

    BT\_UUID\_GATT\_GENLVL\_VAL
    :   GATT Characteristic Generic Level UUID Value.

    BT\_UUID\_GATT\_GENLVL
    :   GATT Characteristic Generic Level.

    BT\_UUID\_GATT\_GTIN\_VAL
    :   GATT Characteristic Global Trade Item Number UUID Value.

    BT\_UUID\_GATT\_GTIN
    :   GATT Characteristic Global Trade Item Number.

    BT\_UUID\_GATT\_ILLUM\_VAL
    :   GATT Characteristic Illuminance UUID Value.

    BT\_UUID\_GATT\_ILLUM
    :   GATT Characteristic Illuminance.

    BT\_UUID\_GATT\_LUMEFF\_VAL
    :   GATT Characteristic Luminous Efficacy UUID Value.

    BT\_UUID\_GATT\_LUMEFF
    :   GATT Characteristic Luminous Efficacy.

    BT\_UUID\_GATT\_LUMNRG\_VAL
    :   GATT Characteristic Luminous Energy UUID Value.

    BT\_UUID\_GATT\_LUMNRG
    :   GATT Characteristic Luminous Energy.

    BT\_UUID\_GATT\_LUMEXP\_VAL
    :   GATT Characteristic Luminous Exposure UUID Value.

    BT\_UUID\_GATT\_LUMEXP
    :   GATT Characteristic Luminous Exposure.

    BT\_UUID\_GATT\_LUMFLX\_VAL
    :   GATT Characteristic Luminous Flux UUID Value.

    BT\_UUID\_GATT\_LUMFLX
    :   GATT Characteristic Luminous Flux.

    BT\_UUID\_GATT\_LUMFLXR\_VAL
    :   GATT Characteristic Luminous Flux Range UUID Value.

    BT\_UUID\_GATT\_LUMFLXR
    :   GATT Characteristic Luminous Flux Range.

    BT\_UUID\_GATT\_LUMINT\_VAL
    :   GATT Characteristic Luminous Intensity UUID Value.

    BT\_UUID\_GATT\_LUMINT
    :   GATT Characteristic Luminous Intensity.

    BT\_UUID\_GATT\_MASSFLOW\_VAL
    :   GATT Characteristic Mass Flow UUID Value.

    BT\_UUID\_GATT\_MASSFLOW
    :   GATT Characteristic Mass Flow.

    BT\_UUID\_GATT\_PERLGHT\_VAL
    :   GATT Characteristic Perceived Lightness UUID Value.

    BT\_UUID\_GATT\_PERLGHT
    :   GATT Characteristic Perceived Lightness.

    BT\_UUID\_GATT\_PER8\_VAL
    :   GATT Characteristic Percentage 8 UUID Value.

    BT\_UUID\_GATT\_PER8
    :   GATT Characteristic Percentage 8.

    BT\_UUID\_GATT\_PWR\_VAL
    :   GATT Characteristic Power UUID Value.

    BT\_UUID\_GATT\_PWR
    :   GATT Characteristic Power.

    BT\_UUID\_GATT\_PWRSPEC\_VAL
    :   GATT Characteristic Power Specification UUID Value.

    BT\_UUID\_GATT\_PWRSPEC
    :   GATT Characteristic Power Specification.

    BT\_UUID\_GATT\_RRICR\_VAL
    :   GATT Characteristic Relative Runtime In A Current Range UUID Value.

    BT\_UUID\_GATT\_RRICR
    :   GATT Characteristic Relative Runtime In A Current Range.

    BT\_UUID\_GATT\_RRIGLR\_VAL
    :   GATT Characteristic Relative Runtime In A Generic Level Range UUID Value.

    BT\_UUID\_GATT\_RRIGLR
    :   GATT Characteristic Relative Runtime In A Generic Level Range.

    BT\_UUID\_GATT\_RVIVR\_VAL
    :   GATT Characteristic Relative Value In A Voltage Range UUID Value.

    BT\_UUID\_GATT\_RVIVR
    :   GATT Characteristic Relative Value In A Voltage Range.

    BT\_UUID\_GATT\_RVIIR\_VAL
    :   GATT Characteristic Relative Value In A Illuminance Range UUID Value.

    BT\_UUID\_GATT\_RVIIR
    :   GATT Characteristic Relative Value In A Illuminance Range.

    BT\_UUID\_GATT\_RVIPOD\_VAL
    :   GATT Characteristic Relative Value In A Period Of Day UUID Value.

    BT\_UUID\_GATT\_RVIPOD
    :   GATT Characteristic Relative Value In A Period Of Day.

    BT\_UUID\_GATT\_RVITR\_VAL
    :   GATT Characteristic Relative Value In A Temperature Range UUID Value.

    BT\_UUID\_GATT\_RVITR
    :   GATT Characteristic Relative Value In A Temperature Range.

    BT\_UUID\_GATT\_TEMP8\_VAL
    :   GATT Characteristic Temperature 8 UUID Value.

    BT\_UUID\_GATT\_TEMP8
    :   GATT Characteristic Temperature 8.

    BT\_UUID\_GATT\_TEMP8\_IPOD\_VAL
    :   GATT Characteristic Temperature 8 In A Period Of Day UUID Value.

    BT\_UUID\_GATT\_TEMP8\_IPOD
    :   GATT Characteristic Temperature 8 In A Period Of Day.

    BT\_UUID\_GATT\_TEMP8\_STAT\_VAL
    :   GATT Characteristic Temperature 8 Statistics UUID Value.

    BT\_UUID\_GATT\_TEMP8\_STAT
    :   GATT Characteristic Temperature 8 Statistics.

    BT\_UUID\_GATT\_TEMP\_RNG\_VAL
    :   GATT Characteristic Temperature Range UUID Value.

    BT\_UUID\_GATT\_TEMP\_RNG
    :   GATT Characteristic Temperature Range.

    BT\_UUID\_GATT\_TEMP\_STAT\_VAL
    :   GATT Characteristic Temperature Statistics UUID Value.

    BT\_UUID\_GATT\_TEMP\_STAT
    :   GATT Characteristic Temperature Statistics.

    BT\_UUID\_GATT\_TIM\_DC8\_VAL
    :   GATT Characteristic Time Decihour 8 UUID Value.

    BT\_UUID\_GATT\_TIM\_DC8
    :   GATT Characteristic Time Decihour 8.

    BT\_UUID\_GATT\_TIM\_EXP8\_VAL
    :   GATT Characteristic Time Exponential 8 UUID Value.

    BT\_UUID\_GATT\_TIM\_EXP8
    :   GATT Characteristic Time Exponential 8.

    BT\_UUID\_GATT\_TIM\_H24\_VAL
    :   GATT Characteristic Time Hour 24 UUID Value.

    BT\_UUID\_GATT\_TIM\_H24
    :   GATT Characteristic Time Hour 24.

    BT\_UUID\_GATT\_TIM\_MS24\_VAL
    :   GATT Characteristic Time Millisecond 24 UUID Value.

    BT\_UUID\_GATT\_TIM\_MS24
    :   GATT Characteristic Time Millisecond 24.

    BT\_UUID\_GATT\_TIM\_S16\_VAL
    :   GATT Characteristic Time Second 16 UUID Value.

    BT\_UUID\_GATT\_TIM\_S16
    :   GATT Characteristic Time Second 16.

    BT\_UUID\_GATT\_TIM\_S8\_VAL
    :   GATT Characteristic Time Second 8 UUID Value.

    BT\_UUID\_GATT\_TIM\_S8
    :   GATT Characteristic Time Second 8.

    BT\_UUID\_GATT\_V\_VAL
    :   GATT Characteristic Voltage UUID Value.

    BT\_UUID\_GATT\_V
    :   GATT Characteristic Voltage.

    BT\_UUID\_GATT\_V\_SPEC\_VAL
    :   GATT Characteristic Voltage Specification UUID Value.

    BT\_UUID\_GATT\_V\_SPEC
    :   GATT Characteristic Voltage Specification.

    BT\_UUID\_GATT\_V\_STAT\_VAL
    :   GATT Characteristic Voltage Statistics UUID Value.

    BT\_UUID\_GATT\_V\_STAT
    :   GATT Characteristic Voltage Statistics.

    BT\_UUID\_GATT\_VOLF\_VAL
    :   GATT Characteristic Volume Flow UUID Value.

    BT\_UUID\_GATT\_VOLF
    :   GATT Characteristic Volume Flow.

    BT\_UUID\_GATT\_CRCOORD\_VAL
    :   GATT Characteristic Chromaticity Coordinate (not Coordinates) UUID Value.

    BT\_UUID\_GATT\_CRCOORD
    :   GATT Characteristic Chromaticity Coordinate (not Coordinates).

    BT\_UUID\_GATT\_RCF\_VAL
    :   GATT Characteristic RC Feature UUID Value.

    BT\_UUID\_GATT\_RCF
    :   GATT Characteristic RC Feature.

    BT\_UUID\_GATT\_RCSET\_VAL
    :   GATT Characteristic RC Settings UUID Value.

    BT\_UUID\_GATT\_RCSET
    :   GATT Characteristic RC Settings.

    BT\_UUID\_GATT\_RCCP\_VAL
    :   GATT Characteristic Reconnection Configuration Control Point UUID Value.

    BT\_UUID\_GATT\_RCCP
    :   GATT Characteristic Reconnection Configuration Control Point.

    BT\_UUID\_GATT\_IDD\_SC\_VAL
    :   GATT Characteristic IDD Status Changed UUID Value.

    BT\_UUID\_GATT\_IDD\_SC
    :   GATT Characteristic IDD Status Changed.

    BT\_UUID\_GATT\_IDD\_S\_VAL
    :   GATT Characteristic IDD Status UUID Value.

    BT\_UUID\_GATT\_IDD\_S
    :   GATT Characteristic IDD Status.

    BT\_UUID\_GATT\_IDD\_AS\_VAL
    :   GATT Characteristic IDD Annunciation Status UUID Value.

    BT\_UUID\_GATT\_IDD\_AS
    :   GATT Characteristic IDD Annunciation Status.

    BT\_UUID\_GATT\_IDD\_F\_VAL
    :   GATT Characteristic IDD Features UUID Value.

    BT\_UUID\_GATT\_IDD\_F
    :   GATT Characteristic IDD Features.

    BT\_UUID\_GATT\_IDD\_SRCP\_VAL
    :   GATT Characteristic IDD Status Reader Control Point UUID Value.

    BT\_UUID\_GATT\_IDD\_SRCP
    :   GATT Characteristic IDD Status Reader Control Point.

    BT\_UUID\_GATT\_IDD\_CCP\_VAL
    :   GATT Characteristic IDD Command Control Point UUID Value.

    BT\_UUID\_GATT\_IDD\_CCP
    :   GATT Characteristic IDD Command Control Point.

    BT\_UUID\_GATT\_IDD\_CD\_VAL
    :   GATT Characteristic IDD Command Data UUID Value.

    BT\_UUID\_GATT\_IDD\_CD
    :   GATT Characteristic IDD Command Data.

    BT\_UUID\_GATT\_IDD\_RACP\_VAL
    :   GATT Characteristic IDD Record Access Control Point UUID Value.

    BT\_UUID\_GATT\_IDD\_RACP
    :   GATT Characteristic IDD Record Access Control Point.

    BT\_UUID\_GATT\_IDD\_HD\_VAL
    :   GATT Characteristic IDD History Data UUID Value.

    BT\_UUID\_GATT\_IDD\_HD
    :   GATT Characteristic IDD History Data.

    BT\_UUID\_GATT\_CLIENT\_FEATURES\_VAL
    :   GATT Characteristic Client Supported Features UUID value.

    BT\_UUID\_GATT\_CLIENT\_FEATURES
    :   GATT Characteristic Client Supported Features.

    BT\_UUID\_GATT\_DB\_HASH\_VAL
    :   GATT Characteristic Database Hash UUID value.

    BT\_UUID\_GATT\_DB\_HASH
    :   GATT Characteristic Database Hash.

    BT\_UUID\_GATT\_BSS\_CP\_VAL
    :   GATT Characteristic BSS Control Point UUID Value.

    BT\_UUID\_GATT\_BSS\_CP
    :   GATT Characteristic BSS Control Point.

    BT\_UUID\_GATT\_BSS\_R\_VAL
    :   GATT Characteristic BSS Response UUID Value.

    BT\_UUID\_GATT\_BSS\_R
    :   GATT Characteristic BSS Response.

    BT\_UUID\_GATT\_EMG\_ID\_VAL
    :   GATT Characteristic Emergency ID UUID Value.

    BT\_UUID\_GATT\_EMG\_ID
    :   GATT Characteristic Emergency ID.

    BT\_UUID\_GATT\_EMG\_TXT\_VAL
    :   GATT Characteristic Emergency Text UUID Value.

    BT\_UUID\_GATT\_EMG\_TXT
    :   GATT Characteristic Emergency Text.

    BT\_UUID\_GATT\_ACS\_S\_VAL
    :   GATT Characteristic ACS Status UUID Value.

    BT\_UUID\_GATT\_ACS\_S
    :   GATT Characteristic ACS Status.

    BT\_UUID\_GATT\_ACS\_DI\_VAL
    :   GATT Characteristic ACS Data In UUID Value.

    BT\_UUID\_GATT\_ACS\_DI
    :   GATT Characteristic ACS Data In.

    BT\_UUID\_GATT\_ACS\_DON\_VAL
    :   GATT Characteristic ACS Data Out Notify UUID Value.

    BT\_UUID\_GATT\_ACS\_DON
    :   GATT Characteristic ACS Data Out Notify.

    BT\_UUID\_GATT\_ACS\_DOI\_VAL
    :   GATT Characteristic ACS Data Out Indicate UUID Value.

    BT\_UUID\_GATT\_ACS\_DOI
    :   GATT Characteristic ACS Data Out Indicate.

    BT\_UUID\_GATT\_ACS\_CP\_VAL
    :   GATT Characteristic ACS Control Point UUID Value.

    BT\_UUID\_GATT\_ACS\_CP
    :   GATT Characteristic ACS Control Point.

    BT\_UUID\_GATT\_EBPM\_VAL
    :   GATT Characteristic Enhanced Blood Pressure Measurement UUID Value.

    BT\_UUID\_GATT\_EBPM
    :   GATT Characteristic Enhanced Blood Pressure Measurement.

    BT\_UUID\_GATT\_EICP\_VAL
    :   GATT Characteristic Enhanced Intermediate Cuff Pressure UUID Value.

    BT\_UUID\_GATT\_EICP
    :   GATT Characteristic Enhanced Intermediate Cuff Pressure.

    BT\_UUID\_GATT\_BPR\_VAL
    :   GATT Characteristic Blood Pressure Record UUID Value.

    BT\_UUID\_GATT\_BPR
    :   GATT Characteristic Blood Pressure Record.

    BT\_UUID\_GATT\_RU\_VAL
    :   GATT Characteristic Registered User UUID Value.

    BT\_UUID\_GATT\_RU
    :   GATT Characteristic Registered User.

    BT\_UUID\_GATT\_BR\_EDR\_HD\_VAL
    :   GATT Characteristic BR-EDR Handover Data UUID Value.

    BT\_UUID\_GATT\_BR\_EDR\_HD
    :   GATT Characteristic BR-EDR Handover Data.

    BT\_UUID\_GATT\_BT\_SIG\_D\_VAL
    :   GATT Characteristic Bluetooth SIG Data UUID Value.

    BT\_UUID\_GATT\_BT\_SIG\_D
    :   GATT Characteristic Bluetooth SIG Data.

    BT\_UUID\_GATT\_SERVER\_FEATURES\_VAL
    :   GATT Characteristic Server Supported Features UUID value.

    BT\_UUID\_GATT\_SERVER\_FEATURES
    :   GATT Characteristic Server Supported Features.

    BT\_UUID\_GATT\_PHY\_AMF\_VAL
    :   GATT Characteristic Physical Activity Monitor Features UUID Value.

    BT\_UUID\_GATT\_PHY\_AMF
    :   GATT Characteristic Physical Activity Monitor Features.

    BT\_UUID\_GATT\_GEN\_AID\_VAL
    :   GATT Characteristic General Activity Instantaneous Data UUID Value.

    BT\_UUID\_GATT\_GEN\_AID
    :   GATT Characteristic General Activity Instantaneous Data.

    BT\_UUID\_GATT\_GEN\_ASD\_VAL
    :   GATT Characteristic General Activity Summary Data UUID Value.

    BT\_UUID\_GATT\_GEN\_ASD
    :   GATT Characteristic General Activity Summary Data.

    BT\_UUID\_GATT\_CR\_AID\_VAL
    :   GATT Characteristic CardioRespiratory Activity Instantaneous Data UUID Value.

    BT\_UUID\_GATT\_CR\_AID
    :   GATT Characteristic CardioRespiratory Activity Instantaneous Data.

    BT\_UUID\_GATT\_CR\_ASD\_VAL
    :   GATT Characteristic CardioRespiratory Activity Summary Data UUID Value.

    BT\_UUID\_GATT\_CR\_ASD
    :   GATT Characteristic CardioRespiratory Activity Summary Data.

    BT\_UUID\_GATT\_SC\_ASD\_VAL
    :   GATT Characteristic Step Counter Activity Summary Data UUID Value.

    BT\_UUID\_GATT\_SC\_ASD
    :   GATT Characteristic Step Counter Activity Summary Data.

    BT\_UUID\_GATT\_SLP\_AID\_VAL
    :   GATT Characteristic Sleep Activity Instantaneous Data UUID Value.

    BT\_UUID\_GATT\_SLP\_AID
    :   GATT Characteristic Sleep Activity Instantaneous Data.

    BT\_UUID\_GATT\_SLP\_ASD\_VAL
    :   GATT Characteristic Sleep Activity Summary Data UUID Value.

    BT\_UUID\_GATT\_SLP\_ASD
    :   GATT Characteristic Sleep Activity Summary Data.

    BT\_UUID\_GATT\_PHY\_AMCP\_VAL
    :   GATT Characteristic Physical Activity Monitor Control Point UUID Value.

    BT\_UUID\_GATT\_PHY\_AMCP
    :   GATT Characteristic Physical Activity Monitor Control Point.

    BT\_UUID\_GATT\_ACS\_VAL
    :   GATT Characteristic Activity Current Session UUID Value.

    BT\_UUID\_GATT\_ACS
    :   GATT Characteristic Activity Current Session.

    BT\_UUID\_GATT\_PHY\_ASDESC\_VAL
    :   GATT Characteristic Physical Activity Session Descriptor UUID Value.

    BT\_UUID\_GATT\_PHY\_ASDESC
    :   GATT Characteristic Physical Activity Session Descriptor.

    BT\_UUID\_GATT\_PREF\_U\_VAL
    :   GATT Characteristic Preferred Units UUID Value.

    BT\_UUID\_GATT\_PREF\_U
    :   GATT Characteristic Preferred Units.

    BT\_UUID\_GATT\_HRES\_H\_VAL
    :   GATT Characteristic High Resolution Height UUID Value.

    BT\_UUID\_GATT\_HRES\_H
    :   GATT Characteristic High Resolution Height.

    BT\_UUID\_GATT\_MID\_NAME\_VAL
    :   GATT Characteristic Middle Name UUID Value.

    BT\_UUID\_GATT\_MID\_NAME
    :   GATT Characteristic Middle Name.

    BT\_UUID\_GATT\_STRDLEN\_VAL
    :   GATT Characteristic Stride Length UUID Value.

    BT\_UUID\_GATT\_STRDLEN
    :   GATT Characteristic Stride Length.

    BT\_UUID\_GATT\_HANDEDNESS\_VAL
    :   GATT Characteristic Handedness UUID Value.

    BT\_UUID\_GATT\_HANDEDNESS
    :   GATT Characteristic Handedness.

    BT\_UUID\_GATT\_DEVICE\_WP\_VAL
    :   GATT Characteristic Device Wearing Position UUID Value.

    BT\_UUID\_GATT\_DEVICE\_WP
    :   GATT Characteristic Device Wearing Position.

    BT\_UUID\_GATT\_4ZHRL\_VAL
    :   GATT Characteristic Four Zone Heart Rate Limit UUID Value.

    BT\_UUID\_GATT\_4ZHRL
    :   GATT Characteristic Four Zone Heart Rate Limit.

    BT\_UUID\_GATT\_HIET\_VAL
    :   GATT Characteristic High Intensity Exercise Threshold UUID Value.

    BT\_UUID\_GATT\_HIET
    :   GATT Characteristic High Intensity Exercise Threshold.

    BT\_UUID\_GATT\_AG\_VAL
    :   GATT Characteristic Activity Goal UUID Value.

    BT\_UUID\_GATT\_AG
    :   GATT Characteristic Activity Goal.

    BT\_UUID\_GATT\_SIN\_VAL
    :   GATT Characteristic Sedentary Interval Notification UUID Value.

    BT\_UUID\_GATT\_SIN
    :   GATT Characteristic Sedentary Interval Notification.

    BT\_UUID\_GATT\_CI\_VAL
    :   GATT Characteristic Caloric Intake UUID Value.

    BT\_UUID\_GATT\_CI
    :   GATT Characteristic Caloric Intake.

    BT\_UUID\_GATT\_TMAPR\_VAL
    :   GATT Characteristic TMAP Role UUID Value.

    BT\_UUID\_GATT\_TMAPR
    :   GATT Characteristic TMAP Role.

    BT\_UUID\_AICS\_STATE\_VAL
    :   Audio Input Control Service State value.

    BT\_UUID\_AICS\_STATE
    :   Audio Input Control Service State.

    BT\_UUID\_AICS\_GAIN\_SETTINGS\_VAL
    :   Audio Input Control Service Gain Settings Properties value.

    BT\_UUID\_AICS\_GAIN\_SETTINGS
    :   Audio Input Control Service Gain Settings Properties.

    BT\_UUID\_AICS\_INPUT\_TYPE\_VAL
    :   Audio Input Control Service Input Type value.

    BT\_UUID\_AICS\_INPUT\_TYPE
    :   Audio Input Control Service Input Type.

    BT\_UUID\_AICS\_INPUT\_STATUS\_VAL
    :   Audio Input Control Service Input Status value.

    BT\_UUID\_AICS\_INPUT\_STATUS
    :   Audio Input Control Service Input Status.

    BT\_UUID\_AICS\_CONTROL\_VAL
    :   Audio Input Control Service Control Point value.

    BT\_UUID\_AICS\_CONTROL
    :   Audio Input Control Service Control Point.

    BT\_UUID\_AICS\_DESCRIPTION\_VAL
    :   Audio Input Control Service Input Description value.

    BT\_UUID\_AICS\_DESCRIPTION
    :   Audio Input Control Service Input Description.

    BT\_UUID\_VCS\_STATE\_VAL
    :   Volume Control Setting value.

    BT\_UUID\_VCS\_STATE
    :   Volume Control Setting.

    BT\_UUID\_VCS\_CONTROL\_VAL
    :   Volume Control Control point value.

    BT\_UUID\_VCS\_CONTROL
    :   Volume Control Control point.

    BT\_UUID\_VCS\_FLAGS\_VAL
    :   Volume Control Flags value.

    BT\_UUID\_VCS\_FLAGS
    :   Volume Control Flags.

    BT\_UUID\_VOCS\_STATE\_VAL
    :   Volume Offset State value.

    BT\_UUID\_VOCS\_STATE
    :   Volume Offset State.

    BT\_UUID\_VOCS\_LOCATION\_VAL
    :   Audio Location value.

    BT\_UUID\_VOCS\_LOCATION
    :   Audio Location.

    BT\_UUID\_VOCS\_CONTROL\_VAL
    :   Volume Offset Control Point value.

    BT\_UUID\_VOCS\_CONTROL
    :   Volume Offset Control Point.

    BT\_UUID\_VOCS\_DESCRIPTION\_VAL
    :   Volume Offset Audio Output Description value.

    BT\_UUID\_VOCS\_DESCRIPTION
    :   Volume Offset Audio Output Description.

    BT\_UUID\_CSIS\_SIRK\_VAL
    :   Set Identity Resolving Key value.

    BT\_UUID\_CSIS\_SIRK
    :   Set Identity Resolving Key.

    BT\_UUID\_CSIS\_SET\_SIZE\_VAL
    :   Set size value.

    BT\_UUID\_CSIS\_SET\_SIZE
    :   Set size.

    BT\_UUID\_CSIS\_SET\_LOCK\_VAL
    :   Set lock value.

    BT\_UUID\_CSIS\_SET\_LOCK
    :   Set lock.

    BT\_UUID\_CSIS\_RANK\_VAL
    :   Rank value.

    BT\_UUID\_CSIS\_RANK
    :   Rank.

    BT\_UUID\_GATT\_EDKM\_VAL
    :   GATT Characteristic Encrypted Data Key Material UUID Value.

    BT\_UUID\_GATT\_EDKM
    :   GATT Characteristic Encrypted Data Key Material.

    BT\_UUID\_GATT\_AE32\_VAL
    :   GATT Characteristic Apparent Energy 32 UUID Value.

    BT\_UUID\_GATT\_AE32
    :   GATT Characteristic Apparent Energy 32.

    BT\_UUID\_GATT\_AP\_VAL
    :   GATT Characteristic Apparent Power UUID Value.

    BT\_UUID\_GATT\_AP
    :   GATT Characteristic Apparent Power.

    BT\_UUID\_GATT\_CO2CONC\_VAL
    :   GATT Characteristic CO2 Concentration UUID Value.

    BT\_UUID\_GATT\_CO2CONC
    :   GATT Characteristic CO2 Concentration.

    BT\_UUID\_GATT\_COS\_VAL
    :   GATT Characteristic Cosine of the Angle UUID Value.

    BT\_UUID\_GATT\_COS
    :   GATT Characteristic Cosine of the Angle.

    BT\_UUID\_GATT\_DEVTF\_VAL
    :   GATT Characteristic Device Time Feature UUID Value.

    BT\_UUID\_GATT\_DEVTF
    :   GATT Characteristic Device Time Feature.

    BT\_UUID\_GATT\_DEVTP\_VAL
    :   GATT Characteristic Device Time Parameters UUID Value.

    BT\_UUID\_GATT\_DEVTP
    :   GATT Characteristic Device Time Parameters.

    BT\_UUID\_GATT\_DEVT\_VAL
    :   GATT Characteristic Device Time UUID Value.

    BT\_UUID\_GATT\_DEVT
    :   GATT Characteristic String.

    BT\_UUID\_GATT\_DEVTCP\_VAL
    :   GATT Characteristic Device Time Control Point UUID Value.

    BT\_UUID\_GATT\_DEVTCP
    :   GATT Characteristic Device Time Control Point.

    BT\_UUID\_GATT\_TCLD\_VAL
    :   GATT Characteristic Time Change Log Data UUID Value.

    BT\_UUID\_GATT\_TCLD
    :   GATT Characteristic Time Change Log Data.

    BT\_UUID\_MCS\_PLAYER\_NAME\_VAL
    :   Media player name value.

    BT\_UUID\_MCS\_PLAYER\_NAME
    :   Media player name.

    BT\_UUID\_MCS\_ICON\_OBJ\_ID\_VAL
    :   Media Icon Object ID value.

    BT\_UUID\_MCS\_ICON\_OBJ\_ID
    :   Media Icon Object ID.

    BT\_UUID\_MCS\_ICON\_URL\_VAL
    :   Media Icon URL value.

    BT\_UUID\_MCS\_ICON\_URL
    :   Media Icon URL.

    BT\_UUID\_MCS\_TRACK\_CHANGED\_VAL
    :   Track Changed value.

    BT\_UUID\_MCS\_TRACK\_CHANGED
    :   Track Changed.

    BT\_UUID\_MCS\_TRACK\_TITLE\_VAL
    :   Track Title value.

    BT\_UUID\_MCS\_TRACK\_TITLE
    :   Track Title.

    BT\_UUID\_MCS\_TRACK\_DURATION\_VAL
    :   Track Duration value.

    BT\_UUID\_MCS\_TRACK\_DURATION
    :   Track Duration.

    BT\_UUID\_MCS\_TRACK\_POSITION\_VAL
    :   Track Position value.

    BT\_UUID\_MCS\_TRACK\_POSITION
    :   Track Position.

    BT\_UUID\_MCS\_PLAYBACK\_SPEED\_VAL
    :   Playback Speed value.

    BT\_UUID\_MCS\_PLAYBACK\_SPEED
    :   Playback Speed.

    BT\_UUID\_MCS\_SEEKING\_SPEED\_VAL
    :   Seeking Speed value.

    BT\_UUID\_MCS\_SEEKING\_SPEED
    :   Seeking Speed.

    BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID\_VAL
    :   Track Segments Object ID value.

    BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID
    :   Track Segments Object ID.

    BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID\_VAL
    :   Current Track Object ID value.

    BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID
    :   Current Track Object ID.

    BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID\_VAL
    :   Next Track Object ID value.

    BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID
    :   Next Track Object ID.

    BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID\_VAL
    :   Parent Group Object ID value.

    BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID
    :   Parent Group Object ID.

    BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID\_VAL
    :   Group Object ID value.

    BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID
    :   Group Object ID.

    BT\_UUID\_MCS\_PLAYING\_ORDER\_VAL
    :   Playing Order value.

    BT\_UUID\_MCS\_PLAYING\_ORDER
    :   Playing Order.

    BT\_UUID\_MCS\_PLAYING\_ORDERS\_VAL
    :   Playing Orders supported value.

    BT\_UUID\_MCS\_PLAYING\_ORDERS
    :   Playing Orders supported.

    BT\_UUID\_MCS\_MEDIA\_STATE\_VAL
    :   Media State value.

    BT\_UUID\_MCS\_MEDIA\_STATE
    :   Media State.

    BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT\_VAL
    :   Media Control Point value.

    BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT
    :   Media Control Point.

    BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES\_VAL
    :   Media control opcodes supported value.

    BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES
    :   Media control opcodes supported.

    BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID\_VAL
    :   Search result object ID value.

    BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID
    :   Search result object ID.

    BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT\_VAL
    :   Search control point value.

    BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT
    :   Search control point.

    BT\_UUID\_GATT\_E32\_VAL
    :   GATT Characteristic Energy 32 UUID Value.

    BT\_UUID\_GATT\_E32
    :   GATT Characteristic Energy 32.

    BT\_UUID\_OTS\_TYPE\_MPL\_ICON\_VAL
    :   Media Player Icon Object Type value.

    BT\_UUID\_OTS\_TYPE\_MPL\_ICON
    :   Media Player Icon Object Type.

    BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT\_VAL
    :   Track Segments Object Type value.

    BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT
    :   Track Segments Object Type.

    BT\_UUID\_OTS\_TYPE\_TRACK\_VAL
    :   Track Object Type value.

    BT\_UUID\_OTS\_TYPE\_TRACK
    :   Track Object Type.

    BT\_UUID\_OTS\_TYPE\_GROUP\_VAL
    :   Group Object Type value.

    BT\_UUID\_OTS\_TYPE\_GROUP
    :   Group Object Type.

    BT\_UUID\_GATT\_CTEE\_VAL
    :   GATT Characteristic Constant Tone Extension Enable UUID Value.

    BT\_UUID\_GATT\_CTEE
    :   GATT Characteristic Constant Tone Extension Enable.

    BT\_UUID\_GATT\_ACTEML\_VAL
    :   GATT Characteristic Advertising Constant Tone Extension Minimum Length UUID Value.

    BT\_UUID\_GATT\_ACTEML
    :   GATT Characteristic Advertising Constant Tone Extension Minimum Length.

    BT\_UUID\_GATT\_ACTEMTC\_VAL
    :   GATT Characteristic Advertising Constant Tone Extension Minimum Transmit Count UUID Value.

    BT\_UUID\_GATT\_ACTEMTC
    :   GATT Characteristic Advertising Constant Tone Extension Minimum Transmit Count.

    BT\_UUID\_GATT\_ACTETD\_VAL
    :   GATT Characteristic Advertising Constant Tone Extension Transmit Duration UUID Value.

    BT\_UUID\_GATT\_ACTETD
    :   GATT Characteristic Advertising Constant Tone Extension Transmit Duration.

    BT\_UUID\_GATT\_ACTEI\_VAL
    :   GATT Characteristic Advertising Constant Tone Extension Interval UUID Value.

    BT\_UUID\_GATT\_ACTEI
    :   GATT Characteristic Advertising Constant Tone Extension Interval.

    BT\_UUID\_GATT\_ACTEP\_VAL
    :   GATT Characteristic Advertising Constant Tone Extension PHY UUID Value.

    BT\_UUID\_GATT\_ACTEP
    :   GATT Characteristic Advertising Constant Tone Extension PHY.

    BT\_UUID\_TBS\_PROVIDER\_NAME\_VAL
    :   Bearer Provider Name value.

    BT\_UUID\_TBS\_PROVIDER\_NAME
    :   Bearer Provider Name.

    BT\_UUID\_TBS\_UCI\_VAL
    :   Bearer UCI value.

    BT\_UUID\_TBS\_UCI
    :   Bearer UCI.

    BT\_UUID\_TBS\_TECHNOLOGY\_VAL
    :   Bearer Technology value.

    BT\_UUID\_TBS\_TECHNOLOGY
    :   Bearer Technology.

    BT\_UUID\_TBS\_URI\_LIST\_VAL
    :   Bearer URI Prefixes Supported List value.

    BT\_UUID\_TBS\_URI\_LIST
    :   Bearer URI Prefixes Supported List.

    BT\_UUID\_TBS\_SIGNAL\_STRENGTH\_VAL
    :   Bearer Signal Strength value.

    BT\_UUID\_TBS\_SIGNAL\_STRENGTH
    :   Bearer Signal Strength.

    BT\_UUID\_TBS\_SIGNAL\_INTERVAL\_VAL
    :   Bearer Signal Strength Reporting Interval value.

    BT\_UUID\_TBS\_SIGNAL\_INTERVAL
    :   Bearer Signal Strength Reporting Interval.

    BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS\_VAL
    :   Bearer List Current Calls value.

    BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS
    :   Bearer List Current Calls.

    BT\_UUID\_CCID\_VAL
    :   Content Control ID value.

    BT\_UUID\_CCID
    :   Content Control ID.

    BT\_UUID\_TBS\_STATUS\_FLAGS\_VAL
    :   Status flags value.

    BT\_UUID\_TBS\_STATUS\_FLAGS
    :   Status flags.

    BT\_UUID\_TBS\_INCOMING\_URI\_VAL
    :   Incoming Call Target Caller ID value.

    BT\_UUID\_TBS\_INCOMING\_URI
    :   Incoming Call Target Caller ID.

    BT\_UUID\_TBS\_CALL\_STATE\_VAL
    :   Call State value.

    BT\_UUID\_TBS\_CALL\_STATE
    :   Call State.

    BT\_UUID\_TBS\_CALL\_CONTROL\_POINT\_VAL
    :   Call Control Point value.

    BT\_UUID\_TBS\_CALL\_CONTROL\_POINT
    :   Call Control Point.

    BT\_UUID\_TBS\_OPTIONAL\_OPCODES\_VAL
    :   Optional Opcodes value.

    BT\_UUID\_TBS\_OPTIONAL\_OPCODES
    :   Optional Opcodes.

    BT\_UUID\_TBS\_TERMINATE\_REASON\_VAL
    :   BT\_UUID\_TBS\_TERMINATE\_REASON\_VAL.

        Terminate reason value

    BT\_UUID\_TBS\_TERMINATE\_REASON
    :   BT\_UUID\_TBS\_TERMINATE\_REASON.

        Terminate reason

    BT\_UUID\_TBS\_INCOMING\_CALL\_VAL
    :   Incoming Call value.

    BT\_UUID\_TBS\_INCOMING\_CALL
    :   Incoming Call.

    BT\_UUID\_TBS\_FRIENDLY\_NAME\_VAL
    :   Incoming Call Friendly name value.

    BT\_UUID\_TBS\_FRIENDLY\_NAME
    :   Incoming Call Friendly name.

    BT\_UUID\_MICS\_MUTE\_VAL
    :   Microphone Control Service Mute value.

    BT\_UUID\_MICS\_MUTE
    :   Microphone Control Service Mute.

    BT\_UUID\_ASCS\_ASE\_SNK\_VAL
    :   Audio Stream Endpoint Sink Characteristic value.

    BT\_UUID\_ASCS\_ASE\_SNK
    :   Audio Stream Endpoint Sink Characteristic.

    BT\_UUID\_ASCS\_ASE\_SRC\_VAL
    :   Audio Stream Endpoint Source Characteristic value.

    BT\_UUID\_ASCS\_ASE\_SRC
    :   Audio Stream Endpoint Source Characteristic.

    BT\_UUID\_ASCS\_ASE\_CP\_VAL
    :   Audio Stream Endpoint Control Point Characteristic value.

    BT\_UUID\_ASCS\_ASE\_CP
    :   Audio Stream Endpoint Control Point Characteristic.

    BT\_UUID\_BASS\_CONTROL\_POINT\_VAL
    :   Broadcast Audio Scan Service Scan State value.

    BT\_UUID\_BASS\_CONTROL\_POINT
    :   Broadcast Audio Scan Service Scan State.

    BT\_UUID\_BASS\_RECV\_STATE\_VAL
    :   Broadcast Audio Scan Service Receive State value.

    BT\_UUID\_BASS\_RECV\_STATE
    :   Broadcast Audio Scan Service Receive State.

    BT\_UUID\_PACS\_SNK\_VAL
    :   Sink PAC Characteristic value.

    BT\_UUID\_PACS\_SNK
    :   Sink PAC Characteristic.

    BT\_UUID\_PACS\_SNK\_LOC\_VAL
    :   Sink PAC Locations Characteristic value.

    BT\_UUID\_PACS\_SNK\_LOC
    :   Sink PAC Locations Characteristic.

    BT\_UUID\_PACS\_SRC\_VAL
    :   Source PAC Characteristic value.

    BT\_UUID\_PACS\_SRC
    :   Source PAC Characteristic.

    BT\_UUID\_PACS\_SRC\_LOC\_VAL
    :   Source PAC Locations Characteristic value.

    BT\_UUID\_PACS\_SRC\_LOC
    :   Source PAC Locations Characteristic.

    BT\_UUID\_PACS\_AVAILABLE\_CONTEXT\_VAL
    :   Available Audio Contexts Characteristic value.

    BT\_UUID\_PACS\_AVAILABLE\_CONTEXT
    :   Available Audio Contexts Characteristic.

    BT\_UUID\_PACS\_SUPPORTED\_CONTEXT\_VAL
    :   Supported Audio Context Characteristic value.

    BT\_UUID\_PACS\_SUPPORTED\_CONTEXT
    :   Supported Audio Context Characteristic.

    BT\_UUID\_GATT\_NH4CONC\_VAL
    :   GATT Characteristic Ammonia Concentration UUID Value.

    BT\_UUID\_GATT\_NH4CONC
    :   GATT Characteristic Ammonia Concentration.

    BT\_UUID\_GATT\_COCONC\_VAL
    :   GATT Characteristic Carbon Monoxide Concentration UUID Value.

    BT\_UUID\_GATT\_COCONC
    :   GATT Characteristic Carbon Monoxide Concentration.

    BT\_UUID\_GATT\_CH4CONC\_VAL
    :   GATT Characteristic Methane Concentration UUID Value.

    BT\_UUID\_GATT\_CH4CONC
    :   GATT Characteristic Methane Concentration.

    BT\_UUID\_GATT\_NO2CONC\_VAL
    :   GATT Characteristic Nitrogen Dioxide Concentration UUID Value.

    BT\_UUID\_GATT\_NO2CONC
    :   GATT Characteristic Nitrogen Dioxide Concentration.

    BT\_UUID\_GATT\_NONCH4CONC\_VAL
    :   GATT Characteristic Non-Methane Volatile Organic Compounds Concentration UUID Value.

    BT\_UUID\_GATT\_NONCH4CONC
    :   GATT Characteristic Non-Methane Volatile Organic Compounds Concentration.

    BT\_UUID\_GATT\_O3CONC\_VAL
    :   GATT Characteristic Ozone Concentration UUID Value.

    BT\_UUID\_GATT\_O3CONC
    :   GATT Characteristic Ozone Concentration.

    BT\_UUID\_GATT\_PM1CONC\_VAL
    :   GATT Characteristic Particulate Matter - PM1 Concentration UUID Value.

    BT\_UUID\_GATT\_PM1CONC
    :   GATT Characteristic Particulate Matter - PM1 Concentration.

    BT\_UUID\_GATT\_PM25CONC\_VAL
    :   GATT Characteristic Particulate Matter - PM2.5 Concentration UUID Value.

    BT\_UUID\_GATT\_PM25CONC
    :   GATT Characteristic Particulate Matter - PM2.5 Concentration.

    BT\_UUID\_GATT\_PM10CONC\_VAL
    :   GATT Characteristic Particulate Matter - PM10 Concentration UUID Value.

    BT\_UUID\_GATT\_PM10CONC
    :   GATT Characteristic Particulate Matter - PM10 Concentration.

    BT\_UUID\_GATT\_SO2CONC\_VAL
    :   GATT Characteristic Sulfur Dioxide Concentration UUID Value.

    BT\_UUID\_GATT\_SO2CONC
    :   GATT Characteristic Sulfur Dioxide Concentration.

    BT\_UUID\_GATT\_SF6CONC\_VAL
    :   GATT Characteristic Sulfur Hexafluoride Concentration UUID Value.

    BT\_UUID\_GATT\_SF6CONC
    :   GATT Characteristic Sulfur Hexafluoride Concentration.

    BT\_UUID\_HAS\_HEARING\_AID\_FEATURES\_VAL
    :   Hearing Aid Features Characteristic value.

    BT\_UUID\_HAS\_HEARING\_AID\_FEATURES
    :   Hearing Aid Features Characteristic.

    BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT\_VAL
    :   Hearing Aid Preset Control Point Characteristic value.

    BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT
    :   Hearing Aid Preset Control Point Characteristic.

    BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX\_VAL
    :   Active Preset Index Characteristic value.

    BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX
    :   Active Preset Index Characteristic.

    BT\_UUID\_GATT\_FSTR64\_VAL
    :   GATT Characteristic Fixed String 64 UUID Value.

    BT\_UUID\_GATT\_FSTR64
    :   GATT Characteristic Fixed String 64.

    BT\_UUID\_GATT\_HITEMP\_VAL
    :   GATT Characteristic High Temperature UUID Value.

    BT\_UUID\_GATT\_HITEMP
    :   GATT Characteristic High Temperature.

    BT\_UUID\_GATT\_HV\_VAL
    :   GATT Characteristic High Voltage UUID Value.

    BT\_UUID\_GATT\_HV
    :   GATT Characteristic High Voltage.

    BT\_UUID\_GATT\_LD\_VAL
    :   GATT Characteristic Light Distribution UUID Value.

    BT\_UUID\_GATT\_LD
    :   GATT Characteristic Light Distribution.

    BT\_UUID\_GATT\_LO\_VAL
    :   GATT Characteristic Light Output UUID Value.

    BT\_UUID\_GATT\_LO
    :   GATT Characteristic Light Output.

    BT\_UUID\_GATT\_LST\_VAL
    :   GATT Characteristic Light Source Type UUID Value.

    BT\_UUID\_GATT\_LST
    :   GATT Characteristic Light Source Type.

    BT\_UUID\_GATT\_NOISE\_VAL
    :   GATT Characteristic Noise UUID Value.

    BT\_UUID\_GATT\_NOISE
    :   GATT Characteristic Noise.

    BT\_UUID\_GATT\_RRCCTP\_VAL
    :   GATT Characteristic Relative Runtime in a Correlated Color Temperature Range UUID Value.

    BT\_UUID\_GATT\_RRCCTR
    :   GATT Characteristic Relative Runtime in a Correlated Color Temperature Range.

    BT\_UUID\_GATT\_TIM\_S32\_VAL
    :   GATT Characteristic Time Second 32 UUID Value.

    BT\_UUID\_GATT\_TIM\_S32
    :   GATT Characteristic Time Second 32.

    BT\_UUID\_GATT\_VOCCONC\_VAL
    :   GATT Characteristic VOC Concentration UUID Value.

    BT\_UUID\_GATT\_VOCCONC
    :   GATT Characteristic VOC Concentration.

    BT\_UUID\_GATT\_VF\_VAL
    :   GATT Characteristic Voltage Frequency UUID Value.

    BT\_UUID\_GATT\_VF
    :   GATT Characteristic Voltage Frequency.

    BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS\_VAL
    :   BAS Characteristic Battery Critical Status UUID Value.

    BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS
    :   BAS Characteristic Battery Critical Status.

    BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS\_VAL
    :   BAS Characteristic Battery Health Status UUID Value.

    BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS
    :   BAS Characteristic Battery Health Status.

    BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF\_VAL
    :   BAS Characteristic Battery Health Information UUID Value.

    BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF
    :   BAS Characteristic Battery Health Information.

    BT\_UUID\_BAS\_BATTERY\_INF\_VAL
    :   BAS Characteristic Battery Information UUID Value.

    BT\_UUID\_BAS\_BATTERY\_INF
    :   BAS Characteristic Battery Information.

    BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS\_VAL
    :   BAS Characteristic Battery Level Status UUID Value.

    BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS
    :   BAS Characteristic Battery Level Status.

    BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS\_VAL
    :   BAS Characteristic Battery Time Status UUID Value.

    BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS
    :   BAS Characteristic Battery Time Status.

    BT\_UUID\_GATT\_ESD\_VAL
    :   GATT Characteristic Estimated Service Date UUID Value.

    BT\_UUID\_GATT\_ESD
    :   GATT Characteristic Estimated Service Date.

    BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS\_VAL
    :   BAS Characteristic Battery Energy Status UUID Value.

    BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS
    :   BAS Characteristic Battery Energy Status.

    BT\_UUID\_GATT\_SL\_VAL
    :   GATT Characteristic LE GATT Security Levels UUID Value.

    BT\_UUID\_GATT\_SL
    :   GATT Characteristic LE GATT Security Levels.

    BT\_UUID\_GMAS\_VAL
    :   Gaming Service UUID value.

    BT\_UUID\_GMAS
    :   Common Audio Service.

    BT\_UUID\_GMAP\_ROLE\_VAL
    :   Gaming Audio Profile Role UUID value.

    BT\_UUID\_GMAP\_ROLE
    :   Gaming Audio Profile Role.

    BT\_UUID\_GMAP\_UGG\_FEAT\_VAL
    :   Gaming Audio Profile Unicast Game Gateway Features UUID value.

    BT\_UUID\_GMAP\_UGG\_FEAT
    :   Gaming Audio Profile Unicast Game Gateway Features.

    BT\_UUID\_GMAP\_UGT\_FEAT\_VAL
    :   Gaming Audio Profile Unicast Game Terminal Features UUID value.

    BT\_UUID\_GMAP\_UGT\_FEAT
    :   Gaming Audio Profile Unicast Game Terminal Features.

    BT\_UUID\_GMAP\_BGS\_FEAT\_VAL
    :   Gaming Audio Profile Broadcast Game Sender Features UUID value.

    BT\_UUID\_GMAP\_BGS\_FEAT
    :   Gaming Audio Profile Broadcast Game Sender Features.

    BT\_UUID\_GMAP\_BGR\_FEAT\_VAL
    :   Gaming Audio Profile Broadcast Game Receiver Features UUID value.

    BT\_UUID\_GMAP\_BGR\_FEAT
    :   Gaming Audio Profile Broadcast Game Receiver Features.

    BT\_UUID\_SDP\_VAL

    BT\_UUID\_SDP

    BT\_UUID\_UDP\_VAL

    BT\_UUID\_UDP

    BT\_UUID\_RFCOMM\_VAL

    BT\_UUID\_RFCOMM

    BT\_UUID\_TCP\_VAL

    BT\_UUID\_TCP

    BT\_UUID\_TCS\_BIN\_VAL

    BT\_UUID\_TCS\_BIN

    BT\_UUID\_TCS\_AT\_VAL

    BT\_UUID\_TCS\_AT

    BT\_UUID\_ATT\_VAL

    BT\_UUID\_ATT

    BT\_UUID\_OBEX\_VAL

    BT\_UUID\_OBEX

    BT\_UUID\_IP\_VAL

    BT\_UUID\_IP

    BT\_UUID\_FTP\_VAL

    BT\_UUID\_FTP

    BT\_UUID\_HTTP\_VAL

    BT\_UUID\_HTTP

    BT\_UUID\_WSP\_VAL

    BT\_UUID\_WSP

    BT\_UUID\_BNEP\_VAL

    BT\_UUID\_BNEP

    BT\_UUID\_UPNP\_VAL

    BT\_UUID\_UPNP

    BT\_UUID\_HIDP\_VAL

    BT\_UUID\_HIDP

    BT\_UUID\_HCRP\_CTRL\_VAL

    BT\_UUID\_HCRP\_CTRL

    BT\_UUID\_HCRP\_DATA\_VAL

    BT\_UUID\_HCRP\_DATA

    BT\_UUID\_HCRP\_NOTE\_VAL

    BT\_UUID\_HCRP\_NOTE

    BT\_UUID\_AVCTP\_VAL

    BT\_UUID\_AVCTP

    BT\_UUID\_AVDTP\_VAL

    BT\_UUID\_AVDTP

    BT\_UUID\_CMTP\_VAL

    BT\_UUID\_CMTP

    BT\_UUID\_UDI\_VAL

    BT\_UUID\_UDI

    BT\_UUID\_MCAP\_CTRL\_VAL

    BT\_UUID\_MCAP\_CTRL

    BT\_UUID\_MCAP\_DATA\_VAL

    BT\_UUID\_MCAP\_DATA

    BT\_UUID\_L2CAP\_VAL

    BT\_UUID\_L2CAP

    Enums

    enum [anonymous]
    :   Bluetooth UUID types.

        *Values:*

        enumerator BT\_UUID\_TYPE\_16
        :   UUID type 16-bit.

        enumerator BT\_UUID\_TYPE\_32
        :   UUID type 32-bit.

        enumerator BT\_UUID\_TYPE\_128
        :   UUID type 128-bit.

    Functions

    int bt\_uuid\_cmp(const struct [bt\_uuid](#c.bt_uuid) \*u1, const struct [bt\_uuid](#c.bt_uuid) \*u2)
    :   Compare Bluetooth UUIDs.

        Compares 2 Bluetooth UUIDs, if the types are different both UUIDs are first converted to 128 bits format before comparing.

        Parameters:
        :   - **u1** – First Bluetooth UUID to compare
            - **u2** – Second Bluetooth UUID to compare

        Returns:
        :   negative value if *u1* < *u2*, 0 if *u1* == *u2*, else positive

    bool bt\_uuid\_create(struct [bt\_uuid](#c.bt_uuid) \*uuid, const uint8\_t \*data, uint8\_t data\_len)
    :   Create a [bt\_uuid](#structbt__uuid) from a little-endian data buffer.

        Create a [bt\_uuid](#structbt__uuid) from a little-endian data buffer. The data\_len parameter is used to determine whether the UUID is in 16, 32 or 128 bit format (length 2, 4 or 16). Note: 32 bit format is not allowed over the air.

        Parameters:
        :   - **uuid** – Pointer to the [bt\_uuid](#structbt__uuid) variable
            - **data** – pointer to UUID stored in little-endian data buffer
            - **data\_len** – length of the UUID in the data buffer

        Returns:
        :   true if the data was valid and the UUID was successfully created.

    void bt\_uuid\_to\_str(const struct [bt\_uuid](#c.bt_uuid) \*uuid, char \*str, size\_t len)
    :   Convert Bluetooth UUID to string.

        Converts Bluetooth UUID to string. UUID can be in any format, 16-bit, 32-bit or 128-bit.

        Parameters:
        :   - **uuid** – Bluetooth UUID
            - **str** – pointer where to put converted string
            - **len** – length of str

    struct bt\_uuid
    :   *#include <uuid.h>*

        This is a ‘tentative’ type and should be used as a pointer only.

    struct bt\_uuid\_16
    :   *#include <uuid.h>*

        Public Members

        struct [bt\_uuid](#c.bt_uuid) uuid
        :   UUID generic type.

        uint16\_t val
        :   UUID value, 16-bit in host endianness.

    struct bt\_uuid\_32
    :   *#include <uuid.h>*

        Public Members

        struct [bt\_uuid](#c.bt_uuid) uuid
        :   UUID generic type.

        uint32\_t val
        :   UUID value, 32-bit in host endianness.

    struct bt\_uuid\_128
    :   *#include <uuid.h>*

        Public Members

        struct [bt\_uuid](#c.bt_uuid) uuid
        :   UUID generic type.

        uint8\_t val[16]
        :   UUID value, 128-bit in little-endian format.
