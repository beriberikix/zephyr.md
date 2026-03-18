---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/net_linkaddr.html
original_path: connectivity/networking/api/net_linkaddr.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Link Layer Address Handling

## [Overview](#id1)

The link layer addresses are set for network interfaces so that L2
connectivity works correctly in the network stack. Typically the link layer
addresses are 6 bytes long like in Ethernet but for IEEE 802.15.4 the link
layer address length is 8 bytes.

## [API Reference](#id2)

*group* net\_linkaddr
:   Network link address library.

    Defines

    NET\_LINK\_ADDR\_MAX\_LENGTH
    :   Maximum length of the link address.

    Enums

    enum net\_link\_type
    :   Type of the link address.

        This indicates the network technology that this address is used in. Note that in order to save space we store the value into a uint8\_t variable, so please do not introduce any values > 255 in this enum.

        *Values:*

        enumerator NET\_LINK\_UNKNOWN = 0
        :   Unknown link address type.

        enumerator NET\_LINK\_IEEE802154
        :   IEEE 802.15.4 link address.

        enumerator NET\_LINK\_BLUETOOTH
        :   Bluetooth IPSP link address.

        enumerator NET\_LINK\_ETHERNET
        :   Ethernet link address.

        enumerator NET\_LINK\_DUMMY
        :   Dummy link address.

            Used in testing apps and loopback support.

        enumerator NET\_LINK\_CANBUS\_RAW
        :   CANBUS link address.

    Functions

    static inline bool net\_linkaddr\_cmp(struct [net\_linkaddr](#c.net_linkaddr) \*lladdr1, struct [net\_linkaddr](#c.net_linkaddr) \*lladdr2)
    :   Compare two link layer addresses.

        Parameters:
        :   - **lladdr1** – Pointer to a link layer address
            - **lladdr2** – Pointer to a link layer address

        Returns:
        :   True if the addresses are the same, false otherwise.

    static inline int net\_linkaddr\_set(struct [net\_linkaddr\_storage](#c.net_linkaddr_storage) \*lladdr\_store, uint8\_t \*new\_addr, uint8\_t new\_len)
    :   Set the member data of a link layer address storage structure.

        Parameters:
        :   - **lladdr\_store** – The link address storage structure to change.
            - **new\_addr** – Array of bytes containing the link address.
            - **new\_len** – Length of the link address array. This value should always be <= NET\_LINK\_ADDR\_MAX\_LENGTH.

    struct net\_linkaddr
    :   *#include <net\_linkaddr.h>*

        Hardware link address structure.

        Used to hold the link address information

        Public Members

        uint8\_t \*addr
        :   The array of byte representing the address.

        uint8\_t len
        :   Length of that address array.

        uint8\_t type
        :   What kind of address is this for.

    struct net\_linkaddr\_storage
    :   *#include <net\_linkaddr.h>*

        Hardware link address structure.

        Used to hold the link address information. This variant is needed when we have to store the link layer address.

        Note that you cannot cast this to [net\_linkaddr](#structnet__linkaddr) as uint8\_t \* is handled differently than uint8\_t addr[] and the fields are purposely in different order.

        Public Members

        uint8\_t type
        :   What kind of address is this for.

        uint8\_t len
        :   The real length of the ll address.

        uint8\_t addr[6]
        :   The array of bytes representing the address.
