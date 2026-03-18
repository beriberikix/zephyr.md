---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/cfg_cli.html
original_path: connectivity/bluetooth/api/mesh/cfg_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Configuration Client

The Configuration Client model is a foundation model defined by the Bluetooth Mesh
specification. It provides functionality for configuring most parameters of a
mesh node, including encryption keys, model configuration and feature
enabling.

The Configuration Client model communicates with a
[Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv) model using the device key of the target
node. The Configuration Client model may communicate with servers on other
nodes or self-configure through the local Configuration Server model.

All configuration functions in the Configuration Client API have `net_idx`
and `addr` as their first parameters. These should be set to the network
index and primary unicast address that the target node was provisioned with.

The Configuration Client model is optional, and it must only be instantiated on the
primary element if present in the Composition Data.

## API reference

*group* Configuration Client Model
:   Configuration Client Model.

    Defines

    BT\_MESH\_MODEL\_CFG\_CLI(cli\_data)
    :   Generic Configuration Client model composition data entry.

        Parameters:
        :   - **cli\_data** – Pointer to a [Configuration Client Model](#group__bt__mesh__cfg__cli) instance.

    BT\_MESH\_PUB\_PERIOD\_100MS(steps)
    :   Helper macro to encode model publication period in units of 100ms.

        Parameters:
        :   - **steps** – Number of 100ms steps.

        Returns:
        :   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](#structbt__mesh__cfg__cli__mod__pub_1a104afe2b8d9766e037293b09c0c1b91c)

    BT\_MESH\_PUB\_PERIOD\_SEC(steps)
    :   Helper macro to encode model publication period in units of 1 second.

        Parameters:
        :   - **steps** – Number of 1 second steps.

        Returns:
        :   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](#structbt__mesh__cfg__cli__mod__pub_1a104afe2b8d9766e037293b09c0c1b91c)

    BT\_MESH\_PUB\_PERIOD\_10SEC(steps)
    :   Helper macro to encode model publication period in units of 10 seconds.

        Parameters:
        :   - **steps** – Number of 10 second steps.

        Returns:
        :   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](#structbt__mesh__cfg__cli__mod__pub_1a104afe2b8d9766e037293b09c0c1b91c)

    BT\_MESH\_PUB\_PERIOD\_10MIN(steps)
    :   Helper macro to encode model publication period in units of 10 minutes.

        Parameters:
        :   - **steps** – Number of 10 minute steps.

        Returns:
        :   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](#structbt__mesh__cfg__cli__mod__pub_1a104afe2b8d9766e037293b09c0c1b91c)

    Functions

    int bt\_mesh\_cfg\_cli\_node\_reset(uint16\_t net\_idx, uint16\_t addr, bool \*status)
    :   Reset the target node and remove it from the network.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **status** – Status response parameter

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_comp\_data\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t page, uint8\_t \*rsp, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*comp)
    :   Get the target node’s composition data.

        If the other device does not have the given composition data page, it will return the largest page number it supports that is less than the requested page index. The actual page the device responds with is returned in `rsp`.

        This method can be used asynchronously by setting `rsp` and `comp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **page** – Composition data page, or 0xff to request the first available page.
            - **rsp** – Return parameter for the returned page number, or NULL.
            - **comp** – Composition data buffer to fill.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_beacon\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status)
    :   Get the target node’s network beacon state.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **status** – Status response parameter, returns one of [BT\_MESH\_BEACON\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga8fa3d0ac3cb9f69464c4068ca61689b9) or [BT\_MESH\_BEACON\_ENABLED](cfg.md#group__bt__mesh__cfg_1ga01235217559423b93d7e6cf2236278f0) on success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_krp\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status, uint8\_t \*phase)
    :   Get the target node’s network key refresh phase state.

        This method can be used asynchronously by setting `status` and `phase` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index.
            - **status** – Status response parameter.
            - **phase** – Pointer to the Key Refresh variable to fill.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_krp\_set(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t transition, uint8\_t \*status, uint8\_t \*phase)
    :   Set the target node’s network key refresh phase parameters.

        This method can be used asynchronously by setting `status` and `phase` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index.
            - **transition** – Transition parameter.
            - **status** – Status response parameter.
            - **phase** – Pointer to the new Key Refresh phase. Will return the actual Key Refresh phase after updating.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_beacon\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*status)
    :   Set the target node’s network beacon state.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New network beacon state, should be one of [BT\_MESH\_BEACON\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga8fa3d0ac3cb9f69464c4068ca61689b9) or [BT\_MESH\_BEACON\_ENABLED](cfg.md#group__bt__mesh__cfg_1ga01235217559423b93d7e6cf2236278f0).
            - **status** – Status response parameter. Returns one of [BT\_MESH\_BEACON\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga8fa3d0ac3cb9f69464c4068ca61689b9) or [BT\_MESH\_BEACON\_ENABLED](cfg.md#group__bt__mesh__cfg_1ga01235217559423b93d7e6cf2236278f0) on success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_ttl\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*ttl)
    :   Get the target node’s Time To Live value.

        This method can be used asynchronously by setting `ttl` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **ttl** – TTL response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_ttl\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*ttl)
    :   Set the target node’s Time To Live value.

        This method can be used asynchronously by setting `ttl` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New Time To Live value.
            - **ttl** – TTL response buffer.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_friend\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status)
    :   Get the target node’s Friend feature status.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **status** – Status response parameter. Returns one of [BT\_MESH\_FRIEND\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga29fe48989e760438f2c5241110134c8c), [BT\_MESH\_FRIEND\_ENABLED](cfg.md#group__bt__mesh__cfg_1gaa23bba212dc1b322651723ca20f497a3) or [BT\_MESH\_FRIEND\_NOT\_SUPPORTED](cfg.md#group__bt__mesh__cfg_1ga35f85e6a9c085cdad4f70b8e60d0b027) on success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_friend\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*status)
    :   Set the target node’s Friend feature state.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New Friend feature state. Should be one of [BT\_MESH\_FRIEND\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga29fe48989e760438f2c5241110134c8c) or [BT\_MESH\_FRIEND\_ENABLED](cfg.md#group__bt__mesh__cfg_1gaa23bba212dc1b322651723ca20f497a3).
            - **status** – Status response parameter. Returns one of [BT\_MESH\_FRIEND\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga29fe48989e760438f2c5241110134c8c), [BT\_MESH\_FRIEND\_ENABLED](cfg.md#group__bt__mesh__cfg_1gaa23bba212dc1b322651723ca20f497a3) or [BT\_MESH\_FRIEND\_NOT\_SUPPORTED](cfg.md#group__bt__mesh__cfg_1ga35f85e6a9c085cdad4f70b8e60d0b027) on success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_gatt\_proxy\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status)
    :   Get the target node’s Proxy feature state.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **status** – Status response parameter. Returns one of [BT\_MESH\_GATT\_PROXY\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga3fe3e68efd25a3a03a041b978435fd7b), [BT\_MESH\_GATT\_PROXY\_ENABLED](cfg.md#group__bt__mesh__cfg_1ga77f4438624aae49ea2bb66437c9623f7) or [BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED](cfg.md#group__bt__mesh__cfg_1gaecec3747198a29dd10185e3755e660f8) on success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_gatt\_proxy\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*status)
    :   Set the target node’s Proxy feature state.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New Proxy feature state. Must be one of [BT\_MESH\_GATT\_PROXY\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga3fe3e68efd25a3a03a041b978435fd7b) or [BT\_MESH\_GATT\_PROXY\_ENABLED](cfg.md#group__bt__mesh__cfg_1ga77f4438624aae49ea2bb66437c9623f7).
            - **status** – Status response parameter. Returns one of [BT\_MESH\_GATT\_PROXY\_DISABLED](cfg.md#group__bt__mesh__cfg_1ga3fe3e68efd25a3a03a041b978435fd7b), [BT\_MESH\_GATT\_PROXY\_ENABLED](cfg.md#group__bt__mesh__cfg_1ga77f4438624aae49ea2bb66437c9623f7) or [BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED](cfg.md#group__bt__mesh__cfg_1gaecec3747198a29dd10185e3755e660f8) on success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_net\_transmit\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*transmit)
    :   Get the target node’s network\_transmit state.

        This method can be used asynchronously by setting `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **transmit** – Network transmit response parameter. Returns the encoded network transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](access.md#group__bt__mesh__access_1ga62fda0d731241efbaa4827e4eb9d1795) and [BT\_MESH\_TRANSMIT\_INT](access.md#group__bt__mesh__access_1ga2aa21171c5677d23ad0c472291639417).

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_net\_transmit\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*transmit)
    :   Set the target node’s network transmit parameters.

        This method can be used asynchronously by setting `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        See also

        [BT\_MESH\_TRANSMIT](access.md#group__bt__mesh__access_1gaff82bf652232fbce71c31f38a10577a9).

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New encoded network transmit parameters.
            - **transmit** – Network transmit response parameter. Returns the encoded network transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](access.md#group__bt__mesh__access_1ga62fda0d731241efbaa4827e4eb9d1795) and [BT\_MESH\_TRANSMIT\_INT](access.md#group__bt__mesh__access_1ga2aa21171c5677d23ad0c472291639417).

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_relay\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status, uint8\_t \*transmit)
    :   Get the target node’s Relay feature state.

        This method can be used asynchronously by setting `status` and `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **status** – Status response parameter. Returns one of [BT\_MESH\_RELAY\_DISABLED](cfg.md#group__bt__mesh__cfg_1gaafd10319da7d2f938207b8fd6de02dbc), [BT\_MESH\_RELAY\_ENABLED](cfg.md#group__bt__mesh__cfg_1gae5d235a7c182a8add961d7ce344f87aa) or [BT\_MESH\_RELAY\_NOT\_SUPPORTED](cfg.md#group__bt__mesh__cfg_1gabbbbddd31c2a92256fe2f7a7520e76f7) on success.
            - **transmit** – Transmit response parameter. Returns the encoded relay transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](access.md#group__bt__mesh__access_1ga62fda0d731241efbaa4827e4eb9d1795) and [BT\_MESH\_TRANSMIT\_INT](access.md#group__bt__mesh__access_1ga2aa21171c5677d23ad0c472291639417).

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_relay\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t new\_relay, uint8\_t new\_transmit, uint8\_t \*status, uint8\_t \*transmit)
    :   Set the target node’s Relay parameters.

        This method can be used asynchronously by setting `status` and `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        See also

        [BT\_MESH\_TRANSMIT](access.md#group__bt__mesh__access_1gaff82bf652232fbce71c31f38a10577a9).

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **new\_relay** – New relay state. Must be one of [BT\_MESH\_RELAY\_DISABLED](cfg.md#group__bt__mesh__cfg_1gaafd10319da7d2f938207b8fd6de02dbc) or [BT\_MESH\_RELAY\_ENABLED](cfg.md#group__bt__mesh__cfg_1gae5d235a7c182a8add961d7ce344f87aa).
            - **new\_transmit** – New encoded relay transmit parameters.
            - **status** – Status response parameter. Returns one of [BT\_MESH\_RELAY\_DISABLED](cfg.md#group__bt__mesh__cfg_1gaafd10319da7d2f938207b8fd6de02dbc), [BT\_MESH\_RELAY\_ENABLED](cfg.md#group__bt__mesh__cfg_1gae5d235a7c182a8add961d7ce344f87aa) or [BT\_MESH\_RELAY\_NOT\_SUPPORTED](cfg.md#group__bt__mesh__cfg_1gabbbbddd31c2a92256fe2f7a7520e76f7) on success.
            - **transmit** – Transmit response parameter. Returns the encoded relay transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](access.md#group__bt__mesh__access_1ga62fda0d731241efbaa4827e4eb9d1795) and [BT\_MESH\_TRANSMIT\_INT](access.md#group__bt__mesh__access_1ga2aa21171c5677d23ad0c472291639417).

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_net\_key\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, const uint8\_t net\_key[16], uint8\_t \*status)
    :   Add a network key to the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index.
            - **net\_key** – Network key.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_net\_key\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t \*keys, size\_t \*key\_cnt)
    :   Get a list of the target node’s network key indexes.

        This method can be used asynchronously by setting `keys` or `key_cnt` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **keys** – Net key index list response parameter. Will be filled with all the returned network key indexes it can fill.
            - **key\_cnt** – Net key index list length. Should be set to the capacity of the `keys` list when calling. Will return the number of returned network key indexes upon success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_net\_key\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status)
    :   Delete a network key from the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_app\_key\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint16\_t key\_app\_idx, const uint8\_t app\_key[16], uint8\_t \*status)
    :   Add an application key to the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index the application key belongs to.
            - **key\_app\_idx** – Application key index.
            - **app\_key** – Application key.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_app\_key\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status, uint16\_t \*keys, size\_t \*key\_cnt)
    :   Get a list of the target node’s application key indexes for a specific network key.

        This method can be used asynchronously by setting `status` and ( `keys` or `key_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index to request the app key indexes of.
            - **status** – Status response parameter.
            - **keys** – App key index list response parameter. Will be filled with all the returned application key indexes it can fill.
            - **key\_cnt** – App key index list length. Should be set to the capacity of the `keys` list when calling. Will return the number of returned application key indexes upon success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_app\_key\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint16\_t key\_app\_idx, uint8\_t \*status)
    :   Delete an application key from the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index the application key belongs to.
            - **key\_app\_idx** – Application key index.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_app\_bind(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint8\_t \*status)
    :   Bind an application to a SIG model on the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_app\_idx** – Application index to bind.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_app\_unbind(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint8\_t \*status)
    :   Unbind an application from a SIG model on the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_app\_idx** – Application index to unbind.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)
    :   Bind an application to a vendor model on the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_app\_idx** – Application index to bind.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)
    :   Unbind an application from a vendor model on the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_app\_idx** – Application index to unbind.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_app\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint8\_t \*status, uint16\_t \*apps, size\_t \*app\_cnt)
    :   Get a list of all applications bound to a SIG model on the target node.

        This method can be used asynchronously by setting `status` and ( `apps` or `app_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.
            - **apps** – App index list response parameter. Will be filled with all the returned application key indexes it can fill.
            - **app\_cnt** – App index list length. Should be set to the capacity of the `apps` list when calling. Will return the number of returned application key indexes upon success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status, uint16\_t \*apps, size\_t \*app\_cnt)
    :   Get a list of all applications bound to a vendor model on the target node.

        This method can be used asynchronously by setting `status` and ( `apps` or `app_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.
            - **apps** – App index list response parameter. Will be filled with all the returned application key indexes it can fill.
            - **app\_cnt** – App index list length. Should be set to the capacity of the `apps` list when calling. Will return the number of returned application key indexes upon success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_pub\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](#c.bt_mesh_cfg_cli_mod_pub) \*pub, uint8\_t \*status)
    :   Get publish parameters for a SIG model on the target node.

        This method can be used asynchronously by setting `status` and `pub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **pub** – Publication parameter return buffer.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](#c.bt_mesh_cfg_cli_mod_pub) \*pub, uint8\_t \*status)
    :   Get publish parameters for a vendor model on the target node.

        This method can be used asynchronously by setting `status` and `pub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **pub** – Publication parameter return buffer.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_pub\_set(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](#c.bt_mesh_cfg_cli_mod_pub) \*pub, uint8\_t \*status)
    :   Set publish parameters for a SIG model on the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        `pub` shall not be NULL.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **pub** – Publication parameters.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](#c.bt_mesh_cfg_cli_mod_pub) \*pub, uint8\_t \*status)
    :   Set publish parameters for a vendor model on the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        `pub` shall not be NULL.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **pub** – Publication parameters.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint8\_t \*status)
    :   Add a group address to a SIG model’s subscription list.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **sub\_addr** – Group address to add to the subscription list.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)
    :   Add a group address to a vendor model’s subscription list.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **sub\_addr** – Group address to add to the subscription list.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint8\_t \*status)
    :   Delete a group address in a SIG model’s subscription list.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **sub\_addr** – Group address to add to the subscription list.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)
    :   Delete a group address in a vendor model’s subscription list.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **sub\_addr** – Group address to add to the subscription list.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint8\_t \*status)
    :   Overwrite all addresses in a SIG model’s subscription list with a group address.

        Deletes all subscriptions in the model’s subscription list, and adds a single group address instead.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **sub\_addr** – Group address to add to the subscription list.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)
    :   Overwrite all addresses in a vendor model’s subscription list with a group address.

        Deletes all subscriptions in the model’s subscription list, and adds a single group address instead.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **sub\_addr** – Group address to add to the subscription list.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t \*virt\_addr, uint8\_t \*status)
    :   Add a virtual address to a SIG model’s subscription list.

        This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **label** – Virtual address label to add to the subscription list.
            - **mod\_id** – Model ID.
            - **virt\_addr** – Virtual address response parameter.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t cid, uint16\_t \*virt\_addr, uint8\_t \*status)
    :   Add a virtual address to a vendor model’s subscription list.

        This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **label** – Virtual address label to add to the subscription list.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **virt\_addr** – Virtual address response parameter.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t \*virt\_addr, uint8\_t \*status)
    :   Delete a virtual address in a SIG model’s subscription list.

        This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **label** – Virtual address parameter to add to the subscription list.
            - **mod\_id** – Model ID.
            - **virt\_addr** – Virtual address response parameter.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t cid, uint16\_t \*virt\_addr, uint8\_t \*status)
    :   Delete a virtual address in a vendor model’s subscription list.

        This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **label** – Virtual address label to add to the subscription list.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **virt\_addr** – Virtual address response parameter.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t \*virt\_addr, uint8\_t \*status)
    :   Overwrite all addresses in a SIG model’s subscription list with a virtual address.

        Deletes all subscriptions in the model’s subscription list, and adds a single group address instead.

        This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **label** – Virtual address label to add to the subscription list.
            - **mod\_id** – Model ID.
            - **virt\_addr** – Virtual address response parameter.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t cid, uint16\_t \*virt\_addr, uint8\_t \*status)
    :   Overwrite all addresses in a vendor model’s subscription list with a virtual address.

        Deletes all subscriptions in the model’s subscription list, and adds a single group address instead.

        This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **label** – Virtual address label to add to the subscription list.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **virt\_addr** – Virtual address response parameter.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint8\_t \*status, uint16\_t \*subs, size\_t \*sub\_cnt)
    :   Get the subscription list of a SIG model on the target node.

        This method can be used asynchronously by setting `status` and ( `subs` or `sub_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.
            - **subs** – Subscription list response parameter. Will be filled with all the returned subscriptions it can fill.
            - **sub\_cnt** – Subscription list element count. Should be set to the capacity of the `subs` list when calling. Will return the number of returned subscriptions upon success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status, uint16\_t \*subs, size\_t \*sub\_cnt)
    :   Get the subscription list of a vendor model on the target node.

        This method can be used asynchronously by setting `status` and ( `subs` or `sub_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.
            - **subs** – Subscription list response parameter. Will be filled with all the returned subscriptions it can fill.
            - **sub\_cnt** – Subscription list element count. Should be set to the capacity of the `subs` list when calling. Will return the number of returned subscriptions upon success.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_hb\_sub\_set(uint16\_t net\_idx, uint16\_t addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](#c.bt_mesh_cfg_cli_hb_sub) \*sub, uint8\_t \*status)
    :   Set the target node’s Heartbeat subscription parameters.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        `sub` shall not be null.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **sub** – New Heartbeat subscription parameters.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_hb\_sub\_get(uint16\_t net\_idx, uint16\_t addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](#c.bt_mesh_cfg_cli_hb_sub) \*sub, uint8\_t \*status)
    :   Get the target node’s Heartbeat subscription parameters.

        This method can be used asynchronously by setting `status` and `sub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **sub** – Heartbeat subscription parameter return buffer.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_hb\_pub\_set(uint16\_t net\_idx, uint16\_t addr, const struct [bt\_mesh\_cfg\_cli\_hb\_pub](#c.bt_mesh_cfg_cli_hb_pub) \*pub, uint8\_t \*status)
    :   Set the target node’s Heartbeat publication parameters.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        `pub` shall not be NULL;

        Note

        The target node must already have received the specified network key.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **pub** – New Heartbeat publication parameters.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_hb\_pub\_get(uint16\_t net\_idx, uint16\_t addr, struct [bt\_mesh\_cfg\_cli\_hb\_pub](#c.bt_mesh_cfg_cli_hb_pub) \*pub, uint8\_t \*status)
    :   Get the target node’s Heartbeat publication parameters.

        This method can be used asynchronously by setting `status` and `pub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **pub** – Heartbeat publication parameter return buffer.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint8\_t \*status)
    :   Delete all group addresses in a SIG model’s subscription list.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)
    :   Delete all group addresses in a vendor model’s subscription list.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **elem\_addr** – Element address the model is in.
            - **mod\_id** – Model ID.
            - **cid** – Company ID of the model.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_net\_key\_update(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, const uint8\_t net\_key[16], uint8\_t \*status)
    :   Update a network key to the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index.
            - **net\_key** – Network key.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_app\_key\_update(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint16\_t key\_app\_idx, const uint8\_t app\_key[16], uint8\_t \*status)
    :   Update an application key to the target node.

        This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index the application key belongs to.
            - **key\_app\_idx** – Application key index.
            - **app\_key** – Application key.
            - **status** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_node\_identity\_set(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t new\_identity, uint8\_t \*status, uint8\_t \*identity)
    :   Set the Node Identity parameters.

        This method can be used asynchronously by setting `status` and `identity` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **new\_identity** – New identity state. Must be one of [BT\_MESH\_NODE\_IDENTITY\_STOPPED](cfg.md#group__bt__mesh__cfg_1ga9a83214cdbd34ac1d4bc644136523bd9) or [BT\_MESH\_NODE\_IDENTITY\_RUNNING](cfg.md#group__bt__mesh__cfg_1ga86e88acc6fdcc26a9cea4415daad016c)
            - **key\_net\_idx** – Network key index the application key belongs to.
            - **status** – Status response parameter.
            - **identity** – Identity response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_node\_identity\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status, uint8\_t \*identity)
    :   Get the Node Identity parameters.

        This method can be used asynchronously by setting `status` and `identity` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network key index the application key belongs to.
            - **status** – Status response parameter.
            - **identity** – Identity response parameter. Must be one of [BT\_MESH\_NODE\_IDENTITY\_STOPPED](cfg.md#group__bt__mesh__cfg_1ga9a83214cdbd34ac1d4bc644136523bd9) or [BT\_MESH\_NODE\_IDENTITY\_RUNNING](cfg.md#group__bt__mesh__cfg_1ga86e88acc6fdcc26a9cea4415daad016c)

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_cfg\_cli\_lpn\_timeout\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t unicast\_addr, int32\_t \*polltimeout)
    :   Get the Low Power Node Polltimeout parameters.

        This method can be used asynchronously by setting `polltimeout` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **unicast\_addr** – LPN unicast address.
            - **polltimeout** – Poll timeout response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int32\_t bt\_mesh\_cfg\_cli\_timeout\_get(void)
    :   Get the current transmission timeout value.

        Returns:
        :   The configured transmission timeout in milliseconds.

    void bt\_mesh\_cfg\_cli\_timeout\_set(int32\_t timeout)
    :   Set the transmission timeout value.

        Parameters:
        :   - **timeout** – The new transmission timeout.

    int bt\_mesh\_comp\_p0\_get(struct [bt\_mesh\_comp\_p0](#c.bt_mesh_comp_p0) \*comp, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Create a composition data page 0 representation from a buffer.

        The composition data page object will take ownership over the buffer, which should not be manipulated directly after this call.

        This function can be used in combination with [bt\_mesh\_cfg\_cli\_comp\_data\_get](#group__bt__mesh__cfg__cli_1ga36259e9c811a8f1a21d642739cf297df) to read out composition data page 0 from other devices:

        ```text
        NET_BUF_SIMPLE_DEFINE(buf, BT_MESH_RX_SDU_MAX);
        struct bt_mesh_comp_p0 comp;

        err = bt_mesh_cfg_cli_comp_data_get(net_idx, addr, 0, &page, &buf);
        if (!err) {
                bt_mesh_comp_p0_get(&comp, &buf);
        }
        ```

        Parameters:
        :   - **buf** – Network buffer containing composition data.
            - **comp** – Composition data structure to fill.

        Returns:
        :   0 on success, or (negative) error code on failure.

    struct [bt\_mesh\_comp\_p0\_elem](#c.bt_mesh_comp_p0_elem) \*bt\_mesh\_comp\_p0\_elem\_pull(const struct [bt\_mesh\_comp\_p0](#c.bt_mesh_comp_p0) \*comp, struct [bt\_mesh\_comp\_p0\_elem](#c.bt_mesh_comp_p0_elem) \*elem)
    :   Pull a composition data page 0 element from a composition data page 0 instance.

        Each call to this function will pull out a new element from the composition data page, until all elements have been pulled.

        Parameters:
        :   - **comp** – Composition data page
            - **elem** – Element to fill.

        Returns:
        :   A pointer to `elem` on success, or NULL if no more elements could be pulled.

    uint16\_t bt\_mesh\_comp\_p0\_elem\_mod(struct [bt\_mesh\_comp\_p0\_elem](#c.bt_mesh_comp_p0_elem) \*elem, int idx)
    :   Get a SIG model from the given composition data page 0 element.

        Parameters:
        :   - **elem** – Element to read the model from.
            - **idx** – Index of the SIG model to read.

        Returns:
        :   The Model ID of the SIG model at the given index, or 0xffff if the index is out of bounds.

    struct [bt\_mesh\_mod\_id\_vnd](access.md#c.bt_mesh_mod_id_vnd "bt_mesh_mod_id_vnd") bt\_mesh\_comp\_p0\_elem\_mod\_vnd(struct [bt\_mesh\_comp\_p0\_elem](#c.bt_mesh_comp_p0_elem) \*elem, int idx)
    :   Get a vendor model from the given composition data page 0 element.

        Parameters:
        :   - **elem** – Element to read the model from.
            - **idx** – Index of the vendor model to read.

        Returns:
        :   The model ID of the vendor model at the given index, or {0xffff, 0xffff} if the index is out of bounds.

    struct [bt\_mesh\_comp\_p1\_elem](#c.bt_mesh_comp_p1_elem) \*bt\_mesh\_comp\_p1\_elem\_pull(struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf, struct [bt\_mesh\_comp\_p1\_elem](#c.bt_mesh_comp_p1_elem) \*elem)
    :   Pull a Composition Data Page 1 Element from a composition data page 1 instance.

        Each call to this function will pull out a new element from the composition data page, until all elements have been pulled.

        Parameters:
        :   - **buf** – Composition data page 1 buffer
            - **elem** – Element to fill.

        Returns:
        :   A pointer to `elem` on success, or NULL if no more elements could be pulled.

    struct [bt\_mesh\_comp\_p1\_model\_item](#c.bt_mesh_comp_p1_model_item) \*bt\_mesh\_comp\_p1\_item\_pull(struct [bt\_mesh\_comp\_p1\_elem](#c.bt_mesh_comp_p1_elem) \*elem, struct [bt\_mesh\_comp\_p1\_model\_item](#c.bt_mesh_comp_p1_model_item) \*item)
    :   Pull a Composition Data Page 1 Model Item from a Composition Data Page 1 Element.

        Each call to this function will pull out a new item from the Composition Data Page 1 Element, until all items have been pulled.

        Parameters:
        :   - **elem** – Composition data page 1 Element
            - **item** – Model Item to fill.

        Returns:
        :   A pointer to `item` on success, or NULL if no more elements could be pulled.

    struct [bt\_mesh\_comp\_p1\_ext\_item](#c.bt_mesh_comp_p1_ext_item) \*bt\_mesh\_comp\_p1\_pull\_ext\_item(struct [bt\_mesh\_comp\_p1\_model\_item](#c.bt_mesh_comp_p1_model_item) \*item, struct [bt\_mesh\_comp\_p1\_ext\_item](#c.bt_mesh_comp_p1_ext_item) \*ext\_item)
    :   Pull Extended Model Item contained in Model Item.

        Each call to this function will pull out a new element from the Extended Model Item, until all elements have been pulled.

        Parameters:
        :   - **item** – Model Item to pull Extended Model Items from
            - **ext\_item** – Extended Model Item to fill

        Returns:
        :   A pointer to `ext_item` on success, or NULL if item could not be pulled

    struct [bt\_mesh\_comp\_p2\_record](#c.bt_mesh_comp_p2_record) \*bt\_mesh\_comp\_p2\_record\_pull(struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf, struct [bt\_mesh\_comp\_p2\_record](#c.bt_mesh_comp_p2_record) \*record)
    :   Pull a Composition Data Page 2 Record from a composition data page 2 instance.

        Each call to this function will pull out a new element from the composition data page, until all elements have been pulled.

        Parameters:
        :   - **buf** – Composition data page 2 buffer
            - **record** – Record to fill.

        Returns:
        :   A pointer to `record` on success, or NULL if no more elements could be pulled.

    int bt\_mesh\_key\_idx\_unpack\_list(struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf, uint16\_t \*dst\_arr, size\_t \*dst\_cnt)
    :   Unpack a list of key index entries from a buffer.

        On success, `dst_cnt` is set to the amount of unpacked key index entries.

        Parameters:
        :   - **buf** – Message buffer containing encoded AppKey or NetKey Indexes.
            - **dst\_arr** – Destination array for the unpacked list.
            - **dst\_cnt** – Size of the destination array.

        Returns:
        :   0 on success.

        Returns:
        :   -EMSGSIZE if dst\_arr size is to small to parse full message.

    struct bt\_mesh\_cfg\_cli\_cb
    :   *#include <cfg\_cli.h>*

        Mesh Configuration Client Status messages callback.

        Public Members

        void (\*comp\_data)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t page, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Optional callback for Composition data messages.

            Handles received Composition data messages from a server.

            Note

            For decoding `buf`, please refer to [bt\_mesh\_comp\_p0\_get](#group__bt__mesh__cfg__cli_1ga1f79d98273a984f1c49b4d5dd5bf8d30) and [bt\_mesh\_comp\_p1\_elem\_pull](#group__bt__mesh__cfg__cli_1gae9a19b089d898af914ea5c287aca8fba).

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param page:
            :   Composition data page.

            Param buf:
            :   Composition data buffer.

        void (\*mod\_pub\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](#c.bt_mesh_cfg_cli_mod_pub) \*pub)
        :   Optional callback for Model Pub status messages.

            Handles received Model Pub status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status code for the message.

            Param elem\_addr:
            :   Address of the element.

            Param mod\_id:
            :   Model ID.

            Param cid:
            :   Company ID.

            Param pub:
            :   Publication configuration parameters.

        void (\*mod\_sub\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t sub\_addr, uint32\_t mod\_id)
        :   Optional callback for Model Sub Status messages.

            Handles received Model Sub Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

            Param elem\_addr:
            :   The unicast address of the element.

            Param sub\_addr:
            :   The sub address.

            Param mod\_id:
            :   The model ID within the element.

        void (\*mod\_sub\_list)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Optional callback for Model Sub list messages.

            Handles received Model Sub list messages from a server.

            Note

            The `buf` parameter should be decoded using [net\_buf\_simple\_pull\_le16](../../../networking/api/net_buf.md#group__net__buf_1gad59d180ae81b55f6d618565a37d25dba) in iteration, as long as `buf->len` is greater than or equal to 2.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status code for the message.

            Param elem\_addr:
            :   Address of the element.

            Param mod\_id:
            :   Model ID.

            Param cid:
            :   Company ID.

            Param buf:
            :   Message buffer containing subscription addresses.

        void (\*node\_reset\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr)
        :   Optional callback for Node Reset Status messages.

            Handles received Node Reset Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

        void (\*beacon\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status)
        :   Optional callback for Beacon Status messages.

            Handles received Beacon Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

        void (\*ttl\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status)
        :   Optional callback for Default TTL Status messages.

            Handles received Default TTL Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

        void (\*friend\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status)
        :   Optional callback for Friend Status messages.

            Handles received Friend Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

        void (\*gatt\_proxy\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status)
        :   Optional callback for GATT Proxy Status messages.

            Handles received GATT Proxy Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

        void (\*network\_transmit\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status)
        :   Optional callback for Network Transmit Status messages.

            Handles received Network Transmit Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

        void (\*relay\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint8\_t transmit)
        :   Optional callback for Relay Status messages.

            Handles received Relay Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

            Param transmit:
            :   The relay retransmit count and interval steps.

        void (\*net\_key\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx)
        :   Optional callback for NetKey Status messages.

            Handles received NetKey Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

            Param net\_idx:
            :   The index of the NetKey.

        void (\*net\_key\_list)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Optional callback for Netkey list messages.

            Handles received Netkey list messages from a server.

            Note

            The `buf` parameter should be decoded using the [bt\_mesh\_key\_idx\_unpack\_list](#group__bt__mesh__cfg__cli_1gaa411ab7db2e71a114a8108eaec9ca12c) helper function.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param buf:
            :   Message buffer containing key indexes.

        void (\*app\_key\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, uint16\_t app\_idx)
        :   Optional callback for AppKey Status messages.

            Handles received AppKey Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

            Param net\_idx:
            :   The index of the NetKey.

            Param app\_idx:
            :   The index of the AppKey.

        void (\*app\_key\_list)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Optional callback for Appkey list messages.

            Handles received Appkey list messages from a server.

            Note

            The `buf` parameter should be decoded using the [bt\_mesh\_key\_idx\_unpack\_list](#group__bt__mesh__cfg__cli_1gaa411ab7db2e71a114a8108eaec9ca12c) helper function.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status code for the message.

            Param net\_idx:
            :   The index of the NetKey.

            Param buf:
            :   Message buffer containing key indexes.

        void (\*mod\_app\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t app\_idx, uint32\_t mod\_id)
        :   Optional callback for Model App Status messages.

            Handles received Model App Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

            Param elem\_addr:
            :   The unicast address of the element.

            Param app\_idx:
            :   The sub address.

            Param mod\_id:
            :   The model ID within the element.

        void (\*mod\_app\_list)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
        :   Optional callback for Model App list messages.

            Handles received Model App list messages from a server.

            Note

            The `buf` parameter should be decoded using the [bt\_mesh\_key\_idx\_unpack\_list](#group__bt__mesh__cfg__cli_1gaa411ab7db2e71a114a8108eaec9ca12c) helper function.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status code for the message.

            Param elem\_addr:
            :   Address of the element.

            Param mod\_id:
            :   Model ID.

            Param cid:
            :   Company ID.

            Param buf:
            :   Message buffer containing key indexes.

        void (\*node\_identity\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, uint8\_t identity)
        :   Optional callback for Node Identity Status messages.

            Handles received Node Identity Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status Code for requesting message.

            Param net\_idx:
            :   The index of the NetKey.

            Param identity:
            :   The node identity state.

        void (\*lpn\_timeout\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint16\_t elem\_addr, uint32\_t timeout)
        :   Optional callback for LPN PollTimeout Status messages.

            Handles received LPN PollTimeout Status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param elem\_addr:
            :   The unicast address of the LPN.

            Param timeout:
            :   Current value of PollTimeout timer of the LPN.

        void (\*krp\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, uint8\_t phase)
        :   Optional callback for Key Refresh Phase status messages.

            Handles received Key Refresh Phase status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status code for the message.

            Param net\_idx:
            :   The index of the NetKey.

            Param phase:
            :   Phase of the KRP.

        void (\*hb\_pub\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, struct [bt\_mesh\_cfg\_cli\_hb\_pub](#c.bt_mesh_cfg_cli_hb_pub) \*pub)
        :   Optional callback for Heartbeat pub status messages.

            Handles received Heartbeat pub status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status code for the message.

            Param pub:
            :   HB publication configuration parameters.

        void (\*hb\_sub\_status)(struct [bt\_mesh\_cfg\_cli](#c.bt_mesh_cfg_cli) \*cli, uint16\_t addr, uint8\_t status, struct [bt\_mesh\_cfg\_cli\_hb\_sub](#c.bt_mesh_cfg_cli_hb_sub) \*sub)
        :   Optional callback for Heartbeat Sub status messages.

            Handles received Heartbeat Sub status messages from a server.

            Param cli:
            :   Client that received the status message.

            Param addr:
            :   Address of the sender.

            Param status:
            :   Status code for the message.

            Param sub:
            :   HB subscription configuration parameters.

    struct bt\_mesh\_cfg\_cli
    :   *#include <cfg\_cli.h>*

        Mesh Configuration Client Model Context.

        Public Members

        const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model
        :   Composition data model entry pointer.

        const struct [bt\_mesh\_cfg\_cli\_cb](#c.bt_mesh_cfg_cli_cb) \*cb
        :   Optional callback for Mesh Configuration Client Status messages.

    struct bt\_mesh\_cfg\_cli\_mod\_pub
    :   *#include <cfg\_cli.h>*

        Model publication configuration parameters.

        Public Members

        uint16\_t addr
        :   Publication destination address.

        const uint8\_t \*uuid
        :   Virtual address UUID, or NULL if this is not a virtual address.

        uint16\_t app\_idx
        :   Application index to publish with.

        bool cred\_flag
        :   Friendship credential flag.

        uint8\_t ttl
        :   Time To Live to publish with.

        uint8\_t period
        :   Encoded publish period.

            See also

            [BT\_MESH\_PUB\_PERIOD\_100MS](#group__bt__mesh__cfg__cli_1gab542c707fb5bad0a15088fefda775a42), [BT\_MESH\_PUB\_PERIOD\_SEC](#group__bt__mesh__cfg__cli_1ga29435e527a73ff6e19339b773c8eb79e), [BT\_MESH\_PUB\_PERIOD\_10SEC](#group__bt__mesh__cfg__cli_1ga654204077adaa08259d1afbfe92e070e), [BT\_MESH\_PUB\_PERIOD\_10MIN](#group__bt__mesh__cfg__cli_1ga36c37f644ee39ad91b6167f68c806b7e)

        uint8\_t transmit
        :   Encoded transmit parameters.

            See also

            [BT\_MESH\_TRANSMIT](access.md#group__bt__mesh__access_1gaff82bf652232fbce71c31f38a10577a9)

    struct bt\_mesh\_cfg\_cli\_hb\_sub
    :   *#include <cfg\_cli.h>*

        Heartbeat subscription configuration parameters.

        Public Members

        uint16\_t src
        :   Source address to receive Heartbeat messages from.

        uint16\_t dst
        :   Destination address to receive Heartbeat messages on.

        uint8\_t period
        :   Logarithmic subscription period to keep listening for.

            The decoded subscription period is (1 << (period - 1)) seconds, or 0 seconds if period is 0.

        uint8\_t count
        :   Logarithmic Heartbeat subscription receive count.

            The decoded Heartbeat count is (1 << (count - 1)) if count is between 1 and 0xfe, 0 if count is 0 and 0xffff if count is 0xff.

            Ignored in Heartbeat subscription set.

        uint8\_t min
        :   Minimum hops in received messages, ie the shortest registered path from the publishing node to the subscribing node.

            A Heartbeat received from an immediate neighbor has hop count = 1.

            Ignored in Heartbeat subscription set.

        uint8\_t max
        :   Maximum hops in received messages, ie the longest registered path from the publishing node to the subscribing node.

            A Heartbeat received from an immediate neighbor has hop count = 1.

            Ignored in Heartbeat subscription set.

    struct bt\_mesh\_cfg\_cli\_hb\_pub
    :   *#include <cfg\_cli.h>*

        Heartbeat publication configuration parameters.

        Public Members

        uint16\_t dst
        :   Heartbeat destination address.

        uint8\_t count
        :   Logarithmic Heartbeat count.

            Decoded as (1 << (count - 1)) if count is between 1 and 0x11, 0 if count is 0, or “indefinitely” if count is 0xff.

            When used in Heartbeat publication set, this parameter denotes the number of Heartbeat messages to send.

            When returned from Heartbeat publication get, this parameter denotes the number of Heartbeat messages remaining to be sent.

        uint8\_t period
        :   Logarithmic Heartbeat publication transmit interval in seconds.

            Decoded as (1 << (period - 1)) if period is between 1 and 0x11. If period is 0, Heartbeat publication is disabled.

        uint8\_t ttl
        :   Publication message Time To Live value.

        uint16\_t feat
        :   Bitmap of features that trigger Heartbeat publications.

            Legal values are [BT\_MESH\_FEAT\_RELAY](core.md#group__bt__mesh_1gac588eefe83db94784a420ce063f02b55), [BT\_MESH\_FEAT\_PROXY](core.md#group__bt__mesh_1gaee648ce202316c56d4d588cb0ad5aeb4), [BT\_MESH\_FEAT\_FRIEND](core.md#group__bt__mesh_1ga8f27086b3bc3c4a6e14621836f9f8e80) and [BT\_MESH\_FEAT\_LOW\_POWER](core.md#group__bt__mesh_1gaad71a36c82b4e4d3fa334ecff5cc0171)

        uint16\_t net\_idx
        :   Network index to publish with.

    struct bt\_mesh\_comp\_p0
    :   *#include <cfg\_cli.h>*

        Parsed Composition data page 0 representation.

        Should be pulled from the return buffer passed to [bt\_mesh\_cfg\_cli\_comp\_data\_get](#group__bt__mesh__cfg__cli_1ga36259e9c811a8f1a21d642739cf297df) using [bt\_mesh\_comp\_p0\_get](#group__bt__mesh__cfg__cli_1ga1f79d98273a984f1c49b4d5dd5bf8d30).

        Public Members

        uint16\_t cid
        :   Company ID.

        uint16\_t pid
        :   Product ID.

        uint16\_t vid
        :   Version ID.

        uint16\_t crpl
        :   Replay protection list size.

        uint16\_t feat
        :   Supported features, see [BT\_MESH\_FEAT\_SUPPORTED](core.md#group__bt__mesh_1gac337fd8688d70e862974e010ad42a11b).

    struct bt\_mesh\_comp\_p0\_elem
    :   *#include <cfg\_cli.h>*

        Composition data page 0 element representation.

        Public Members

        uint16\_t loc
        :   Element location.

        size\_t nsig
        :   The number of SIG models in this element.

        size\_t nvnd
        :   The number of vendor models in this element.

    struct bt\_mesh\_comp\_p1\_elem
    :   *#include <cfg\_cli.h>*

        Composition data page 1 element representation.

        Public Members

        size\_t nsig
        :   The number of SIG models in this element.

        size\_t nvnd
        :   The number of vendor models in this element.

    struct bt\_mesh\_comp\_p1\_model\_item
    :   *#include <cfg\_cli.h>*

        Composition data page 1 model item representation.

        Public Members

        bool cor\_present
        :   Corresponding\_Group\_ID field indicator.

        bool format
        :   Determines the format of Extended Model Item.

        uint8\_t ext\_item\_cnt
        :   Number of items in Extended Model Items.

        uint8\_t cor\_id
        :   Buffer containing Extended Model Items.

            If cor\_present is set to 1 it starts with Corresponding\_Group\_ID

    struct bt\_mesh\_comp\_p1\_item\_short
    :   *#include <cfg\_cli.h>*

        Extended Model Item in short representation.

        Public Members

        uint8\_t elem\_offset
        :   Element address modifier.

        uint8\_t mod\_item\_idx
        :   Model Index.

    struct bt\_mesh\_comp\_p1\_item\_long
    :   *#include <cfg\_cli.h>*

        Extended Model Item in long representation.

        Public Members

        uint8\_t elem\_offset
        :   Element address modifier.

        uint8\_t mod\_item\_idx
        :   Model Index.

    struct bt\_mesh\_comp\_p1\_ext\_item
    :   *#include <cfg\_cli.h>*

        Extended Model Item.

        Public Members

        struct [bt\_mesh\_comp\_p1\_item\_short](#c.bt_mesh_comp_p1_item_short) short\_item
        :   Item in short representation.

        struct [bt\_mesh\_comp\_p1\_item\_long](#c.bt_mesh_comp_p1_item_long) long\_item
        :   Item in long representation.

    struct bt\_mesh\_comp\_p2\_record
    :   *#include <cfg\_cli.h>*

        Composition data page 2 record parsing structure.

        Public Members

        uint16\_t id
        :   Mesh profile ID.

        uint8\_t x
        :   Major version.

        uint8\_t y
        :   Minor version.

        uint8\_t z
        :   Z version.

        struct [bt\_mesh\_comp\_p2\_record](#c.bt_mesh_comp_p2_record).[anonymous] version
        :   Mesh Profile Version.

        struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*elem\_buf
        :   Element offset buffer.

        struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*data\_buf
        :   Additional data buffer.
