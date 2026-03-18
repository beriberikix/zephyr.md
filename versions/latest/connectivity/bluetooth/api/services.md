---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/services.html
original_path: connectivity/bluetooth/api/services.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth standard services

## Battery Service

*group* bt\_bas
:   Battery Service (BAS).

    [Experimental] Users should note that the APIs can change as a part of ongoing development.

    Functions

    uint8\_t bt\_bas\_get\_battery\_level(void)
    :   Read battery level value.

        Read the characteristic value of the battery level

        Returns:
        :   The battery level in percent.

    int bt\_bas\_set\_battery\_level(uint8\_t level)
    :   Update battery level value.

        Update the characteristic value of the battery level This will send a GATT notification to all current subscribers.

        Parameters:
        :   - **level** – The battery level in percent.

        Returns:
        :   Zero in case of success and error code in case of error.

## Heart Rate Service

*group* bt\_hrs
:   Heart Rate Service (HRS).

    [Experimental] Users should note that the APIs can change as a part of ongoing development.

    Functions

    int bt\_hrs\_cb\_register(struct [bt\_hrs\_cb](#c.bt_hrs_cb) \*cb)
    :   Heart rate service callback register.

        This function will register callbacks that will be called in certain events related to Heart rate service.

        Parameters:
        :   - **cb** – Pointer to callbacks structure. Must point to memory that remains valid until unregistered.

        Returns:
        :   0 on success

        Returns:
        :   -EINVAL in case `cb` is NULL

    int bt\_hrs\_cb\_unregister(struct [bt\_hrs\_cb](#c.bt_hrs_cb) \*cb)
    :   Heart rate service callback unregister.

        This function will unregister callback from Heart rate service.

        Parameters:
        :   - **cb** – Pointer to callbacks structure

        Returns:
        :   0 on success

        Returns:
        :   -EINVAL in case `cb` is NULL

        Returns:
        :   -ENOENT in case the `cb` was not found in registered callbacks

    int bt\_hrs\_notify(uint16\_t heartrate)
    :   Notify heart rate measurement.

        This will send a GATT notification to all current subscribers.

        Parameters:
        :   - **heartrate** – The heartrate measurement in beats per minute.

        Returns:
        :   Zero in case of success and error code in case of error.

    struct bt\_hrs\_cb
    :   *#include <hrs.h>*

        Heart rate service callback structure.

        Public Members

        void (\*ntf\_changed)(bool enabled)
        :   Heart rate notifications changed.

            Param enabled:
            :   Flag that is true if notifications were enabled, false if they were disabled.

## Immediate Alert Service

*group* bt\_ias
:   Immediate Alert Service (IAS).

    [Experimental] Users should note that the APIs can change as a part of ongoing development.

    Defines

    BT\_IAS\_CB\_DEFINE(\_name)
    :   Register a callback structure for immediate alert events.

        Parameters:
        :   - **\_name** – Name of callback structure.

    Enums

    enum bt\_ias\_alert\_lvl
    :   *Values:*

        enumerator BT\_IAS\_ALERT\_LVL\_NO\_ALERT
        :   No alerting should be done on device.

        enumerator BT\_IAS\_ALERT\_LVL\_MILD\_ALERT
        :   Device shall alert.

        enumerator BT\_IAS\_ALERT\_LVL\_HIGH\_ALERT
        :   Device should alert in strongest possible way.

    Functions

    int bt\_ias\_local\_alert\_stop(void)
    :   Method for stopping alert locally.

        Returns:
        :   Zero in case of success and error code in case of error.

    int bt\_ias\_client\_alert\_write(struct bt\_conn \*conn, enum [bt\_ias\_alert\_lvl](#c.bt_ias_alert_lvl))
    :   Set alert level.

        Parameters:
        :   - **conn** – Bluetooth connection object
            - **bt\_ias\_alert\_lvl** – Level of alert to write

        Returns:
        :   Zero in case of success and error code in case of error.

    int bt\_ias\_discover(struct bt\_conn \*conn)
    :   Discover Immediate Alert Service.

        Parameters:
        :   - **conn** – Bluetooth connection object

        Returns:
        :   Zero in case of success and error code in case of error.

    int bt\_ias\_client\_cb\_register(const struct [bt\_ias\_client\_cb](#c.bt_ias_client_cb) \*cb)
    :   Register Immediate Alert Client callbacks.

        Parameters:
        :   - **cb** – The callback structure

        Returns:
        :   Zero in case of success and error code in case of error.

    struct bt\_ias\_cb
    :   *#include <ias.h>*

        Immediate Alert Service callback structure.

        Public Members

        void (\*no\_alert)(void)
        :   Callback function to stop alert.

            This callback is called when peer commands to disable alert.

        void (\*mild\_alert)(void)
        :   Callback function for alert level value.

            This callback is called when peer commands to alert.

        void (\*high\_alert)(void)
        :   Callback function for alert level value.

            This callback is called when peer commands to alert in the strongest possible way.

    struct bt\_ias\_client\_cb
    :   *#include <ias.h>*

        Public Members

        void (\*discover)(struct bt\_conn \*conn, int err)
        :   Callback function for bt\_ias\_discover.

            This callback is called when discovery procedure is complete.

            Param conn:
            :   Bluetooth connection object.

            Param err:
            :   0 on success, ATT error or negative errno otherwise

## Object Transfer Service

*group* bt\_ots
:   Object Transfer Service (OTS).

    [Experimental] Users should note that the APIs can change as a part of ongoing development.

    Defines

    BT\_OTS\_OBJ\_ID\_SIZE
    :   Size of OTS object ID (in bytes).

    BT\_OTS\_OBJ\_ID\_MIN
    :   Minimum allowed value for object ID (except ID for directory listing).

    BT\_OTS\_OBJ\_ID\_MAX
    :   Maximum allowed value for object ID (except ID for directory listing).

    OTS\_OBJ\_ID\_DIR\_LIST
    :   ID of the Directory Listing Object.

    BT\_OTS\_OBJ\_ID\_MASK
    :   Mask for OTS object IDs, preserving the 48 bits.

    BT\_OTS\_OBJ\_ID\_STR\_LEN
    :   Length of OTS object ID string (in bytes).

    BT\_OTS\_OBJ\_SET\_PROP\_DELETE(prop)
    :   Set [BT\_OTS\_OBJ\_PROP\_DELETE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_SET\_PROP\_EXECUTE(prop)
    :   Set [BT\_OTS\_OBJ\_PROP\_EXECUTE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_SET\_PROP\_READ(prop)
    :   Set [BT\_OTS\_OBJ\_PROP\_READ](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_SET\_PROP\_WRITE(prop)
    :   Set [BT\_OTS\_OBJ\_PROP\_WRITE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_SET\_PROP\_APPEND(prop)
    :   Set [BT\_OTS\_OBJ\_PROP\_APPEND](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_SET\_PROP\_TRUNCATE(prop)
    :   Set [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_SET\_PROP\_PATCH(prop)
    :   Set [BT\_OTS\_OBJ\_PROP\_PATCH](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_SET\_PROP\_MARKED(prop)
    :   Set [BT\_OTS\_OBJ\_SET\_PROP\_MARKED](#group__bt__ots_1gae21e599a85549d5cd4462c0f36c291ac) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_DELETE(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_DELETE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_EXECUTE(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_EXECUTE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_READ(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_READ](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_WRITE(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_WRITE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_APPEND(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_APPEND](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_TRUNCATE(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_PATCH(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_PATCH](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OBJ\_GET\_PROP\_MARKED(prop)
    :   Get [BT\_OTS\_OBJ\_PROP\_MARKED](#group__bt__ots_1ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3) property.

        Parameters:
        :   - **prop** – Object properties.

    BT\_OTS\_OACP\_SET\_FEAT\_CREATE(feat)
    :   Set [BT\_OTS\_OACP\_SET\_FEAT\_CREATE](#group__bt__ots_1ga8cc851f268de24fe3445a9a0c3af6abf) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_DELETE(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_DELETE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_CHECKSUM(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_EXECUTE(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_EXECUTE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_READ(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_READ](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_WRITE(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_WRITE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_APPEND(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_APPEND](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_TRUNCATE(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_PATCH(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_PATCH](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_SET\_FEAT\_ABORT(feat)
    :   Set [BT\_OTS\_OACP\_FEAT\_ABORT](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_CREATE(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_CREATE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_DELETE(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_DELETE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_CHECKSUM(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_EXECUTE(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_EXECUTE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_READ(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_READ](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_WRITE(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_WRITE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_APPEND(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_APPEND](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_TRUNCATE(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_PATCH(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_PATCH](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OACP\_GET\_FEAT\_ABORT(feat)
    :   Get [BT\_OTS\_OACP\_FEAT\_ABORT](#group__bt__ots_1gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_SET\_FEAT\_GO\_TO(feat)
    :   Set [BT\_OTS\_OLCP\_FEAT\_GO\_TO](#group__bt__ots_1gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_SET\_FEAT\_ORDER(feat)
    :   Set [BT\_OTS\_OLCP\_FEAT\_ORDER](#group__bt__ots_1gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_SET\_FEAT\_NUM\_REQ(feat)
    :   Set [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](#group__bt__ots_1gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_SET\_FEAT\_CLEAR(feat)
    :   Set [BT\_OTS\_OLCP\_FEAT\_CLEAR](#group__bt__ots_1gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO(feat)
    :   Get [BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO](#group__bt__ots_1ga7ec49843849613ee3f8f72209cae68c2) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_GET\_FEAT\_ORDER(feat)
    :   Get [BT\_OTS\_OLCP\_GET\_FEAT\_ORDER](#group__bt__ots_1gad4393e56c94c2484cd344b48cb54b255) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ(feat)
    :   Get [BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ](#group__bt__ots_1ga2a1a62e410586b1117fd3571e42363d8) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR(feat)
    :   Get [BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR](#group__bt__ots_1ga0f57d172615d1c6ea857506dc0c10e55) feature.

        Parameters:
        :   - **feat** – OTS features.

    BT\_OTS\_DATE\_TIME\_FIELD\_SIZE

    BT\_OTS\_STOP

    BT\_OTS\_CONTINUE

    Typedefs

    typedef int (\*bt\_ots\_client\_dirlisting\_cb)(struct [bt\_ots\_obj\_metadata](#c.bt_ots_obj_metadata) \*meta)
    :   Directory listing object metadata callback.

        If a directory listing is decoded using [bt\_ots\_client\_decode\_dirlisting()](#group__bt__ots_1gabe485816a2e536758a7ce85c593ea486), this callback will be called for each object in the directory listing.

        Param meta:
        :   The metadata of the decoded object

        Return:
        :   int BT\_OTS\_STOP or BT\_OTS\_CONTINUE. BT\_OTS\_STOP can be used to stop the decoding.

    Enums

    enum [anonymous]
    :   Properties of an OTS object.

        *Values:*

        enumerator BT\_OTS\_OBJ\_PROP\_DELETE = 0
        :   Bit 0 Deletion of this object is permitted.

        enumerator BT\_OTS\_OBJ\_PROP\_EXECUTE = 1
        :   Bit 1 Execution of this object is permitted.

        enumerator BT\_OTS\_OBJ\_PROP\_READ = 2
        :   Bit 2 Reading this object is permitted.

        enumerator BT\_OTS\_OBJ\_PROP\_WRITE = 3
        :   Bit 3 Writing data to this object is permitted.

        enumerator BT\_OTS\_OBJ\_PROP\_APPEND = 4
        :   Bit 4 Appending data to this object is permitted.

            Appending data increases its Allocated Size.

        enumerator BT\_OTS\_OBJ\_PROP\_TRUNCATE = 5
        :   Bit 5 Truncation of this object is permitted.

        enumerator BT\_OTS\_OBJ\_PROP\_PATCH = 6
        :   Bit 6 Patching this object is permitted.

            Patching this object overwrites some of the object’s existing contents.

        enumerator BT\_OTS\_OBJ\_PROP\_MARKED = 7
        :   Bit 7 This object is a marked object.

    enum [anonymous]
    :   Object Action Control Point Feature bits.

        *Values:*

        enumerator BT\_OTS\_OACP\_FEAT\_CREATE = 0
        :   Bit 0 OACP Create Op Code Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_DELETE = 1
        :   Bit 1 OACP Delete Op Code Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_CHECKSUM = 2
        :   Bit 2 OACP Calculate Checksum Op Code Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_EXECUTE = 3
        :   Bit 3 OACP Execute Op Code Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_READ = 4
        :   Bit 4 OACP Read Op Code Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_WRITE = 5
        :   Bit 5 OACP Write Op Code Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_APPEND = 6
        :   Bit 6 Appending Additional Data to Objects Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_TRUNCATE = 7
        :   Bit 7 Truncation of Objects Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_PATCH = 8
        :   Bit 8 Patching of Objects Supported.

        enumerator BT\_OTS\_OACP\_FEAT\_ABORT = 9
        :   Bit 9 OACP Abort Op Code Supported.

    enum bt\_ots\_oacp\_write\_op\_mode
    :   *Values:*

        enumerator BT\_OTS\_OACP\_WRITE\_OP\_MODE\_NONE = 0

        enumerator BT\_OTS\_OACP\_WRITE\_OP\_MODE\_TRUNCATE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)

    enum [anonymous]
    :   Object List Control Point Feature bits.

        *Values:*

        enumerator BT\_OTS\_OLCP\_FEAT\_GO\_TO = 0
        :   Bit 0 OLCP Go To Op Code Supported.

        enumerator BT\_OTS\_OLCP\_FEAT\_ORDER = 1
        :   Bit 1 OLCP Order Op Code Supported.

        enumerator BT\_OTS\_OLCP\_FEAT\_NUM\_REQ = 2
        :   Bit 2 OLCP Request Number of Objects Op Code Supported.

        enumerator BT\_OTS\_OLCP\_FEAT\_CLEAR = 3
        :   Bit 3 OLCP Clear Marking Op Code Supported.

    enum [anonymous]
    :   Object metadata request bit field values.

        *Values:*

        enumerator BT\_OTS\_METADATA\_REQ\_NAME = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Request object name.

        enumerator BT\_OTS\_METADATA\_REQ\_TYPE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Request object type.

        enumerator BT\_OTS\_METADATA\_REQ\_SIZE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Request object size.

        enumerator BT\_OTS\_METADATA\_REQ\_CREATED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Request object first created time.

        enumerator BT\_OTS\_METADATA\_REQ\_MODIFIED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Request object last modified time.

        enumerator BT\_OTS\_METADATA\_REQ\_ID = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Request object ID.

        enumerator BT\_OTS\_METADATA\_REQ\_PROPS = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)
        :   Request object properties.

        enumerator BT\_OTS\_METADATA\_REQ\_ALL = 0x7F
        :   Request all object metadata.

    Functions

    int bt\_ots\_obj\_add(struct bt\_ots \*ots, const struct [bt\_ots\_obj\_add\_param](#c.bt_ots_obj_add_param) \*param)
    :   Add an object to the OTS instance.

        This function adds an object to the OTS database. When the object is being added, a callback obj\_created() is called to notify the user about a new object ID.

        Parameters:
        :   - **ots** – OTS instance.
            - **param** – Object addition parameters.

        Returns:
        :   ID of created object in case of success.

        Returns:
        :   negative value in case of error.

    int bt\_ots\_obj\_delete(struct bt\_ots \*ots, uint64\_t id)
    :   Delete an object from the OTS instance.

        This function deletes an object from the OTS database. When the object is deleted a callback obj\_deleted() is called to notify the user about this event. At this point, it is possible to free allocated buffer for object data.

        Parameters:
        :   - **ots** – OTS instance.
            - **id** – ID of the object to be deleted (uint48).

        Returns:
        :   0 in case of success or negative value in case of error.

    void \*bt\_ots\_svc\_decl\_get(struct bt\_ots \*ots)
    :   Get the service declaration attribute.

        This function is enabled for CONFIG\_BT\_OTS\_SECONDARY\_SVC configuration. The first service attribute can be included in any other GATT service.

        Parameters:
        :   - **ots** – OTS instance.

        Returns:
        :   The first OTS attribute instance.

    int bt\_ots\_init(struct bt\_ots \*ots, struct [bt\_ots\_init\_param](#c.bt_ots_init_param) \*ots\_init)
    :   Initialize the OTS instance.

        Parameters:
        :   - **ots** – OTS instance.
            - **ots\_init** – OTS initialization descriptor.

        Returns:
        :   0 in case of success or negative value in case of error.

    struct bt\_ots \*bt\_ots\_free\_instance\_get(void)
    :   Get a free instance of OTS from the pool.

        Returns:
        :   OTS instance in case of success or NULL in case of error.

    int bt\_ots\_client\_register(struct [bt\_ots\_client](#c.bt_ots_client) \*ots\_inst)
    :   Register an Object Transfer Service Instance.

        Register an Object Transfer Service instance discovered on the peer. Call this function when an OTS instance is discovered (discovery is to be handled by the higher layer).

        Parameters:
        :   - **ots\_inst** – **[in]** Discovered OTS instance.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_unregister(uint8\_t index)
    :   Unregister an Object Transfer Service Instance.

        Unregister an Object Transfer Service instance when disconnect from the peer. Call this function when an ACL using OTS instance is disconnected.

        Parameters:
        :   - **index** – **[in]** Index of OTS instance.

        Returns:
        :   int 0 if success, ERRNO on failure.

    uint8\_t bt\_ots\_client\_indicate\_handler(struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](gatt.md#c.bt_gatt_subscribe_params "bt_gatt_subscribe_params") \*params, const void \*data, uint16\_t length)
    :   OTS Indicate Handler function.

        Set this function as callback for indicate handler when discovering OTS.

        Parameters:
        :   - **conn** – Connection object. May be NULL, indicating that the peer is being unpaired.
            - **params** – Subscription parameters.
            - **data** – Attribute value data. If NULL then subscription was removed.
            - **length** – Attribute value length.

    int bt\_ots\_client\_read\_feature(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn)
    :   Read the OTS feature characteristic.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_select\_id(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn, uint64\_t obj\_id)
    :   Select an object by its Object ID.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.
            - **obj\_id** – Object’s ID.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_select\_first(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn)
    :   Select the first object.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_select\_last(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn)
    :   Select the last object.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_select\_next(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn)
    :   Select the next object.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_select\_prev(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn)
    :   Select the previous object.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_read\_object\_metadata(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn, uint8\_t metadata)
    :   Read the metadata of the current object.

        The metadata are returned in the obj\_metadata\_read() callback.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.
            - **metadata** – Bitfield (`BT_OTS_METADATA_REQ_*`) of the metadata to read.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_read\_object\_data(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn)
    :   Read the data of the current selected object.

        This will trigger an OACP read operation for the current size of the object with a 0 offset and then expect receiving the content via the L2CAP CoC.

        The data of the object are returned in the obj\_data\_read() callback.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_write\_object\_data(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn, const void \*buf, size\_t len, off\_t offset, enum [bt\_ots\_oacp\_write\_op\_mode](#c.bt_ots_oacp_write_op_mode) mode)
    :   Write the data of the current selected object.

        This will trigger an OACP write operation for the current object with a specified offset and then expect transferring the content via the L2CAP CoC.

        The length of the data written to object is returned in the obj\_data\_written() callback.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.
            - **buf** – Pointer to the data buffer to be written.
            - **len** – Size of data.
            - **offset** – Offset to write, usually 0.
            - **mode** – Mode Parameter for OACP Write Op Code. See [bt\_ots\_oacp\_write\_op\_mode](#group__bt__ots_1gaebdd2b8a80948d1050d42fa3963cc863).

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_get\_object\_checksum(struct [bt\_ots\_client](#c.bt_ots_client) \*otc\_inst, struct bt\_conn \*conn, off\_t offset, size\_t len)
    :   Get the checksum of the current selected object.

        This will trigger an OACP calculate checksum operation for the current object with a specified offset and length.

        The checksum goes to OACP IND and obj\_checksum\_calculated() callback.

        Parameters:
        :   - **otc\_inst** – Pointer to the OTC instance.
            - **conn** – Pointer to the connection object.
            - **offset** – Offset to calculate, usually 0.
            - **len** – Len of data to calculate checksum for. May be less than the current object’s size, but shall not be larger.

        Returns:
        :   int 0 if success, ERRNO on failure.

    int bt\_ots\_client\_decode\_dirlisting(uint8\_t \*data, uint16\_t length, [bt\_ots\_client\_dirlisting\_cb](#c.bt_ots_client_dirlisting_cb) cb)
    :   Decode Directory Listing object into object metadata.

        If the Directory Listing object contains multiple objects, then the callback will be called for each of them.

        Parameters:
        :   - **data** – The data received for the directory listing object.
            - **length** – Length of the data.
            - **cb** – The callback that will be called for each object.

    static inline int bt\_ots\_obj\_id\_to\_str(uint64\_t obj\_id, char \*str, size\_t len)
    :   Converts binary OTS Object ID to string.

        Parameters:
        :   - **obj\_id** – Object ID.
            - **str** – Address of user buffer with enough room to store formatted string containing binary Object ID.
            - **len** – Length of data to be copied to user string buffer. Refer to BT\_OTS\_OBJ\_ID\_STR\_LEN about recommended value.

        Returns:
        :   Number of successfully formatted bytes from binary ID.

    void bt\_ots\_metadata\_display(struct [bt\_ots\_obj\_metadata](#c.bt_ots_obj_metadata) \*metadata, uint16\_t count)
    :   Displays one or more object metadata as text with LOG\_INF.

        Parameters:
        :   - **metadata** – Pointer to the first (or only) metadata in an array.
            - **count** – Number of metadata objects to display information of.

    struct bt\_ots\_obj\_type
    :   *#include <ots.h>*

        Type of an OTS object.

    struct bt\_ots\_obj\_size
    :   *#include <ots.h>*

        Descriptor for OTS Object Size parameter.

        Public Members

        uint32\_t cur
        :   Current Size.

        uint32\_t alloc
        :   Allocated Size.

    struct bt\_ots\_feat
    :   *#include <ots.h>*

        Features of the OTS.

    struct bt\_ots\_date\_time
    :   *#include <ots.h>*

        Date and Time structure.

    struct bt\_ots\_obj\_metadata
    :   *#include <ots.h>*

        Metadata of an OTS object.

        Used by the server as a descriptor for OTS object initialization. Used by the client to present object metadata to the application.

        Public Members

        struct [bt\_ots\_obj\_type](#c.bt_ots_obj_type) type
        :   Object Type.

        struct [bt\_ots\_obj\_size](#c.bt_ots_obj_size) size
        :   Object Size.

        uint32\_t props
        :   Object Properties.

    struct bt\_ots\_obj\_add\_param
    :   *#include <ots.h>*

        Descriptor for OTS object addition.

        Public Members

        uint32\_t size
        :   Object size to allocate.

        struct [bt\_ots\_obj\_type](#c.bt_ots_obj_type) type
        :   Object type.

    struct bt\_ots\_obj\_created\_desc
    :   *#include <ots.h>*

        Descriptor for OTS created object.

        Descriptor for OTS object created by the application. This descriptor is returned by [bt\_ots\_cb::obj\_created](#structbt__ots__cb_1a0c95b2bc382474be3c1ae849936a8206) callback which contains further documentation on distinguishing between server and client object creation.

        Public Members

        char \*name
        :   Object name.

            The object name as a NULL terminated string.

            When the server creates a new object the name shall be > 0 and <= BT\_OTS\_OBJ\_MAX\_NAME\_LEN When the client creates a new object the name shall be an empty string

        struct [bt\_ots\_obj\_size](#c.bt_ots_obj_size) size
        :   Object size.

            [bt\_ots\_obj\_size::alloc](#structbt__ots__obj__size_1a86a5675532eae69d40b3305436e81cfb) shall be >= [bt\_ots\_obj\_add\_param::size](#structbt__ots__obj__add__param_1a721734439b43e40324c3a548b5a4eb34)

            When the server creates a new object [bt\_ots\_obj\_size::cur](#structbt__ots__obj__size_1a217290f0fae68a54046eef50ac2a3773) shall be <= [bt\_ots\_obj\_add\_param::size](#structbt__ots__obj__add__param_1a721734439b43e40324c3a548b5a4eb34) When the client creates a new object [bt\_ots\_obj\_size::cur](#structbt__ots__obj__size_1a217290f0fae68a54046eef50ac2a3773) shall be 0

        uint32\_t props
        :   Object properties.

    struct bt\_ots\_cb
    :   *#include <ots.h>*

        OTS callback structure.

        Public Members

        int (\*obj\_created)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, const struct [bt\_ots\_obj\_add\_param](#c.bt_ots_obj_add_param) \*add\_param, struct [bt\_ots\_obj\_created\_desc](#c.bt_ots_obj_created_desc) \*created\_desc)
        :   Object created callback.

            This callback is called whenever a new object is created. Application can reject this request by returning an error when it does not have necessary resources to hold this new object. This callback is also triggered when the server creates a new object with [bt\_ots\_obj\_add()](#group__bt__ots_1gabf59844edd0ffd434acd94bad9a7b52c) API.

            Param ots:
            :   OTS instance.

            Param conn:
            :   The connection that is requesting object creation or NULL if object is created by [bt\_ots\_obj\_add()](#group__bt__ots_1gabf59844edd0ffd434acd94bad9a7b52c).

            Param id:
            :   Object ID.

            Param add\_param:
            :   Object creation requested parameters.

            Param created\_desc:
            :   Created object descriptor that shall be filled by the receiver of this callback.

            Return:
            :   0 in case of success or negative value in case of error.

            Return:
            :   -ENOTSUP if object type is not supported

            Return:
            :   -ENOMEM if no available space for new object.

            Return:
            :   -EINVAL if an invalid parameter is provided

            Return:
            :   other negative values are treated as a generic operation failure

        int (\*obj\_deleted)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id)
        :   Object deleted callback.

            This callback is called whenever an object is deleted. It is also triggered when the server deletes an object with [bt\_ots\_obj\_delete()](#group__bt__ots_1ga872ba5a73fa4e617b9d48e7361af74c7) API.

            Param ots:
            :   OTS instance.

            Param conn:
            :   The connection that deleted the object or NULL if this request came from the server.

            Param id:
            :   Object ID.

            Retval When:
            :   an error is indicated by using a negative value, the object delete procedure is aborted and a corresponding failed status is returned to the client.

            Return:
            :   0 in case of success.

            Return:
            :   -EBUSY if the object is locked. This is generally not expected to be returned by the application as the OTS layer tracks object accesses. An object locked status is returned to the client.

            Return:
            :   Other negative values in case of error. A generic operation failed status is returned to the client.

        void (\*obj\_selected)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id)
        :   Object selected callback.

            This callback is called on successful object selection.

            Param ots:
            :   OTS instance.

            Param conn:
            :   The connection that selected new object.

            Param id:
            :   Object ID.

        ssize\_t (\*obj\_read)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, void \*\*data, size\_t len, off\_t offset)
        :   Object read callback.

            This callback is called multiple times during the Object read operation. OTS module will keep requesting successive Object fragments from the application until the read operation is completed. The end of read operation is indicated by NULL data parameter.

            Param ots:
            :   OTS instance.

            Param conn:
            :   The connection that read object.

            Param id:
            :   Object ID.

            Param data:
            :   In: NULL once the read operations is completed. Out: Next chunk of data to be sent.

            Param len:
            :   Remaining length requested by the client.

            Param offset:
            :   Object data offset.

            Return:
            :   Data length to be sent via data parameter. This value shall be smaller or equal to the len parameter.

            Return:
            :   Negative value in case of an error.

        ssize\_t (\*obj\_write)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, const void \*data, size\_t len, off\_t offset, size\_t rem)
        :   Object write callback.

            This callback is called multiple times during the Object write operation. OTS module will keep providing successive Object fragments to the application until the write operation is completed. The offset and length of each write fragment is validated by the OTS module to be within the allocated size of the object. The remaining length indicates data length remaining to be written and will decrease each write iteration until it reaches 0 in the last write fragment.

            Param ots:
            :   OTS instance.

            Param conn:
            :   The connection that wrote object.

            Param id:
            :   Object ID.

            Param data:
            :   Next chunk of data to be written.

            Param len:
            :   Length of the current chunk of data in the buffer.

            Param offset:
            :   Object data offset.

            Param rem:
            :   Remaining length in the write operation.

            Return:
            :   Number of bytes written in case of success, if the number of bytes written does not match len, -EIO is returned to the L2CAP layer.

            Return:
            :   A negative value in case of an error.

            Return:
            :   -EINPROGRESS has a special meaning and is unsupported at the moment. It should not be returned.

        void (\*obj\_name\_written)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, const char \*cur\_name, const char \*new\_name)
        :   Object name written callback.

            This callback is called when the object name is written. This is a notification to the application that the object name will be updated by the OTS service implementation.

            Param ots:
            :   OTS instance.

            Param conn:
            :   The connection that wrote object name.

            Param id:
            :   Object ID.

            Param cur\_name:
            :   Current object name.

            Param new\_name:
            :   New object name.

        int (\*obj\_cal\_checksum)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, off\_t offset, size\_t len, void \*\*data)
        :   Object Calculate checksum callback.

            This callback is called when the OACP Calculate Checksum procedure is performed. Because object data is opaque to OTS, the application is the only one who knows where data is and should return pointer of actual object data.

            Param ots:
            :   **[in]** OTS instance.

            Param conn:
            :   **[in]** The connection that wrote object.

            Param id:
            :   **[in]** Object ID.

            Param offset:
            :   **[in]** The first octet of the object contents need to be calculated.

            Param len:
            :   **[in]** The length number of octets object name.

            Param data:
            :   **[out]** Pointer of actual object data.

            Return:
            :   0 to accept, or any negative value to reject.

    struct bt\_ots\_init\_param
    :   *#include <ots.h>*

        Descriptor for OTS initialization.

    struct bt\_ots\_client
    :   *#include <ots.h>*

        OTS client instance.

    struct bt\_ots\_client\_cb
    :   *#include <ots.h>*

        OTS client callback structure.

        Public Members

        void (\*obj\_selected)(struct [bt\_ots\_client](#c.bt_ots_client) \*ots\_inst, struct bt\_conn \*conn, int err)
        :   Callback function when a new object is selected.

            Called when the a new object is selected and the current object has changed. The `cur_object` in `ots_inst` will have been reset, and metadata should be read again with [bt\_ots\_client\_read\_object\_metadata()](#group__bt__ots_1ga936f392c880c9d1a73f2bd632e5b63e0).

            Param ots\_inst:
            :   Pointer to the OTC instance.

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error code (bt\_ots\_olcp\_res\_code).

        int (\*obj\_data\_read)(struct [bt\_ots\_client](#c.bt_ots_client) \*ots\_inst, struct bt\_conn \*conn, uint32\_t offset, uint32\_t len, uint8\_t \*data\_p, bool is\_complete)
        :   Callback function for the data of the selected object.

            Called when the data of the selected object are read using [bt\_ots\_client\_read\_object\_data()](#group__bt__ots_1ga8ad1c53325c1b77271307507317a5965).

            Param ots\_inst:
            :   Pointer to the OTC instance.

            Param conn:
            :   The connection to the peer device.

            Param offset:
            :   Offset of the received data.

            Param len:
            :   Length of the received data.

            Param data\_p:
            :   Pointer to the received data.

            Param is\_complete:
            :   Indicate if the whole object has been received.

            Return:
            :   int BT\_OTS\_STOP or BT\_OTS\_CONTINUE. BT\_OTS\_STOP can be used to stop reading.

        void (\*obj\_metadata\_read)(struct [bt\_ots\_client](#c.bt_ots_client) \*ots\_inst, struct bt\_conn \*conn, int err, uint8\_t metadata\_read)
        :   Callback function for metadata of the selected object.

            Called when metadata of the selected object are read using [bt\_ots\_client\_read\_object\_metadata()](#group__bt__ots_1ga936f392c880c9d1a73f2bd632e5b63e0). Not all of the metadata may have been initialized.

            Param ots\_inst:
            :   Pointer to the OTC instance.

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error value. 0 on success, GATT error or ERRNO on fail.

            Param metadata\_read:
            :   Bitfield of the metadata that was successfully read.

        void (\*obj\_data\_written)(struct [bt\_ots\_client](#c.bt_ots_client) \*ots\_inst, struct bt\_conn \*conn, size\_t len)
        :   Callback function for the data of the write object.

            Called when the data of the selected object is written using [bt\_ots\_client\_write\_object\_data()](#group__bt__ots_1ga9444b064c616718dae1577b21540fb9a).

            Param ots\_inst:
            :   Pointer to the OTC instance.

            Param conn:
            :   The connection to the peer device.

            Param len:
            :   Length of the written data.

        void (\*obj\_checksum\_calculated)(struct [bt\_ots\_client](#c.bt_ots_client) \*ots\_inst, struct bt\_conn \*conn, int err, uint32\_t checksum)
        :   Callback function when checksum indication is received.

            Called when the oacp\_ind\_handler received response of OP BT\_GATT\_OTS\_OACP\_PROC\_CHECKSUM\_CALC.

            Param ots\_inst:
            :   Pointer to the OTC instance.

            Param conn:
            :   The connection to the peer device.

            Param err:
            :   Error code (bt\_gatt\_ots\_oacp\_res\_code).

            Param Checksum:
            :   Checksum if error code is BT\_GATT\_OTS\_OACP\_RES\_SUCCESS, otherwise 0.
