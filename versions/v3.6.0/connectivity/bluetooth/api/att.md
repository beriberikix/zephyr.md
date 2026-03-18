---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/att.html
original_path: connectivity/bluetooth/api/att.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Attribute Protocol (ATT)

## API Reference

*group* bt\_att
:   Attribute Protocol (ATT).

    Defines

    BT\_ATT\_ERR\_SUCCESS
    :   The ATT operation was successful.

    BT\_ATT\_ERR\_INVALID\_HANDLE
    :   The attribute handle given was not valid on the server.

    BT\_ATT\_ERR\_READ\_NOT\_PERMITTED
    :   The attribute cannot be read.

    BT\_ATT\_ERR\_WRITE\_NOT\_PERMITTED
    :   The attribute cannot be written.

    BT\_ATT\_ERR\_INVALID\_PDU
    :   The attribute PDU was invalid.

    BT\_ATT\_ERR\_AUTHENTICATION
    :   The attribute requires authentication before it can be read or written.

    BT\_ATT\_ERR\_NOT\_SUPPORTED
    :   The ATT Server does not support the request received from the client.

    BT\_ATT\_ERR\_INVALID\_OFFSET
    :   Offset specified was past the end of the attribute.

    BT\_ATT\_ERR\_AUTHORIZATION
    :   The attribute requires authorization before it can be read or written.

    BT\_ATT\_ERR\_PREPARE\_QUEUE\_FULL
    :   Too many prepare writes have been queued.

    BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_FOUND
    :   No attribute found within the given attribute handle range.

    BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_LONG
    :   The attribute cannot be read using the ATT\_READ\_BLOB\_REQ PDU.

    BT\_ATT\_ERR\_ENCRYPTION\_KEY\_SIZE
    :   The Encryption Key Size used for encrypting this link is too short.

    BT\_ATT\_ERR\_INVALID\_ATTRIBUTE\_LEN
    :   The attribute value length is invalid for the operation.

    BT\_ATT\_ERR\_UNLIKELY
    :   The attribute request that was requested has encountered an error that was unlikely.

        The attribute request could therefore not be completed as requested

    BT\_ATT\_ERR\_INSUFFICIENT\_ENCRYPTION
    :   The attribute requires encryption before it can be read or written.

    BT\_ATT\_ERR\_UNSUPPORTED\_GROUP\_TYPE
    :   The attribute type is not a supported grouping attribute.

        The attribute type is not a supported grouping attribute as defined by a higher layer specification.

    BT\_ATT\_ERR\_INSUFFICIENT\_RESOURCES
    :   Insufficient Resources to complete the request.

    BT\_ATT\_ERR\_DB\_OUT\_OF\_SYNC
    :   The server requests the client to rediscover the database.

    BT\_ATT\_ERR\_VALUE\_NOT\_ALLOWED
    :   The attribute parameter value was not allowed.

    BT\_ATT\_ERR\_WRITE\_REQ\_REJECTED
    :   Write Request Rejected.

    BT\_ATT\_ERR\_CCC\_IMPROPER\_CONF
    :   Client Characteristic Configuration Descriptor Improperly Configured.

    BT\_ATT\_ERR\_PROCEDURE\_IN\_PROGRESS
    :   Procedure Already in Progress.

    BT\_ATT\_ERR\_OUT\_OF\_RANGE
    :   Out of Range.

    BT\_ATT\_MAX\_ATTRIBUTE\_LEN

    BT\_ATT\_FIRST\_ATTRIBUTE\_HANDLE

    BT\_ATT\_FIRST\_ATTTRIBUTE\_HANDLE

    BT\_ATT\_LAST\_ATTRIBUTE\_HANDLE

    BT\_ATT\_LAST\_ATTTRIBUTE\_HANDLE

    Enums

    enum bt\_att\_chan\_opt
    :   ATT channel option bit field values.

        Note

        [BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY](#group__bt__att_1ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4) and [BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY](#group__bt__att_1ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6) are mutually exclusive and both bits may not be set.

        *Values:*

        enumerator BT\_ATT\_CHAN\_OPT\_NONE = 0x0
        :   Both Enhanced and Unenhanced channels can be used.

        enumerator BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Only Unenhanced channels will be used.

        enumerator BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Only Enhanced channels will be used.

    Functions

    int bt\_eatt\_connect(struct bt\_conn \*conn, size\_t num\_channels)
    :   Connect Enhanced ATT channels.

        Sends a series of Credit Based Connection Requests to connect `num_channels` Enhanced ATT channels. The peer may have limited resources and fewer channels may be created.

        Parameters:
        :   - **conn** – The connection to send the request on
            - **num\_channels** – The number of Enhanced ATT beares to request. Must be in the range 1 -  [`CONFIG_BT_EATT_MAX`](../../../kconfig.md#CONFIG_BT_EATT_MAX "CONFIG_BT_EATT_MAX") , inclusive.

        Return values:
        :   - **-EINVAL** – if `num_channels` is not in the allowed range or `conn` is NULL.
            - **-ENOMEM** – if less than `num_channels` are allocated.
            - **0** – in case of success

        Returns:
        :   0 in case of success or negative value in case of error.

    size\_t bt\_eatt\_count(struct bt\_conn \*conn)
    :   Get number of EATT channels connected.

        Parameters:
        :   - **conn** – The connection to get the number of EATT channels for.

        Returns:
        :   The number of EATT channels connected. Returns 0 if `conn` is NULL or not connected.
