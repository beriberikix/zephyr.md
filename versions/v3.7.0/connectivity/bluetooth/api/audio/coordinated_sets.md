---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/audio/coordinated_sets.html
original_path: connectivity/bluetooth/api/audio/coordinated_sets.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth Coordinated Sets

## API Reference

*group* Coordinated Set Identification Profile (CSIP)
:   Coordinated Set Identification Profile (CSIP).

    Published Audio Capabilities Service (PACS).

    The Coordinated Set Identification Profile (CSIP) provides procedures to discover and coordinate sets of devices.

    **Since**
    :   3.0

    **Version**
    :   0.8.0

    The Published Audio Capabilities Service (PACS) is used to expose capabilities to remote devices.

    **Since**
    :   3.0

    **Version**
    :   0.8.0

    Defines

    BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE
    :   Recommended timer for member discovery.

    BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES
    :   Defines the maximum number of Coordinated Set Identification service instances for the Coordinated Set Identification Set Coordinator.

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT
    :   Accept the request to read the SIRK as plaintext.

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC
    :   Accept the request to read the SIRK, but return encrypted SIRK.

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT
    :   Reject the request to read the SIRK.

    BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY
    :   SIRK is available only via an OOB procedure.

    BT\_CSIP\_SIRK\_SIZE
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
    :   Helper to declare [bt\_data](../gap.md#structbt__data) array including RSI.

        This macro is mainly for creating an array of struct [bt\_data](../gap.md#structbt__data) elements which is then passed to e.g. [bt\_le\_ext\_adv\_start()](../gap.md#group__bt__gap_1gaf0f436c55482d9429f674303ae3aa815).

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

    typedef void (\*bt\_csip\_set\_coordinator\_sirk\_changed\_cb)(struct [bt\_csip\_set\_coordinator\_csis\_inst](#c.bt_csip_set_coordinator_csis_inst) \*inst)
    :   Callback when the SIRK value of a set of a connected device changes.

        Param inst:
        :   The Coordinated Set Identification Service instance that was changed. The new SIRK can be accessed via the `inst.info`.

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

    typedef bool (\*bt\_pacs\_cap\_foreach\_func\_t)(const struct [bt\_pacs\_cap](#c.bt_pacs_cap) \*cap, void \*user\_data)
    :   Published Audio Capability iterator callback.

        Param cap:
        :   Capability found.

        Param user\_data:
        :   Data given.

        Return:
        :   true to continue to the next capability

        Return:
        :   false to stop the iteration

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

    int bt\_csip\_set\_member\_sirk(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, const uint8\_t sirk[16])
    :   Set the SIRK of a service instance.

        Parameters:
        :   - **svc\_inst** – Pointer to the registered Coordinated Set Identification Service.
            - **sirk** – The new SIRK.

    int bt\_csip\_set\_member\_get\_sirk(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, uint8\_t sirk[16])
    :   Get the SIRK of a service instance.

        Parameters:
        :   - **svc\_inst** – **[in]** Pointer to the registered Coordinated Set Identification Service.
            - **sirk** – **[out]** Array to store the SIRK in.

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

    struct [bt\_csip\_set\_coordinator\_set\_member](#c.bt_csip_set_coordinator_set_member) \*bt\_csip\_set\_coordinator\_set\_member\_by\_conn(const struct bt\_conn \*conn)
    :   Get the set member from a connection pointer.

        Get the Coordinated Set Identification Profile Set Coordinator pointer from a connection pointer. Only Set Coordinators that have been initiated via [bt\_csip\_set\_coordinator\_discover()](#group__bt__gatt__csip_1ga7e7ea4a92bb76aded86807571a2cbb73) can be retrieved.

        Parameters:
        :   - **conn** – Connection pointer.

        Return values:
        :   - **Pointer** – to a Coordinated Set Identification Profile Set Coordinator instance
            - **NULL** – if `conn` is NULL or if the connection has not done discovery yet

    bool bt\_csip\_set\_coordinator\_is\_set\_member(const uint8\_t sirk[16], struct [bt\_data](../gap.md#c.bt_data "bt_data") \*data)
    :   Check if advertising data indicates a set member.

        Parameters:
        :   - **sirk** – The SIRK of the set to check against
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

        This function will read the lock state of all devices and if all devices are in the unlocked state, then `cb` will be called with the same members as provided by `members`, but where the members are ordered by rank (if present). Once this procedure is finished or an error occurs, [bt\_csip\_set\_coordinator\_cb::ordered\_access](#structbt__csip__set__coordinator__cb_1ae8cf52f1ace4ea1d56ec2204c59bb71c) will be called.

        This procedure only works if all the members have the lock characteristic, and all either has rank = 0 or unique ranks.

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

    void bt\_pacs\_cap\_foreach(enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, [bt\_pacs\_cap\_foreach\_func\_t](#c.bt_pacs_cap_foreach_func_t) func, void \*user\_data)
    :   Published Audio Capability iterator.

        Iterate capabilities with endpoint direction specified.

        Parameters:
        :   - **dir** – Direction of the endpoint to look capability for.
            - **func** – Callback function.
            - **user\_data** – Data to pass to the callback.

    int bt\_pacs\_cap\_register(enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, struct [bt\_pacs\_cap](#c.bt_pacs_cap) \*cap)
    :   Register Published Audio Capability.

        Register Audio Local Capability.

        Parameters:
        :   - **dir** – Direction of the endpoint to register capability for.
            - **cap** – Capability structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_pacs\_cap\_unregister(enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, struct [bt\_pacs\_cap](#c.bt_pacs_cap) \*cap)
    :   Unregister Published Audio Capability.

        Unregister Audio Local Capability.

        Parameters:
        :   - **dir** – Direction of the endpoint to unregister capability for.
            - **cap** – Capability structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_pacs\_set\_location(enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, enum [bt\_audio\_location](audio.md#c.bt_audio_location "bt_audio_location") location)
    :   Set the location for an endpoint type.

        Parameters:
        :   - **dir** – Direction of the endpoints to change location for.
            - **location** – The location to be set.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_pacs\_set\_available\_contexts(enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, enum [bt\_audio\_context](audio.md#c.bt_audio_context "bt_audio_context") contexts)
    :   Set the available contexts for an endpoint type.

        Parameters:
        :   - **dir** – Direction of the endpoints to change available contexts for.
            - **contexts** – The contexts to be set.

        Returns:
        :   0 in case of success or negative value in case of error.

    enum [bt\_audio\_context](audio.md#c.bt_audio_context "bt_audio_context") bt\_pacs\_get\_available\_contexts(enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir)
    :   Get the available contexts for an endpoint type.

        Parameters:
        :   - **dir** – Direction of the endpoints to get contexts for.

        Returns:
        :   Bitmask of available contexts.

    int bt\_pacs\_conn\_set\_available\_contexts\_for\_conn(struct bt\_conn \*conn, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, enum [bt\_audio\_context](audio.md#c.bt_audio_context "bt_audio_context") \*contexts)
    :   Set the available contexts for a given connection.

        This function sets the available contexts value for a given `conn` connection object. If the `contexts` parameter is NULL the available contexts value is reset to default. The default value of the available contexts is set using [bt\_pacs\_set\_available\_contexts](#group__bt__gatt__csip_1ga29a1ec26c1e5e82e02eac39e1088332c) function. The Available Context Value is reset to default on ACL disconnection.

        Parameters:
        :   - **conn** – Connection object.
            - **dir** – Direction of the endpoints to change available contexts for.
            - **contexts** – The contexts to be set or NULL to reset to default.

        Returns:
        :   0 in case of success or negative value in case of error.

    enum [bt\_audio\_context](audio.md#c.bt_audio_context "bt_audio_context") bt\_pacs\_get\_available\_contexts\_for\_conn(struct bt\_conn \*conn, enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir)
    :   Get the available contexts for a given connection.

        This server function returns the available contexts value for a given `conn` connection object. The value returned is the one set with [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](#group__bt__gatt__csip_1ga12f283d2daf72302a01cefb4a4a8fc70) function or the default value set with [bt\_pacs\_set\_available\_contexts](#group__bt__gatt__csip_1ga29a1ec26c1e5e82e02eac39e1088332c) function.

        Parameters:
        :   - **conn** – Connection object.
            - **dir** – Direction of the endpoints to get contexts for.

        Return values:
        :   **BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED** – if `conn` or `dir` are invalid

        Returns:
        :   Bitmask of available contexts.

    int bt\_pacs\_set\_supported\_contexts(enum [bt\_audio\_dir](audio.md#c.bt_audio_dir "bt_audio_dir") dir, enum [bt\_audio\_context](audio.md#c.bt_audio_context "bt_audio_context") contexts)
    :   Set the supported contexts for an endpoint type.

        Parameters:
        :   - **dir** – Direction of the endpoints to change available contexts for.
            - **contexts** – The contexts to be set.

        Returns:
        :   0 in case of success or negative value in case of error.

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

        uint8\_t sirk[16]
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

        const struct [bt\_gatt\_service](../gatt.md#c.bt_gatt_service "bt_gatt_service") \*parent
        :   Parent service pointer.

            Mandatory parent service pointer if this CSIS instance is included by another service. All CSIS instances when  [`CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT`](../../../../kconfig.md#CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT "CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT") is above 1 shall be included by another service, as per the Coordinated Set Identification Profile (CSIP).

    struct bt\_csip\_set\_coordinator\_set\_info
    :   *#include <csip.h>*

        Information about a specific set.

        Public Members

        uint8\_t sirk[16]
        :   The 16 octet set Set Identity Resolving Key (SIRK).

            The SIRK may not be exposed by the server over Bluetooth, and may require an out-of-band solution.

        uint8\_t set\_size
        :   The size of the set.

            Will be 0 if not exposed by the server.

        uint8\_t rank
        :   The rank of the set on the remote device.

            Will be 0 if not exposed by the server.

        bool lockable
        :   Whether or not the set can be locked on this device.

    struct bt\_csip\_set\_coordinator\_csis\_inst
    :   *#include <csip.h>*

        Struct representing a coordinated set instance on a remote device.

        The values in this struct will be populated during discovery of sets ([bt\_csip\_set\_coordinator\_discover()](#group__bt__gatt__csip_1ga7e7ea4a92bb76aded86807571a2cbb73)).

        Public Members

        struct [bt\_csip\_set\_coordinator\_set\_info](#c.bt_csip_set_coordinator_set_info) info
        :   Information about the coordinated set.

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

        Struct to hold the Coordinated Set Identification Profile Set Coordinator callbacks.

        These can be registered for usage with [bt\_csip\_set\_coordinator\_register\_cb()](#group__bt__gatt__csip_1ga08c514fda44e5a9b5cfc16be629c2b37).

        Public Members

        [bt\_csip\_set\_coordinator\_discover\_cb](#c.bt_csip_set_coordinator_discover_cb) discover
        :   Callback when discovery has finished.

        [bt\_csip\_set\_coordinator\_lock\_set\_cb](#c.bt_csip_set_coordinator_lock_set_cb) lock\_set
        :   Callback when locking a set has finished.

        [bt\_csip\_set\_coordinator\_lock\_set\_cb](#c.bt_csip_set_coordinator_lock_set_cb) release\_set
        :   Callback when unlocking a set has finished.

        [bt\_csip\_set\_coordinator\_lock\_changed\_cb](#c.bt_csip_set_coordinator_lock_changed_cb) lock\_changed
        :   Callback when a set’s lock state has changed.

        [bt\_csip\_set\_coordinator\_sirk\_changed\_cb](#c.bt_csip_set_coordinator_sirk_changed_cb) sirk\_changed
        :   Callback when a set’s SIRK has changed.

        [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](#c.bt_csip_set_coordinator_ordered_access_cb_t) ordered\_access
        :   Callback for the ordered access procedure.

    struct bt\_pacs\_cap
    :   *#include <pacs.h>*

        Published Audio Capability structure.

        Public Members

        const struct [bt\_audio\_codec\_cap](audio.md#c.bt_audio_codec_cap "bt_audio_codec_cap") \*codec\_cap
        :   Codec capability reference.
