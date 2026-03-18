---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/coordinated_sets.html
original_path: connectivity/bluetooth/api/coordinated_sets.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth Coordinated Sets

## API Reference

*group* bt\_gatt\_csip
:   Copyright (c) 2021-2022 Nordic Semiconductor ASA.

    SPDX-License-Identifier: Apache-2.0

    Coordinated Set Identification Profile (CSIP)

    - [Experimental] Users should note that the APIs can change as a part of ongoing development.

    Defines

    BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE
    :   Recommended timer for member discovery.

    BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT
    :   Accept the request to read the SIRK as plaintext.

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC
    :   Accept the request to read the SIRK, but return encrypted SIRK.

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT
    :   Reject the request to read the SIRK.

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY
    :   SIRK is available only via an OOB procedure.

    BT\_CSIP\_SET\_SIRK\_SIZE
    :   Size of the Set Identification Resolving Key (SIRK).

    BT\_CSIP\_RSI\_SIZE
    :   Size of the Resolvable Set Identifier (RSI).

    BT\_CSIP\_ERROR\_LOCK\_DENIED
    :   Service is already locked.

    BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED
    :   Service is not locked.

    BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE
    :   Invalid lock value.

    BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY
    :   SIRK only available out-of-band.

    BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED
    :   Client is already owner of the lock.

    BT\_CSIP\_DATA\_RSI(\_rsi)
    :   Helper to declare [bt\_data](gap.md#structbt__data) array including RSI.

        This macro is mainly for creating an array of struct [bt\_data](gap.md#structbt__data) elements which is then passed to e.g. [bt\_le\_ext\_adv\_start()](gap.md#group__bt__gap_1gaddc6da5166cd8415d2b367380447eac1).

        Parameters:
        :   - **\_rsi** – Pointer to the RSI value

    Typedefs

    typedef void (\*bt\_csip\_set\_coordinator\_discover\_cb)(struct bt\_conn \*conn, const struct [bt\_csip\_set\_coordinator\_set\_member](#c.bt_csip_set_coordinator_set_member) \*member, int err, size\_t set\_count)
    :   Callback for discovering Coordinated Set Identification Services.

        Param conn:
        :   Pointer to the remote device.

        Param member:
        :   Pointer to the set member.

        Param err:
        :   0 on success, or an errno value on error.

        Param set\_count:
        :   Number of sets on the member.

    typedef void (\*bt\_csip\_set\_coordinator\_lock\_set\_cb)(int err)
    :   Callback for locking a set across one or more devices.

        Param err:
        :   0 on success, or an errno value on error.

    typedef void (\*bt\_csip\_set\_coordinator\_lock\_changed\_cb)(struct [bt\_csip\_set\_coordinator\_csis\_inst](#c.bt_csip_set_coordinator_csis_inst) \*inst, bool locked)
    :   Callback when the lock value on a set of a connected device changes.

        Param inst:
        :   The Coordinated Set Identification Service instance that was changed.

        Param locked:
        :   Whether the lock is locked or release.

        Return:
        :   int Return 0 on success, or an errno value on error.

    typedef void (\*bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t)(const struct [bt\_csip\_set\_coordinator\_set\_info](#c.bt_csip_set_coordinator_set_info) \*set\_info, int err, bool locked, struct [bt\_csip\_set\_coordinator\_set\_member](#c.bt_csip_set_coordinator_set_member) \*member)
    :   Callback for [bt\_csip\_set\_coordinator\_ordered\_access()](#group__bt__gatt__csip_1gacd83494562a62fbdbc7282107d4454b4).

        If any of the set members supplied to [bt\_csip\_set\_coordinator\_ordered\_access()](#group__bt__gatt__csip_1gacd83494562a62fbdbc7282107d4454b4) is in the locked state, this will be called with `locked` true and `member` will be the locked member, and the ordered access procedure is cancelled. Likewise, if any error occurs, the procedure will also be aborted.

        Param set\_info:
        :   Pointer to the a specific set\_info struct.

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail.

        Param locked:
        :   Whether the lock is locked or release.

        Param member:
        :   The locked member if `locked` is true, otherwise NULL.

    typedef bool (\*bt\_csip\_set\_coordinator\_ordered\_access\_t)(const struct [bt\_csip\_set\_coordinator\_set\_info](#c.bt_csip_set_coordinator_set_info) \*set\_info, struct [bt\_csip\_set\_coordinator\_set\_member](#c.bt_csip_set_coordinator_set_member) \*members[], size\_t count)
    :   Callback function definition for [bt\_csip\_set\_coordinator\_ordered\_access()](#group__bt__gatt__csip_1gacd83494562a62fbdbc7282107d4454b4).

        Param set\_info:
        :   Pointer to the a specific set\_info struct.

        Param members:
        :   Array of members ordered by rank. The procedure shall be done on the members in ascending order.

        Param count:
        :   Number of members in `members`.

        Return:
        :   true if the procedures can be successfully done, or false to stop the procedure.

    Functions

    void \*bt\_csip\_set\_member\_svc\_decl\_get(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)
    :   Get the service declaration attribute.

        The first service attribute can be included in any other GATT service.

        Parameters:
        :   - **svc\_inst** – Pointer to the Coordinated Set Identification Service.

        Returns:
        :   The first CSIS attribute instance.

    int bt\_csip\_set\_member\_register(const struct [bt\_csip\_set\_member\_register\_param](#c.bt_csip_set_member_register_param) \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst)
    :   Register a Coordinated Set Identification Service instance.

        This will register and enable the service and make it discoverable by clients.

        This shall only be done as a server.

        Parameters:
        :   - **param** – Coordinated Set Identification Service register parameters.
            - **svc\_inst** – **[out]** Pointer to the registered Coordinated Set Identification Service.

        Returns:
        :   0 if success, errno on failure.

    int bt\_csip\_set\_member\_unregister(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)
    :   Unregister a Coordinated Set Identification Service instance.

        This will unregister and disable the service instance.

        Parameters:
        :   - **svc\_inst** – Pointer to the registered Coordinated Set Identification Service.

        Returns:
        :   0 if success, errno on failure.

    void bt\_csip\_set\_member\_print\_sirk(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)
    :   Print the SIRK to the debug output.

        Parameters:
        :   - **svc\_inst** – Pointer to the Coordinated Set Identification Service.

    int bt\_csip\_set\_member\_generate\_rsi(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, uint8\_t rsi[6])
    :   Generate the Resolvable Set Identifier (RSI) value.

        This will generate RSI for given `svc_inst` instance.

        Parameters:
        :   - **svc\_inst** – Pointer to the Coordinated Set Identification Service.
            - **rsi** – Pointer to the 6-octet newly generated RSI data in little-endian.

        Returns:
        :   int 0 if on success, errno on error.

    int bt\_csip\_set\_member\_lock(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, bool lock, bool force)
    :   Locks a specific Coordinated Set Identification Service instance on the server.

        Parameters:
        :   - **svc\_inst** – Pointer to the Coordinated Set Identification Service.
            - **lock** – If true lock the set, if false release the set.
            - **force** – This argument only have meaning when `lock` is false (release) and will force release the lock, regardless of who took the lock.

        Returns:
        :   0 on success, GATT error on error.

    int bt\_csip\_set\_coordinator\_discover(struct bt\_conn \*conn)
    :   Initialise the csip\_set\_coordinator instance for a connection.

        This will do a discovery on the device and prepare the instance for following commands.

        Parameters:
        :   - **conn** – Pointer to remote device to perform discovery on.

        Returns:
        :   int Return 0 on success, or an errno value on error.

    bool bt\_csip\_set\_coordinator\_is\_set\_member(const uint8\_t set\_sirk[16], struct [bt\_data](gap.md#c.bt_data "bt_data") \*data)
    :   Check if advertising data indicates a set member.

        Parameters:
        :   - **set\_sirk** – The SIRK of the set to check against
            - **data** – The advertising data

        Returns:
        :   true if the advertising data indicates a set member, false otherwise

    int bt\_csip\_set\_coordinator\_register\_cb(struct [bt\_csip\_set\_coordinator\_cb](#c.bt_csip_set_coordinator_cb) \*cb)
    :   Registers callbacks for csip\_set\_coordinator.

        Parameters:
        :   - **cb** – Pointer to the callback structure.

        Returns:
        :   Return 0 on success, or an errno value on error.

    int bt\_csip\_set\_coordinator\_ordered\_access(const struct [bt\_csip\_set\_coordinator\_set\_member](#c.bt_csip_set_coordinator_set_member) \*members[], uint8\_t count, const struct [bt\_csip\_set\_coordinator\_set\_info](#c.bt_csip_set_coordinator_set_info) \*set\_info, [bt\_csip\_set\_coordinator\_ordered\_access\_t](#c.bt_csip_set_coordinator_ordered_access_t) cb)
    :   Access Coordinated Set devices in an ordered manner as a client.

        This function will read the lock state of all devices and if all devices are in the unlocked state, then `cb` will be called with the same members as provided by `members`, but where the members are ordered by rank (if present). Once this procedure is finished or an error occurs, bt\_csip\_set\_coordinator\_cb::ordered\_access will be called.

        This procedure only works if all the members have the lock characterstic, and all either has rank = 0 or unique ranks.

        If any of the members are in the locked state, the procedure will be cancelled.

        This can only be done on members that are bonded.

        Parameters:
        :   - **members** – Array of set members to access.
            - **count** – Number of set members in `members`.
            - **set\_info** – Pointer to the a specific set\_info struct, as a member may be part of multiple sets.
            - **cb** – The callback function to be called for each member.

    int bt\_csip\_set\_coordinator\_lock(const struct [bt\_csip\_set\_coordinator\_set\_member](#c.bt_csip_set_coordinator_set_member) \*\*members, uint8\_t count, const struct [bt\_csip\_set\_coordinator\_set\_info](#c.bt_csip_set_coordinator_set_info) \*set\_info)
    :   Lock an array of set members.

        The members will be locked starting from lowest rank going up.

        TODO: If locking fails, the already locked members will not be unlocked.

        Parameters:
        :   - **members** – Array of set members to lock.
            - **count** – Number of set members in `members`.
            - **set\_info** – Pointer to the a specific set\_info struct, as a member may be part of multiple sets.

        Returns:
        :   Return 0 on success, or an errno value on error.

    int bt\_csip\_set\_coordinator\_release(const struct [bt\_csip\_set\_coordinator\_set\_member](#c.bt_csip_set_coordinator_set_member) \*\*members, uint8\_t count, const struct [bt\_csip\_set\_coordinator\_set\_info](#c.bt_csip_set_coordinator_set_info) \*set\_info)
    :   Release an array of set members.

        The members will be released starting from highest rank going down.

        Parameters:
        :   - **members** – Array of set members to lock.
            - **count** – Number of set members in `members`.
            - **set\_info** – Pointer to the a specific set\_info struct, as a member may be part of multiple sets.

        Returns:
        :   Return 0 on success, or an errno value on error.

    struct bt\_csip\_set\_member\_cb
    :   *#include <csip.h>*

        Callback structure for the Coordinated Set Identification Service.

        Public Members

        void (\*lock\_changed)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, bool locked)
        :   Callback whenever the lock changes on the server.

            Param conn:
            :   The connection to the client that changed the lock. NULL if server changed it, either by calling [bt\_csip\_set\_member\_lock()](#group__bt__gatt__csip_1ga95e2ba4b65ec42eedb26bf5ad181b606) or by timeout.

            Param svc\_inst:
            :   Pointer to the Coordinated Set Identification Service.

            Param locked:
            :   Whether the lock was locked or released.

        uint8\_t (\*sirk\_read\_req)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)
        :   Request from a peer device to read the sirk.

            If this callback is not set, all clients will be allowed to read the SIRK unencrypted.

            Param conn:
            :   The connection to the client that requested to read the SIRK.

            Param svc\_inst:
            :   Pointer to the Coordinated Set Identification Service.

            Return:
            :   A BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_\* response code.

    struct bt\_csip\_set\_member\_register\_param
    :   *#include <csip.h>*

        Register structure for Coordinated Set Identification Service.

        Public Members

        uint8\_t set\_size
        :   Size of the set.

            If set to 0, the set size characteristic won’t be initialized.

        uint8\_t set\_sirk[16]
        :   The unique Set Identity Resolving Key (SIRK).

            This shall be unique between different sets, and shall be the same for each set member for each set.

        bool lockable
        :   Boolean to set whether the set is lockable by clients.

            Setting this to false will disable the lock characteristic.

        uint8\_t rank
        :   Rank of this device in this set.

            If the lockable parameter is set to true, this shall be > 0 and <= to the set\_size. If the lockable parameter is set to false, this may be set to 0 to disable the rank characteristic.

        struct [bt\_csip\_set\_member\_cb](#c.bt_csip_set_member_cb) \*cb
        :   Pointer to the callback structure.

    struct bt\_csip\_set\_coordinator\_set\_info
    :   *#include <csip.h>*

        Information about a specific set.

        Public Members

        uint8\_t set\_sirk[16]
        :   The 16 octet set Set Identity Resolving Key (SIRK).

            The Set SIRK may not be exposed by the server over Bluetooth, and may require an out-of-band solution.

        uint8\_t set\_size
        :   The size of the set.

            Will be 0 if not exposed by the server.

        uint8\_t rank
        :   The rank of the set on on the remote device.

            Will be 0 if not exposed by the server.

        bool lockable
        :   Whether or not the set can be locked on this device.

    struct bt\_csip\_set\_coordinator\_csis\_inst
    :   *#include <csip.h>*

        Struct representing a coordinated set instance on a remote device.

        The values in this struct will be populated during discovery of sets ([bt\_csip\_set\_coordinator\_discover()](#group__bt__gatt__csip_1ga7e7ea4a92bb76aded86807571a2cbb73)).

        Public Members

        void \*svc\_inst
        :   Internally used pointer value.

    struct bt\_csip\_set\_coordinator\_set\_member
    :   *#include <csip.h>*

        Struct representing a remote device as a set member.

        Public Members

        struct [bt\_csip\_set\_coordinator\_csis\_inst](#c.bt_csip_set_coordinator_csis_inst) insts[0]
        :   Array of Coordinated Set Identification Service instances for the remote device.

    struct bt\_csip\_set\_coordinator\_cb
    :   *#include <csip.h>*
