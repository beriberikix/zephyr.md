---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/gap.html
original_path: connectivity/bluetooth/api/gap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Generic Access Profile (GAP)

## API Reference

*group* bt\_gap
:   Generic Access Profile (GAP).

    Defines

    BT\_ID\_DEFAULT
    :   Convenience macro for specifying the default identity.

        This helps make the code more readable, especially when only one identity is supported.

    BT\_DATA\_SERIALIZED\_SIZE(data\_len)
    :   Bluetooth data serialized size.

        Get the size of a serialized [bt\_data](#structbt__data) given its data length.

        Size of ‘AD Structure’->’Length’ field, equal to 1. Size of ‘AD Structure’->’Data’->’AD Type’ field, equal to 1. Size of ‘AD Structure’->’Data’->’AD Data’ field, equal to data\_len.

        See Core Specification Version 5.4 Vol. 3 Part C, 11, Figure 11.1.

    BT\_DATA(\_type, \_data, \_data\_len)
    :   Helper to declare elements of [bt\_data](#structbt__data) arrays.

        This macro is mainly for creating an array of struct [bt\_data](#structbt__data) elements which is then passed to e.g. [bt\_le\_adv\_start()](#group__bt__gap_1gad2e3caef88d52d720e8e4d21df767b02).

        Parameters:
        :   - **\_type** – Type of advertising data field
            - **\_data** – Pointer to the data field payload
            - **\_data\_len** – Number of bytes behind the \_data pointer

    BT\_DATA\_BYTES(\_type, \_bytes...)
    :   Helper to declare elements of [bt\_data](#structbt__data) arrays.

        This macro is mainly for creating an array of struct [bt\_data](#structbt__data) elements which is then passed to e.g. [bt\_le\_adv\_start()](#group__bt__gap_1gad2e3caef88d52d720e8e4d21df767b02).

        Parameters:
        :   - **\_type** – Type of advertising data field
            - **\_bytes** – Variable number of single-byte parameters

    BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer)
    :   Initialize advertising parameters.

        Parameters:
        :   - **\_options** – Advertising Options
            - **\_int\_min** – Minimum advertising interval
            - **\_int\_max** – Maximum advertising interval
            - **\_peer** – Peer address, set to NULL for undirected advertising or address of peer for directed advertising.

    BT\_LE\_ADV\_PARAM(\_options, \_int\_min, \_int\_max, \_peer)
    :   Helper to declare advertising parameters inline.

        Parameters:
        :   - **\_options** – Advertising Options
            - **\_int\_min** – Minimum advertising interval
            - **\_int\_max** – Maximum advertising interval
            - **\_peer** – Peer address, set to NULL for undirected advertising or address of peer for directed advertising.

    BT\_LE\_ADV\_CONN\_DIR(\_peer)

    BT\_LE\_ADV\_CONN

    BT\_LE\_ADV\_CONN\_NAME

    BT\_LE\_ADV\_CONN\_NAME\_AD

    BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY(\_peer)

    BT\_LE\_ADV\_NCONN
    :   Non-connectable advertising with private address.

    BT\_LE\_ADV\_NCONN\_NAME
    :   Non-connectable advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398).

    BT\_LE\_ADV\_NCONN\_IDENTITY
    :   Non-connectable advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e).

    BT\_LE\_EXT\_ADV\_CONN\_NAME
    :   Connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398).

    BT\_LE\_EXT\_ADV\_SCAN\_NAME
    :   Scannable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398).

    BT\_LE\_EXT\_ADV\_NCONN
    :   Non-connectable extended advertising with private address.

    BT\_LE\_EXT\_ADV\_NCONN\_NAME
    :   Non-connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398).

    BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY
    :   Non-connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e).

    BT\_LE\_EXT\_ADV\_CODED\_NCONN
    :   Non-connectable extended advertising on coded PHY with private address.

    BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME
    :   Non-connectable extended advertising on coded PHY with [BT\_LE\_ADV\_OPT\_USE\_NAME](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398).

    BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY
    :   Non-connectable extended advertising on coded PHY with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e).

    BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT(\_timeout, \_n\_evts)
    :   Helper to initialize extended advertising start parameters inline.

        Parameters:
        :   - **\_timeout** – Advertiser timeout
            - **\_n\_evts** – Number of advertising events

    BT\_LE\_EXT\_ADV\_START\_PARAM(\_timeout, \_n\_evts)
    :   Helper to declare extended advertising start parameters inline.

        Parameters:
        :   - **\_timeout** – Advertiser timeout
            - **\_n\_evts** – Number of advertising events

    BT\_LE\_EXT\_ADV\_START\_DEFAULT

    BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options)
    :   Helper to declare periodic advertising parameters inline.

        Parameters:
        :   - **\_int\_min** – Minimum periodic advertising interval
            - **\_int\_max** – Maximum periodic advertising interval
            - **\_options** – Periodic advertising properties bitfield.

    BT\_LE\_PER\_ADV\_PARAM(\_int\_min, \_int\_max, \_options)
    :   Helper to declare periodic advertising parameters inline.

        Parameters:
        :   - **\_int\_min** – Minimum periodic advertising interval
            - **\_int\_max** – Maximum periodic advertising interval
            - **\_options** – Periodic advertising properties bitfield.

    BT\_LE\_PER\_ADV\_DEFAULT

    BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST

    BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window)
    :   Initialize scan parameters.

        Parameters:
        :   - **\_type** – Scan Type, BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE.
            - **\_options** – Scan options
            - **\_interval** – Scan Interval (N \* 0.625 ms)
            - **\_window** – Scan Window (N \* 0.625 ms)

    BT\_LE\_SCAN\_PARAM(\_type, \_options, \_interval, \_window)
    :   Helper to declare scan parameters inline.

        Parameters:
        :   - **\_type** – Scan Type, BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE.
            - **\_options** – Scan options
            - **\_interval** – Scan Interval (N \* 0.625 ms)
            - **\_window** – Scan Window (N \* 0.625 ms)

    BT\_LE\_SCAN\_ACTIVE
    :   Helper macro to enable active scanning to discover new devices.

    BT\_LE\_SCAN\_PASSIVE
    :   Helper macro to enable passive scanning to discover new devices.

        This macro should be used if information required for device identification (e.g., UUID) are known to be placed in Advertising Data.

    BT\_LE\_SCAN\_CODED\_ACTIVE
    :   Helper macro to enable active scanning to discover new devices.

        Include scanning on Coded PHY in addition to 1M PHY.

    BT\_LE\_SCAN\_CODED\_PASSIVE
    :   Helper macro to enable passive scanning to discover new devices.

        Include scanning on Coded PHY in addition to 1M PHY.

        This macro should be used if information required for device identification (e.g., UUID) are known to be placed in Advertising Data.

    Typedefs

    typedef void (\*bt\_ready\_cb\_t)(int err)
    :   Callback for notifying that Bluetooth has been enabled.

        Param err:
        :   zero on success or (negative) error code otherwise.

    typedef void bt\_le\_scan\_cb\_t(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr, int8\_t rssi, uint8\_t adv\_type, struct [net\_buf\_simple](../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Callback type for reporting LE scan results.

        A function of this type is given to the [bt\_le\_scan\_start()](#group__bt__gap_1gac5e19c26b53a08dadb8efa7ecc692ad6) function and will be called for any discovered LE device.

        Param addr:
        :   Advertiser LE address and type.

        Param rssi:
        :   Strength of advertiser signal.

        Param adv\_type:
        :   Type of advertising response from advertiser. Uses the BT\_GAP\_ADV\_TYPE\_\* values.

        Param buf:
        :   Buffer containing advertiser data.

    typedef void bt\_br\_discovery\_cb\_t(struct [bt\_br\_discovery\_result](#c.bt_br_discovery_result) \*results, size\_t count)
    :   Callback type for reporting BR/EDR discovery (inquiry) results.

        A callback of this type is given to the [bt\_br\_discovery\_start()](#group__bt__gap_1gaf7efa6302cde58a10efaf0b68f5cb3c6) function and will be called at the end of the discovery with information about found devices populated in the results array.

        Param results:
        :   Storage used for discovery results

        Param count:
        :   Number of valid discovery results.

    Enums

    enum [anonymous]
    :   Advertising options.

        *Values:*

        enumerator BT\_LE\_ADV\_OPT\_NONE = 0
        :   Convenience value when no options are specified.

        enumerator BT\_LE\_ADV\_OPT\_CONNECTABLE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Advertise as connectable.

            Advertise as connectable. If not connectable then the type of advertising is determined by providing scan response data. The advertiser address is determined by the type of advertising and/or enabling privacy  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") .

        enumerator BT\_LE\_ADV\_OPT\_ONE\_TIME = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Advertise one time.

            Don’t try to resume connectable advertising after a connection. This option is only meaningful when used together with BT\_LE\_ADV\_OPT\_CONNECTABLE. If set the advertising will be stopped when [bt\_le\_adv\_stop()](#group__bt__gap_1ga1776e310b9d80898e6b32d50c4fe0b49) is called or when an incoming (peripheral) connection happens. If this option is not set the stack will take care of keeping advertising enabled even as connections occur. If Advertising directed or the advertiser was started with [bt\_le\_ext\_adv\_start](#group__bt__gap_1gaddc6da5166cd8415d2b367380447eac1) then this behavior is the default behavior and this flag has no effect.

        enumerator BT\_LE\_ADV\_OPT\_USE\_IDENTITY = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Advertise using identity address.

            Advertise using the identity address as the advertiser address.

            Note

            The address used for advertising will not be the same as returned by [bt\_le\_oob\_get\_local](#group__bt__gap_1ga296d1adf3c9ed2f2c65bb75b887d59ee), instead [bt\_id\_get](#group__bt__gap_1ga06d0ae35cbf4382679cc3cfe612cee4d) should be used to get the LE address.

            Warning

            This will compromise the privacy of the device, so care must be taken when using this option.

        enumerator BT\_LE\_ADV\_OPT\_USE\_NAME = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Advertise using GAP device name.

            Include the GAP device name automatically when advertising. By default the GAP device name is put at the end of the scan response data. When advertising using [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) and not [BT\_LE\_ADV\_OPT\_SCANNABLE](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) then it will be put at the end of the advertising data. If the GAP device name does not fit into advertising data it will be converted to a shortened name if possible. [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) can be used to force the device name to appear in the advertising data of an advert with scan response data.

            The application can set the device name itself by including the following in the advertising data.

            ```text
            BT_DATA(BT_DATA_NAME_COMPLETE, name, sizeof(name) - 1)
            ```

        enumerator BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Low duty cycle directed advertising.

            Use low duty directed advertising mode, otherwise high duty mode will be used.

        enumerator BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Directed advertising to privacy-enabled peer.

            Enable use of Resolvable Private Address (RPA) as the target address in directed advertisements. This is required if the remote device is privacy-enabled and supports address resolution of the target address in directed advertisement. It is the responsibility of the application to check that the remote device supports address resolution of directed advertisements by reading its Central Address Resolution characteristic.

        enumerator BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)
        :   Use filter accept list to filter devices that can request scan response data.

        enumerator BT\_LE\_ADV\_OPT\_FILTER\_CONN = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)
        :   Use filter accept list to filter devices that can connect.

        enumerator BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(8)
        :   Notify the application when a scan response data has been sent to an active scanner.

        enumerator BT\_LE\_ADV\_OPT\_SCANNABLE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(9)
        :   Support scan response data.

            When used together with [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) then this option cannot be used together with the [BT\_LE\_ADV\_OPT\_CONNECTABLE](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) option. When used together with [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) then scan response data must be set.

        enumerator BT\_LE\_ADV\_OPT\_EXT\_ADV = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(10)
        :   Advertise with extended advertising.

            This options enables extended advertising in the advertising set. In extended advertising the advertising set will send a small header packet on the three primary advertising channels. This small header points to the advertising data packet that will be sent on one of the 37 secondary advertising channels. The advertiser will send primary advertising on LE 1M PHY, and secondary advertising on LE 2M PHY. Connections will be established on LE 2M PHY.

            Without this option the advertiser will send advertising data on the three primary advertising channels.

            Note

            Enabling this option requires extended advertising support in the peer devices scanning for advertisement packets.

            Note

            This cannot be used with [bt\_le\_adv\_start()](#group__bt__gap_1gad2e3caef88d52d720e8e4d21df767b02).

        enumerator BT\_LE\_ADV\_OPT\_NO\_2M = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(11)
        :   Disable use of LE 2M PHY on the secondary advertising channel.

            Disabling the use of LE 2M PHY could be necessary if scanners don’t support the LE 2M PHY. The advertiser will send primary advertising on LE 1M PHY, and secondary advertising on LE 1M PHY. Connections will be established on LE 1M PHY.

            Note

            Cannot be set if BT\_LE\_ADV\_OPT\_CODED is set.

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab).

        enumerator BT\_LE\_ADV\_OPT\_CODED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(12)
        :   Advertise on the LE Coded PHY (Long Range).

            The advertiser will send both primary and secondary advertising on the LE Coded PHY. This gives the advertiser increased range with the trade-off of lower data rate and higher power consumption. Connections will be established on LE Coded PHY.

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

        enumerator BT\_LE\_ADV\_OPT\_ANONYMOUS = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(13)
        :   Advertise without a device address (identity or RPA).

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

        enumerator BT\_LE\_ADV\_OPT\_USE\_TX\_POWER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(14)
        :   Advertise with transmit power.

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

        enumerator BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(15)
        :   Disable advertising on channel index 37.

        enumerator BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(16)
        :   Disable advertising on channel index 38.

        enumerator BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(17)
        :   Disable advertising on channel index 39.

        enumerator BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(18)
        :   Put GAP device name into advert data.

            Will place the GAP device name into the advertising data rather than the scan response data.

            Note

            Requires [BT\_LE\_ADV\_OPT\_USE\_NAME](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

        enumerator BT\_LE\_ADV\_OPT\_USE\_NRPA = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(19)
        :   Advertise using a Non-Resolvable Private Address.

            A new NRPA is set when updating the advertising parameters.

            This is an advanced feature; most users will want to enable  [`CONFIG_BT_EXT_ADV`](../../../kconfig.md#CONFIG_BT_EXT_ADV "CONFIG_BT_EXT_ADV") instead.

            Note

            Not implemented when  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") .

            Note

            Mutually exclusive with BT\_LE\_ADV\_OPT\_USE\_IDENTITY.

    enum [anonymous]
    :   Periodic Advertising options.

        *Values:*

        enumerator BT\_LE\_PER\_ADV\_OPT\_NONE = 0
        :   Convenience value when no options are specified.

        enumerator BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Advertise with transmit power.

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

        enumerator BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Advertise with included AdvDataInfo (ADI).

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

    enum [anonymous]
    :   Periodic advertising sync options.

        *Values:*

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE = 0
        :   Convenience value when no options are specified.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Use the periodic advertising list to sync with advertiser.

            When this option is set, the address and SID of the parameters are ignored.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Disables periodic advertising reports.

            No advertisement reports will be handled until enabled.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Filter duplicate Periodic Advertising reports.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Sync with Angle of Arrival (AoA) constant tone extension.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Sync with Angle of Departure (AoD) 1 us constant tone extension.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Sync with Angle of Departure (AoD) 2 us constant tone extension.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)
        :   Do not sync to packets without a constant tone extension.

    enum [anonymous]
    :   Periodic Advertising Sync Transfer options.

        *Values:*

        enumerator BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE = 0
        :   Convenience value when no options are specified.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   No Angle of Arrival (AoA).

            Do not sync with Angle of Arrival (AoA) constant tone extension

        enumerator BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   No Angle of Departure (AoD) 1 us.

            Do not sync with Angle of Departure (AoD) 1 us constant tone extension

        enumerator BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   No Angle of Departure (AoD) 2.

            Do not sync with Angle of Departure (AoD) 2 us constant tone extension

        enumerator BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Only sync to packets with constant tone extension.

        enumerator BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Sync to received PAST packets but don’t generate sync reports.

            This option must not be set at the same time as [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](#group__bt__gap_1gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c).

        enumerator BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Sync to received PAST packets and generate sync reports with duplicate filtering.

            This option must not be set at the same time as [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](#group__bt__gap_1gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc).

    enum [anonymous]
    :   *Values:*

        enumerator BT\_LE\_SCAN\_OPT\_NONE = 0
        :   Convenience value when no options are specified.

        enumerator BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Filter duplicates.

        enumerator BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Filter using filter accept list.

        enumerator BT\_LE\_SCAN\_OPT\_CODED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Enable scan on coded PHY (Long Range).

        enumerator BT\_LE\_SCAN\_OPT\_NO\_1M = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Disable scan on 1M phy.

            Note

            Requires [BT\_LE\_SCAN\_OPT\_CODED](#group__bt__gap_1gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb).

    enum [anonymous]
    :   *Values:*

        enumerator BT\_LE\_SCAN\_TYPE\_PASSIVE = 0x00
        :   Scan without requesting additional information from advertisers.

        enumerator BT\_LE\_SCAN\_TYPE\_ACTIVE = 0x01
        :   Scan and request additional information from advertisers.

            Using this scan type will automatically send scan requests to all devices. Scan responses are received in the same manner and using the same callbacks as advertising reports.

    Functions

    int bt\_enable([bt\_ready\_cb\_t](#c.bt_ready_cb_t) cb)
    :   Enable Bluetooth.

        Enable Bluetooth. Must be the called before any calls that require communication with the local Bluetooth hardware.

        When  [`CONFIG_BT_SETTINGS`](../../../kconfig.md#CONFIG_BT_SETTINGS "CONFIG_BT_SETTINGS") is enabled, the application must load the Bluetooth settings after this API call successfully completes before Bluetooth APIs can be used. Loading the settings before calling this function is insufficient. Bluetooth settings can be loaded with [settings\_load()](../../../services/settings/index.md#group__settings_1ga89c6d618df81f197cc5c1a2018b00648) or [settings\_load\_subtree()](../../../services/settings/index.md#group__settings_1gab80e8a21c80243359b652386f7ce2424) with argument “bt”. The latter selectively loads only Bluetooth settings and is recommended if [settings\_load()](../../../services/settings/index.md#group__settings_1ga89c6d618df81f197cc5c1a2018b00648) has been called earlier.

        Parameters:
        :   - **cb** – Callback to notify completion or NULL to perform the enabling synchronously.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_disable(void)
    :   Disable Bluetooth.

        Disable Bluetooth. Can’t be called before bt\_enable has completed.

        Close and release HCI resources. Result is architecture dependent.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    bool bt\_is\_ready(void)
    :   Check if Bluetooth is ready.

        Returns:
        :   true when Bluetooth is ready, false otherwise

    int bt\_set\_name(const char \*name)
    :   Set Bluetooth Device Name.

        Set Bluetooth GAP Device Name.

        When advertising with device name in the advertising data the name should be updated by calling [bt\_le\_adv\_update\_data](#group__bt__gap_1ga9a406ebfefac3dd09935a4ae0e317817) or [bt\_le\_ext\_adv\_set\_data](#group__bt__gap_1gad731f829b3566be3e56485b2a64f80b1).

        See also

        [`CONFIG_BT_DEVICE_NAME_MAX`](../../../kconfig.md#CONFIG_BT_DEVICE_NAME_MAX "CONFIG_BT_DEVICE_NAME_MAX") .

        Note

        Requires  [`CONFIG_BT_DEVICE_NAME_DYNAMIC`](../../../kconfig.md#CONFIG_BT_DEVICE_NAME_DYNAMIC "CONFIG_BT_DEVICE_NAME_DYNAMIC") .

        Parameters:
        :   - **name** – New name

        Returns:
        :   Zero on success or (negative) error code otherwise.

    const char \*bt\_get\_name(void)
    :   Get Bluetooth Device Name.

        Get Bluetooth GAP Device Name.

        Returns:
        :   Bluetooth Device Name

    uint16\_t bt\_get\_appearance(void)
    :   Get local Bluetooth appearance.

        Bluetooth Appearance is a description of the external appearance of a device in terms of an Appearance Value.

        See also

        [https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf](https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf)

        Returns:
        :   Appearance Value of local Bluetooth host.

    int bt\_set\_appearance(uint16\_t new\_appearance)
    :   Set local Bluetooth appearance.

        Automatically preserves the new appearance across reboots if  [`CONFIG_BT_SETTINGS`](../../../kconfig.md#CONFIG_BT_SETTINGS "CONFIG_BT_SETTINGS") is enabled.

        This symbol is linkable if  [`CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC`](../../../kconfig.md#CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC "CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC") is enabled.

        Parameters:
        :   - **new\_appearance** – Appearance Value

        Return values:
        :   - **0** – Success.
            - **other** – Persistent storage failed. Appearance was not updated.

    void bt\_id\_get([bt\_addr\_le\_t](#c.bt_addr_le_t) \*addrs, size\_t \*count)
    :   Get the currently configured identities.

        Returns an array of the currently configured identity addresses. To make sure all available identities can be retrieved, the number of elements in the *addrs* array should be CONFIG\_BT\_ID\_MAX. The identity identifier that some APIs expect (such as advertising parameters) is simply the index of the identity in the *addrs* array.

        If *addrs* is passed as NULL, then returned *count* contains the count of all available identities that can be retrieved with a subsequent call to this function with non-NULL *addrs* parameter.

        Note

        Deleted identities may show up as [BT\_ADDR\_LE\_ANY](#group__bt__addr_1ga17e9efacd50c682b2f709c217e920d48) in the returned array.

        Parameters:
        :   - **addrs** – Array where to store the configured identities.
            - **count** – Should be initialized to the array size. Once the function returns it will contain the number of returned identities.

    int bt\_id\_create([bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr, uint8\_t \*irk)
    :   Create a new identity.

        Create a new identity using the given address and IRK. This function can be called before calling [bt\_enable()](#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b). However, the new identity will only be stored persistently in flash when this API is used after [bt\_enable()](#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b). The reason is that the persistent settings are loaded after [bt\_enable()](#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b) and would therefore cause potential conflicts with the stack blindly overwriting what’s stored in flash. The identity will also not be written to flash in case a pre-defined address is provided, since in such a situation the app clearly has some place it got the address from and will be able to repeat the procedure on every power cycle, i.e. it would be redundant to also store the information in flash.

        Generating random static address or random IRK is not supported when calling this function before [bt\_enable()](#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b).

        If the application wants to have the stack randomly generate identities and store them in flash for later recovery, the way to do it would be to first initialize the stack (using bt\_enable), then call [settings\_load()](../../../services/settings/index.md#group__settings_1ga89c6d618df81f197cc5c1a2018b00648), and after that check with [bt\_id\_get()](#group__bt__gap_1ga06d0ae35cbf4382679cc3cfe612cee4d) how many identities were recovered. If an insufficient amount of identities were recovered the app may then call [bt\_id\_create()](#group__bt__gap_1gae11eb8ad254418c38a0e8689df25a159) to create new ones.

        If supported by the HCI driver (indicated by setting  [`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](../../../kconfig.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR "CONFIG_BT_HCI_SET_PUBLIC_ADDR") ), the first call to this function can be used to set the controller’s public identity address. This call must happen before calling [bt\_enable()](#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b). Subsequent calls always add/generate random static addresses.

        Parameters:
        :   - **addr** – Address to use for the new identity. If NULL or initialized to BT\_ADDR\_LE\_ANY the stack will generate a new random static address for the identity and copy it to the given parameter upon return from this function (in case the parameter was non-NULL).
            - **irk** – Identity Resolving Key (16 bytes) to be used with this identity. If set to all zeroes or NULL, the stack will generate a random IRK for the identity and copy it back to the parameter upon return from this function (in case the parameter was non-NULL). If privacy  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") is not enabled this parameter must be NULL.

        Returns:
        :   Identity identifier (>= 0) in case of success, or a negative error code on failure.

    int bt\_id\_reset(uint8\_t id, [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr, uint8\_t \*irk)
    :   Reset/reclaim an identity for reuse.

        The semantics of the *addr* and *irk* parameters of this function are the same as with [bt\_id\_create()](#group__bt__gap_1gae11eb8ad254418c38a0e8689df25a159). The difference is the first *id* parameter that needs to be an existing identity (if it doesn’t exist this function will return an error). When given an existing identity this function will disconnect any connections created using it, remove any pairing keys or other data associated with it, and then create a new identity in the same slot, based on the *addr* and *irk* parameters.

        Note

        the default identity (BT\_ID\_DEFAULT) cannot be reset, i.e. this API will return an error if asked to do that.

        Parameters:
        :   - **id** – Existing identity identifier.
            - **addr** – Address to use for the new identity. If NULL or initialized to BT\_ADDR\_LE\_ANY the stack will generate a new static random address for the identity and copy it to the given parameter upon return from this function (in case the parameter was non-NULL).
            - **irk** – Identity Resolving Key (16 bytes) to be used with this identity. If set to all zeroes or NULL, the stack will generate a random IRK for the identity and copy it back to the parameter upon return from this function (in case the parameter was non-NULL). If privacy  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") is not enabled this parameter must be NULL.

        Returns:
        :   Identity identifier (>= 0) in case of success, or a negative error code on failure.

    int bt\_id\_delete(uint8\_t id)
    :   Delete an identity.

        When given a valid identity this function will disconnect any connections created using it, remove any pairing keys or other data associated with it, and then flag is as deleted, so that it can not be used for any operations. To take back into use the slot the identity was occupying the [bt\_id\_reset()](#group__bt__gap_1gabb3353edc8a3a8d29a0370049b20cbe4) API needs to be used.

        Note

        the default identity (BT\_ID\_DEFAULT) cannot be deleted, i.e. this API will return an error if asked to do that.

        Parameters:
        :   - **id** – Existing identity identifier.

        Returns:
        :   0 in case of success, or a negative error code on failure.

    size\_t bt\_data\_get\_len(const struct [bt\_data](#c.bt_data) data[], size\_t data\_count)
    :   Get the total size (in bytes) of a given set of [bt\_data](#structbt__data) structures.

        Parameters:
        :   - **data** – **[in]** Array of [bt\_data](#structbt__data) structures.
            - **data\_count** – **[in]** Number of [bt\_data](#structbt__data) structures in `data`.

        Returns:
        :   Size of the concatenated data, built from the [bt\_data](#structbt__data) structure set.

    size\_t bt\_data\_serialize(const struct [bt\_data](#c.bt_data) \*input, uint8\_t \*output)
    :   Serialize a [bt\_data](#structbt__data) struct into an advertising structure (a flat byte array).

        The data are formatted according to the Bluetooth Core Specification v. 5.4, vol. 3, part C, 11.

        Parameters:
        :   - **input** – **[in]** Single [bt\_data](#structbt__data) structure to read from.
            - **output** – **[out]** Buffer large enough to store the advertising structure in `input`. The size of it must be at least the size of the `input->data_len + 2` (for the type and the length).

        Returns:
        :   Number of bytes written in `output`.

    int bt\_le\_adv\_start(const struct [bt\_le\_adv\_param](#c.bt_le_adv_param) \*param, const struct [bt\_data](#c.bt_data) \*ad, size\_t ad\_len, const struct [bt\_data](#c.bt_data) \*sd, size\_t sd\_len)
    :   Start advertising.

        Set advertisement data, scan response data, advertisement parameters and start advertising.

        When the advertisement parameter peer address has been set the advertising will be directed to the peer. In this case advertisement data and scan response data parameters are ignored. If the mode is high duty cycle the timeout will be [BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT](#group__bt__gap__defines_1gabe483d4dd601b11ac3eea570c962b1ec).

        This function cannot be used with [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) in the `param.options`. For extended advertising, the bt\_le\_ext\_adv\_\* functions must be used.

        Parameters:
        :   - **param** – Advertising parameters.
            - **ad** – Data to be used in advertisement packets.
            - **ad\_len** – Number of elements in ad
            - **sd** – Data to be used in scan response packets.
            - **sd\_len** – Number of elements in sd

        Returns:
        :   Zero on success or (negative) error code otherwise.

        Returns:
        :   -ENOMEM No free connection objects available for connectable advertiser.

        Returns:
        :   -ECONNREFUSED When connectable advertising is requested and there is already maximum number of connections established in the controller. This error code is only guaranteed when using Zephyr controller, for other controllers code returned in this case may be -EIO.

    int bt\_le\_adv\_update\_data(const struct [bt\_data](#c.bt_data) \*ad, size\_t ad\_len, const struct [bt\_data](#c.bt_data) \*sd, size\_t sd\_len)
    :   Update advertising.

        Update advertisement and scan response data.

        Parameters:
        :   - **ad** – Data to be used in advertisement packets.
            - **ad\_len** – Number of elements in ad
            - **sd** – Data to be used in scan response packets.
            - **sd\_len** – Number of elements in sd

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_adv\_stop(void)
    :   Stop advertising.

        Stops ongoing advertising.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_ext\_adv\_create(const struct [bt\_le\_adv\_param](#c.bt_le_adv_param) \*param, const struct [bt\_le\_ext\_adv\_cb](#c.bt_le_ext_adv_cb) \*cb, struct bt\_le\_ext\_adv \*\*adv)
    :   Create advertising set.

        Create a new advertising set and set advertising parameters. Advertising parameters can be updated with [bt\_le\_ext\_adv\_update\_param](#group__bt__gap_1ga1aabdb81cb1a1841ff0fb91d849123fc).

        Parameters:
        :   - **param** – **[in]** Advertising parameters.
            - **cb** – **[in]** Callback struct to notify about advertiser activity. Can be NULL. Must point to valid memory during the lifetime of the advertising set.
            - **adv** – **[out]** Valid advertising set object on success.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_ext\_adv\_start(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_start\_param](#c.bt_le_ext_adv_start_param) \*param)
    :   Start advertising with the given advertising set.

        If the advertiser is limited by either the timeout or number of advertising events the application will be notified by the advertiser sent callback once the limit is reached. If the advertiser is limited by both the timeout and the number of advertising events then the limit that is reached first will stop the advertiser.

        Parameters:
        :   - **adv** – Advertising set object.
            - **param** – Advertise start parameters.

    int bt\_le\_ext\_adv\_stop(struct bt\_le\_ext\_adv \*adv)
    :   Stop advertising with the given advertising set.

        Stop advertising with a specific advertising set. When using this function the advertising sent callback will not be called.

        Parameters:
        :   - **adv** – Advertising set object.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_ext\_adv\_set\_data(struct bt\_le\_ext\_adv \*adv, const struct [bt\_data](#c.bt_data) \*ad, size\_t ad\_len, const struct [bt\_data](#c.bt_data) \*sd, size\_t sd\_len)
    :   Set an advertising set’s advertising or scan response data.

        Set advertisement data or scan response data. If the advertising set is currently advertising then the advertising data will be updated in subsequent advertising events.

        When both [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) and [BT\_LE\_ADV\_OPT\_SCANNABLE](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) are enabled then advertising data is ignored. When [BT\_LE\_ADV\_OPT\_SCANNABLE](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) is not enabled then scan response data is ignored.

        If the advertising set has been configured to send advertising data on the primary advertising channels then the maximum data length is [BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN](#group__bt__gap__defines_1ga39ab5040c9471631486da7dbebd9c36f) bytes. If the advertising set has been configured for extended advertising, then the maximum data length is defined by the controller with the maximum possible of [BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN](#group__bt__gap__defines_1ga53af114e4925482739dc50dc84c2f641) bytes.

        Note

        Not all scanners support extended data length advertising data.

        Note

        When updating the advertising data while advertising the advertising data and scan response data length must be smaller or equal to what can be fit in a single advertising packet. Otherwise the advertiser must be stopped.

        Parameters:
        :   - **adv** – Advertising set object.
            - **ad** – Data to be used in advertisement packets.
            - **ad\_len** – Number of elements in ad
            - **sd** – Data to be used in scan response packets.
            - **sd\_len** – Number of elements in sd

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_ext\_adv\_update\_param(struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_adv\_param](#c.bt_le_adv_param) \*param)
    :   Update advertising parameters.

        Update the advertising parameters. The function will return an error if the advertiser set is currently advertising. Stop the advertising set before calling this function.

        Note

        When changing the option [BT\_LE\_ADV\_OPT\_USE\_NAME](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) then [bt\_le\_ext\_adv\_set\_data](#group__bt__gap_1gad731f829b3566be3e56485b2a64f80b1) needs to be called in order to update the advertising data and scan response data.

        Parameters:
        :   - **adv** – Advertising set object.
            - **param** – Advertising parameters.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_ext\_adv\_delete(struct bt\_le\_ext\_adv \*adv)
    :   Delete advertising set.

        Delete advertising set. This will free up the advertising set and make it possible to create a new advertising set.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    uint8\_t bt\_le\_ext\_adv\_get\_index(struct bt\_le\_ext\_adv \*adv)
    :   Get array index of an advertising set.

        This function is used to map bt\_adv to index of an array of advertising sets. The array has CONFIG\_BT\_EXT\_ADV\_MAX\_ADV\_SET elements.

        Parameters:
        :   - **adv** – Advertising set.

        Returns:
        :   Index of the advertising set object. The range of the returned value is 0..CONFIG\_BT\_EXT\_ADV\_MAX\_ADV\_SET-1

    int bt\_le\_ext\_adv\_get\_info(const struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_info](#c.bt_le_ext_adv_info) \*info)
    :   Get advertising set info.

        Parameters:
        :   - **adv** – Advertising set object
            - **info** – Advertising set info object

        Returns:
        :   Zero on success or (negative) error code on failure.

    int bt\_le\_per\_adv\_set\_param(struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_per\_adv\_param](#c.bt_le_per_adv_param) \*param)
    :   Set or update the periodic advertising parameters.

        The periodic advertising parameters can only be set or updated on an extended advertisement set which is neither scannable, connectable nor anonymous.

        Parameters:
        :   - **adv** – Advertising set object.
            - **param** – Advertising parameters.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_set\_data(const struct bt\_le\_ext\_adv \*adv, const struct [bt\_data](#c.bt_data) \*ad, size\_t ad\_len)
    :   Set or update the periodic advertising data.

        The periodic advertisement data can only be set or updated on an extended advertisement set which is neither scannable, connectable nor anonymous.

        Parameters:
        :   - **adv** – Advertising set object.
            - **ad** – Advertising data.
            - **ad\_len** – Advertising data length.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_set\_subevent\_data(const struct bt\_le\_ext\_adv \*adv, uint8\_t num\_subevents, const struct [bt\_le\_per\_adv\_subevent\_data\_params](#c.bt_le_per_adv_subevent_data_params) \*params)
    :   Set the periodic advertising with response subevent data.

        Set the data for one or more subevents of a Periodic Advertising with Responses Advertiser in reply data request.

        Parameters:
        :   - **adv** – The extended advertiser the PAwR train belongs to.
            - **num\_subevents** – The number of subevents to set data for.
            - **params** – Subevent parameters.

        Pre:
        :   There are `num_subevents` elements in `params`.

        Pre:
        :   The controller has requested data for the subevents in `params`.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_start(struct bt\_le\_ext\_adv \*adv)
    :   Starts periodic advertising.

        Enabling the periodic advertising can be done independently of extended advertising, but both periodic advertising and extended advertising shall be enabled before any periodic advertising data is sent. The periodic advertising and extended advertising can be enabled in any order.

        Once periodic advertising has been enabled, it will continue advertising until [bt\_le\_per\_adv\_stop()](#group__bt__gap_1ga1b15206fc552d597c12af369d48ff7d5) has been called, or if the advertising set is deleted by [bt\_le\_ext\_adv\_delete()](#group__bt__gap_1ga62310a27f7fea925dfcf3abd7c454787). Calling [bt\_le\_ext\_adv\_stop()](#group__bt__gap_1ga1c864c4b183f9a86c9f70a11471c5b15) will not stop the periodic advertising.

        Parameters:
        :   - **adv** – Advertising set object.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_stop(struct bt\_le\_ext\_adv \*adv)
    :   Stops periodic advertising.

        Disabling the periodic advertising can be done independently of extended advertising. Disabling periodic advertising will not disable extended advertising.

        Parameters:
        :   - **adv** – Advertising set object.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    uint8\_t bt\_le\_per\_adv\_sync\_get\_index(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)
    :   Get array index of an periodic advertising sync object.

        This function is get the index of an array of periodic advertising sync objects. The array has CONFIG\_BT\_PER\_ADV\_SYNC\_MAX elements.

        Parameters:
        :   - **per\_adv\_sync** – The periodic advertising sync object.

        Returns:
        :   Index of the periodic advertising sync object. The range of the returned value is 0..CONFIG\_BT\_PER\_ADV\_SYNC\_MAX-1

    struct bt\_le\_per\_adv\_sync \*bt\_le\_per\_adv\_sync\_lookup\_index(uint8\_t index)
    :   Get a periodic advertising sync object from the array index.

        This function is to get the periodic advertising sync object from the array index. The array has CONFIG\_BT\_PER\_ADV\_SYNC\_MAX elements.

        Parameters:
        :   - **index** – The index of the periodic advertising sync object. The range of the index value is 0..CONFIG\_BT\_PER\_ADV\_SYNC\_MAX-1

        Returns:
        :   The periodic advertising sync object of the array index or NULL if invalid index.

    int bt\_le\_per\_adv\_sync\_get\_info(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct [bt\_le\_per\_adv\_sync\_info](#c.bt_le_per_adv_sync_info) \*info)
    :   Get periodic adv sync information.

        Parameters:
        :   - **per\_adv\_sync** – Periodic advertising sync object.
            - **info** – Periodic advertising sync info object

        Returns:
        :   Zero on success or (negative) error code on failure.

    struct bt\_le\_per\_adv\_sync \*bt\_le\_per\_adv\_sync\_lookup\_addr(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*adv\_addr, uint8\_t sid)
    :   Look up an existing periodic advertising sync object by advertiser address.

        Parameters:
        :   - **adv\_addr** – Advertiser address.
            - **sid** – The advertising set ID.

        Returns:
        :   Periodic advertising sync object or NULL if not found.

    int bt\_le\_per\_adv\_sync\_create(const struct [bt\_le\_per\_adv\_sync\_param](#c.bt_le_per_adv_sync_param) \*param, struct bt\_le\_per\_adv\_sync \*\*out\_sync)
    :   Create a periodic advertising sync object.

        Create a periodic advertising sync object that can try to synchronize to periodic advertising reports from an advertiser. Scan shall either be disabled or extended scan shall be enabled.

        This function does not timeout, and will continue to look for an advertiser until it either finds it or [bt\_le\_per\_adv\_sync\_delete()](#group__bt__gap_1gaa0c218ff3c78b26dcfaa726ee30267a6) is called. It is thus suggested to implement a timeout when using this, if it is expected to find the advertiser within a reasonable timeframe.

        Parameters:
        :   - **param** – **[in]** Periodic advertising sync parameters.
            - **out\_sync** – **[out]** Periodic advertising sync object on.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_sync\_delete(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)
    :   Delete periodic advertising sync.

        Delete the periodic advertising sync object. Can be called regardless of the state of the sync. If the syncing is currently syncing, the syncing is cancelled. If the sync has been established, it is terminated. The periodic advertising sync object will be invalidated afterwards.

        If the state of the sync object is syncing, then a new periodic advertising sync object may not be created until the controller has finished canceling this object.

        Parameters:
        :   - **per\_adv\_sync** – The periodic advertising sync object.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    void bt\_le\_per\_adv\_sync\_cb\_register(struct [bt\_le\_per\_adv\_sync\_cb](#c.bt_le_per_adv_sync_cb) \*cb)
    :   Register periodic advertising sync callbacks.

        Adds the callback structure to the list of callback structures for periodic advertising syncs.

        This callback will be called for all periodic advertising sync activity, such as synced, terminated and when data is received.

        Parameters:
        :   - **cb** – Callback struct. Must point to memory that remains valid.

    int bt\_le\_per\_adv\_sync\_recv\_enable(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)
    :   Enables receiving periodic advertising reports for a sync.

        If the sync is already receiving the reports, -EALREADY is returned.

        Parameters:
        :   - **per\_adv\_sync** – The periodic advertising sync object.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_sync\_recv\_disable(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)
    :   Disables receiving periodic advertising reports for a sync.

        If the sync report receiving is already disabled, -EALREADY is returned.

        Parameters:
        :   - **per\_adv\_sync** – The periodic advertising sync object.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_sync\_transfer(const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct bt\_conn \*conn, uint16\_t service\_data)
    :   Transfer the periodic advertising sync information to a peer device.

        This will allow another device to quickly synchronize to the same periodic advertising train that this device is currently synced to.

        Parameters:
        :   - **per\_adv\_sync** – The periodic advertising sync to transfer.
            - **conn** – The peer device that will receive the sync information.
            - **service\_data** – Application service data provided to the remote host.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_set\_info\_transfer(const struct bt\_le\_ext\_adv \*adv, const struct bt\_conn \*conn, uint16\_t service\_data)
    :   Transfer the information about a periodic advertising set.

        This will allow another device to quickly synchronize to periodic advertising set from this device.

        Parameters:
        :   - **adv** – The periodic advertising set to transfer info of.
            - **conn** – The peer device that will receive the information.
            - **service\_data** – Application service data provided to the remote host.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_sync\_transfer\_subscribe(const struct bt\_conn \*conn, const struct [bt\_le\_per\_adv\_sync\_transfer\_param](#c.bt_le_per_adv_sync_transfer_param) \*param)
    :   Subscribe to periodic advertising sync transfers (PASTs).

        Sets the parameters and allow other devices to transfer periodic advertising syncs.

        Parameters:
        :   - **conn** – The connection to set the parameters for. If NULL default parameters for all connections will be set. Parameters set for specific connection will always have precedence.
            - **param** – The periodic advertising sync transfer parameters.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_sync\_transfer\_unsubscribe(const struct bt\_conn \*conn)
    :   Unsubscribe from periodic advertising sync transfers (PASTs).

        Remove the parameters that allow other devices to transfer periodic advertising syncs.

        Parameters:
        :   - **conn** – The connection to remove the parameters for. If NULL default parameters for all connections will be removed. Unsubscribing for a specific device, will still allow other devices to transfer periodic advertising syncs.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_list\_add(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr, uint8\_t sid)
    :   Add a device to the periodic advertising list.

        Add peer device LE address to the periodic advertising list. This will make it possibly to automatically create a periodic advertising sync to this device.

        Parameters:
        :   - **addr** – Bluetooth LE identity address.
            - **sid** – The advertising set ID. This value is obtained from the [bt\_le\_scan\_recv\_info](#structbt__le__scan__recv__info) in the scan callback.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_list\_remove(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr, uint8\_t sid)
    :   Remove a device from the periodic advertising list.

        Removes peer device LE address from the periodic advertising list.

        Parameters:
        :   - **addr** – Bluetooth LE identity address.
            - **sid** – The advertising set ID. This value is obtained from the [bt\_le\_scan\_recv\_info](#structbt__le__scan__recv__info) in the scan callback.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_per\_adv\_list\_clear(void)
    :   Clear the periodic advertising list.

        Clears the entire periodic advertising list.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_le\_scan\_start(const struct [bt\_le\_scan\_param](#c.bt_le_scan_param) \*param, [bt\_le\_scan\_cb\_t](#c.bt_le_scan_cb_t) cb)
    :   Start (LE) scanning.

        Start LE scanning with given parameters and provide results through the specified callback.

        Note

        The LE scanner by default does not use the Identity Address of the local device when  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") is disabled. This is to prevent the active scanner from disclosing the identity information when requesting additional information from advertisers. In order to enable directed advertiser reports then  [`CONFIG_BT_SCAN_WITH_IDENTITY`](../../../kconfig.md#CONFIG_BT_SCAN_WITH_IDENTITY "CONFIG_BT_SCAN_WITH_IDENTITY") must be enabled.

        Parameters:
        :   - **param** – Scan parameters.
            - **cb** – Callback to notify scan results. May be NULL if callback registration through [bt\_le\_scan\_cb\_register](#group__bt__gap_1gad7c2f18de7f67b73ccc0e7813f48f096) is preferred.

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    int bt\_le\_scan\_stop(void)
    :   Stop (LE) scanning.

        Stops ongoing LE scanning.

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    void bt\_le\_scan\_cb\_register(struct [bt\_le\_scan\_cb](#c.bt_le_scan_cb) \*cb)
    :   Register scanner packet callbacks.

        Adds the callback structure to the list of callback structures that monitors scanner activity.

        This callback will be called for all scanner activity, regardless of what API was used to start the scanner.

        Parameters:
        :   - **cb** – Callback struct. Must point to memory that remains valid.

    void bt\_le\_scan\_cb\_unregister(struct [bt\_le\_scan\_cb](#c.bt_le_scan_cb) \*cb)
    :   Unregister scanner packet callbacks.

        Remove the callback structure from the list of scanner callbacks.

        Parameters:
        :   - **cb** – Callback struct. Must point to memory that remains valid.

    int bt\_le\_filter\_accept\_list\_add(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Add device (LE) to filter accept list.

        Add peer device LE address to the filter accept list.

        Note

        The filter accept list cannot be modified when an LE role is using the filter accept list, i.e advertiser or scanner using a filter accept list or automatic connecting to devices using filter accept list.

        Parameters:
        :   - **addr** – Bluetooth LE identity address.

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    static inline int bt\_le\_whitelist\_add(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)

    int bt\_le\_filter\_accept\_list\_remove(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Remove device (LE) from filter accept list.

        Remove peer device LE address from the filter accept list.

        Note

        The filter accept list cannot be modified when an LE role is using the filter accept list, i.e advertiser or scanner using a filter accept list or automatic connecting to devices using filter accept list.

        Parameters:
        :   - **addr** – Bluetooth LE identity address.

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    static inline int bt\_le\_whitelist\_rem(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)

    int bt\_le\_filter\_accept\_list\_clear(void)
    :   Clear filter accept list.

        Clear all devices from the filter accept list.

        Note

        The filter accept list cannot be modified when an LE role is using the filter accept list, i.e advertiser or scanner using a filter accept list or automatic connecting to devices using filter accept list.

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    static inline int bt\_le\_whitelist\_clear(void)

    int bt\_le\_set\_chan\_map(uint8\_t chan\_map[5])
    :   Set (LE) channel map.

        Parameters:
        :   - **chan\_map** – Channel map.

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    int bt\_le\_set\_rpa\_timeout(uint16\_t new\_rpa\_timeout)
    :   Set the Resolvable Private Address timeout in runtime.

        The new RPA timeout value will be used for the next RPA rotation and all subsequent rotations until another override is scheduled with this API.

        Initially, the if  [`CONFIG_BT_RPA_TIMEOUT`](../../../kconfig.md#CONFIG_BT_RPA_TIMEOUT "CONFIG_BT_RPA_TIMEOUT") is used as the RPA timeout.

        This symbol is linkable if  [`CONFIG_BT_RPA_TIMEOUT_DYNAMIC`](../../../kconfig.md#CONFIG_BT_RPA_TIMEOUT_DYNAMIC "CONFIG_BT_RPA_TIMEOUT_DYNAMIC") is enabled.

        Parameters:
        :   - **new\_rpa\_timeout** – Resolvable Private Address timeout in seconds

        Return values:
        :   - **0** – Success.
            - **-EINVAL** – RPA timeout value is invalid. Valid range is 1s - 3600s.

    void bt\_data\_parse(struct [net\_buf\_simple](../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*ad, bool (\*func)(struct [bt\_data](#c.bt_data) \*data, void \*user\_data), void \*user\_data)
    :   Helper for parsing advertising (or EIR or OOB) data.

        A helper for parsing the basic data types used for Extended Inquiry Response (EIR), Advertising Data (AD), and OOB data blocks. The most common scenario is to call this helper on the advertising data received in the callback that was given to [bt\_le\_scan\_start()](#group__bt__gap_1gac5e19c26b53a08dadb8efa7ecc692ad6).

        Warning

        This helper function will consume `ad` when parsing. The user should make a copy if the original data is to be used afterwards

        Parameters:
        :   - **ad** – Advertising data as given to the [bt\_le\_scan\_cb\_t](#group__bt__gap_1ga1c53d22b6e2dee38c825c58f3eeee9b4) callback.
            - **func** – Callback function which will be called for each element that’s found in the data. The callback should return true to continue parsing, or false to stop parsing.
            - **user\_data** – User data to be passed to the callback.

    int bt\_le\_oob\_get\_local(uint8\_t id, struct [bt\_le\_oob](#c.bt_le_oob) \*oob)
    :   Get local LE Out of Band (OOB) information.

        This function allows to get local information that are useful for Out of Band pairing or connection creation.

        If privacy  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") is enabled this will result in generating new Resolvable Private Address (RPA) that is valid for  [`CONFIG_BT_RPA_TIMEOUT`](../../../kconfig.md#CONFIG_BT_RPA_TIMEOUT "CONFIG_BT_RPA_TIMEOUT") seconds. This address will be used for advertising started by [bt\_le\_adv\_start](#group__bt__gap_1gad2e3caef88d52d720e8e4d21df767b02), active scanning and connection creation.

        Note

        If privacy is enabled the RPA cannot be refreshed in the following cases:

        - Creating a connection in progress, wait for the connected callback. In addition when extended advertising  [`CONFIG_BT_EXT_ADV`](../../../kconfig.md#CONFIG_BT_EXT_ADV "CONFIG_BT_EXT_ADV") is not enabled or not supported by the controller:
        - Advertiser is enabled using a Random Static Identity Address for a different local identity.
        - The local identity conflicts with the local identity used by other roles.

        Parameters:
        :   - **id** – **[in]** Local identity, in most cases BT\_ID\_DEFAULT.
            - **oob** – **[out]** LE OOB information

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    int bt\_le\_ext\_adv\_oob\_get\_local(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_oob](#c.bt_le_oob) \*oob)
    :   Get local LE Out of Band (OOB) information.

        This function allows to get local information that are useful for Out of Band pairing or connection creation.

        If privacy  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") is enabled this will result in generating new Resolvable Private Address (RPA) that is valid for  [`CONFIG_BT_RPA_TIMEOUT`](../../../kconfig.md#CONFIG_BT_RPA_TIMEOUT "CONFIG_BT_RPA_TIMEOUT") seconds. This address will be used by the advertising set.

        Note

        When generating OOB information for multiple advertising set all OOB information needs to be generated at the same time.

        Note

        If privacy is enabled the RPA cannot be refreshed in the following cases:

        - Creating a connection in progress, wait for the connected callback.

        Parameters:
        :   - **adv** – **[in]** The advertising set object
            - **oob** – **[out]** LE OOB information

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    int bt\_br\_discovery\_start(const struct [bt\_br\_discovery\_param](#c.bt_br_discovery_param) \*param, struct [bt\_br\_discovery\_result](#c.bt_br_discovery_result) \*results, size\_t count, [bt\_br\_discovery\_cb\_t](#c.bt_br_discovery_cb_t) cb)
    :   Start BR/EDR discovery.

        Start BR/EDR discovery (inquiry) and provide results through the specified callback. When [bt\_br\_discovery\_cb\_t](#group__bt__gap_1ga4606f9a083b5c333d8c1dc92b759333a) is called it indicates that discovery has completed. If more inquiry results were received during session than fits in provided result storage, only ones with highest RSSI will be reported.

        Parameters:
        :   - **param** – Discovery parameters.
            - **results** – Storage for discovery results.
            - **count** – Number of results in storage. Valid range: 1-255.
            - **cb** – Callback to notify discovery results.

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error

    int bt\_br\_discovery\_stop(void)
    :   Stop BR/EDR discovery.

        Stops ongoing BR/EDR discovery. If discovery was stopped by this call results won’t be reported

        Returns:
        :   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

    int bt\_br\_oob\_get\_local(struct [bt\_br\_oob](#c.bt_br_oob) \*oob)
    :   Get BR/EDR local Out Of Band information.

        This function allows to get local controller information that are useful for Out Of Band pairing or connection creation process.

        Parameters:
        :   - **oob** – Out Of Band information

    int bt\_br\_set\_discoverable(bool enable)
    :   Enable/disable set controller in discoverable state.

        Allows make local controller to listen on INQUIRY SCAN channel and responds to devices making general inquiry. To enable this state it’s mandatory to first be in connectable state.

        Parameters:
        :   - **enable** – Value allowing/disallowing controller to become discoverable.

        Returns:
        :   Negative if fail set to requested state or requested state has been already set. Zero if done successfully.

    int bt\_br\_set\_connectable(bool enable)
    :   Enable/disable set controller in connectable state.

        Allows make local controller to be connectable. It means the controller start listen to devices requests on PAGE SCAN channel. If disabled also resets discoverability if was set.

        Parameters:
        :   - **enable** – Value allowing/disallowing controller to be connectable.

        Returns:
        :   Negative if fail set to requested state or requested state has been already set. Zero if done successfully.

    int bt\_unpair(uint8\_t id, const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Clear pairing information.

        Parameters:
        :   - **id** – Local identity (mostly just BT\_ID\_DEFAULT).
            - **addr** – Remote address, NULL or BT\_ADDR\_LE\_ANY to clear all remote devices.

        Returns:
        :   0 on success or negative error value on failure.

    void bt\_foreach\_bond(uint8\_t id, void (\*func)(const struct [bt\_bond\_info](#c.bt_bond_info) \*info, void \*user\_data), void \*user\_data)
    :   Iterate through all existing bonds.

        Parameters:
        :   - **id** – Local identity (mostly just BT\_ID\_DEFAULT).
            - **func** – Function to call for each bond.
            - **user\_data** – Data to pass to the callback function.

    int bt\_configure\_data\_path(uint8\_t dir, uint8\_t id, uint8\_t vs\_config\_len, const uint8\_t \*vs\_config)
    :   Configure vendor data path.

        Request the Controller to configure the data transport path in a given direction between the Controller and the Host.

        Parameters:
        :   - **dir** – Direction to be configured, BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR or BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST
            - **id** – Vendor specific logical transport channel ID, range [BT\_HCI\_DATAPATH\_ID\_VS..BT\_HCI\_DATAPATH\_ID\_VS\_END]
            - **vs\_config\_len** – Length of additional vendor specific configuration data
            - **vs\_config** – Pointer to additional vendor specific configuration data

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_le\_per\_adv\_sync\_subevent(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct [bt\_le\_per\_adv\_sync\_subevent\_params](#c.bt_le_per_adv_sync_subevent_params) \*params)
    :   Synchronize with a subset of subevents.

        Until this command is issued, the subevent(s) the controller is synchronized to is unspecified.

        Parameters:
        :   - **per\_adv\_sync** – The periodic advertising sync object.
            - **params** – Parameters.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_le\_per\_adv\_set\_response\_data(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct [bt\_le\_per\_adv\_response\_params](#c.bt_le_per_adv_response_params) \*params, const struct [net\_buf\_simple](../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*data)
    :   Set the data for a response slot in a specific subevent of the PAwR.

        This function is called by the application to set the response data. The data for a response slot shall be transmitted only once.

        Parameters:
        :   - **per\_adv\_sync** – The periodic advertising sync object.
            - **params** – Parameters.
            - **data** – The response data to send.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    struct bt\_le\_ext\_adv\_sent\_info
    :   *#include <bluetooth.h>*

        Public Members

        uint8\_t num\_sent
        :   The number of advertising events completed.

    struct bt\_le\_ext\_adv\_connected\_info
    :   *#include <bluetooth.h>*

        Public Members

        struct bt\_conn \*conn
        :   Connection object of the new connection.

    struct bt\_le\_ext\_adv\_scanned\_info
    :   *#include <bluetooth.h>*

        Public Members

        [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr
        :   Active scanner LE address and type.

    struct bt\_le\_per\_adv\_data\_request
    :   *#include <bluetooth.h>*

        Public Members

        uint8\_t start
        :   The first subevent data can be set for.

        uint8\_t count
        :   The number of subevents data can be set for.

    struct bt\_le\_per\_adv\_response\_info
    :   *#include <bluetooth.h>*

        Public Members

        uint8\_t subevent
        :   The subevent the response was received in.

        uint8\_t tx\_status
        :   Status of the subevent indication.

            0 if subevent indication was transmitted. 1 if subevent indication was not transmitted. All other values RFU.

        int8\_t tx\_power
        :   The TX power of the response in dBm.

        int8\_t rssi
        :   The RSSI of the response in dBm.

        uint8\_t cte\_type
        :   The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

        uint8\_t response\_slot
        :   The slot the response was received in.

    struct bt\_le\_ext\_adv\_cb
    :   *#include <bluetooth.h>*

        Public Members

        void (\*sent)(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_sent\_info](#c.bt_le_ext_adv_sent_info) \*info)
        :   The advertising set has finished sending adv data.

            This callback notifies the application that the advertising set has finished sending advertising data. The advertising set can either have been stopped by a timeout or because the specified number of advertising events has been reached.

            Param adv:
            :   The advertising set object.

            Param info:
            :   Information about the sent event.

        void (\*connected)(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_connected\_info](#c.bt_le_ext_adv_connected_info) \*info)
        :   The advertising set has accepted a new connection.

            This callback notifies the application that the advertising set has accepted a new connection.

            Param adv:
            :   The advertising set object.

            Param info:
            :   Information about the connected event.

        void (\*scanned)(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_scanned\_info](#c.bt_le_ext_adv_scanned_info) \*info)
        :   The advertising set has sent scan response data.

            This callback notifies the application that the advertising set has has received a Scan Request packet, and has sent a Scan Response packet.

            Param adv:
            :   The advertising set object.

            Param addr:
            :   Information about the scanned event.

    struct bt\_data
    :   *#include <bluetooth.h>*

        Bluetooth data.

        Description of different data types that can be encoded into advertising data. Used to form arrays that are passed to the [bt\_le\_adv\_start()](#group__bt__gap_1gad2e3caef88d52d720e8e4d21df767b02) function.

    struct bt\_le\_adv\_param
    :   *#include <bluetooth.h>*

        LE Advertising Parameters.

        Public Members

        uint8\_t id
        :   Local identity.

            Note

            When extended advertising  [`CONFIG_BT_EXT_ADV`](../../../kconfig.md#CONFIG_BT_EXT_ADV "CONFIG_BT_EXT_ADV") is not enabled or not supported by the controller it is not possible to scan and advertise simultaneously using two different random addresses.

        uint8\_t sid
        :   Advertising Set Identifier, valid range 0x00 - 0x0f.

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

        uint8\_t secondary\_max\_skip
        :   Secondary channel maximum skip count.

            Maximum advertising events the advertiser can skip before it must send advertising data on the secondary advertising channel.

            Note

            Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

        uint32\_t options
        :   Bit-field of advertising options.

        uint32\_t interval\_min
        :   Minimum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than or equal to the Maximum Advertising Interval.

            The Minimum Advertising Interval and Maximum Advertising Interval should not be the same value (as stated in Bluetooth Core Spec 5.2, section 7.8.5) Range: 0x0020 to 0x4000

        uint32\_t interval\_max
        :   Maximum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than or equal to the Maximum Advertising Interval.

            The Minimum Advertising Interval and Maximum Advertising Interval should not be the same value (as stated in Bluetooth Core Spec 5.2, section 7.8.5) Range: 0x0020 to 0x4000

        const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*peer
        :   Directed advertising to peer.

            When this parameter is set the advertiser will send directed advertising to the remote device.

            The advertising type will either be high duty cycle, or low duty cycle if the BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY option is enabled. When using [BT\_LE\_ADV\_OPT\_EXT\_ADV](#group__bt__gap_1gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) then only low duty cycle is allowed.

            In case of connectable high duty cycle if the connection could not be established within the timeout the connected() callback will be called with the status set to BT\_HCI\_ERR\_ADV\_TIMEOUT.

    struct bt\_le\_per\_adv\_param
    :   *#include <bluetooth.h>*

        Public Members

        uint16\_t interval\_min
        :   Minimum Periodic Advertising Interval (N \* 1.25 ms).

            Shall be greater or equal to BT\_GAP\_PER\_ADV\_MIN\_INTERVAL and less or equal to interval\_max.

        uint16\_t interval\_max
        :   Maximum Periodic Advertising Interval (N \* 1.25 ms).

            Shall be less or equal to BT\_GAP\_PER\_ADV\_MAX\_INTERVAL and greater or equal to interval\_min.

        uint32\_t options
        :   Bit-field of periodic advertising options.

    struct bt\_le\_ext\_adv\_start\_param
    :   *#include <bluetooth.h>*

        Public Members

        uint16\_t timeout
        :   Advertiser timeout (N \* 10 ms).

            Application will be notified by the advertiser sent callback. Set to zero for no timeout.

            When using high duty cycle directed connectable advertising then this parameters must be set to a non-zero value less than or equal to the maximum of [BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT](#group__bt__gap__defines_1gabe483d4dd601b11ac3eea570c962b1ec).

            If privacy  [`CONFIG_BT_PRIVACY`](../../../kconfig.md#CONFIG_BT_PRIVACY "CONFIG_BT_PRIVACY") is enabled then the timeout must be less than  [`CONFIG_BT_RPA_TIMEOUT`](../../../kconfig.md#CONFIG_BT_RPA_TIMEOUT "CONFIG_BT_RPA_TIMEOUT") .

        uint8\_t num\_events
        :   Number of advertising events.

            Application will be notified by the advertiser sent callback. Set to zero for no limit.

    struct bt\_le\_ext\_adv\_info
    :   *#include <bluetooth.h>*

        Advertising set info structure.

        Public Members

        int8\_t tx\_power
        :   Currently selected Transmit Power (dBM).

        const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr
        :   Current local advertising address used.

    struct bt\_le\_per\_adv\_subevent\_data\_params
    :   *#include <bluetooth.h>*

        Public Members

        uint8\_t subevent
        :   The subevent to set data for.

        uint8\_t response\_slot\_start
        :   The first response slot to listen to.

        uint8\_t response\_slot\_count
        :   The number of response slots to listen to.

        const struct [net\_buf\_simple](../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*data
        :   The data to send.

    struct bt\_le\_per\_adv\_sync\_synced\_info
    :   *#include <bluetooth.h>*

        Public Members

        const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr
        :   Advertiser LE address and type.

        uint8\_t sid
        :   Advertiser SID.

        uint16\_t interval
        :   Periodic advertising interval (N \* 1.25 ms).

        uint8\_t phy
        :   Advertiser PHY.

        bool recv\_enabled
        :   True if receiving periodic advertisements, false otherwise.

        uint16\_t service\_data
        :   Service Data provided by the peer when sync is transferred.

            Will always be 0 when the sync is locally created.

        struct bt\_conn \*conn
        :   Peer that transferred the periodic advertising sync.

            Will always be 0 when the sync is locally created.

    struct bt\_le\_per\_adv\_sync\_term\_info
    :   *#include <bluetooth.h>*

        Public Members

        const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr
        :   Advertiser LE address and type.

        uint8\_t sid
        :   Advertiser SID.

        uint8\_t reason
        :   Cause of periodic advertising termination.

    struct bt\_le\_per\_adv\_sync\_recv\_info
    :   *#include <bluetooth.h>*

        Public Members

        const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr
        :   Advertiser LE address and type.

        uint8\_t sid
        :   Advertiser SID.

        int8\_t tx\_power
        :   The TX power of the advertisement.

        int8\_t rssi
        :   The RSSI of the advertisement excluding any CTE.

        uint8\_t cte\_type
        :   The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

    struct bt\_le\_per\_adv\_sync\_state\_info
    :   *#include <bluetooth.h>*

        Public Members

        bool recv\_enabled
        :   True if receiving periodic advertisements, false otherwise.

    struct bt\_le\_per\_adv\_sync\_cb
    :   *#include <bluetooth.h>*

        Public Members

        void (\*synced)(struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_le\_per\_adv\_sync\_synced\_info](#c.bt_le_per_adv_sync_synced_info) \*info)
        :   The periodic advertising has been successfully synced.

            This callback notifies the application that the periodic advertising set has been successfully synced, and will now start to receive periodic advertising reports.

            Param sync:
            :   The periodic advertising sync object.

            Param info:
            :   Information about the sync event.

        void (\*term)(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_term\_info](#c.bt_le_per_adv_sync_term_info) \*info)
        :   The periodic advertising sync has been terminated.

            This callback notifies the application that the periodic advertising sync has been terminated, either by local request, remote request or because due to missing data, e.g. by being out of range or sync.

            Param sync:
            :   The periodic advertising sync object.

        void (\*recv)(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_recv\_info](#c.bt_le_per_adv_sync_recv_info) \*info, struct [net\_buf\_simple](../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Periodic advertising data received.

            This callback notifies the application of an periodic advertising report.

            Param sync:
            :   The advertising set object.

            Param info:
            :   Information about the periodic advertising event.

            Param buf:
            :   Buffer containing the periodic advertising data. NULL if the controller failed to receive a subevent indication. Only happens if  [`CONFIG_BT_PER_ADV_SYNC_RSP`](../../../kconfig.md#CONFIG_BT_PER_ADV_SYNC_RSP "CONFIG_BT_PER_ADV_SYNC_RSP") is enabled.

        void (\*state\_changed)(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_state\_info](#c.bt_le_per_adv_sync_state_info) \*info)
        :   The periodic advertising sync state has changed.

            This callback notifies the application about changes to the sync state. Initialize sync and termination is handled by their individual callbacks, and won’t be notified here.

            Param sync:
            :   The periodic advertising sync object.

            Param info:
            :   Information about the state change.

        void (\*biginfo)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_iso\_biginfo \*biginfo)
        :   BIGInfo advertising report received.

            This callback notifies the application of a BIGInfo advertising report. This is received if the advertiser is broadcasting isochronous streams in a BIG. See iso.h for more information.

            Param sync:
            :   The advertising set object.

            Param biginfo:
            :   The BIGInfo report.

        void (\*cte\_report\_cb)(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_df\_per\_adv\_sync\_iq\_samples\_report const \*info)
        :   Callback for IQ samples report collected when sampling CTE received with periodic advertising PDU.

            Param sync:
            :   The periodic advertising sync object.

            Param info:
            :   Information about the sync event.

    struct bt\_le\_per\_adv\_sync\_param
    :   *#include <bluetooth.h>*

        Public Members

        [bt\_addr\_le\_t](#c.bt_addr_le_t) addr
        :   Periodic Advertiser Address.

            Only valid if not using the periodic advertising list (BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST)

        uint8\_t sid
        :   Advertiser SID.

            Only valid if not using the periodic advertising list (BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST)

        uint32\_t options
        :   Bit-field of periodic advertising sync options.

        uint16\_t skip
        :   Maximum event skip.

            Maximum number of periodic advertising events that can be skipped after a successful receive. Range: 0x0000 to 0x01F3

        uint16\_t timeout
        :   Synchronization timeout (N \* 10 ms).

            Synchronization timeout for the periodic advertising sync. Range 0x000A to 0x4000 (100 ms to 163840 ms)

    struct bt\_le\_per\_adv\_sync\_info
    :   *#include <bluetooth.h>*

        Advertising set info structure.

        Public Members

        [bt\_addr\_le\_t](#c.bt_addr_le_t) addr
        :   Periodic Advertiser Address.

        uint8\_t sid
        :   Advertiser SID.

        uint16\_t interval
        :   Periodic advertising interval (N \* 1.25 ms).

        uint8\_t phy
        :   Advertiser PHY.

    struct bt\_le\_per\_adv\_sync\_transfer\_param
    :   *#include <bluetooth.h>*

        Public Members

        uint16\_t skip
        :   Maximum event skip.

            The number of periodic advertising packets that can be skipped after a successful receive.

        uint16\_t timeout
        :   Synchronization timeout (N \* 10 ms).

            Synchronization timeout for the periodic advertising sync. Range 0x000A to 0x4000 (100 ms to 163840 ms)

        uint32\_t options
        :   Periodic Advertising Sync Transfer options.

    struct bt\_le\_scan\_param
    :   *#include <bluetooth.h>*

        LE scan parameters.

        Public Members

        uint8\_t type
        :   Scan type (BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE).

        uint32\_t options
        :   Bit-field of scanning options.

        uint16\_t interval
        :   Scan interval (N \* 0.625 ms).

        uint16\_t window
        :   Scan window (N \* 0.625 ms).

        uint16\_t timeout
        :   Scan timeout (N \* 10 ms).

            Application will be notified by the scan timeout callback. Set zero to disable timeout.

        uint16\_t interval\_coded
        :   Scan interval LE Coded PHY (N \* 0.625 MS).

            Set zero to use same as LE 1M PHY scan interval.

        uint16\_t window\_coded
        :   Scan window LE Coded PHY (N \* 0.625 MS).

            Set zero to use same as LE 1M PHY scan window.

    struct bt\_le\_scan\_recv\_info
    :   *#include <bluetooth.h>*

        LE advertisement and scan response packet information.

        Public Members

        const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr
        :   Advertiser LE address and type.

            If advertiser is anonymous then this address will be [BT\_ADDR\_LE\_ANY](#group__bt__addr_1ga17e9efacd50c682b2f709c217e920d48).

        uint8\_t sid
        :   Advertising Set Identifier.

        int8\_t rssi
        :   Strength of advertiser signal.

        int8\_t tx\_power
        :   Transmit power of the advertiser.

        uint8\_t adv\_type
        :   Advertising packet type.

            Uses the BT\_GAP\_ADV\_TYPE\_\* value.

            May indicate that this is a scan response if the type is [BT\_GAP\_ADV\_TYPE\_SCAN\_RSP](#group__bt__gap__defines_1ggab5a881b0cb1df3cf98de07a14e818c3ea5387de0177d3a9da9fd0c44ca30c7018).

        uint16\_t adv\_props
        :   Advertising packet properties bitfield.

            Uses the BT\_GAP\_ADV\_PROP\_\* values. May indicate that this is a scan response if the value contains the [BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE](#group__bt__gap__defines_1ggabf1a0417a549ec0a97263c2d990e711ba55258ac9a7b355db87aeec5d443718f7) bit.

        uint16\_t interval
        :   Periodic advertising interval.

            If 0 there is no periodic advertising.

        uint8\_t primary\_phy
        :   Primary advertising channel PHY.

        uint8\_t secondary\_phy
        :   Secondary advertising channel PHY.

    struct bt\_le\_scan\_cb
    :   *#include <bluetooth.h>*

        Listener context for (LE) scanning.

        Public Members

        void (\*recv)(const struct [bt\_le\_scan\_recv\_info](#c.bt_le_scan_recv_info) \*info, struct [net\_buf\_simple](../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Advertisement packet and scan response received callback.

            Param info:
            :   Advertiser packet and scan response information.

            Param buf:
            :   Buffer containing advertiser data.

        void (\*timeout)(void)
        :   The scanner has stopped scanning after scan timeout.

    struct bt\_le\_oob\_sc\_data
    :   *#include <bluetooth.h>*

        LE Secure Connections pairing Out of Band data.

        Public Members

        uint8\_t r[16]
        :   Random Number.

        uint8\_t c[16]
        :   Confirm Value.

    struct bt\_le\_oob
    :   *#include <bluetooth.h>*

        LE Out of Band information.

        Public Members

        [bt\_addr\_le\_t](#c.bt_addr_le_t) addr
        :   LE address.

            If privacy is enabled this is a Resolvable Private Address.

        struct [bt\_le\_oob\_sc\_data](#c.bt_le_oob_sc_data) le\_sc\_data
        :   LE Secure Connections pairing Out of Band data.

    struct bt\_br\_discovery\_result
    :   *#include <bluetooth.h>*

        BR/EDR discovery result structure.

        Public Members

        [bt\_addr\_t](#c.bt_addr_t) addr
        :   Remote device address.

        int8\_t rssi
        :   RSSI from inquiry.

        uint8\_t cod[3]
        :   Class of Device.

        uint8\_t eir[240]
        :   Extended Inquiry Response.

    struct bt\_br\_discovery\_param
    :   *#include <bluetooth.h>*

        BR/EDR discovery parameters.

        Public Members

        uint8\_t length
        :   Maximum length of the discovery in units of 1.28 seconds.

            Valid range is 0x01 - 0x30.

        bool limited
        :   True if limited discovery procedure is to be used.

    struct bt\_br\_oob
    :   *#include <bluetooth.h>*

        Public Members

        [bt\_addr\_t](#c.bt_addr_t) addr
        :   BR/EDR address.

    struct bt\_bond\_info
    :   *#include <bluetooth.h>*

        Information about a bond with a remote device.

        Public Members

        [bt\_addr\_le\_t](#c.bt_addr_le_t) addr
        :   Address of the remote device.

    struct bt\_le\_per\_adv\_sync\_subevent\_params
    :   *#include <bluetooth.h>*

        Public Members

        uint16\_t properties
        :   Periodic Advertising Properties.

            Bit 6 is include TxPower, all others RFU.

        uint8\_t num\_subevents
        :   Number of subevents to sync to.

        uint8\_t \*subevents
        :   The subevent(s) to synchronize with.

            The array must have [num\_subevents](#structbt__le__per__adv__sync__subevent__params_1a867c66bf09461a4369da3d250701d2ae) elements.

    struct bt\_le\_per\_adv\_response\_params
    :   *#include <bluetooth.h>*

        Public Members

        uint16\_t request\_event
        :   The periodic event counter of the request the response is sent to.

            [bt\_le\_per\_adv\_sync\_recv\_info](#structbt__le__per__adv__sync__recv__info)

            Note

            The response can be sent up to one periodic interval after the request was received.

        uint8\_t request\_subevent
        :   The subevent counter of the request the response is sent to.

            [bt\_le\_per\_adv\_sync\_recv\_info](#structbt__le__per__adv__sync__recv__info)

        uint8\_t response\_subevent
        :   The subevent the response shall be sent in.

        uint8\_t response\_slot
        :   The response slot the response shall be sent in.

*group* bt\_addr
:   Bluetooth device address definitions and utilities.

    Defines

    BT\_ADDR\_LE\_PUBLIC

    BT\_ADDR\_LE\_RANDOM

    BT\_ADDR\_LE\_PUBLIC\_ID

    BT\_ADDR\_LE\_RANDOM\_ID

    BT\_ADDR\_LE\_UNRESOLVED

    BT\_ADDR\_LE\_ANONYMOUS

    BT\_ADDR\_SIZE
    :   Length in bytes of a standard Bluetooth address.

    BT\_ADDR\_LE\_SIZE
    :   Length in bytes of an LE Bluetooth address.

        Not packed, so no sizeof()

    BT\_ADDR\_ANY
    :   Bluetooth device “any” address, not a valid address.

    BT\_ADDR\_NONE
    :   Bluetooth device “none” address, not a valid address.

    BT\_ADDR\_LE\_ANY
    :   Bluetooth LE device “any” address, not a valid address.

    BT\_ADDR\_LE\_NONE
    :   Bluetooth LE device “none” address, not a valid address.

    BT\_ADDR\_IS\_RPA(a)
    :   Check if a Bluetooth LE random address is resolvable private address.

    BT\_ADDR\_IS\_NRPA(a)
    :   Check if a Bluetooth LE random address is a non-resolvable private address.

    BT\_ADDR\_IS\_STATIC(a)
    :   Check if a Bluetooth LE random address is a static address.

    BT\_ADDR\_SET\_RPA(a)
    :   Set a Bluetooth LE random address as a resolvable private address.

    BT\_ADDR\_SET\_NRPA(a)
    :   Set a Bluetooth LE random address as a non-resolvable private address.

    BT\_ADDR\_SET\_STATIC(a)
    :   Set a Bluetooth LE random address as a static address.

    BT\_ADDR\_STR\_LEN
    :   Recommended length of user string buffer for Bluetooth address.

        The recommended length guarantee the output of address conversion will not lose valuable information about address being processed.

    BT\_ADDR\_LE\_STR\_LEN
    :   Recommended length of user string buffer for Bluetooth LE address.

        The recommended length guarantee the output of address conversion will not lose valuable information about address being processed.

    Functions

    static inline int bt\_addr\_cmp(const [bt\_addr\_t](#c.bt_addr_t) \*a, const [bt\_addr\_t](#c.bt_addr_t) \*b)
    :   Compare Bluetooth device addresses.

        Parameters:
        :   - **a** – First Bluetooth device address to compare
            - **b** – Second Bluetooth device address to compare

        Returns:
        :   negative value if *a* < *b*, 0 if *a* == *b*, else positive

    static inline bool bt\_addr\_eq(const [bt\_addr\_t](#c.bt_addr_t) \*a, const [bt\_addr\_t](#c.bt_addr_t) \*b)
    :   Determine equality of two Bluetooth device addresses.

        Return values:
        :   - **true** – if the two addresses are equal
            - **false** – otherwise

    static inline int bt\_addr\_le\_cmp(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*a, const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*b)
    :   Compare Bluetooth LE device addresses.

        See also

        [bt\_addr\_le\_eq](#group__bt__addr_1ga8644e77108f029088adb203e5392016b)

        Parameters:
        :   - **a** – First Bluetooth LE device address to compare
            - **b** – Second Bluetooth LE device address to compare

        Returns:
        :   negative value if *a* < *b*, 0 if *a* == *b*, else positive

    static inline bool bt\_addr\_le\_eq(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*a, const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*b)
    :   Determine equality of two Bluetooth LE device addresses.

        The Bluetooth LE addresses are equal iff both the types and the 48-bit addresses are numerically equal.

        Return values:
        :   - **true** – if the two addresses are equal
            - **false** – otherwise

    static inline void bt\_addr\_copy([bt\_addr\_t](#c.bt_addr_t) \*dst, const [bt\_addr\_t](#c.bt_addr_t) \*src)
    :   Copy Bluetooth device address.

        Parameters:
        :   - **dst** – Bluetooth device address destination buffer.
            - **src** – Bluetooth device address source buffer.

    static inline void bt\_addr\_le\_copy([bt\_addr\_le\_t](#c.bt_addr_le_t) \*dst, const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*src)
    :   Copy Bluetooth LE device address.

        Parameters:
        :   - **dst** – Bluetooth LE device address destination buffer.
            - **src** – Bluetooth LE device address source buffer.

    int bt\_addr\_le\_create\_nrpa([bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Create a Bluetooth LE random non-resolvable private address.

    int bt\_addr\_le\_create\_static([bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Create a Bluetooth LE random static address.

    static inline bool bt\_addr\_le\_is\_rpa(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Check if a Bluetooth LE address is a random private resolvable address.

        Parameters:
        :   - **addr** – Bluetooth LE device address.

        Returns:
        :   true if address is a random private resolvable address.

    static inline bool bt\_addr\_le\_is\_identity(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Check if a Bluetooth LE address is valid identity address.

        Valid Bluetooth LE identity addresses are either public address or random static address.

        Parameters:
        :   - **addr** – Bluetooth LE device address.

        Returns:
        :   true if address is a valid identity address.

    static inline int bt\_addr\_to\_str(const [bt\_addr\_t](#c.bt_addr_t) \*addr, char \*str, size\_t len)
    :   Converts binary Bluetooth address to string.

        Parameters:
        :   - **addr** – Address of buffer containing binary Bluetooth address.
            - **str** – Address of user buffer with enough room to store formatted string containing binary address.
            - **len** – Length of data to be copied to user string buffer. Refer to BT\_ADDR\_STR\_LEN about recommended value.

        Returns:
        :   Number of successfully formatted bytes from binary address.

    static inline int bt\_addr\_le\_to\_str(const [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr, char \*str, size\_t len)
    :   Converts binary LE Bluetooth address to string.

        Parameters:
        :   - **addr** – Address of buffer containing binary LE Bluetooth address.
            - **str** – Address of user buffer with enough room to store formatted string containing binary LE address.
            - **len** – Length of data to be copied to user string buffer. Refer to BT\_ADDR\_LE\_STR\_LEN about recommended value.

        Returns:
        :   Number of successfully formatted bytes from binary address.

    int bt\_addr\_from\_str(const char \*str, [bt\_addr\_t](#c.bt_addr_t) \*addr)
    :   Convert Bluetooth address from string to binary.

        Parameters:
        :   - **str** – **[in]** The string representation of a Bluetooth address.
            - **addr** – **[out]** Address of buffer to store the Bluetooth address

        Return values:
        :   **0** – Success. The parsed address is stored in `addr`.

        Returns:
        :   -EINVAL Invalid address string. `str` is not a well-formed Bluetooth address.

    int bt\_addr\_le\_from\_str(const char \*str, const char \*type, [bt\_addr\_le\_t](#c.bt_addr_le_t) \*addr)
    :   Convert LE Bluetooth address from string to binary.

        Parameters:
        :   - **str** – **[in]** The string representation of an LE Bluetooth address.
            - **type** – **[in]** The string representation of the LE Bluetooth address type.
            - **addr** – **[out]** Address of buffer to store the LE Bluetooth address

        Returns:
        :   Zero on success or (negative) error code otherwise.

    Variables

    const [bt\_addr\_t](#c.bt_addr_t) bt\_addr\_any

    const [bt\_addr\_t](#c.bt_addr_t) bt\_addr\_none

    const [bt\_addr\_le\_t](#c.bt_addr_le_t) bt\_addr\_le\_any

    const [bt\_addr\_le\_t](#c.bt_addr_le_t) bt\_addr\_le\_none

    struct bt\_addr\_t
    :   *#include <addr.h>*

        Bluetooth Device Address.

    struct bt\_addr\_le\_t
    :   *#include <addr.h>*

        Bluetooth LE Device Address.

*group* bt\_gap\_defines
:   Bluetooth Generic Access Profile defines and Assigned Numbers.

    Company Identifiers (see Bluetooth Assigned Numbers)

    BT\_COMP\_ID\_LF
    :   The Linux Foundation.

    EIR/AD data type definitions

    BT\_DATA\_FLAGS
    :   AD flags.

    BT\_DATA\_UUID16\_SOME
    :   16-bit UUID, more available

    BT\_DATA\_UUID16\_ALL
    :   16-bit UUID, all listed

    BT\_DATA\_UUID32\_SOME
    :   32-bit UUID, more available

    BT\_DATA\_UUID32\_ALL
    :   32-bit UUID, all listed

    BT\_DATA\_UUID128\_SOME
    :   128-bit UUID, more available

    BT\_DATA\_UUID128\_ALL
    :   128-bit UUID, all listed

    BT\_DATA\_NAME\_SHORTENED
    :   Shortened name.

    BT\_DATA\_NAME\_COMPLETE
    :   Complete name.

    BT\_DATA\_TX\_POWER
    :   Tx Power.

    BT\_DATA\_SM\_TK\_VALUE
    :   Security Manager TK Value.

    BT\_DATA\_SM\_OOB\_FLAGS
    :   Security Manager OOB Flags.

    BT\_DATA\_PERIPHERAL\_INT\_RANGE
    :   Peripheral Connection Interval Range.

    BT\_DATA\_SOLICIT16
    :   Solicit UUIDs, 16-bit.

    BT\_DATA\_SOLICIT128
    :   Solicit UUIDs, 128-bit.

    BT\_DATA\_SVC\_DATA16
    :   Service data, 16-bit UUID.

    BT\_DATA\_PUB\_TARGET\_ADDR
    :   Public Target Address.

    BT\_DATA\_RAND\_TARGET\_ADDR
    :   Random Target Address.

    BT\_DATA\_GAP\_APPEARANCE
    :   GAP appearance.

    BT\_DATA\_ADV\_INT
    :   Advertising Interval.

    BT\_DATA\_LE\_BT\_DEVICE\_ADDRESS
    :   LE Bluetooth Device Address.

    BT\_DATA\_LE\_ROLE
    :   LE Role.

    BT\_DATA\_SIMPLE\_PAIRING\_HASH
    :   Simple Pairing Hash C256.

    BT\_DATA\_SIMPLE\_PAIRING\_RAND
    :   Simple Pairing Randomizer R256.

    BT\_DATA\_SOLICIT32
    :   Solicit UUIDs, 32-bit.

    BT\_DATA\_SVC\_DATA32
    :   Service data, 32-bit UUID.

    BT\_DATA\_SVC\_DATA128
    :   Service data, 128-bit UUID.

    BT\_DATA\_LE\_SC\_CONFIRM\_VALUE
    :   LE SC Confirmation Value.

    BT\_DATA\_LE\_SC\_RANDOM\_VALUE
    :   LE SC Random Value.

    BT\_DATA\_URI
    :   URI.

    BT\_DATA\_INDOOR\_POS
    :   Indoor Positioning.

    BT\_DATA\_TRANS\_DISCOVER\_DATA
    :   Transport Discovery Data.

    BT\_DATA\_LE\_SUPPORTED\_FEATURES
    :   LE Supported Features.

    BT\_DATA\_CHANNEL\_MAP\_UPDATE\_IND
    :   Channel Map Update Indication.

    BT\_DATA\_MESH\_PROV
    :   Mesh Provisioning PDU.

    BT\_DATA\_MESH\_MESSAGE
    :   Mesh Networking PDU.

    BT\_DATA\_MESH\_BEACON
    :   Mesh Beacon.

    BT\_DATA\_BIG\_INFO
    :   BIGInfo.

    BT\_DATA\_BROADCAST\_CODE
    :   Broadcast Code.

    BT\_DATA\_CSIS\_RSI
    :   CSIS Random Set ID type.

    BT\_DATA\_ADV\_INT\_LONG
    :   Advertising Interval long.

    BT\_DATA\_BROADCAST\_NAME
    :   Broadcast Name.

    BT\_DATA\_ENCRYPTED\_AD\_DATA
    :   Encrypted Advertising Data.

    BT\_DATA\_3D\_INFO
    :   3D Information Data

    BT\_DATA\_MANUFACTURER\_DATA
    :   Manufacturer Specific Data.

    BT\_LE\_AD\_LIMITED
    :   Limited Discoverable.

    BT\_LE\_AD\_GENERAL
    :   General Discoverable.

    BT\_LE\_AD\_NO\_BREDR
    :   BR/EDR not supported.

    Appearance Values

    Last Modified on 2023-01-05

    BT\_APPEARANCE\_UNKNOWN
    :   Generic Unknown.

    BT\_APPEARANCE\_GENERIC\_PHONE
    :   Generic Phone.

    BT\_APPEARANCE\_GENERIC\_COMPUTER
    :   Generic Computer.

    BT\_APPEARANCE\_COMPUTER\_DESKTOP\_WORKSTATION
    :   Desktop Workstation.

    BT\_APPEARANCE\_COMPUTER\_SERVER\_CLASS
    :   Server-class Computer.

    BT\_APPEARANCE\_COMPUTER\_LAPTOP
    :   Laptop.

    BT\_APPEARANCE\_COMPUTER\_HANDHELD\_PCPDA
    :   Handheld PC/PDA (clamshell).

    BT\_APPEARANCE\_COMPUTER\_PALMSIZE\_PCPDA
    :   Palm­size PC/PDA.

    BT\_APPEARANCE\_COMPUTER\_WEARABLE\_COMPUTER
    :   Wearable computer (watch size).

    BT\_APPEARANCE\_COMPUTER\_TABLET
    :   Tablet.

    BT\_APPEARANCE\_COMPUTER\_DOCKING\_STATION
    :   Docking Station.

    BT\_APPEARANCE\_COMPUTER\_ALL\_IN\_ONE
    :   All in One.

    BT\_APPEARANCE\_COMPUTER\_BLADE\_SERVER
    :   Blade Server.

    BT\_APPEARANCE\_COMPUTER\_CONVERTIBLE
    :   Convertible.

    BT\_APPEARANCE\_COMPUTER\_DETACHABLE
    :   Detachable.

    BT\_APPEARANCE\_COMPUTER\_IOT\_GATEWAY
    :   IoT Gateway.

    BT\_APPEARANCE\_COMPUTER\_MINI\_PC
    :   Mini PC.

    BT\_APPEARANCE\_COMPUTER\_STICK\_PC
    :   Stick PC.

    BT\_APPEARANCE\_GENERIC\_WATCH
    :   Generic Watch.

    BT\_APPEARANCE\_SPORTS\_WATCH
    :   Sports Watch.

    BT\_APPEARANCE\_SMARTWATCH
    :   Smartwatch.

    BT\_APPEARANCE\_GENERIC\_CLOCK
    :   Generic Clock.

    BT\_APPEARANCE\_GENERIC\_DISPLAY
    :   Generic Display.

    BT\_APPEARANCE\_GENERIC\_REMOTE
    :   Generic Remote Control.

    BT\_APPEARANCE\_GENERIC\_EYEGLASSES
    :   Generic Eye-glasses.

    BT\_APPEARANCE\_GENERIC\_TAG
    :   Generic Tag.

    BT\_APPEARANCE\_GENERIC\_KEYRING
    :   Generic Keyring.

    BT\_APPEARANCE\_GENERIC\_MEDIA\_PLAYER
    :   Generic Media Player.

    BT\_APPEARANCE\_GENERIC\_BARCODE\_SCANNER
    :   Generic Barcode Scanner.

    BT\_APPEARANCE\_GENERIC\_THERMOMETER
    :   Generic Thermometer.

    BT\_APPEARANCE\_THERMOMETER\_EAR
    :   Ear Thermometer.

    BT\_APPEARANCE\_GENERIC\_HEART\_RATE
    :   Generic Heart Rate Sensor.

    BT\_APPEARANCE\_HEART\_RATE\_BELT
    :   Heart Rate Belt.

    BT\_APPEARANCE\_GENERIC\_BLOOD\_PRESSURE
    :   Generic Blood Pressure.

    BT\_APPEARANCE\_BLOOD\_PRESSURE\_ARM
    :   Arm Blood Pressure.

    BT\_APPEARANCE\_BLOOD\_PRESSURE\_WRIST
    :   Wrist Blood Pressure.

    BT\_APPEARANCE\_GENERIC\_HID
    :   Generic Human Interface Device.

    BT\_APPEARANCE\_HID\_KEYBOARD
    :   Keyboard.

    BT\_APPEARANCE\_HID\_MOUSE
    :   Mouse.

    BT\_APPEARANCE\_HID\_JOYSTICK
    :   Joystick.

    BT\_APPEARANCE\_HID\_GAMEPAD
    :   Gamepad.

    BT\_APPEARANCE\_HID\_DIGITIZER\_TABLET
    :   Digitizer Tablet.

    BT\_APPEARANCE\_HID\_CARD\_READER
    :   Card Reader.

    BT\_APPEARANCE\_HID\_DIGITAL\_PEN
    :   Digital Pen.

    BT\_APPEARANCE\_HID\_BARCODE\_SCANNER
    :   Barcode Scanner.

    BT\_APPEARANCE\_HID\_TOUCHPAD
    :   Touchpad.

    BT\_APPEARANCE\_HID\_PRESENTATION\_REMOTE
    :   Presentation Remote.

    BT\_APPEARANCE\_GENERIC\_GLUCOSE
    :   Generic Glucose Meter.

    BT\_APPEARANCE\_GENERIC\_WALKING
    :   Generic Running Walking Sensor.

    BT\_APPEARANCE\_WALKING\_IN\_SHOE
    :   In-Shoe Running Walking Sensor.

    BT\_APPEARANCE\_WALKING\_ON\_SHOE
    :   On-Shoe Running Walking Sensor.

    BT\_APPEARANCE\_WALKING\_ON\_HIP
    :   On-Hip Running Walking Sensor.

    BT\_APPEARANCE\_GENERIC\_CYCLING
    :   Generic Cycling.

    BT\_APPEARANCE\_CYCLING\_COMPUTER
    :   Cycling Computer.

    BT\_APPEARANCE\_CYCLING\_SPEED
    :   Speed Sensor.

    BT\_APPEARANCE\_CYCLING\_CADENCE
    :   Cadence Sensor.

    BT\_APPEARANCE\_CYCLING\_POWER
    :   Power Sensor.

    BT\_APPEARANCE\_CYCLING\_SPEED\_CADENCE
    :   Speed and Cadence Sensor.

    BT\_APPEARANCE\_GENERIC\_CONTROL\_DEVICE
    :   Generic Control Device.

    BT\_APPEARANCE\_CONTROL\_SWITCH
    :   Switch.

    BT\_APPEARANCE\_CONTROL\_MULTI\_SWITCH
    :   Multi-switch.

    BT\_APPEARANCE\_CONTROL\_BUTTON
    :   Button.

    BT\_APPEARANCE\_CONTROL\_SLIDER
    :   Slider.

    BT\_APPEARANCE\_CONTROL\_ROTARY\_SWITCH
    :   Rotary Switch.

    BT\_APPEARANCE\_CONTROL\_TOUCH\_PANEL
    :   Touch Panel.

    BT\_APPEARANCE\_CONTROL\_SINGLE\_SWITCH
    :   Single Switch.

    BT\_APPEARANCE\_CONTROL\_DOUBLE\_SWITCH
    :   Double Switch.

    BT\_APPEARANCE\_CONTROL\_TRIPLE\_SWITCH
    :   Triple Switch.

    BT\_APPEARANCE\_CONTROL\_BATTERY\_SWITCH
    :   Battery Switch.

    BT\_APPEARANCE\_CONTROL\_ENERGY\_HARVESTING\_SWITCH
    :   Energy Harvesting Switch.

    BT\_APPEARANCE\_CONTROL\_PUSH\_BUTTON
    :   Push Button.

    BT\_APPEARANCE\_GENERIC\_NETWORK\_DEVICE
    :   Generic Network Device.

    BT\_APPEARANCE\_NETWORK\_ACCESS\_POINT
    :   Access Point.

    BT\_APPEARANCE\_NETWORK\_MESH\_DEVICE
    :   Mesh Device.

    BT\_APPEARANCE\_NETWORK\_MESH\_PROXY
    :   Mesh Network Proxy.

    BT\_APPEARANCE\_GENERIC\_SENSOR
    :   Generic Sensor.

    BT\_APPEARANCE\_SENSOR\_MOTION
    :   Motion Sensor.

    BT\_APPEARANCE\_SENSOR\_AIR\_QUALITY
    :   Air quality Sensor.

    BT\_APPEARANCE\_SENSOR\_TEMPERATURE
    :   Temperature Sensor.

    BT\_APPEARANCE\_SENSOR\_HUMIDITY
    :   Humidity Sensor.

    BT\_APPEARANCE\_SENSOR\_LEAK
    :   Leak Sensor.

    BT\_APPEARANCE\_SENSOR\_SMOKE
    :   Smoke Sensor.

    BT\_APPEARANCE\_SENSOR\_OCCUPANCY
    :   Occupancy Sensor.

    BT\_APPEARANCE\_SENSOR\_CONTACT
    :   Contact Sensor.

    BT\_APPEARANCE\_SENSOR\_CARBON\_MONOXIDE
    :   Carbon Monoxide Sensor.

    BT\_APPEARANCE\_SENSOR\_CARBON\_DIOXIDE
    :   Carbon Dioxide Sensor.

    BT\_APPEARANCE\_SENSOR\_AMBIENT\_LIGHT
    :   Ambient Light Sensor.

    BT\_APPEARANCE\_SENSOR\_ENERGY
    :   Energy Sensor.

    BT\_APPEARANCE\_SENSOR\_COLOR\_LIGHT
    :   Color Light Sensor.

    BT\_APPEARANCE\_SENSOR\_RAIN
    :   Rain Sensor.

    BT\_APPEARANCE\_SENSOR\_FIRE
    :   Fire Sensor.

    BT\_APPEARANCE\_SENSOR\_WIND
    :   Wind Sensor.

    BT\_APPEARANCE\_SENSOR\_PROXIMITY
    :   Proximity Sensor.

    BT\_APPEARANCE\_SENSOR\_MULTI
    :   Multi-Sensor.

    BT\_APPEARANCE\_SENSOR\_FLUSH\_MOUNTED
    :   Flush Mounted Sensor.

    BT\_APPEARANCE\_SENSOR\_CEILING\_MOUNTED
    :   Ceiling Mounted Sensor.

    BT\_APPEARANCE\_SENSOR\_WALL\_MOUNTED
    :   Wall Mounted Sensor.

    BT\_APPEARANCE\_MULTISENSOR
    :   Multisensor.

    BT\_APPEARANCE\_SENSOR\_ENERGY\_METER
    :   Energy Meter.

    BT\_APPEARANCE\_SENSOR\_FLAME\_DETECTOR
    :   Flame Detector.

    BT\_APPEARANCE\_SENSOR\_VEHICLE\_TIRE\_PRESSURE
    :   Vehicle Tire Pressure Sensor.

    BT\_APPEARANCE\_GENERIC\_LIGHT\_FIXTURES
    :   Generic Light Fixtures.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_WALL
    :   Wall Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_CEILING
    :   Ceiling Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOR
    :   Floor Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_CABINET
    :   Cabinet Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_DESK
    :   Desk Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_TROFFER
    :   Troffer Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_PENDANT
    :   Pendant Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_IN\_GROUND
    :   In-ground Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOD
    :   Flood Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_UNDERWATER
    :   Underwater Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_BOLLARD\_WITH
    :   Bollard with Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_PATHWAY
    :   Pathway Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_GARDEN
    :   Garden Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_POLE\_TOP
    :   Pole-top Light.

    BT\_APPEARANCE\_SPOT\_LIGHT
    :   Spotlight.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_LINEAR
    :   Linear Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_STREET
    :   Street Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_SHELVES
    :   Shelves Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_BAY
    :   Bay Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_EMERGENCY\_EXIT
    :   Emergency Exit Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_CONTROLLER
    :   Light Controller.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_DRIVER
    :   Light Driver.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_BULB
    :   Bulb.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_LOW\_BAY
    :   Low-bay Light.

    BT\_APPEARANCE\_LIGHT\_FIXTURES\_HIGH\_BAY
    :   High-bay Light.

    BT\_APPEARANCE\_GENERIC\_FAN
    :   Generic Fan.

    BT\_APPEARANCE\_FAN\_CEILING
    :   Ceiling Fan.

    BT\_APPEARANCE\_FAN\_AXIAL
    :   Axial Fan.

    BT\_APPEARANCE\_FAN\_EXHAUST
    :   Exhaust Fan.

    BT\_APPEARANCE\_FAN\_PEDESTAL
    :   Pedestal Fan.

    BT\_APPEARANCE\_FAN\_DESK
    :   Desk Fan.

    BT\_APPEARANCE\_FAN\_WALL
    :   Wall Fan.

    BT\_APPEARANCE\_GENERIC\_HVAC
    :   Generic HVAC.

    BT\_APPEARANCE\_HVAC\_THERMOSTAT
    :   Thermostat.

    BT\_APPEARANCE\_HVAC\_HUMIDIFIER
    :   Humidifier.

    BT\_APPEARANCE\_HVAC\_DEHUMIDIFIER
    :   De-humidifier.

    BT\_APPEARANCE\_HVAC\_HEATER
    :   Heater.

    BT\_APPEARANCE\_HVAC\_RADIATOR
    :   Radiator.

    BT\_APPEARANCE\_HVAC\_BOILER
    :   Boiler.

    BT\_APPEARANCE\_HVAC\_HEAT\_PUMP
    :   Heat Pump.

    BT\_APPEARANCE\_HVAC\_INFRARED\_HEATER
    :   Infrared Heater.

    BT\_APPEARANCE\_HVAC\_RADIANT\_PANEL\_HEATER
    :   Radiant Panel Heater.

    BT\_APPEARANCE\_HVAC\_FAN\_HEATER
    :   Fan Heater.

    BT\_APPEARANCE\_HVAC\_AIR\_CURTAIN
    :   Air Curtain.

    BT\_APPEARANCE\_GENERIC\_AIR\_CONDITIONING
    :   Generic Air Conditioning.

    BT\_APPEARANCE\_GENERIC\_HUMIDIFIER
    :   Generic Humidifier.

    BT\_APPEARANCE\_GENERIC\_HEATING
    :   Generic Heating.

    BT\_APPEARANCE\_HEATING\_RADIATOR
    :   Radiator.

    BT\_APPEARANCE\_HEATING\_BOILER
    :   Boiler.

    BT\_APPEARANCE\_HEATING\_HEAT\_PUMP
    :   Heat Pump.

    BT\_APPEARANCE\_HEATING\_INFRARED\_HEATER
    :   Infrared Heater.

    BT\_APPEARANCE\_HEATING\_RADIANT\_PANEL\_HEATER
    :   Radiant Panel Heater.

    BT\_APPEARANCE\_HEATING\_FAN\_HEATER
    :   Fan Heater.

    BT\_APPEARANCE\_HEATING\_AIR\_CURTAIN
    :   Air Curtain.

    BT\_APPEARANCE\_GENERIC\_ACCESS\_CONTROL
    :   Generic Access Control.

    BT\_APPEARANCE\_CONTROL\_ACCESS\_DOOR
    :   Access Door.

    BT\_APPEARANCE\_CONTROL\_GARAGE\_DOOR
    :   Garage Door.

    BT\_APPEARANCE\_CONTROL\_EMERGENCY\_EXIT\_DOOR
    :   Emergency Exit Door.

    BT\_APPEARANCE\_CONTROL\_ACCESS\_LOCK
    :   Access Lock.

    BT\_APPEARANCE\_CONTROL\_ELEVATOR
    :   Elevator.

    BT\_APPEARANCE\_CONTROL\_WINDOW
    :   Window.

    BT\_APPEARANCE\_CONTROL\_ENTRANCE\_GATE
    :   Entrance Gate.

    BT\_APPEARANCE\_CONTROL\_DOOR\_LOCK
    :   Door Lock.

    BT\_APPEARANCE\_CONTROL\_LOCKER
    :   Locker.

    BT\_APPEARANCE\_GENERIC\_MOTORIZED\_DEVICE
    :   Generic Motorized Device.

    BT\_APPEARANCE\_MOTORIZED\_GATE
    :   Motorized Gate.

    BT\_APPEARANCE\_MOTORIZED\_AWNING
    :   Awning.

    BT\_APPEARANCE\_MOTORIZED\_BLINDS\_OR\_SHADES
    :   Blinds or Shades.

    BT\_APPEARANCE\_MOTORIZED\_CURTAINS
    :   Curtains.

    BT\_APPEARANCE\_MOTORIZED\_SCREEN
    :   Screen.

    BT\_APPEARANCE\_GENERIC\_POWER\_DEVICE
    :   Generic Power Device.

    BT\_APPEARANCE\_POWER\_OUTLET
    :   Power Outlet.

    BT\_APPEARANCE\_POWER\_STRIP
    :   Power Strip.

    BT\_APPEARANCE\_POWER\_PLUG
    :   Plug.

    BT\_APPEARANCE\_POWER\_SUPPLY
    :   Power Supply.

    BT\_APPEARANCE\_POWER\_LED\_DRIVER
    :   LED Driver.

    BT\_APPEARANCE\_POWER\_FLUORESCENT\_LAMP\_GEAR
    :   Fluorescent Lamp Gear.

    BT\_APPEARANCE\_POWER\_HID\_LAMP\_GEAR
    :   HID Lamp Gear.

    BT\_APPEARANCE\_POWER\_CHARGE\_CASE
    :   Charge Case.

    BT\_APPEARANCE\_POWER\_POWER\_BANK
    :   Power Bank.

    BT\_APPEARANCE\_GENERIC\_LIGHT\_SOURCE
    :   Generic Light Source.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_INCANDESCENT\_BULB
    :   Incandescent Light Bulb.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_LAMP
    :   LED Lamp.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_HID\_LAMP
    :   HID Lamp.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_FLUORESCENT\_LAMP
    :   Fluorescent Lamp.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_ARRAY
    :   LED Array.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_MULTICOLOR\_LED\_ARRAY
    :   Multi-Color LED Array.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_LOW\_VOLTAGE\_HALOGEN
    :   Low voltage halogen.

    BT\_APPEARANCE\_LIGHT\_SOURCE\_OLED
    :   Organic light emitting diode.

    BT\_APPEARANCE\_GENERIC\_WINDOW\_COVERING
    :   Generic Window Covering.

    BT\_APPEARANCE\_WINDOW\_SHADES
    :   Window Shades.

    BT\_APPEARANCE\_WINDOW\_BLINDS
    :   Window Blinds.

    BT\_APPEARANCE\_WINDOW\_AWNING
    :   Window Awning.

    BT\_APPEARANCE\_WINDOW\_CURTAIN
    :   Window Curtain.

    BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SHUTTER
    :   Exterior Shutter.

    BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SCREEN
    :   Exterior Screen.

    BT\_APPEARANCE\_GENERIC\_AUDIO\_SINK
    :   Generic Audio Sink.

    BT\_APPEARANCE\_AUDIO\_SINK\_STANDALONE\_SPEAKER
    :   Standalone Speaker.

    BT\_APPEARANCE\_AUDIO\_SINK\_SOUNDBAR
    :   Soundbar.

    BT\_APPEARANCE\_AUDIO\_SINK\_BOOKSHELF\_SPEAKER
    :   Bookshelf Speaker.

    BT\_APPEARANCE\_AUDIO\_SINK\_STANDMOUNTED\_SPEAKER
    :   Standmounted Speaker.

    BT\_APPEARANCE\_AUDIO\_SINK\_SPEAKERPHONE
    :   Speakerphone.

    BT\_APPEARANCE\_GENERIC\_AUDIO\_SOURCE
    :   Generic Audio Source.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_MICROPHONE
    :   Microphone.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_ALARM
    :   Alarm.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_BELL
    :   Bell.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_HORN
    :   Horn.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_DEVICE
    :   Broadcasting Device.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_SERVICE\_DESK
    :   Service Desk.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_KIOSK
    :   Kiosk.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_ROOM
    :   Broadcasting Room.

    BT\_APPEARANCE\_AUDIO\_SOURCE\_AUDITORIUM
    :   Auditorium.

    BT\_APPEARANCE\_GENERIC\_MOTORIZED\_VEHICLE
    :   Generic Motorized Vehicle.

    BT\_APPEARANCE\_VEHICLE\_CAR
    :   Car.

    BT\_APPEARANCE\_VEHICLE\_LARGE\_GOODS
    :   Large Goods Vehicle.

    BT\_APPEARANCE\_VEHICLE\_TWO\_WHEELED
    :   2-Wheeled Vehicle

    BT\_APPEARANCE\_VEHICLE\_MOTORBIKE
    :   Motorbike.

    BT\_APPEARANCE\_VEHICLE\_SCOOTER
    :   Scooter.

    BT\_APPEARANCE\_VEHICLE\_MOPED
    :   Moped.

    BT\_APPEARANCE\_VEHICLE\_THREE\_WHEELED
    :   3-Wheeled Vehicle

    BT\_APPEARANCE\_VEHICLE\_LIGHT
    :   Light Vehicle.

    BT\_APPEARANCE\_VEHICLE\_QUAD\_BIKE
    :   Quad Bike.

    BT\_APPEARANCE\_VEHICLE\_MINIBUS
    :   Minibus.

    BT\_APPEARANCE\_VEHICLE\_BUS
    :   Bus.

    BT\_APPEARANCE\_VEHICLE\_TROLLEY
    :   Trolley.

    BT\_APPEARANCE\_VEHICLE\_AGRICULTURAL
    :   Agricultural Vehicle.

    BT\_APPEARANCE\_VEHICLE\_CAMPER\_OR\_CARAVAN
    :   Camper/Caravan.

    BT\_APPEARANCE\_VEHICLE\_RECREATIONAL
    :   Recreational Vehicle/Motor Home.

    BT\_APPEARANCE\_GENERIC\_DOMESTIC\_APPLIANCE
    :   Generic Domestic Appliance.

    BT\_APPEARANCE\_APPLIANCE\_REFRIGERATOR
    :   Refrigerator.

    BT\_APPEARANCE\_APPLIANCE\_FREEZER
    :   Freezer.

    BT\_APPEARANCE\_APPLIANCE\_OVEN
    :   Oven.

    BT\_APPEARANCE\_APPLIANCE\_MICROWAVE
    :   Microwave.

    BT\_APPEARANCE\_APPLIANCE\_TOASTER
    :   Toaster.

    BT\_APPEARANCE\_APPLIANCE\_WASHING\_MACHINE
    :   Washing Machine.

    BT\_APPEARANCE\_APPLIANCE\_DRYER
    :   Dryer.

    BT\_APPEARANCE\_APPLIANCE\_COFFEE\_MAKER
    :   Coffee maker.

    BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_IRON
    :   Clothes iron.

    BT\_APPEARANCE\_APPLIANCE\_CURLING\_IRON
    :   Curling iron.

    BT\_APPEARANCE\_APPLIANCE\_HAIR\_DRYER
    :   Hair dryer.

    BT\_APPEARANCE\_APPLIANCE\_VACUUM\_CLEANER
    :   Vacuum cleaner.

    BT\_APPEARANCE\_APPLIANCE\_ROBOTIC\_VACUUM\_CLEANER
    :   Robotic vacuum cleaner.

    BT\_APPEARANCE\_APPLIANCE\_RICE\_COOKER
    :   Rice cooker.

    BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_STEAMER
    :   Clothes steamer.

    BT\_APPEARANCE\_GENERIC\_WEARABLE\_AUDIO\_DEVICE
    :   Generic Wearable Audio Device.

    BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_EARBUD
    :   Earbud.

    BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADSET
    :   Headset.

    BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADPHONES
    :   Headphones.

    BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_NECK\_BAND
    :   Neck Band.

    BT\_APPEARANCE\_GENERIC\_AIRCRAFT
    :   Generic Aircraft.

    BT\_APPEARANCE\_AIRCRAFT\_LIGHT
    :   Light Aircraft.

    BT\_APPEARANCE\_AIRCRAFT\_MICROLIGHT
    :   Microlight.

    BT\_APPEARANCE\_AIRCRAFT\_PARAGLIDER
    :   Paraglider.

    BT\_APPEARANCE\_AIRCRAFT\_LARGE\_PASSENGER
    :   Large Passenger Aircraft.

    BT\_APPEARANCE\_GENERIC\_AV\_EQUIPMENT
    :   Generic AV Equipment.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_AMPLIFIER
    :   Amplifier.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_RECEIVER
    :   Receiver.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_RADIO
    :   Radio.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_TUNER
    :   Tuner.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_TURNTABLE
    :   Turntable.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_CD\_PLAYER
    :   CD Player.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_DVD\_PLAYER
    :   DVD Player.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_BLURAY\_PLAYER
    :   Bluray Player.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_OPTICAL\_DISC\_PLAYER
    :   Optical Disc Player.

    BT\_APPEARANCE\_AV\_EQUIPMENT\_SET\_TOP\_BOX
    :   Set-Top Box.

    BT\_APPEARANCE\_GENERIC\_DISPLAY\_EQUIPMENT
    :   Generic Display Equipment.

    BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_TELEVISION
    :   Television.

    BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_MONITOR
    :   Monitor.

    BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_PROJECTOR
    :   Projector.

    BT\_APPEARANCE\_GENERIC\_HEARING\_AID
    :   Generic Hearing aid.

    BT\_APPEARANCE\_HEARING\_AID\_IN\_EAR
    :   In-ear hearing aid.

    BT\_APPEARANCE\_HEARING\_AID\_BEHIND\_EAR
    :   Behind-ear hearing aid.

    BT\_APPEARANCE\_HEARING\_AID\_COCHLEAR\_IMPLANT
    :   Cochlear Implant.

    BT\_APPEARANCE\_GENERIC\_GAMING
    :   Generic Gaming.

    BT\_APPEARANCE\_HOME\_VIDEO\_GAME\_CONSOLE
    :   Home Video Game Console.

    BT\_APPEARANCE\_PORTABLE\_HANDHELD\_CONSOLE
    :   Portable handheld console.

    BT\_APPEARANCE\_GENERIC\_SIGNAGE
    :   Generic Signage.

    BT\_APPEARANCE\_SIGNAGE\_DIGITAL
    :   Digital Signage.

    BT\_APPEARANCE\_SIGNAGE\_ELECTRONIC\_LABEL
    :   Electronic Label.

    BT\_APPEARANCE\_GENERIC\_PULSE\_OXIMETER
    :   Generic Pulse Oximeter.

    BT\_APPEARANCE\_PULSE\_OXIMETER\_FINGERTIP
    :   Fingertip Pulse Oximeter.

    BT\_APPEARANCE\_PULSE\_OXIMETER\_WRIST
    :   Wrist Worn Pulse Oximeter.

    BT\_APPEARANCE\_GENERIC\_WEIGHT\_SCALE
    :   Generic Weight Scale.

    BT\_APPEARANCE\_GENERIC\_PERSONAL\_MOBILITY\_DEVICE
    :   Generic Personal Mobility Device.

    BT\_APPEARANCE\_MOBILITY\_POWERED\_WHEELCHAIR
    :   Powered Wheelchair.

    BT\_APPEARANCE\_MOBILITY\_SCOOTER
    :   Mobility Scooter.

    BT\_APPEARANCE\_CONTINUOUS\_GLUCOSE\_MONITOR
    :   Continuous Glucose Monitor.

    BT\_APPEARANCE\_GENERIC\_INSULIN\_PUMP
    :   Generic Insulin Pump.

    BT\_APPEARANCE\_INSULIN\_PUMP\_DURABLE
    :   Insulin Pump, durable pump.

    BT\_APPEARANCE\_INSULIN\_PUMP\_PATCH
    :   Insulin Pump, patch pump.

    BT\_APPEARANCE\_INSULIN\_PEN
    :   Insulin Pen.

    BT\_APPEARANCE\_GENERIC\_MEDICATION\_DELIVERY
    :   Generic Medication Delivery.

    BT\_APPEARANCE\_GENERIC\_SPIROMETER
    :   Generic Spirometer.

    BT\_APPEARANCE\_SPIROMETER\_HANDHELD
    :   Handheld Spirometer.

    BT\_APPEARANCE\_GENERIC\_OUTDOOR\_SPORTS
    :   Generic Outdoor Sports Activity.

    BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION
    :   Location Display.

    BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_AND\_NAV
    :   Location and Navigation Display.

    BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD
    :   Location Pod.

    BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD\_AND\_NAV
    :   Location and Navigation Pod.

    Defined GAP timers

    BT\_GAP\_SCAN\_FAST\_INTERVAL

    BT\_GAP\_SCAN\_FAST\_WINDOW

    BT\_GAP\_SCAN\_SLOW\_INTERVAL\_1

    BT\_GAP\_SCAN\_SLOW\_WINDOW\_1

    BT\_GAP\_SCAN\_SLOW\_INTERVAL\_2

    BT\_GAP\_SCAN\_SLOW\_WINDOW\_2

    BT\_GAP\_ADV\_FAST\_INT\_MIN\_1

    BT\_GAP\_ADV\_FAST\_INT\_MAX\_1

    BT\_GAP\_ADV\_FAST\_INT\_MIN\_2

    BT\_GAP\_ADV\_FAST\_INT\_MAX\_2

    BT\_GAP\_ADV\_SLOW\_INT\_MIN

    BT\_GAP\_ADV\_SLOW\_INT\_MAX

    BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_1

    BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_1

    BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_2

    BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_2

    BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN

    BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX

    BT\_GAP\_INIT\_CONN\_INT\_MIN

    BT\_GAP\_INIT\_CONN\_INT\_MAX

    Defines

    BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN
    :   Maximum advertising data length.

    BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN
    :   Maximum extended advertising data length.

        Note

        The maximum advertising data length that can be sent by an extended advertiser is defined by the controller.

    BT\_GAP\_TX\_POWER\_INVALID

    BT\_GAP\_RSSI\_INVALID

    BT\_GAP\_SID\_INVALID

    BT\_GAP\_NO\_TIMEOUT

    BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT

    BT\_GAP\_DATA\_LEN\_DEFAULT
    :   Default data length.

    BT\_GAP\_DATA\_LEN\_MAX
    :   Maximum data length.

    BT\_GAP\_DATA\_TIME\_DEFAULT
    :   Default data time.

    BT\_GAP\_DATA\_TIME\_MAX
    :   Maximum data time.

    BT\_GAP\_SID\_MAX
    :   Maximum advertising set number.

    BT\_GAP\_PER\_ADV\_MAX\_SKIP
    :   Maximum number of consecutive periodic advertisement events that can be skipped after a successful receive.

    BT\_GAP\_PER\_ADV\_MIN\_TIMEOUT
    :   Minimum Periodic Advertising Timeout (N \* 10 ms).

    BT\_GAP\_PER\_ADV\_MAX\_TIMEOUT
    :   Maximum Periodic Advertising Timeout (N \* 10 ms).

    BT\_GAP\_PER\_ADV\_MIN\_INTERVAL
    :   Minimum Periodic Advertising Interval (N \* 1.25 ms).

    BT\_GAP\_PER\_ADV\_MAX\_INTERVAL
    :   Maximum Periodic Advertising Interval (N \* 1.25 ms).

    BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_MS(interval)
    :   Convert periodic advertising interval (N \* 1.25 ms) to milliseconds.

        5 / 4 represents 1.25 ms unit.

    BT\_LE\_SUPP\_FEAT\_40\_ENCODE(w64)
    :   Encode 40 least significant bits of 64-bit LE Supported Features into array values in little-endian format.

        Helper macro to encode 40 least significant bits of 64-bit LE Supported Features value into advertising data. The number of bits that are encoded is a number of LE Supported Features defined by BT 5.3 Core specification.

        Example of how to encode the `0x000000DFF00DF00D` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_40_ENCODE(0x000000DFF00DF00D))
        ```

        Parameters:
        :   - **w64** – LE Supported Features value (64-bits)

        Returns:
        :   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](#group__bt__gap_1ga4c51f9b7a3a4e84abb4df3f1f714c6e2).

    BT\_LE\_SUPP\_FEAT\_32\_ENCODE(w64)
    :   Encode 4 least significant bytes of 64-bit LE Supported Features into 4 bytes long array of values in little-endian format.

        Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes 4 least significant bytes into advertising data. Other 4 bytes are not encoded.

        Example of how to encode the `0x000000DFF00DF00D` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_32_ENCODE(0x000000DFF00DF00D))
        ```

        Parameters:
        :   - **w64** – LE Supported Features value (64-bits)

        Returns:
        :   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](#group__bt__gap_1ga4c51f9b7a3a4e84abb4df3f1f714c6e2).

    BT\_LE\_SUPP\_FEAT\_24\_ENCODE(w64)
    :   Encode 3 least significant bytes of 64-bit LE Supported Features into 3 bytes long array of values in little-endian format.

        Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes 3 least significant bytes into advertising data. Other 5 bytes are not encoded.

        Example of how to encode the `0x000000DFF00DF00D` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_24_ENCODE(0x000000DFF00DF00D))
        ```

        Parameters:
        :   - **w64** – LE Supported Features value (64-bits)

        Returns:
        :   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](#group__bt__gap_1ga4c51f9b7a3a4e84abb4df3f1f714c6e2).

    BT\_LE\_SUPP\_FEAT\_16\_ENCODE(w64)
    :   Encode 2 least significant bytes of 64-bit LE Supported Features into 2 bytes long array of values in little-endian format.

        Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes 3 least significant bytes into advertising data. Other 6 bytes are not encoded.

        Example of how to encode the `0x000000DFF00DF00D` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_16_ENCODE(0x000000DFF00DF00D))
        ```

        Parameters:
        :   - **w64** – LE Supported Features value (64-bits)

        Returns:
        :   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](#group__bt__gap_1ga4c51f9b7a3a4e84abb4df3f1f714c6e2).

    BT\_LE\_SUPP\_FEAT\_8\_ENCODE(w64)
    :   Encode the least significant byte of 64-bit LE Supported Features into single byte long array.

        Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes the least significant byte into advertising data. Other 7 bytes are not encoded.

        Example of how to encode the `0x000000DFF00DF00D` into advertising data.

        ```text
        BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_8_ENCODE(0x000000DFF00DF00D))
        ```

        Parameters:
        :   - **w64** – LE Supported Features value (64-bits)

        Returns:
        :   The value of least significant byte of LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](#group__bt__gap_1ga4c51f9b7a3a4e84abb4df3f1f714c6e2).

    BT\_LE\_SUPP\_FEAT\_VALIDATE(w64)
    :   Validate whether LE Supported Features value does not use bits that are reserved for future use.

        Helper macro to check if `w64` has zeros as bits 40-63. The macro is compliant with BT 5.3 Core Specification where bits 0-40 has assigned values. In case of invalid value, build time error is reported.

    Enums

    enum [anonymous]
    :   LE PHY types.

        *Values:*

        enumerator BT\_GAP\_LE\_PHY\_NONE = 0
        :   Convenience macro for when no PHY is set.

        enumerator BT\_GAP\_LE\_PHY\_1M = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   LE 1M PHY.

        enumerator BT\_GAP\_LE\_PHY\_2M = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   LE 2M PHY.

        enumerator BT\_GAP\_LE\_PHY\_CODED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   LE Coded PHY.

    enum [anonymous]
    :   Advertising PDU types.

        *Values:*

        enumerator BT\_GAP\_ADV\_TYPE\_ADV\_IND = 0x00
        :   Scannable and connectable advertising.

        enumerator BT\_GAP\_ADV\_TYPE\_ADV\_DIRECT\_IND = 0x01
        :   Directed connectable advertising.

        enumerator BT\_GAP\_ADV\_TYPE\_ADV\_SCAN\_IND = 0x02
        :   Non-connectable and scannable advertising.

        enumerator BT\_GAP\_ADV\_TYPE\_ADV\_NONCONN\_IND = 0x03
        :   Non-connectable and non-scannable advertising.

        enumerator BT\_GAP\_ADV\_TYPE\_SCAN\_RSP = 0x04
        :   Additional advertising data requested by an active scanner.

        enumerator BT\_GAP\_ADV\_TYPE\_EXT\_ADV = 0x05
        :   Extended advertising, see advertising properties.

    enum [anonymous]
    :   Advertising PDU properties.

        *Values:*

        enumerator BT\_GAP\_ADV\_PROP\_CONNECTABLE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Connectable advertising.

        enumerator BT\_GAP\_ADV\_PROP\_SCANNABLE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Scannable advertising.

        enumerator BT\_GAP\_ADV\_PROP\_DIRECTED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Directed advertising.

        enumerator BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Additional advertising data requested by an active scanner.

        enumerator BT\_GAP\_ADV\_PROP\_EXT\_ADV = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Extended advertising.

    enum [anonymous]
    :   Constant Tone Extension (CTE) types.

        *Values:*

        enumerator BT\_GAP\_CTE\_AOA = 0x00
        :   Angle of Arrival.

        enumerator BT\_GAP\_CTE\_AOD\_1US = 0x01
        :   Angle of Departure with 1 us slots.

        enumerator BT\_GAP\_CTE\_AOD\_2US = 0x02
        :   Angle of Departure with 2 us slots.

        enumerator BT\_GAP\_CTE\_NONE = 0xFF
        :   No extensions.

    enum [anonymous]
    :   Peripheral sleep clock accuracy (SCA) in ppm (parts per million).

        *Values:*

        enumerator BT\_GAP\_SCA\_UNKNOWN = 0
        :   Unknown.

        enumerator BT\_GAP\_SCA\_251\_500 = 0
        :   251 ppm to 500 ppm

        enumerator BT\_GAP\_SCA\_151\_250 = 1
        :   151 ppm to 250 ppm

        enumerator BT\_GAP\_SCA\_101\_150 = 2
        :   101 ppm to 150 ppm

        enumerator BT\_GAP\_SCA\_76\_100 = 3
        :   76 ppm to 100 ppm

        enumerator BT\_GAP\_SCA\_51\_75 = 4
        :   51 ppm to 75 ppm

        enumerator BT\_GAP\_SCA\_31\_50 = 5
        :   31 ppm to 50 ppm

        enumerator BT\_GAP\_SCA\_21\_30 = 6
        :   21 ppm to 30 ppm

        enumerator BT\_GAP\_SCA\_0\_20 = 7
        :   0 ppm to 20 ppm
