---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/wifi.html
original_path: connectivity/networking/api/wifi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Wi-Fi Management

## Overview

The Wi-Fi management API is used to manage Wi-Fi networks. It supports below modes:

- IEEE802.11 Station (STA)
- IEEE802.11 Access Point (AP)

Only personal mode security is supported with below types:

- Open
- WPA2-PSK
- WPA3-PSK-256
- WPA3-SAE

The Wi-Fi management API is implemented in the wifi\_mgmt module as a part of the networking L2 stack.
Currently, two types of Wi-Fi drivers are supported:

- Networking or socket offloaded drivers
- Native L2 Ethernet drivers

### API Reference

*group* Wi-Fi Management
:   Wi-Fi Management API.

    Wi-Fi utility functions.

    Utility functions for the Wi-Fi subsystem.

    int wifi\_utils\_parse\_scan\_bands(char \*scan\_bands\_str, uint8\_t \*band\_map)
    :   Convert a band specification string to a bitmap representing the bands.

        The function will parse a string which specifies Wi-Fi frequency band values as a comma separated string and convert it to a bitmap. The string can use the following characters to represent the bands:

        - 2: 2.4 GHz
        - 5: 5 GHz
        - 6: 6 GHz

        For the bitmap generated refer to [wifi\_frequency\_bands](#group__wifi__mgmt_1ga1e2f0439a322355fa7368ea880c9c15d) for bit position of each band.

        E.g. a string “2,5,6” will be converted to a bitmap value of 0x7

        Parameters:
        :   - **scan\_bands\_str** – String which spe.
            - **band\_map** – Pointer to the bitmap variable to be updated.

        Return values:
        :   - **0** – on success.
            - **-errno** – value in case of failure.

    int wifi\_utils\_parse\_scan\_ssids(char \*scan\_ssids\_str, const char \*ssids[], uint8\_t num\_ssids)
    :   Append a string containing an SSID to an array of SSID strings.

        Parameters:
        :   - **scan\_ssids\_str** – string to be appended in the list of scanned SSIDs.
            - **ssids** – Pointer to an array where the SSIDs pointers are to be stored.
            - **num\_ssids** – Maximum number of SSIDs that can be stored.

        Return values:
        :   - **0** – on success.
            - **-errno** – value in case of failure.

    int wifi\_utils\_parse\_scan\_chan(char \*scan\_chan\_str, struct [wifi\_band\_channel](#c.wifi_band_channel) \*chan, uint8\_t max\_channels)
    :   Convert a string containing a specification of scan channels to an array.

        The function will parse a string which specifies channels to be scanned as a string and convert it to an array.

        The channel string has to be formatted using the colon (:), comma(,), hyphen (-) and underscore (\_) delimiters as follows:

        - A colon identifies the value preceding it as a band. A band value (2: 2.4 GHz, 5: 5 GHz 6: 6 GHz) has to precede the channels in that band (e.g. 2: etc)
        - Hyphens (-) are used to identify channel ranges (e.g. 2-7, 32-48 etc)
        - Commas are used to separate channel values within a band. Channels can be specified as individual values (2,6,48 etc) or channel ranges using hyphens (1-14, 32-48 etc)
        - Underscores (\_) are used to specify multiple band-channel sets (e.g. 2:1,2\_5:36,40 etc)
        - No spaces should be used anywhere, i.e. before/after commas, before/after hyphens etc.

        An example channel specification specifying channels in the 2.4 GHz and 5 GHz bands is as below: 2:1,5,7,9-11\_5:36-48,100,163-167

        Parameters:
        :   - **scan\_chan\_str** – List of channels expressed in the format described above.
            - **chan** – Pointer to an array where the parsed channels are to be stored.
            - **max\_channels** – Maximum number of channels to store

        Return values:
        :   - **0** – on success.
            - **-errno** – value in case of failure.

    bool wifi\_utils\_validate\_chan(uint8\_t band, uint16\_t chan)
    :   Validate a channel against a band.

        Parameters:
        :   - **band** – Band to validate the channel against.
            - **chan** – Channel to validate.

        Return values:
        :   - **true** – if the channel is valid for the band.
            - **false** – if the channel is not valid for the band.

    bool wifi\_utils\_validate\_chan\_2g(uint16\_t chan)
    :   Validate a channel against the 2.4 GHz band.

        Parameters:
        :   - **chan** – Channel to validate.

        Return values:
        :   - **true** – if the channel is valid for the band.
            - **false** – if the channel is not valid for the band.

    bool wifi\_utils\_validate\_chan\_5g(uint16\_t chan)
    :   Validate a channel against the 5 GHz band.

        Parameters:
        :   - **chan** – Channel to validate.

        Return values:
        :   - **true** – if the channel is valid for the band.
            - **false** – if the channel is not valid for the band.

    bool wifi\_utils\_validate\_chan\_6g(uint16\_t chan)
    :   Validate a channel against the 6 GHz band.

        Parameters:
        :   - **chan** – Channel to validate.

        Return values:
        :   - **true** – if the channel is valid for the band.
            - **false** – if the channel is not valid for the band.

    WIFI\_UTILS\_MAX\_BAND\_STR\_LEN
    :   Maximum length of the band specification string.

    WIFI\_UTILS\_MAX\_CHAN\_STR\_LEN
    :   Maximum length of the channel specification string.

    Defines

    WIFI\_COUNTRY\_CODE\_LEN
    :   Length of the country code string.

    WIFI\_SSID\_MAX\_LEN
    :   Max SSID length.

    WIFI\_PSK\_MIN\_LEN
    :   Minimum PSK length.

    WIFI\_PSK\_MAX\_LEN
    :   Maximum PSK length.

    WIFI\_SAE\_PSWD\_MAX\_LEN
    :   Max SAW password length.

    WIFI\_MAC\_ADDR\_LEN
    :   MAC address length.

    WIFI\_CHANNEL\_MIN
    :   Minimum channel number.

    WIFI\_CHANNEL\_MAX
    :   Maximum channel number.

    WIFI\_CHANNEL\_ANY
    :   Any channel number.

    WIFI\_INTERFACE\_INDEX\_MIN
    :   Network interface index min value.

    WIFI\_INTERFACE\_INDEX\_MAX
    :   Network interface index max value.

    NET\_REQUEST\_WIFI\_SCAN
    :   Request a Wi-Fi scan.

    NET\_REQUEST\_WIFI\_CONNECT
    :   Request a Wi-Fi connect.

    NET\_REQUEST\_WIFI\_DISCONNECT
    :   Request a Wi-Fi disconnect.

    NET\_REQUEST\_WIFI\_AP\_ENABLE
    :   Request a Wi-Fi access point enable.

    NET\_REQUEST\_WIFI\_AP\_DISABLE
    :   Request a Wi-Fi access point disable.

    NET\_REQUEST\_WIFI\_IFACE\_STATUS
    :   Request a Wi-Fi network interface status.

    NET\_REQUEST\_WIFI\_PS
    :   Request a Wi-Fi power save.

    NET\_REQUEST\_WIFI\_TWT
    :   Request a Wi-Fi TWT.

    NET\_REQUEST\_WIFI\_PS\_CONFIG
    :   Request a Wi-Fi power save configuration.

    NET\_REQUEST\_WIFI\_REG\_DOMAIN
    :   Request a Wi-Fi regulatory domain.

    NET\_REQUEST\_WIFI\_MODE
    :   Request current Wi-Fi mode.

    NET\_REQUEST\_WIFI\_PACKET\_FILTER
    :   Request Wi-Fi packet filter.

    NET\_REQUEST\_WIFI\_CHANNEL
    :   Request a Wi-Fi channel.

    NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT
    :   Request a Wi-Fi access point to disconnect a station.

    NET\_REQUEST\_WIFI\_VERSION
    :   Request a Wi-Fi version.

    NET\_REQUEST\_WIFI\_RTS\_THRESHOLD
    :   Request a Wi-Fi RTS threshold.

    NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM
    :   Request a Wi-Fi AP parameters configuration.

    NET\_EVENT\_WIFI\_SCAN\_RESULT
    :   Event emitted for Wi-Fi scan result.

    NET\_EVENT\_WIFI\_SCAN\_DONE
    :   Event emitted when Wi-Fi scan is done.

    NET\_EVENT\_WIFI\_CONNECT\_RESULT
    :   Event emitted for Wi-Fi connect result.

    NET\_EVENT\_WIFI\_DISCONNECT\_RESULT
    :   Event emitted for Wi-Fi disconnect result.

    NET\_EVENT\_WIFI\_IFACE\_STATUS
    :   Event emitted for Wi-Fi network interface status.

    NET\_EVENT\_WIFI\_TWT
    :   Event emitted for Wi-Fi TWT information.

    NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE
    :   Event emitted for Wi-Fi TWT sleep state.

    NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT
    :   Event emitted for Wi-Fi raw scan result.

    NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE
    :   Event emitted Wi-Fi disconnect is completed.

    NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT
    :   Event emitted for Wi-Fi access point enable result.

    NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT
    :   Event emitted for Wi-Fi access point disable result.

    NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED
    :   Event emitted when Wi-Fi station is connected in AP mode.

    NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED
    :   Event emitted Wi-Fi station is disconnected from AP.

    MAX\_REG\_CHAN\_NUM
    :   Max regulatory channel number.

    Typedefs

    typedef void (\*scan\_result\_cb\_t)(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, int status, struct [wifi\_scan\_result](#c.wifi_scan_result) \*entry)
    :   Scan result callback.

        Param iface:
        :   Network interface

        Param status:
        :   Scan result status

        Param entry:
        :   Scan result entry

    Enums

    enum wifi\_security\_type
    :   IEEE 802.11 security types.

        *Values:*

        enumerator WIFI\_SECURITY\_TYPE\_NONE = 0
        :   No security.

        enumerator WIFI\_SECURITY\_TYPE\_PSK
        :   WPA2-PSK security.

        enumerator WIFI\_SECURITY\_TYPE\_PSK\_SHA256
        :   WPA2-PSK-SHA256 security.

        enumerator WIFI\_SECURITY\_TYPE\_SAE
        :   WPA3-SAE security.

        enumerator WIFI\_SECURITY\_TYPE\_WAPI
        :   GB 15629.11-2003 WAPI security.

        enumerator WIFI\_SECURITY\_TYPE\_EAP
        :   EAP security - Enterprise.

        enumerator WIFI\_SECURITY\_TYPE\_WEP
        :   WEP security.

        enumerator WIFI\_SECURITY\_TYPE\_WPA\_PSK
        :   WPA-PSK security.

        enumerator WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL
        :   WPA/WPA2/WPA3 PSK security.

    enum wifi\_mfp\_options
    :   IEEE 802.11w - Management frame protection.

        *Values:*

        enumerator WIFI\_MFP\_DISABLE = 0
        :   MFP disabled.

        enumerator WIFI\_MFP\_OPTIONAL
        :   MFP optional.

        enumerator WIFI\_MFP\_REQUIRED
        :   MFP required.

    enum wifi\_frequency\_bands
    :   IEEE 802.11 operational frequency bands (not exhaustive).

        *Values:*

        enumerator WIFI\_FREQ\_BAND\_2\_4\_GHZ = 0
        :   2.4 GHz band.

        enumerator WIFI\_FREQ\_BAND\_5\_GHZ
        :   5 GHz band.

        enumerator WIFI\_FREQ\_BAND\_6\_GHZ
        :   6 GHz band (Wi-Fi 6E, also extends to 7GHz).

        enumerator \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST
        :   Number of frequency bands available.

        enumerator WIFI\_FREQ\_BAND\_MAX = [\_\_WIFI\_FREQ\_BAND\_AFTER\_LAST](#c.wifi_frequency_bands.__WIFI_FREQ_BAND_AFTER_LAST) - 1
        :   Highest frequency band available.

        enumerator WIFI\_FREQ\_BAND\_UNKNOWN
        :   Invalid frequency band.

    enum wifi\_iface\_state
    :   Wi-Fi interface states.

        Based on [https://w1.fi/wpa\_supplicant/devel/defs\_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc](https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc)

        *Values:*

        enumerator WIFI\_STATE\_DISCONNECTED = 0
        :   Interface is disconnected.

        enumerator WIFI\_STATE\_INTERFACE\_DISABLED
        :   Interface is disabled (administratively).

        enumerator WIFI\_STATE\_INACTIVE
        :   No enabled networks in the configuration.

        enumerator WIFI\_STATE\_SCANNING
        :   Interface is scanning for networks.

        enumerator WIFI\_STATE\_AUTHENTICATING
        :   Authentication with a network is in progress.

        enumerator WIFI\_STATE\_ASSOCIATING
        :   Association with a network is in progress.

        enumerator WIFI\_STATE\_ASSOCIATED
        :   Association with a network completed.

        enumerator WIFI\_STATE\_4WAY\_HANDSHAKE
        :   4-way handshake with a network is in progress.

        enumerator WIFI\_STATE\_GROUP\_HANDSHAKE
        :   Group Key exchange with a network is in progress.

        enumerator WIFI\_STATE\_COMPLETED
        :   All authentication completed, ready to pass data.

    enum wifi\_iface\_mode
    :   Wi-Fi interface modes.

        Based on [https://w1.fi/wpa\_supplicant/devel/defs\_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc](https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc)

        *Values:*

        enumerator WIFI\_MODE\_INFRA = 0
        :   Infrastructure station mode.

        enumerator WIFI\_MODE\_IBSS = 1
        :   IBSS (ad-hoc) station mode.

        enumerator WIFI\_MODE\_AP = 2
        :   AP mode.

        enumerator WIFI\_MODE\_P2P\_GO = 3
        :   P2P group owner mode.

        enumerator WIFI\_MODE\_P2P\_GROUP\_FORMATION = 4
        :   P2P group formation mode.

        enumerator WIFI\_MODE\_MESH = 5
        :   802.11s Mesh mode.

    enum wifi\_link\_mode
    :   Wi-Fi link operating modes.

        As per [https://en.wikipedia.org/wiki/Wi-Fi#Versions\_and\_generations](https://en.wikipedia.org/wiki/Wi-Fi#Versions_and_generations).

        *Values:*

        enumerator WIFI\_0 = 0
        :   802.11 (legacy).

        enumerator WIFI\_1
        :   802.11b.

        enumerator WIFI\_2
        :   802.11a.

        enumerator WIFI\_3
        :   802.11g.

        enumerator WIFI\_4
        :   802.11n.

        enumerator WIFI\_5
        :   802.11ac.

        enumerator WIFI\_6
        :   802.11ax.

        enumerator WIFI\_6E
        :   802.11ax 6GHz.

        enumerator WIFI\_7
        :   802.11be.

    enum wifi\_scan\_type
    :   Wi-Fi scanning types.

        *Values:*

        enumerator WIFI\_SCAN\_TYPE\_ACTIVE = 0
        :   Active scanning (default).

        enumerator WIFI\_SCAN\_TYPE\_PASSIVE
        :   Passive scanning.

    enum wifi\_ps
    :   Wi-Fi power save states.

        *Values:*

        enumerator WIFI\_PS\_DISABLED = 0
        :   Power save disabled.

        enumerator WIFI\_PS\_ENABLED
        :   Power save enabled.

    enum wifi\_ps\_mode
    :   Wi-Fi power save modes.

        *Values:*

        enumerator WIFI\_PS\_MODE\_LEGACY = 0
        :   Legacy power save mode.

        enumerator WIFI\_PS\_MODE\_WMM
        :   WMM power save mode.

    enum wifi\_operational\_modes
    :   Wifi operational mode.

        *Values:*

        enumerator WIFI\_STA\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   STA mode setting enable.

        enumerator WIFI\_MONITOR\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Monitor mode setting enable.

        enumerator WIFI\_TX\_INJECTION\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   TX injection mode setting enable.

        enumerator WIFI\_PROMISCUOUS\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Promiscuous mode setting enable.

        enumerator WIFI\_AP\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   AP mode setting enable.

        enumerator WIFI\_SOFTAP\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Softap mode setting enable.

    enum wifi\_filter
    :   Mode filter settings.

        *Values:*

        enumerator WIFI\_PACKET\_FILTER\_ALL = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Support management, data and control packet sniffing.

        enumerator WIFI\_PACKET\_FILTER\_MGMT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Support only sniffing of management packets.

        enumerator WIFI\_PACKET\_FILTER\_DATA = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Support only sniffing of data packets.

        enumerator WIFI\_PACKET\_FILTER\_CTRL = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Support only sniffing of control packets.

    enum wifi\_twt\_operation
    :   Wi-Fi Target Wake Time (TWT) operations.

        *Values:*

        enumerator WIFI\_TWT\_SETUP = 0
        :   TWT setup operation.

        enumerator WIFI\_TWT\_TEARDOWN
        :   TWT teardown operation.

    enum wifi\_twt\_negotiation\_type
    :   Wi-Fi Target Wake Time (TWT) negotiation types.

        *Values:*

        enumerator WIFI\_TWT\_INDIVIDUAL = 0
        :   TWT individual negotiation.

        enumerator WIFI\_TWT\_BROADCAST
        :   TWT broadcast negotiation.

        enumerator WIFI\_TWT\_WAKE\_TBTT
        :   TWT wake TBTT negotiation.

    enum wifi\_twt\_setup\_cmd
    :   Wi-Fi Target Wake Time (TWT) setup commands.

        *Values:*

        enumerator WIFI\_TWT\_SETUP\_CMD\_REQUEST = 0
        :   TWT setup request.

        enumerator WIFI\_TWT\_SETUP\_CMD\_SUGGEST
        :   TWT setup suggest (parameters can be changed by AP).

        enumerator WIFI\_TWT\_SETUP\_CMD\_DEMAND
        :   TWT setup demand (parameters can not be changed by AP).

        enumerator WIFI\_TWT\_SETUP\_CMD\_GROUPING
        :   TWT setup grouping (grouping of TWT flows).

        enumerator WIFI\_TWT\_SETUP\_CMD\_ACCEPT
        :   TWT setup accept (parameters accepted by AP).

        enumerator WIFI\_TWT\_SETUP\_CMD\_ALTERNATE
        :   TWT setup alternate (alternate parameters suggested by AP).

        enumerator WIFI\_TWT\_SETUP\_CMD\_DICTATE
        :   TWT setup dictate (parameters dictated by AP).

        enumerator WIFI\_TWT\_SETUP\_CMD\_REJECT
        :   TWT setup reject (parameters rejected by AP).

    enum wifi\_twt\_setup\_resp\_status
    :   Wi-Fi Target Wake Time (TWT) negotiation status.

        *Values:*

        enumerator WIFI\_TWT\_RESP\_RECEIVED = 0
        :   TWT response received for TWT request.

        enumerator WIFI\_TWT\_RESP\_NOT\_RECEIVED
        :   TWT response not received for TWT request.

    enum wifi\_twt\_fail\_reason
    :   Target Wake Time (TWT) error codes.

        *Values:*

        enumerator WIFI\_TWT\_FAIL\_UNSPECIFIED
        :   Unspecified error.

        enumerator WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL
        :   Command execution failed.

        enumerator WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED
        :   Operation not supported.

        enumerator WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS
        :   Unable to get interface status.

        enumerator WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED
        :   Device not connected to AP.

        enumerator WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB
        :   Peer not HE (802.11ax/Wi-Fi 6) capable.

        enumerator WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB
        :   Peer not TWT capable.

        enumerator WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS
        :   A TWT flow is already in progress.

        enumerator WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID
        :   Invalid negotiated flow id.

        enumerator WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED
        :   IP address not assigned or configured.

        enumerator WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS
        :   Flow already exists.

    enum wifi\_twt\_teardown\_status
    :   Wi-Fi Target Wake Time (TWT) teradown status.

        *Values:*

        enumerator WIFI\_TWT\_TEARDOWN\_SUCCESS = 0
        :   TWT teardown success.

        enumerator WIFI\_TWT\_TEARDOWN\_FAILED
        :   TWT teardown failure.

    enum wifi\_ps\_param\_type
    :   Wi-Fi power save parameters.

        *Values:*

        enumerator WIFI\_PS\_PARAM\_STATE
        :   Power save state.

        enumerator WIFI\_PS\_PARAM\_LISTEN\_INTERVAL
        :   Power save listen interval.

        enumerator WIFI\_PS\_PARAM\_WAKEUP\_MODE
        :   Power save wakeup mode.

        enumerator WIFI\_PS\_PARAM\_MODE
        :   Power save mode.

        enumerator WIFI\_PS\_PARAM\_TIMEOUT
        :   Power save timeout.

    enum wifi\_ps\_wakeup\_mode
    :   Wi-Fi power save modes.

        *Values:*

        enumerator WIFI\_PS\_WAKEUP\_MODE\_DTIM = 0
        :   DTIM based wakeup.

        enumerator WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL
        :   Listen interval based wakeup.

    enum wifi\_config\_ps\_param\_fail\_reason
    :   Wi-Fi power save error codes.

        *Values:*

        enumerator WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED
        :   Unspecified error.

        enumerator WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL
        :   Command execution failed.

        enumerator WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED
        :   Parameter not supported.

        enumerator WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS
        :   Unable to get interface status.

        enumerator WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED
        :   Device not connected to AP.

        enumerator WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED
        :   Device already connected to AP.

        enumerator WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID
        :   Listen interval out of range.

    enum wifi\_ap\_config\_param
    :   Wi-Fi AP mode configuration parameter.

        *Values:*

        enumerator WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Used for AP mode configuration parameter ap\_max\_inactivity.

        enumerator WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Used for AP mode configuration parameter max\_num\_sta.

    enum net\_request\_wifi\_cmd
    :   Wi-Fi management commands.

        *Values:*

        enumerator NET\_REQUEST\_WIFI\_CMD\_SCAN = 1
        :   Scan for Wi-Fi networks.

        enumerator NET\_REQUEST\_WIFI\_CMD\_CONNECT
        :   Connect to a Wi-Fi network.

        enumerator NET\_REQUEST\_WIFI\_CMD\_DISCONNECT
        :   Disconnect from a Wi-Fi network.

        enumerator NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE
        :   Enable AP mode.

        enumerator NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE
        :   Disable AP mode.

        enumerator NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS
        :   Get interface status.

        enumerator NET\_REQUEST\_WIFI\_CMD\_PS
        :   Set power save status.

        enumerator NET\_REQUEST\_WIFI\_CMD\_TWT
        :   Setup or teardown TWT flow.

        enumerator NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG
        :   Get power save config.

        enumerator NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN
        :   Set or get regulatory domain.

        enumerator NET\_REQUEST\_WIFI\_CMD\_MODE
        :   Set or get Mode of operation.

        enumerator NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER
        :   Set or get packet filter setting for current mode.

        enumerator NET\_REQUEST\_WIFI\_CMD\_CHANNEL
        :   Set or get Wi-Fi channel for Monitor or TX-Injection mode.

        enumerator NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT
        :   Disconnect a STA from AP.

        enumerator NET\_REQUEST\_WIFI\_CMD\_VERSION
        :   Get Wi-Fi driver and Firmware versions.

        enumerator NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD
        :   Set RTS threshold.

        enumerator NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM
        :   Configure AP parameter.

    enum net\_event\_wifi\_cmd
    :   Wi-Fi management events.

        *Values:*

        enumerator NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT = 1
        :   Scan results available.

        enumerator NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE
        :   Scan done.

        enumerator NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT
        :   Connect result.

        enumerator NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT
        :   Disconnect result.

        enumerator NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS
        :   Interface status.

        enumerator NET\_EVENT\_WIFI\_CMD\_TWT
        :   TWT events.

        enumerator NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE
        :   TWT sleep status: awake or sleeping, can be used by application to determine if it can send data or not.

        enumerator NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT
        :   Raw scan results available.

        enumerator NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE
        :   Disconnect complete.

        enumerator NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT
        :   AP mode enable result.

        enumerator NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT
        :   AP mode disable result.

        enumerator NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED
        :   STA connected to AP.

        enumerator NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED
        :   STA disconnected from AP.

    enum wifi\_conn\_status
    :   Wi-Fi connect result codes.

        To be overlaid on top of [wifi\_status](#structwifi__status) in the connect result event for detailed status.

        *Values:*

        enumerator WIFI\_STATUS\_CONN\_SUCCESS = 0
        :   Connection successful.

        enumerator WIFI\_STATUS\_CONN\_FAIL
        :   Connection failed - generic failure.

        enumerator WIFI\_STATUS\_CONN\_WRONG\_PASSWORD
        :   Connection failed - wrong password Few possible reasons for 4-way handshake failure that we can guess are as follows: 1) Incorrect key 2) EAPoL frames lost causing timeout.

            #1 is the likely cause, so, we convey to the user that it is due to Wrong passphrase/password.

        enumerator WIFI\_STATUS\_CONN\_TIMEOUT
        :   Connection timed out.

        enumerator WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND
        :   Connection failed - AP not found.

        enumerator WIFI\_STATUS\_CONN\_LAST\_STATUS
        :   Last connection status.

        enumerator WIFI\_STATUS\_DISCONN\_FIRST\_STATUS = [WIFI\_STATUS\_CONN\_LAST\_STATUS](#c.wifi_conn_status.WIFI_STATUS_CONN_LAST_STATUS)
        :   Connection disconnected status.

    enum wifi\_disconn\_reason
    :   Wi-Fi disconnect reason codes.

        To be overlaid on top of [wifi\_status](#structwifi__status) in the disconnect result event for detailed reason.

        *Values:*

        enumerator WIFI\_REASON\_DISCONN\_SUCCESS = 0
        :   Success, overload status as reason.

        enumerator WIFI\_REASON\_DISCONN\_UNSPECIFIED
        :   Unspecified reason.

        enumerator WIFI\_REASON\_DISCONN\_USER\_REQUEST
        :   Disconnected due to user request.

        enumerator WIFI\_REASON\_DISCONN\_AP\_LEAVING
        :   Disconnected due to AP leaving.

        enumerator WIFI\_REASON\_DISCONN\_INACTIVITY
        :   Disconnected due to inactivity.

    enum wifi\_ap\_status
    :   Wi-Fi AP mode result codes.

        To be overlaid on top of [wifi\_status](#structwifi__status) in the AP mode enable or disable result event for detailed status.

        *Values:*

        enumerator WIFI\_STATUS\_AP\_SUCCESS = 0
        :   AP mode enable or disable successful.

        enumerator WIFI\_STATUS\_AP\_FAIL
        :   AP mode enable or disable failed - generic failure.

        enumerator WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED
        :   AP mode enable failed - channel not supported.

        enumerator WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED
        :   AP mode enable failed - channel not allowed.

        enumerator WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED
        :   AP mode enable failed - SSID not allowed.

        enumerator WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED
        :   AP mode enable failed - authentication type not supported.

        enumerator WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED
        :   AP mode enable failed - operation not supported.

        enumerator WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED
        :   AP mode enable failed - operation not permitted.

    enum wifi\_mgmt\_op
    :   Generic get/set operation for any command.

        *Values:*

        enumerator WIFI\_MGMT\_GET = 0
        :   Get operation.

        enumerator WIFI\_MGMT\_SET = 1
        :   Set operation.

    enum wifi\_twt\_sleep\_state
    :   Wi-Fi TWT sleep states.

        *Values:*

        enumerator WIFI\_TWT\_STATE\_SLEEP = 0
        :   TWT sleep state: sleeping.

        enumerator WIFI\_TWT\_STATE\_AWAKE = 1
        :   TWT sleep state: awake.

    Functions

    const char \*wifi\_security\_txt(enum [wifi\_security\_type](#c.wifi_security_type) security)
    :   Helper function to get user-friendly security type name.

    const char \*wifi\_mfp\_txt(enum [wifi\_mfp\_options](#c.wifi_mfp_options) mfp)
    :   Helper function to get user-friendly MFP name.

    const char \*wifi\_band\_txt(enum [wifi\_frequency\_bands](#c.wifi_frequency_bands) band)
    :   Helper function to get user-friendly frequency band name.

    const char \*wifi\_state\_txt(enum [wifi\_iface\_state](#c.wifi_iface_state) state)
    :   Helper function to get user-friendly interface state name.

    const char \*wifi\_mode\_txt(enum [wifi\_iface\_mode](#c.wifi_iface_mode) mode)
    :   Helper function to get user-friendly interface mode name.

    const char \*wifi\_link\_mode\_txt(enum [wifi\_link\_mode](#c.wifi_link_mode) link\_mode)
    :   Helper function to get user-friendly link mode name.

    const char \*wifi\_ps\_txt(enum [wifi\_ps](#c.wifi_ps) ps\_name)
    :   Helper function to get user-friendly ps name.

    const char \*wifi\_ps\_mode\_txt(enum [wifi\_ps\_mode](#c.wifi_ps_mode) ps\_mode)
    :   Helper function to get user-friendly ps mode name.

    const char \*wifi\_twt\_operation\_txt(enum [wifi\_twt\_operation](#c.wifi_twt_operation) twt\_operation)
    :   Helper function to get user-friendly twt operation name.

    const char \*wifi\_twt\_negotiation\_type\_txt(enum [wifi\_twt\_negotiation\_type](#c.wifi_twt_negotiation_type) twt\_negotiation)
    :   Helper function to get user-friendly twt negotiation type name.

    const char \*wifi\_twt\_setup\_cmd\_txt(enum [wifi\_twt\_setup\_cmd](#c.wifi_twt_setup_cmd) twt\_setup)
    :   Helper function to get user-friendly twt setup cmd name.

    static inline const char \*wifi\_twt\_get\_err\_code\_str(int16\_t err\_no)
    :   Helper function to get user-friendly TWT error code name.

    const char \*wifi\_ps\_wakeup\_mode\_txt(enum [wifi\_ps\_wakeup\_mode](#c.wifi_ps_wakeup_mode) ps\_wakeup\_mode)
    :   Helper function to get user-friendly ps wakeup mode name.

    static inline const char \*wifi\_ps\_get\_config\_err\_code\_str(int16\_t err\_no)
    :   Helper function to get user-friendly power save error code name.

    void wifi\_mgmt\_raise\_connect\_result\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, int status)
    :   Wi-Fi management connect result event.

        Parameters:
        :   - **iface** – Network interface
            - **status** – Connect result status

    void wifi\_mgmt\_raise\_disconnect\_result\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, int status)
    :   Wi-Fi management disconnect result event.

        Parameters:
        :   - **iface** – Network interface
            - **status** – Disconnect result status

    void wifi\_mgmt\_raise\_iface\_status\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [wifi\_iface\_status](#c.wifi_iface_status) \*iface\_status)
    :   Wi-Fi management interface status event.

        Parameters:
        :   - **iface** – Network interface
            - **iface\_status** – Interface status

    void wifi\_mgmt\_raise\_twt\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [wifi\_twt\_params](#c.wifi_twt_params) \*twt\_params)
    :   Wi-Fi management TWT event.

        Parameters:
        :   - **iface** – Network interface
            - **twt\_params** – TWT parameters

    void wifi\_mgmt\_raise\_twt\_sleep\_state(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, int twt\_sleep\_state)
    :   Wi-Fi management TWT sleep state event.

        Parameters:
        :   - **iface** – Network interface
            - **twt\_sleep\_state** – TWT sleep state

    void wifi\_mgmt\_raise\_raw\_scan\_result\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [wifi\_raw\_scan\_result](#c.wifi_raw_scan_result) \*raw\_scan\_info)
    :   Wi-Fi management raw scan result event.

        Parameters:
        :   - **iface** – Network interface
            - **raw\_scan\_info** – Raw scan result

    void wifi\_mgmt\_raise\_disconnect\_complete\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, int status)
    :   Wi-Fi management disconnect complete event.

        Parameters:
        :   - **iface** – Network interface
            - **status** – Disconnect complete status

    void wifi\_mgmt\_raise\_ap\_enable\_result\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, enum [wifi\_ap\_status](#c.wifi_ap_status) status)
    :   Wi-Fi management AP mode enable result event.

        Parameters:
        :   - **iface** – Network interface
            - **status** – AP mode enable result status

    void wifi\_mgmt\_raise\_ap\_disable\_result\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, enum [wifi\_ap\_status](#c.wifi_ap_status) status)
    :   Wi-Fi management AP mode disable result event.

        Parameters:
        :   - **iface** – Network interface
            - **status** – AP mode disable result status

    void wifi\_mgmt\_raise\_ap\_sta\_connected\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [wifi\_ap\_sta\_info](#c.wifi_ap_sta_info) \*sta\_info)
    :   Wi-Fi management AP mode STA connected event.

        Parameters:
        :   - **iface** – Network interface
            - **sta\_info** – STA information

    void wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [wifi\_ap\_sta\_info](#c.wifi_ap_sta_info) \*sta\_info)
    :   Wi-Fi management AP mode STA disconnected event.

        Parameters:
        :   - **iface** – Network interface
            - **sta\_info** – STA information

    struct wifi\_version
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi version.

        Public Members

        const char \*drv\_version
        :   Driver version.

        const char \*fw\_version
        :   Firmware version.

    struct wifi\_band\_channel
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi structure to uniquely identify a band-channel pair.

        Public Members

        uint8\_t band
        :   Frequency band.

        uint8\_t channel
        :   Channel.

    struct wifi\_scan\_params
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi scan parameters structure.

        Used to specify parameters which can control how the Wi-Fi scan is performed.

        Public Members

        enum [wifi\_scan\_type](#c.wifi_scan_type) scan\_type
        :   Scan type, see enum [wifi\_scan\_type](#group__wifi__mgmt_1gad30e29eda65ccafdbd7f11865937b8ea).

            The scan\_type is only a hint to the underlying Wi-Fi chip for the preferred mode of scan. The actual mode of scan can depend on factors such as the Wi-Fi chip implementation support, regulatory domain restrictions etc.

        uint8\_t bands
        :   Bitmap of bands to be scanned.

            Refer to [wifi\_frequency\_bands](#group__wifi__mgmt_1ga1e2f0439a322355fa7368ea880c9c15d) for bit position of each band.

        uint16\_t dwell\_time\_active
        :   Active scan dwell time (in ms) on a channel.

        uint16\_t dwell\_time\_passive
        :   Passive scan dwell time (in ms) on a channel.

        const char \*ssids[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX]
        :   Array of SSID strings to scan.

        uint16\_t max\_bss\_cnt
        :   Specifies the maximum number of scan results to return.

            These results would be the BSSIDS with the best RSSI values, in all the scanned channels. This should only be used to limit the number of returned scan results, and cannot be counted upon to limit the scan time, since the underlying Wi-Fi chip might have to scan all the channels to find the max\_bss\_cnt number of APs with the best signal strengths. A value of 0 signifies that there is no restriction on the number of scan results to be returned.

        struct [wifi\_band\_channel](#c.wifi_band_channel) band\_chan[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL]
        :   Channel information array indexed on Wi-Fi frequency bands and channels within that band.

            E.g. to scan channel 6 and 11 on the 2.4 GHz band, channel 36 on the 5 GHz band:

            ```c
            chan[0] = {WIFI_FREQ_BAND_2_4_GHZ, 6};
            chan[1] = {WIFI_FREQ_BAND_2_4_GHZ, 11};
            chan[2] = {WIFI_FREQ_BAND_5_GHZ, 36};
            ```

            This list specifies the channels to be **considered for scan**. The underlying Wi-Fi chip can silently omit some channels due to various reasons such as channels not conforming to regulatory restrictions etc. The invoker of the API should ensure that the channels specified follow regulatory rules.

    struct wifi\_scan\_result
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi scan result, each result is provided to the [net\_mgmt\_event\_callback](net_mgmt.md#structnet__mgmt__event__callback) via its info attribute (see net\_mgmt.h).

        Public Members

        uint8\_t ssid[32]
        :   SSID.

        uint8\_t ssid\_length
        :   SSID length.

        uint8\_t band
        :   Frequency band.

        uint8\_t channel
        :   Channel.

        enum [wifi\_security\_type](#c.wifi_security_type) security
        :   Security type.

        enum [wifi\_mfp\_options](#c.wifi_mfp_options) mfp
        :   MFP options.

        int8\_t rssi
        :   RSSI.

        uint8\_t mac[6]
        :   BSSID.

        uint8\_t mac\_length
        :   BSSID length.

    struct wifi\_connect\_req\_params
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi connect request parameters.

        Public Members

        const uint8\_t \*ssid
        :   SSID.

        uint8\_t ssid\_length
        :   SSID length.

        const uint8\_t \*psk
        :   Pre-shared key.

        uint8\_t psk\_length
        :   Pre-shared key length.

        const uint8\_t \*sae\_password
        :   SAE password (same as PSK but with no length restrictions), optional.

        uint8\_t sae\_password\_length
        :   SAE password length.

        uint8\_t band
        :   Frequency band.

        uint8\_t channel
        :   Channel.

        enum [wifi\_security\_type](#c.wifi_security_type) security
        :   Security type.

        enum [wifi\_mfp\_options](#c.wifi_mfp_options) mfp
        :   MFP options.

        uint8\_t bssid[6]
        :   BSSID.

        int timeout
        :   Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

    struct wifi\_status
    :   *#include <wifi\_mgmt.h>*

        Generic Wi-Fi status for commands and events.

        Public Members

        int status
        :   Status value.

        enum [wifi\_conn\_status](#c.wifi_conn_status) conn\_status
        :   Connection status.

        enum [wifi\_disconn\_reason](#c.wifi_disconn_reason) disconn\_reason
        :   Disconnection reason status.

        enum [wifi\_ap\_status](#c.wifi_ap_status) ap\_status
        :   Access point status.

    struct wifi\_iface\_status
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi interface status.

        Public Members

        int state
        :   Interface state, see enum [wifi\_iface\_state](#group__wifi__mgmt_1ga981961f747b919d61d3ccbd41e4508b4).

        unsigned int ssid\_len
        :   SSID length.

        char ssid[32]
        :   SSID.

        char bssid[6]
        :   BSSID.

        enum [wifi\_frequency\_bands](#c.wifi_frequency_bands) band
        :   Frequency band.

        unsigned int channel
        :   Channel.

        enum [wifi\_iface\_mode](#c.wifi_iface_mode) iface\_mode
        :   Interface mode, see enum [wifi\_iface\_mode](#group__wifi__mgmt_1ga584f6239ac14e2bedc5e6bd72756423b).

        enum [wifi\_link\_mode](#c.wifi_link_mode) link\_mode
        :   Link mode, see enum [wifi\_link\_mode](#group__wifi__mgmt_1gabdb2a784d4727b71ab44cca04e422c62).

        enum [wifi\_security\_type](#c.wifi_security_type) security
        :   Security type, see enum [wifi\_security\_type](#group__wifi__mgmt_1gadde31a04fa25ed805115c6b31854cd9c).

        enum [wifi\_mfp\_options](#c.wifi_mfp_options) mfp
        :   MFP options, see enum [wifi\_mfp\_options](#group__wifi__mgmt_1ga1f252da47d9650023d7fff6d08e49c76).

        int rssi
        :   RSSI.

        unsigned char dtim\_period
        :   DTIM period.

        unsigned short beacon\_interval
        :   Beacon interval.

        bool twt\_capable
        :   is TWT capable?

    struct wifi\_ps\_params
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi power save parameters.

        Public Members

        enum [wifi\_ps](#c.wifi_ps) enabled
        :   Power save state.

        unsigned short listen\_interval
        :   Listen interval.

        enum [wifi\_ps\_wakeup\_mode](#c.wifi_ps_wakeup_mode) wakeup\_mode
        :   Wi-Fi power save wakeup mode.

        enum [wifi\_ps\_mode](#c.wifi_ps_mode) mode
        :   Wi-Fi power save mode.

        unsigned int timeout\_ms
        :   Wi-Fi power save timeout.

            This is the time out to wait after sending a TX packet before going back to power save (in ms) to receive any replies from the AP. Zero means this feature is disabled.

            It’s a tradeoff between power consumption and latency.

        enum [wifi\_ps\_param\_type](#c.wifi_ps_param_type) type
        :   Wi-Fi power save type.

        enum [wifi\_config\_ps\_param\_fail\_reason](#c.wifi_config_ps_param_fail_reason) fail\_reason
        :   Wi-Fi power save fail reason.

    struct wifi\_twt\_params
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi TWT parameters.

        Public Members

        enum [wifi\_twt\_operation](#c.wifi_twt_operation) operation
        :   TWT operation, see enum [wifi\_twt\_operation](#group__wifi__mgmt_1gad0e998aeb1b27c4f203ca76339d323a3).

        enum [wifi\_twt\_negotiation\_type](#c.wifi_twt_negotiation_type) negotiation\_type
        :   TWT negotiation type, see enum [wifi\_twt\_negotiation\_type](#group__wifi__mgmt_1ga695123cd534e2499f516a07fdc5cafa8).

        enum [wifi\_twt\_setup\_cmd](#c.wifi_twt_setup_cmd) setup\_cmd
        :   TWT setup command, see enum [wifi\_twt\_setup\_cmd](#group__wifi__mgmt_1ga31c78afc89bfdc4b54cee177843f8022).

        enum [wifi\_twt\_setup\_resp\_status](#c.wifi_twt_setup_resp_status) resp\_status
        :   TWT setup response status, see enum [wifi\_twt\_setup\_resp\_status](#group__wifi__mgmt_1ga4d03aedac13ee4512d7717ac624f319a).

        enum [wifi\_twt\_teardown\_status](#c.wifi_twt_teardown_status) teardown\_status
        :   TWT teardown cmd status, see enum [wifi\_twt\_teardown\_status](#group__wifi__mgmt_1gad3709d07aaa3ed59b48f9dd7bd181989).

        uint8\_t dialog\_token
        :   Dialog token, used to map requests to responses.

        uint8\_t flow\_id
        :   Flow ID, used to map setup with teardown.

        uint64\_t twt\_interval
        :   Interval = Wake up time + Sleeping time.

        bool responder
        :   Requestor or responder.

        bool trigger
        :   Trigger enabled or disabled.

        bool implicit
        :   Implicit or explicit.

        bool announce
        :   Announced or unannounced.

        uint32\_t twt\_wake\_interval
        :   Wake up time.

        uint32\_t twt\_wake\_ahead\_duration
        :   Wake ahead notification is sent earlier than TWT Service period (SP) start based on this duration.

            This should give applications ample time to prepare the data before TWT SP starts.

        struct [wifi\_twt\_params](#c.wifi_twt_params).[anonymous].[anonymous] setup
        :   Setup specific parameters.

        bool teardown\_all
        :   Teardown all flows.

        struct [wifi\_twt\_params](#c.wifi_twt_params).[anonymous].[anonymous] teardown
        :   Teardown specific parameters.

        enum [wifi\_twt\_fail\_reason](#c.wifi_twt_fail_reason) fail\_reason
        :   TWT fail reason, see enum [wifi\_twt\_fail\_reason](#group__wifi__mgmt_1ga97fa304f9a1db2294a93cccd4c93bcf6).

    struct wifi\_twt\_flow\_info
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi TWT flow information.

        Public Members

        uint64\_t twt\_interval
        :   Interval = Wake up time + Sleeping time.

        uint8\_t dialog\_token
        :   Dialog token, used to map requests to responses.

        uint8\_t flow\_id
        :   Flow ID, used to map setup with teardown.

        enum [wifi\_twt\_negotiation\_type](#c.wifi_twt_negotiation_type) negotiation\_type
        :   TWT negotiation type, see enum [wifi\_twt\_negotiation\_type](#group__wifi__mgmt_1ga695123cd534e2499f516a07fdc5cafa8).

        bool responder
        :   Requestor or responder.

        bool trigger
        :   Trigger enabled or disabled.

        bool implicit
        :   Implicit or explicit.

        bool announce
        :   Announced or unannounced.

        uint32\_t twt\_wake\_interval
        :   Wake up time.

        uint32\_t twt\_wake\_ahead\_duration
        :   Wake ahead duration.

    struct wifi\_ps\_config
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi power save configuration.

        Public Members

        char num\_twt\_flows
        :   Number of TWT flows.

        struct [wifi\_twt\_flow\_info](#c.wifi_twt_flow_info) twt\_flows[WIFI\_MAX\_TWT\_FLOWS]
        :   TWT flow details.

        struct [wifi\_ps\_params](#c.wifi_ps_params) ps\_params
        :   Power save configuration.

    struct wifi\_reg\_chan\_info
    :   *#include <wifi\_mgmt.h>*

        Per-channel regulatory attributes.

        Public Members

        unsigned short center\_frequency
        :   Center frequency in MHz.

        unsigned short max\_power
        :   Maximum transmission power (in dBm).

        unsigned short supported
        :   Is channel supported or not.

        unsigned short passive\_only
        :   Passive transmissions only.

        unsigned short dfs
        :   Is a DFS channel.

    struct wifi\_reg\_domain
    :   *#include <wifi\_mgmt.h>*

        Regulatory domain information or configuration.

        Public Members

        enum [wifi\_mgmt\_op](#c.wifi_mgmt_op) oper
        :   Regulatory domain operation.

        bool force
        :   Ignore all other regulatory hints over this one.

        uint8\_t country\_code[2]
        :   Country code: ISO/IEC 3166-1 alpha-2.

        unsigned int num\_channels
        :   Number of channels supported.

        struct [wifi\_reg\_chan\_info](#c.wifi_reg_chan_info) \*chan\_info
        :   Channels information.

    struct wifi\_raw\_scan\_result
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi raw scan result.

        Public Members

        int8\_t rssi
        :   RSSI.

        int frame\_length
        :   Frame length.

        unsigned short frequency
        :   Frequency.

        uint8\_t data[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH]
        :   Raw scan data.

    struct wifi\_ap\_sta\_info
    :   *#include <wifi\_mgmt.h>*

        AP mode - connected STA details.

        Public Members

        enum [wifi\_link\_mode](#c.wifi_link_mode) link\_mode
        :   Link mode, see enum [wifi\_link\_mode](#group__wifi__mgmt_1gabdb2a784d4727b71ab44cca04e422c62).

        uint8\_t mac[6]
        :   MAC address.

        uint8\_t mac\_length
        :   MAC address length.

        bool twt\_capable
        :   is TWT capable ?

    struct wifi\_mode\_info
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi mode setup.

        Public Members

        uint8\_t mode
        :   Mode setting for a specific mode of operation.

        uint8\_t if\_index
        :   Interface index.

        enum [wifi\_mgmt\_op](#c.wifi_mgmt_op) oper
        :   Get or set operation.

    struct wifi\_filter\_info
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.

        Public Members

        uint8\_t filter
        :   Filter setting.

        uint8\_t if\_index
        :   Interface index.

        uint16\_t buffer\_size
        :   Filter buffer size.

        enum [wifi\_mgmt\_op](#c.wifi_mgmt_op) oper
        :   Get or set operation.

    struct wifi\_channel\_info
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi channel setting for monitor and TX-injection modes.

        Public Members

        uint16\_t channel
        :   Channel value to set.

        uint8\_t if\_index
        :   Interface index.

        enum [wifi\_mgmt\_op](#c.wifi_mgmt_op) oper
        :   Get or set operation.

    struct wifi\_ap\_config\_params
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi AP configuration parameter.

        Public Members

        enum [wifi\_ap\_config\_param](#c.wifi_ap_config_param) type
        :   Parameter used to identify the different AP parameters.

        uint32\_t max\_inactivity
        :   Parameter used for setting maximum inactivity duration for stations.

        uint32\_t max\_num\_sta
        :   Parameter used for setting maximum number of stations.

    struct wifi\_mgmt\_ops
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi management API.

        Public Members

        int (\*scan)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_scan\_params](#c.wifi_scan_params) \*params, [scan\_result\_cb\_t](#c.scan_result_cb_t) cb)
        :   Scan for Wi-Fi networks.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param params:
            :   Scan parameters

            Param cb:
            :   Callback to be called for each result cb parameter is the cb that should be called for each result by the driver. The wifi mgmt part will take care of raising the necessary event etc.

            Return:
            :   0 if ok, < 0 if error

        int (\*connect)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_connect\_req\_params](#c.wifi_connect_req_params) \*params)
        :   Connect to a Wi-Fi network.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param params:
            :   Connect parameters

            Return:
            :   0 if ok, < 0 if error

        int (\*disconnect)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Disconnect from a Wi-Fi network.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Return:
            :   0 if ok, < 0 if error

        int (\*ap\_enable)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_connect\_req\_params](#c.wifi_connect_req_params) \*params)
        :   Enable AP mode.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param params:
            :   AP mode parameters

            Return:
            :   0 if ok, < 0 if error

        int (\*ap\_disable)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Disable AP mode.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Return:
            :   0 if ok, < 0 if error

        int (\*ap\_sta\_disconnect)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*mac)
        :   Disconnect a STA from AP.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param mac:
            :   MAC address of the STA to disconnect

            Return:
            :   0 if ok, < 0 if error

        int (\*iface\_status)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_iface\_status](#c.wifi_iface_status) \*status)
        :   Get interface status.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param status:
            :   Interface status

            Return:
            :   0 if ok, < 0 if error

        int (\*get\_stats)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [net\_stats\_wifi](net_stats.md#c.net_stats_wifi "net_stats_wifi") \*stats)
        :   Get Wi-Fi statistics.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param stats:
            :   Wi-Fi statistics

            Return:
            :   0 if ok, < 0 if error

        int (\*set\_power\_save)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_ps\_params](#c.wifi_ps_params) \*params)
        :   Set power save status.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param params:
            :   Power save parameters

            Return:
            :   0 if ok, < 0 if error

        int (\*set\_twt)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_twt\_params](#c.wifi_twt_params) \*params)
        :   Setup or teardown TWT flow.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param params:
            :   TWT parameters

            Return:
            :   0 if ok, < 0 if error

        int (\*get\_power\_save\_config)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_ps\_config](#c.wifi_ps_config) \*config)
        :   Get power save config.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param config:
            :   Power save config

            Return:
            :   0 if ok, < 0 if error

        int (\*reg\_domain)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_reg\_domain](#c.wifi_reg_domain) \*reg\_domain)
        :   Set or get regulatory domain.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param reg\_domain:
            :   Regulatory domain

            Return:
            :   0 if ok, < 0 if error

        int (\*filter)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_filter\_info](#c.wifi_filter_info) \*filter)
        :   Set or get packet filter settings for monitor and promiscuous modes.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param packet:
            :   filter settings

            Return:
            :   0 if ok, < 0 if error

        int (\*mode)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_mode\_info](#c.wifi_mode_info) \*mode)
        :   Set or get mode of operation.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param mode:
            :   settings

            Return:
            :   0 if ok, < 0 if error

        int (\*channel)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_channel\_info](#c.wifi_channel_info) \*channel)
        :   Set or get current channel of operation.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param channel:
            :   settings

            Return:
            :   0 if ok, < 0 if error

        int (\*get\_version)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_version](#c.wifi_version) \*params)
        :   Get Version of WiFi driver and Firmware.

            The driver that implements the get\_version function must not use stack to allocate the version information pointers that are returned as params struct members. The version pointer parameters should point to a static memory either in ROM (preferred) or in RAM.

            Param dev:
            :   Pointer to the device structure for the driver instance

            Param params:
            :   Version parameters

            Return:
            :   0 if ok, < 0 if error

        int (\*set\_rts\_threshold)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, unsigned int rts\_threshold)
        :   Set RTS threshold value.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param RTS:
            :   threshold value

            Return:
            :   0 if ok, < 0 if error

        int (\*ap\_config\_params)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [wifi\_ap\_config\_params](#c.wifi_ap_config_params) \*params)
        :   Configure AP parameter.

            Param dev:
            :   Pointer to the device structure for the driver instance.

            Param params:
            :   AP mode parameter configuration parameter info

            Return:
            :   0 if ok, < 0 if error

    struct net\_wifi\_mgmt\_offload
    :   *#include <wifi\_mgmt.h>*

        Wi-Fi management offload API.

        Public Members

        struct [ethernet\_api](ethernet.md#c.ethernet_api "ethernet_api") wifi\_iface
        :   Mandatory to get in first position.

            A network device should indeed provide a pointer on such net\_if\_api structure. So we make current structure pointer that can be casted to a net\_if\_api structure pointer. Ethernet API

        const struct [wifi\_mgmt\_ops](#c.wifi_mgmt_ops) \*const wifi\_mgmt\_api
        :   Wi-Fi management API.

        const void \*wifi\_drv\_ops
        :   Wi-Fi supplicant driver API.
