---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/sdp.html
original_path: connectivity/bluetooth/api/sdp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Service Discovery Protocol (SDP)

## API Reference

*group* Service Discovery Protocol (SDP)
:   Service class identifiers of standard services and service groups

    BT\_SDP\_SDP\_SERVER\_SVCLASS
    :   Service Discovery Server.

    BT\_SDP\_BROWSE\_GRP\_DESC\_SVCLASS
    :   Browse Group Descriptor.

    BT\_SDP\_PUBLIC\_BROWSE\_GROUP
    :   Public Browse Group.

    BT\_SDP\_SERIAL\_PORT\_SVCLASS
    :   Serial Port.

    BT\_SDP\_LAN\_ACCESS\_SVCLASS
    :   LAN Access Using PPP.

    BT\_SDP\_DIALUP\_NET\_SVCLASS
    :   Dialup Networking.

    BT\_SDP\_IRMC\_SYNC\_SVCLASS
    :   IrMC Sync.

    BT\_SDP\_OBEX\_OBJPUSH\_SVCLASS
    :   OBEX Object Push.

    BT\_SDP\_OBEX\_FILETRANS\_SVCLASS
    :   OBEX File Transfer.

    BT\_SDP\_IRMC\_SYNC\_CMD\_SVCLASS
    :   IrMC Sync Command.

    BT\_SDP\_HEADSET\_SVCLASS
    :   Headset.

    BT\_SDP\_CORDLESS\_TELEPHONY\_SVCLASS
    :   Cordless Telephony.

    BT\_SDP\_AUDIO\_SOURCE\_SVCLASS
    :   Audio Source.

    BT\_SDP\_AUDIO\_SINK\_SVCLASS
    :   Audio Sink.

    BT\_SDP\_AV\_REMOTE\_TARGET\_SVCLASS
    :   A/V Remote Control Target.

    BT\_SDP\_ADVANCED\_AUDIO\_SVCLASS
    :   Advanced Audio Distribution.

    BT\_SDP\_AV\_REMOTE\_SVCLASS
    :   A/V Remote Control.

    BT\_SDP\_AV\_REMOTE\_CONTROLLER\_SVCLASS
    :   A/V Remote Control Controller.

    BT\_SDP\_INTERCOM\_SVCLASS
    :   Intercom.

    BT\_SDP\_FAX\_SVCLASS
    :   Fax.

    BT\_SDP\_HEADSET\_AGW\_SVCLASS
    :   Headset AG.

    BT\_SDP\_WAP\_SVCLASS
    :   WAP.

    BT\_SDP\_WAP\_CLIENT\_SVCLASS
    :   WAP Client.

    BT\_SDP\_PANU\_SVCLASS
    :   Personal Area Networking User.

    BT\_SDP\_NAP\_SVCLASS
    :   Network Access Point.

    BT\_SDP\_GN\_SVCLASS
    :   Group Network.

    BT\_SDP\_DIRECT\_PRINTING\_SVCLASS
    :   Direct Printing.

    BT\_SDP\_REFERENCE\_PRINTING\_SVCLASS
    :   Reference Printing.

    BT\_SDP\_IMAGING\_SVCLASS
    :   Basic Imaging Profile.

    BT\_SDP\_IMAGING\_RESPONDER\_SVCLASS
    :   Imaging Responder.

    BT\_SDP\_IMAGING\_ARCHIVE\_SVCLASS
    :   Imaging Automatic Archive.

    BT\_SDP\_IMAGING\_REFOBJS\_SVCLASS
    :   Imaging Referenced Objects.

    BT\_SDP\_HANDSFREE\_SVCLASS
    :   Handsfree.

    BT\_SDP\_HANDSFREE\_AGW\_SVCLASS
    :   Handsfree Audio Gateway.

    BT\_SDP\_DIRECT\_PRT\_REFOBJS\_SVCLASS
    :   Direct Printing Reference Objects Service.

    BT\_SDP\_REFLECTED\_UI\_SVCLASS
    :   Reflected UI.

    BT\_SDP\_BASIC\_PRINTING\_SVCLASS
    :   Basic Printing.

    BT\_SDP\_PRINTING\_STATUS\_SVCLASS
    :   Printing Status.

    BT\_SDP\_HID\_SVCLASS
    :   Human Interface Device Service.

    BT\_SDP\_HCR\_SVCLASS
    :   Hardcopy Cable Replacement.

    BT\_SDP\_HCR\_PRINT\_SVCLASS
    :   HCR Print.

    BT\_SDP\_HCR\_SCAN\_SVCLASS
    :   HCR Scan.

    BT\_SDP\_CIP\_SVCLASS
    :   Common ISDN Access.

    BT\_SDP\_VIDEO\_CONF\_GW\_SVCLASS
    :   Video Conferencing Gateway.

    BT\_SDP\_UDI\_MT\_SVCLASS
    :   UDI MT.

    BT\_SDP\_UDI\_TA\_SVCLASS
    :   UDI TA.

    BT\_SDP\_AV\_SVCLASS
    :   Audio/Video.

    BT\_SDP\_SAP\_SVCLASS
    :   SIM Access.

    BT\_SDP\_PBAP\_PCE\_SVCLASS
    :   Phonebook Access Client.

    BT\_SDP\_PBAP\_PSE\_SVCLASS
    :   Phonebook Access Server.

    BT\_SDP\_PBAP\_SVCLASS
    :   Phonebook Access.

    BT\_SDP\_MAP\_MSE\_SVCLASS
    :   Message Access Server.

    BT\_SDP\_MAP\_MCE\_SVCLASS
    :   Message Notification Server.

    BT\_SDP\_MAP\_SVCLASS
    :   Message Access Profile.

    BT\_SDP\_GNSS\_SVCLASS
    :   GNSS.

    BT\_SDP\_GNSS\_SERVER\_SVCLASS
    :   GNSS Server.

    BT\_SDP\_MPS\_SC\_SVCLASS
    :   MPS SC.

    BT\_SDP\_MPS\_SVCLASS
    :   MPS.

    BT\_SDP\_PNP\_INFO\_SVCLASS
    :   PnP Information.

    BT\_SDP\_GENERIC\_NETWORKING\_SVCLASS
    :   Generic Networking.

    BT\_SDP\_GENERIC\_FILETRANS\_SVCLASS
    :   Generic File Transfer.

    BT\_SDP\_GENERIC\_AUDIO\_SVCLASS
    :   Generic Audio.

    BT\_SDP\_GENERIC\_TELEPHONY\_SVCLASS
    :   Generic Telephony.

    BT\_SDP\_UPNP\_SVCLASS
    :   UPnP Service.

    BT\_SDP\_UPNP\_IP\_SVCLASS
    :   UPnP IP Service.

    BT\_SDP\_UPNP\_PAN\_SVCLASS
    :   UPnP IP PAN.

    BT\_SDP\_UPNP\_LAP\_SVCLASS
    :   UPnP IP LAP.

    BT\_SDP\_UPNP\_L2CAP\_SVCLASS
    :   UPnP IP L2CAP.

    BT\_SDP\_VIDEO\_SOURCE\_SVCLASS
    :   Video Source.

    BT\_SDP\_VIDEO\_SINK\_SVCLASS
    :   Video Sink.

    BT\_SDP\_VIDEO\_DISTRIBUTION\_SVCLASS
    :   Video Distribution.

    BT\_SDP\_HDP\_SVCLASS
    :   HDP.

    BT\_SDP\_HDP\_SOURCE\_SVCLASS
    :   HDP Source.

    BT\_SDP\_HDP\_SINK\_SVCLASS
    :   HDP Sink.

    BT\_SDP\_GENERIC\_ACCESS\_SVCLASS
    :   Generic Access Profile.

    BT\_SDP\_GENERIC\_ATTRIB\_SVCLASS
    :   Generic Attribute Profile.

    BT\_SDP\_APPLE\_AGENT\_SVCLASS
    :   Apple Agent.

    Attribute identifier codes

    Possible values for attribute-id are listed below.

    See SDP Spec, section “Service Attribute Definitions” for more details.

    BT\_SDP\_ATTR\_RECORD\_HANDLE
    :   Service Record Handle.

    BT\_SDP\_ATTR\_SVCLASS\_ID\_LIST
    :   Service Class ID List.

    BT\_SDP\_ATTR\_RECORD\_STATE
    :   Service Record State.

    BT\_SDP\_ATTR\_SERVICE\_ID
    :   Service ID.

    BT\_SDP\_ATTR\_PROTO\_DESC\_LIST
    :   Protocol Descriptor List.

    BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST
    :   Browse Group List.

    BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST
    :   Language Base Attribute ID List.

    BT\_SDP\_ATTR\_SVCINFO\_TTL
    :   Service Info Time to Live.

    BT\_SDP\_ATTR\_SERVICE\_AVAILABILITY
    :   Service Availability.

    BT\_SDP\_ATTR\_PROFILE\_DESC\_LIST
    :   Bluetooth Profile Descriptor List.

    BT\_SDP\_ATTR\_DOC\_URL
    :   Documentation URL.

    BT\_SDP\_ATTR\_CLNT\_EXEC\_URL
    :   Client Executable URL.

    BT\_SDP\_ATTR\_ICON\_URL
    :   Icon URL.

    BT\_SDP\_ATTR\_ADD\_PROTO\_DESC\_LIST
    :   Additional Protocol Descriptor List.

    BT\_SDP\_ATTR\_GROUP\_ID
    :   Group ID.

    BT\_SDP\_ATTR\_IP\_SUBNET
    :   IP Subnet.

    BT\_SDP\_ATTR\_VERSION\_NUM\_LIST
    :   Version Number List.

    BT\_SDP\_ATTR\_SUPPORTED\_FEATURES\_LIST
    :   Supported Features List.

    BT\_SDP\_ATTR\_GOEP\_L2CAP\_PSM
    :   GOEP L2CAP PSM.

    BT\_SDP\_ATTR\_SVCDB\_STATE
    :   Service Database State.

    BT\_SDP\_ATTR\_MPSD\_SCENARIOS
    :   MPSD Scenarios.

    BT\_SDP\_ATTR\_MPMD\_SCENARIOS
    :   MPMD Scenarios.

    BT\_SDP\_ATTR\_MPS\_DEPENDENCIES
    :   Supported Profiles & Protocols.

    BT\_SDP\_ATTR\_SERVICE\_VERSION
    :   Service Version.

    BT\_SDP\_ATTR\_EXTERNAL\_NETWORK
    :   External Network.

    BT\_SDP\_ATTR\_SUPPORTED\_DATA\_STORES\_LIST
    :   Supported Data Stores List.

    BT\_SDP\_ATTR\_DATA\_EXCHANGE\_SPEC
    :   Data Exchange Specification.

    BT\_SDP\_ATTR\_NETWORK
    :   Network.

    BT\_SDP\_ATTR\_FAX\_CLASS1\_SUPPORT
    :   Fax Class 1 Support.

    BT\_SDP\_ATTR\_REMOTE\_AUDIO\_VOLUME\_CONTROL
    :   Remote Audio Volume Control.

    BT\_SDP\_ATTR\_MCAP\_SUPPORTED\_PROCEDURES
    :   MCAP Supported Procedures.

    BT\_SDP\_ATTR\_FAX\_CLASS20\_SUPPORT
    :   Fax Class 2.0 Support.

    BT\_SDP\_ATTR\_SUPPORTED\_FORMATS\_LIST
    :   Supported Formats List.

    BT\_SDP\_ATTR\_FAX\_CLASS2\_SUPPORT
    :   Fax Class 2 Support (vendor-specific).

    BT\_SDP\_ATTR\_AUDIO\_FEEDBACK\_SUPPORT
    :   Audio Feedback Support.

    BT\_SDP\_ATTR\_NETWORK\_ADDRESS
    :   Network Address.

    BT\_SDP\_ATTR\_WAP\_GATEWAY
    :   WAP Gateway.

    BT\_SDP\_ATTR\_HOMEPAGE\_URL
    :   Homepage URL.

    BT\_SDP\_ATTR\_WAP\_STACK\_TYPE
    :   WAP Stack Type.

    BT\_SDP\_ATTR\_SECURITY\_DESC
    :   Security Description.

    BT\_SDP\_ATTR\_NET\_ACCESS\_TYPE
    :   Net Access Type.

    BT\_SDP\_ATTR\_MAX\_NET\_ACCESSRATE
    :   Max Net Access Rate.

    BT\_SDP\_ATTR\_IP4\_SUBNET
    :   IPv4 Subnet.

    BT\_SDP\_ATTR\_IP6\_SUBNET
    :   IPv6 Subnet.

    BT\_SDP\_ATTR\_SUPPORTED\_CAPABILITIES
    :   BIP Supported Capabilities.

    BT\_SDP\_ATTR\_SUPPORTED\_FEATURES
    :   BIP Supported Features.

    BT\_SDP\_ATTR\_SUPPORTED\_FUNCTIONS
    :   BIP Supported Functions.

    BT\_SDP\_ATTR\_TOTAL\_IMAGING\_DATA\_CAPACITY
    :   BIP Total Imaging Data Capacity.

    BT\_SDP\_ATTR\_SUPPORTED\_REPOSITORIES
    :   Supported Repositories.

    BT\_SDP\_ATTR\_MAS\_INSTANCE\_ID
    :   MAS Instance ID.

    BT\_SDP\_ATTR\_SUPPORTED\_MESSAGE\_TYPES
    :   Supported Message Types.

    BT\_SDP\_ATTR\_PBAP\_SUPPORTED\_FEATURES
    :   PBAP Supported Features.

    BT\_SDP\_ATTR\_MAP\_SUPPORTED\_FEATURES
    :   MAP Supported Features.

    BT\_SDP\_ATTR\_SPECIFICATION\_ID
    :   Specification ID.

    BT\_SDP\_ATTR\_VENDOR\_ID
    :   Vendor ID.

    BT\_SDP\_ATTR\_PRODUCT\_ID
    :   Product ID.

    BT\_SDP\_ATTR\_VERSION
    :   Version.

    BT\_SDP\_ATTR\_PRIMARY\_RECORD
    :   Primary Record.

    BT\_SDP\_ATTR\_VENDOR\_ID\_SOURCE
    :   Vendor ID Source.

    BT\_SDP\_ATTR\_HID\_DEVICE\_RELEASE\_NUMBER
    :   HID Device Release Number.

    BT\_SDP\_ATTR\_HID\_PARSER\_VERSION
    :   HID Parser Version.

    BT\_SDP\_ATTR\_HID\_DEVICE\_SUBCLASS
    :   HID Device Subclass.

    BT\_SDP\_ATTR\_HID\_COUNTRY\_CODE
    :   HID Country Code.

    BT\_SDP\_ATTR\_HID\_VIRTUAL\_CABLE
    :   HID Virtual Cable.

    BT\_SDP\_ATTR\_HID\_RECONNECT\_INITIATE
    :   HID Reconnect Initiate.

    BT\_SDP\_ATTR\_HID\_DESCRIPTOR\_LIST
    :   HID Descriptor List.

    BT\_SDP\_ATTR\_HID\_LANG\_ID\_BASE\_LIST
    :   HID Language ID Base List.

    BT\_SDP\_ATTR\_HID\_SDP\_DISABLE
    :   HID SDP Disable.

    BT\_SDP\_ATTR\_HID\_BATTERY\_POWER
    :   HID Battery Power.

    BT\_SDP\_ATTR\_HID\_REMOTE\_WAKEUP
    :   HID Remote Wakeup.

    BT\_SDP\_ATTR\_HID\_PROFILE\_VERSION
    :   HID Profile Version.

    BT\_SDP\_ATTR\_HID\_SUPERVISION\_TIMEOUT
    :   HID Supervision Timeout.

    BT\_SDP\_ATTR\_HID\_NORMALLY\_CONNECTABLE
    :   HID Normally Connectable.

    BT\_SDP\_ATTR\_HID\_BOOT\_DEVICE
    :   HID Boot Device.

    The Data representation in SDP PDUs (pps 339, 340 of BT SDP Spec)

    These are the exact data type+size descriptor values that go into the PDU buffer.

    The datatype (leading 5bits) + size descriptor (last 3 bits) is 8 bits. The size descriptor is critical to extract the right number of bytes for the data value from the PDU.

    For most basic types, the datatype+size descriptor is straightforward. However for constructed types and strings, the size of the data is in the next “n” bytes following the 8 bits (datatype+size) descriptor. Exactly what the “n” is specified in the 3 bits of the data size descriptor.

    TextString and URLString can be of size 2^{8, 16, 32} bytes DataSequence and DataSequenceAlternates can be of size 2^{8, 16, 32} The size are computed post-facto in the API and are not known apriori.

    BT\_SDP\_DATA\_NIL
    :   Nil, the null type.

    BT\_SDP\_UINT8
    :   Unsigned 8-bit integer.

    BT\_SDP\_UINT16
    :   Unsigned 16-bit integer.

    BT\_SDP\_UINT32
    :   Unsigned 32-bit integer.

    BT\_SDP\_UINT64
    :   Unsigned 64-bit integer.

    BT\_SDP\_UINT128
    :   Unsigned 128-bit integer.

    BT\_SDP\_INT8
    :   Signed 8-bit integer.

    BT\_SDP\_INT16
    :   Signed 16-bit integer.

    BT\_SDP\_INT32
    :   Signed 32-bit integer.

    BT\_SDP\_INT64
    :   Signed 64-bit integer.

    BT\_SDP\_INT128
    :   Signed 128-bit integer.

    BT\_SDP\_UUID\_UNSPEC
    :   UUID, unspecified size.

    BT\_SDP\_UUID16
    :   UUID, 16-bit.

    BT\_SDP\_UUID32
    :   UUID, 32-bit.

    BT\_SDP\_UUID128
    :   UUID, 128-bit.

    BT\_SDP\_TEXT\_STR\_UNSPEC
    :   Text string, unspecified size.

    BT\_SDP\_TEXT\_STR8
    :   Text string, 8-bit length.

    BT\_SDP\_TEXT\_STR16
    :   Text string, 16-bit length.

    BT\_SDP\_TEXT\_STR32
    :   Text string, 32-bit length.

    BT\_SDP\_BOOL
    :   Boolean.

    BT\_SDP\_SEQ\_UNSPEC
    :   Data element sequence, unspecified size.

    BT\_SDP\_SEQ8
    :   Data element sequence, 8-bit length.

    BT\_SDP\_SEQ16
    :   Data element sequence, 16-bit length.

    BT\_SDP\_SEQ32
    :   Data element sequence, 32-bit length.

    BT\_SDP\_ALT\_UNSPEC
    :   Data element alternative, unspecified size.

    BT\_SDP\_ALT8
    :   Data element alternative, 8-bit length.

    BT\_SDP\_ALT16
    :   Data element alternative, 16-bit length.

    BT\_SDP\_ALT32
    :   Data element alternative, 32-bit length.

    BT\_SDP\_URL\_STR\_UNSPEC
    :   URL string, unspecified size.

    BT\_SDP\_URL\_STR8
    :   URL string, 8-bit length.

    BT\_SDP\_URL\_STR16
    :   URL string, 16-bit length.

    BT\_SDP\_URL\_STR32
    :   URL string, 32-bit length.

    Defines

    BT\_SDP\_SERVER\_RECORD\_HANDLE

    BT\_SDP\_PRIMARY\_LANG\_BASE

    BT\_SDP\_ATTR\_SVCNAME\_PRIMARY

    BT\_SDP\_ATTR\_SVCDESC\_PRIMARY

    BT\_SDP\_ATTR\_PROVNAME\_PRIMARY

    BT\_SDP\_TYPE\_DESC\_MASK

    BT\_SDP\_SIZE\_DESC\_MASK

    BT\_SDP\_SIZE\_INDEX\_OFFSET

    BT\_SDP\_ARRAY\_8(...)
    :   Declare an array of 8-bit elements in an attribute.

    BT\_SDP\_ARRAY\_16(...)
    :   Declare an array of 16-bit elements in an attribute.

    BT\_SDP\_ARRAY\_32(...)
    :   Declare an array of 32-bit elements in an attribute.

    BT\_SDP\_TYPE\_SIZE(\_type)
    :   Declare a fixed-size data element header.

        Parameters:
        :   - **\_type** – Data element header containing type and size descriptors.

    BT\_SDP\_TYPE\_SIZE\_VAR(\_type, \_size)
    :   Declare a variable-size data element header.

        Parameters:
        :   - **\_type** – Data element header containing type and size descriptors.
            - **\_size** – The actual size of the data.

    BT\_SDP\_DATA\_ELEM\_LIST(...)
    :   Declare a list of data elements.

    BT\_SDP\_NEW\_SERVICE
    :   SDP New Service Record Declaration Macro.

        Helper macro to declare a new service record. Default attributes: Record Handle, Record State, Language Base, Root Browse Group

    BT\_SDP\_LIST(\_att\_id, \_type\_size, \_data\_elem\_seq)
    :   Generic SDP List Attribute Declaration Macro.

        Helper macro to declare a list attribute.

        Parameters:
        :   - **\_att\_id** – List Attribute ID.
            - **\_data\_elem\_seq** – Data element sequence for the list.
            - **\_type\_size** – SDP type and size descriptor.

    BT\_SDP\_SERVICE\_ID(\_uuid)
    :   SDP Service ID Attribute Declaration Macro.

        Helper macro to declare a service ID attribute.

        Parameters:
        :   - **\_uuid** – Service ID 16bit UUID.

    BT\_SDP\_SERVICE\_NAME(\_name)
    :   SDP Name Attribute Declaration Macro.

        Helper macro to declare a service name attribute.

        Parameters:
        :   - **\_name** – Service name as a string (up to 256 chars).

    BT\_SDP\_SUPPORTED\_FEATURES(\_features)
    :   SDP Supported Features Attribute Declaration Macro.

        Helper macro to declare supported features of a profile/protocol.

        Parameters:
        :   - **\_features** – Feature mask as 16bit unsigned integer.

    BT\_SDP\_RECORD(\_attrs)
    :   SDP Service Declaration Macro.

        Helper macro to declare a service.

        Parameters:
        :   - **\_attrs** – List of attributes for the service record.

    Typedefs

    typedef uint8\_t (\*bt\_sdp\_discover\_func\_t)(struct bt\_conn \*conn, struct [bt\_sdp\_client\_result](#c.bt_sdp_client_result) \*result)
    :   Callback type reporting to user that there is a resolved result on remote for given UUID and the result record buffer can be used by user for further inspection.

        A function of this type is given by the user to the [bt\_sdp\_discover\_params](#structbt__sdp__discover__params) object. It’ll be called on each valid record discovery completion for given UUID. When UUID resolution gives back no records then NULL is passed to the user. Otherwise user can get valid record(s) and then the internal hint ‘next record’ is set to false saying the UUID resolution is complete or the hint can be set by caller to true meaning that next record is available for given UUID. The returned function value allows the user to control retrieving follow-up resolved records if any. If the user doesn’t want to read more resolved records for given UUID since current record data fulfills its requirements then should return BT\_SDP\_DISCOVER\_UUID\_STOP. Otherwise returned value means more subcall iterations are allowable.

        Param conn:
        :   Connection object identifying connection to queried remote.

        Param result:
        :   Object pointing to logical unparsed SDP record collected on base of response driven by given UUID.

        Return:
        :   BT\_SDP\_DISCOVER\_UUID\_STOP in case of no more need to read next record data and continue discovery for given UUID. By returning BT\_SDP\_DISCOVER\_UUID\_CONTINUE user allows this discovery continuation.

    Enums

    enum [anonymous]
    :   Helper enum to be used as return value of [bt\_sdp\_discover\_func\_t](#group__bt__sdp_1gae5fa4166e3b909f9dcaace11b302f98f).

        The value informs the caller to perform further pending actions or stop them.

        *Values:*

        enumerator BT\_SDP\_DISCOVER\_UUID\_STOP = 0

        enumerator BT\_SDP\_DISCOVER\_UUID\_CONTINUE

    enum bt\_sdp\_proto
    :   Protocols to be asked about specific parameters.

        *Values:*

        enumerator BT\_SDP\_PROTO\_RFCOMM = 0x0003

        enumerator BT\_SDP\_PROTO\_L2CAP = 0x0100

    Functions

    int bt\_sdp\_register\_service(struct [bt\_sdp\_record](#c.bt_sdp_record) \*service)
    :   Register a Service Record.

        Register a Service Record. Applications can make use of macros such as BT\_SDP\_DECLARE\_SERVICE, BT\_SDP\_LIST, BT\_SDP\_SERVICE\_ID, BT\_SDP\_SERVICE\_NAME, etc. A service declaration must start with BT\_SDP\_NEW\_SERVICE.

        Parameters:
        :   - **service** – Service record declared using BT\_SDP\_DECLARE\_SERVICE.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_sdp\_discover(struct bt\_conn \*conn, const struct [bt\_sdp\_discover\_params](#c.bt_sdp_discover_params) \*params)
    :   Allows user to start SDP discovery session.

        The function performs SDP service discovery on remote server driven by user delivered discovery parameters. Discovery session is made as soon as no SDP transaction is ongoing between peers and if any then this one is queued to be processed at discovery completion of previous one. On the service discovery completion the callback function will be called to get feedback to user about findings.

        Parameters:
        :   - **conn** – Object identifying connection to remote.
            - **params** – SDP discovery parameters.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_sdp\_discover\_cancel(struct bt\_conn \*conn, const struct [bt\_sdp\_discover\_params](#c.bt_sdp_discover_params) \*params)
    :   Release waiting SDP discovery request.

        It can cancel valid waiting SDP client request identified by SDP discovery parameters object.

        Parameters:
        :   - **conn** – Object identifying connection to remote.
            - **params** – SDP discovery parameters.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_sdp\_get\_proto\_param(const struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, enum [bt\_sdp\_proto](#c.bt_sdp_proto) proto, uint16\_t \*param)
    :   Give to user parameter value related to given stacked protocol UUID.

        API extracts specific parameter associated with given protocol UUID available in Protocol Descriptor List attribute.

        Parameters:
        :   - **buf** – Original buffered raw record data.
            - **proto** – Known protocol to be checked like RFCOMM or L2CAP.
            - **param** – On success populated by found parameter value.

        Returns:
        :   0 on success when specific parameter associated with given protocol value is found, or negative if error occurred during processing.

    int bt\_sdp\_get\_addl\_proto\_param(const struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, enum [bt\_sdp\_proto](#c.bt_sdp_proto) proto, uint8\_t param\_index, uint16\_t \*param)
    :   Get additional parameter value related to given stacked protocol UUID.

        API extracts specific parameter associated with given protocol UUID available in Additional Protocol Descriptor List attribute.

        Parameters:
        :   - **buf** – Original buffered raw record data.
            - **proto** – Known protocol to be checked like RFCOMM or L2CAP.
            - **param\_index** – There may be more than one parameter related to the given protocol UUID. This function returns the result that is indexed by this parameter. It’s value is from 0, 0 means the first matched result, 1 means the second matched result.
            - **param** – **[out]** On success populated by found parameter value.

        Returns:
        :   0 on success when a specific parameter associated with a given protocol value is found, or negative if error occurred during processing.

    int bt\_sdp\_get\_profile\_version(const struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, uint16\_t profile, uint16\_t \*version)
    :   Get profile version.

        Helper API extracting remote profile version number. To get it proper generic profile parameter needs to be selected usually listed in SDP Interoperability Requirements section for given profile specification.

        Parameters:
        :   - **buf** – Original buffered raw record data.
            - **profile** – Profile family identifier the profile belongs.
            - **version** – On success populated by found version number.

        Returns:
        :   0 on success, negative value if error occurred during processing.

    int bt\_sdp\_get\_features(const struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, uint16\_t \*features)
    :   Get SupportedFeatures attribute value.

        Allows if exposed by remote retrieve SupportedFeature attribute.

        Parameters:
        :   - **buf** – Buffer holding original raw record data from remote.
            - **features** – On success object to be populated with SupportedFeature mask.

        Returns:
        :   0 on success if feature found and valid, negative in case any error

    struct bt\_sdp\_data\_elem
    :   *#include <sdp.h>*

        SDP Generic Data Element Value.

        Public Members

        uint8\_t type
        :   Type of the data element.

        uint32\_t data\_size
        :   Size of the data element.

        uint32\_t total\_size
        :   Total size of the data element.

    struct bt\_sdp\_attribute
    :   *#include <sdp.h>*

        SDP Attribute Value.

        Public Members

        uint16\_t id
        :   Attribute ID.

        struct [bt\_sdp\_data\_elem](#c.bt_sdp_data_elem) val
        :   Attribute data.

    struct bt\_sdp\_record
    :   *#include <sdp.h>*

        SDP Service Record Value.

        Public Members

        uint32\_t handle
        :   Redundant, for quick ref.

        struct [bt\_sdp\_attribute](#c.bt_sdp_attribute) \*attrs
        :   Base addr of attr array.

        size\_t attr\_count
        :   Number of attributes.

        uint8\_t index
        :   Index of the record in LL.

        struct [bt\_sdp\_record](#c.bt_sdp_record) \*next
        :   Next service record.

    struct bt\_sdp\_client\_result
    :   *#include <sdp.h>*

        Generic SDP Client Query Result data holder.

        Public Members

        struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*resp\_buf
        :   buffer containing unparsed SDP record result for given UUID

        bool next\_record\_hint
        :   flag pointing that there are more result chunks for given UUID

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   Reference to UUID object on behalf one discovery was started.

    struct bt\_sdp\_discover\_params
    :   *#include <sdp.h>*

        Main user structure used in SDP discovery of remote.

        Public Members

        const struct [bt\_uuid](uuid.md#c.bt_uuid "bt_uuid") \*uuid
        :   UUID (service) to be discovered on remote SDP entity.

        [bt\_sdp\_discover\_func\_t](#c.bt_sdp_discover_func_t) func
        :   Discover callback to be called on resolved SDP record.

        struct [net\_buf\_pool](../../networking/api/net_buf.md#c.net_buf_pool "net_buf_pool") \*pool
        :   Memory buffer enabled by user for SDP query results.
