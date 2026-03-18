---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/deprecated.html
original_path: doxygen/html/deprecated.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Deprecated List

Global [bt\_gatt\_subscribe\_params::write](structbt__gatt__subscribe__params.md#a1cedb0e0067c8648c603296a63d2e3ee)

Global [CBPRINTF\_PACKAGE\_COPY\_KEEP\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga66d65a0f8f9c32440cb7b92a37d0e248)
:   Use [CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga582ebea3e0d18285840bf277c5382da6 "CBPRINTF_PACKAGE_CONVERT_KEEP_RO_STR") instead.

Global [CBPRINTF\_PACKAGE\_COPY\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga3da36360cc579adbd5e991addf4c3fc6)
:   Use [CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga9802b700abd5d3cd7cef0e0cbcceb3e7 "CBPRINTF_PACKAGE_CONVERT_RO_STR") instead.

Global [CBPRINTF\_PACKAGE\_COPY\_RW\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga1b3b798a2a208276ddc3931b06064323)
:   Use [CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga983c65ed8afb356a29fa2736f9de7b39 "CBPRINTF_PACKAGE_CONVERT_RW_STR") instead.

Global [ceiling\_fraction](group__sys-util.md#gaad408461e7ab356650bcd5c83bc0ed39) (numerator, divider)
:   Use [DIV\_ROUND\_UP()](group__sys-util.md#gae664e7492e37d324831caf2321ddda37 "Divide and round up.") instead.

Global [IEEE802154\_HW\_SLEEP\_TO\_TX](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071)
:   Drivers and L2 SHALL not introduce additional references to this capability and remove existing ones as outlined in #63670.

Global [K\_THREAD\_STACK\_MEMBER](group__thread__stack__api.md#ga753188e7f124f0ee03ed0fa1dad8ecfb) (sym, size)
:   This is now deprecated, as stacks defined in this way are not usable from user mode. Use K\_KERNEL\_STACK\_MEMBER.

Global [lwm2m\_engine\_create\_obj\_inst](group__lwm2m__api.md#ga32f393a9e302f1f60839fd2147ebd7e9) (const char \*pathstr)
:   Use lwm2m\_create\_obj\_inst() instead.

Global [lwm2m\_engine\_create\_res\_inst](group__lwm2m__api.md#ga64b0427f36b6d2d2f8af8cc2e35cdb89) (const char \*pathstr)
:   Use [lwm2m\_create\_res\_inst()](group__lwm2m__api.md#gac69c40474180fe14c3761185b2db1c0c "Create a resource instance.") instead.

Global [lwm2m\_engine\_delete\_obj\_inst](group__lwm2m__api.md#ga3849e960b54bcb089ac00476da8fb430) (const char \*pathstr)
:   Use lwm2m\_delete\_obj\_inst() instead.

Global [lwm2m\_engine\_delete\_res\_inst](group__lwm2m__api.md#gac188cd5fdd226dd105d73a4e391c601b) (const char \*pathstr)
:   Use [lwm2m\_delete\_res\_inst()](group__lwm2m__api.md#gacfeb63db0423e6730ffaa826a87eb262 "Delete a resource instance.") instead.

Global [lwm2m\_engine\_enable\_cache](group__lwm2m__api.md#gaea2d9f740dd6d6152143be0360f19308) (char const \*resource\_path, struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md "LwM2M Time series data structure.") \*data\_cache, size\_t cache\_len)
:   Use lwm2m\_enable\_cache instead

Global [lwm2m\_engine\_get\_bool](group__lwm2m__api.md#ga606e281a1146f930d7c0675d5881c7d6) (const char \*pathstr, bool \*value)
:   Use [lwm2m\_get\_bool()](group__lwm2m__api.md#gafdc72844ce0ca417e297d76288155aa4 "Get resource (instance) value (bool).") instead.

Global [lwm2m\_engine\_get\_float](group__lwm2m__api.md#ga0a272643082347fe6044bddbd7e5cebf) (const char \*pathstr, double \*buf)
:   Use [lwm2m\_get\_f64()](group__lwm2m__api.md#ga03b72e96a67fcbf85feb5bf0b9df81ce "Get resource (instance) value (double).") instead.

Global [lwm2m\_engine\_get\_objlnk](group__lwm2m__api.md#gaf4b23e412fcff5f2838f3e232a3cd224) (const char \*pathstr, struct [lwm2m\_objlnk](structlwm2m__objlnk.md "LWM2M Objlnk resource type structure.") \*buf)
:   Use [lwm2m\_get\_objlnk()](group__lwm2m__api.md#ga4de941c36cf678e12da6e05c378a92e5 "Get resource (instance) value (Objlnk).") instead.

Global [lwm2m\_engine\_get\_opaque](group__lwm2m__api.md#ga3439a579648c15bfe8883337c4618095) (const char \*pathstr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen)
:   Use [lwm2m\_get\_opaque()](group__lwm2m__api.md#gae245a9a1d9456af7e6283b1074944606 "Get resource (instance) value (opaque buffer).") instead.

Global [lwm2m\_engine\_get\_res\_buf](group__lwm2m__api.md#gaff5e10bc0fa34c1fe72a0b4e1ed2bc39) (const char \*pathstr, void \*\*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags)
:   Use [lwm2m\_get\_res\_buf()](group__lwm2m__api.md#gac0b6669d8a19b03eb8b08cbbcdb0c192 "Get data buffer for a resource.") instead.

Global [lwm2m\_engine\_get\_res\_data](group__lwm2m__api.md#ga630079a8d2f2acae1c313297cfdbada9) (const char \*pathstr, void \*\*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags)
:   Use [lwm2m\_get\_res\_buf()](group__lwm2m__api.md#gac0b6669d8a19b03eb8b08cbbcdb0c192 "Get data buffer for a resource.") as it can tell you the size of the buffer as well.

Global [lwm2m\_engine\_get\_s16](group__lwm2m__api.md#ga96f29e6d897b96fedc7f3e19bd906f7c) (const char \*pathstr, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value)
:   Use [lwm2m\_get\_s16()](group__lwm2m__api.md#ga2426db6720b3f3e15e63022cabae5ece "Get resource (instance) value (s16).") instead.

Global [lwm2m\_engine\_get\_s32](group__lwm2m__api.md#ga40895289c1c8b778b6bf30d444dda63a) (const char \*pathstr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value)
:   Use [lwm2m\_get\_s32()](group__lwm2m__api.md#ga99d7189efa25881dbcddd99e2a795f1b "Get resource (instance) value (s32).") instead.

Global [lwm2m\_engine\_get\_s64](group__lwm2m__api.md#ga7ad1a482074d033ad1def72882efd245) (const char \*pathstr, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*value)
:   Use [lwm2m\_get\_s64()](group__lwm2m__api.md#gaaffe06ca9ee5302fb6e26164f250653e "Get resource (instance) value (s64).") instead.

Global [lwm2m\_engine\_get\_s8](group__lwm2m__api.md#ga701d36c7b7a63c8214bfa30c0c19c946) (const char \*pathstr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*value)
:   Use [lwm2m\_get\_s8()](group__lwm2m__api.md#ga12817bfbf0a0cbb742568ee974a1c337 "Get resource (instance) value (s8).") instead.

Global [lwm2m\_engine\_get\_string](group__lwm2m__api.md#ga72e27dfaf0881561245d01d6f800f0dc) (const char \*pathstr, void \*str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen)
:   Use [lwm2m\_get\_string()](group__lwm2m__api.md#ga20fc58b25468bf309175db59d67b820b "Get resource (instance) value (string).") instead.

Global [lwm2m\_engine\_get\_time](group__lwm2m__api.md#ga273fa47b65309b46aa1b73b224d0dfce) (const char \*pathstr, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*buf)
:   Use [lwm2m\_get\_time()](group__lwm2m__api.md#ga2e1d41866b5ea35c5aa29bca9bb43812 "Get resource (instance) value (Time).") instead.

Global [lwm2m\_engine\_get\_u16](group__lwm2m__api.md#ga68986109d78b60f83f9cd85742ed80fb) (const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value)
:   Use [lwm2m\_get\_u16()](group__lwm2m__api.md#ga1b96848f96bdab9939bb2619d3e1059b "Get resource (instance) value (u16).") instead.

Global [lwm2m\_engine\_get\_u32](group__lwm2m__api.md#gafddb717b3f43619e03a240660f65eb03) (const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value)
:   Use [lwm2m\_get\_u32()](group__lwm2m__api.md#ga0bc84cb39a7a537925ec7d62e54b8b48 "Get resource (instance) value (u32).") instead.

Global [lwm2m\_engine\_get\_u64](group__lwm2m__api.md#ga8d9068217afe09b0930996e5796b8aac) (const char \*pathstr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)
:   Use [lwm2m\_get\_u64()](group__lwm2m__api.md#ga831d229d9a4b983223dff626bbde7a66 "Get resource (instance) value (u64).") instead.

Global [lwm2m\_engine\_get\_u8](group__lwm2m__api.md#ga50ee578c777c7b8a1b0fbe028c8342ec) (const char \*pathstr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value)
:   Use [lwm2m\_get\_u8()](group__lwm2m__api.md#gac56e804962e529799c771d81ac1fd027 "Get resource (instance) value (u8).") instead.

Global [lwm2m\_engine\_path\_is\_observed](group__lwm2m__api.md#ga07149d4b624a7294f4508df8c1681b1b) (const char \*pathstr)
:   Use [lwm2m\_path\_is\_observed()](group__lwm2m__api.md#ga1065c729d5caa8ca13de7766fce77953 "Check whether a path is observed.") instead.

Global [lwm2m\_engine\_register\_create\_callback](group__lwm2m__api.md#gaa198bfb55f98183cbd33169468ae0bcc) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf "Asynchronous event notification callback.") cb)
:   Use lwm2m\_register\_create\_callback instead.

Global [lwm2m\_engine\_register\_delete\_callback](group__lwm2m__api.md#ga6a5dfdd29055bed245bf16ecc5829f95) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf "Asynchronous event notification callback.") cb)
:   Use lwm2m\_register\_delete\_callback instead

Global [lwm2m\_engine\_register\_exec\_callback](group__lwm2m__api.md#gad213063b7e68bd7b4f3ce3de3736a237) (const char \*pathstr, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe "Asynchronous execute notification callback.") cb)
:   Use [lwm2m\_register\_exec\_callback()](group__lwm2m__api.md#ga29cc5cdd697e94d7379b1fb178487916 "Set resource execute event callback.") instead.

Global [lwm2m\_engine\_register\_post\_write\_callback](group__lwm2m__api.md#ga5c43bcdb0575f8c56354d6b4e30641a3) (const char \*pathstr, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9 "Asynchronous callback when data has been set to a resource buffer.") cb)
:   Use [lwm2m\_register\_post\_write\_callback()](group__lwm2m__api.md#ga3dd8b38e797173dae902404fb5b7a3f4 "Set resource (instance) post-write callback.") instead.

Global [lwm2m\_engine\_register\_pre\_write\_callback](group__lwm2m__api.md#ga1354bc59163db5b3435e8e86c8feafd8) (const char \*pathstr, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384 "Asynchronous callback to get a resource buffer and length.") cb)
:   Use [lwm2m\_register\_pre\_write\_callback()](group__lwm2m__api.md#ga6f775837e07ba9b0032be8917a593e16 "Set resource (instance) pre-write callback.") instead.

Global [lwm2m\_engine\_register\_read\_callback](group__lwm2m__api.md#ga21d15060cce1c039a11106d71d681f4c) (const char \*pathstr, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384 "Asynchronous callback to get a resource buffer and length.") cb)
:   Use [lwm2m\_register\_read\_callback()](group__lwm2m__api.md#gaf33bd6a527b6d399f3d92b666ac77dfb "Set resource (instance) read callback.") instead.

Global [lwm2m\_engine\_register\_validate\_callback](group__lwm2m__api.md#gac1c92e1ee3a804b325aacfe116bad096) (const char \*pathstr, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9 "Asynchronous callback when data has been set to a resource buffer.") cb)
:   Use [lwm2m\_register\_validate\_callback()](group__lwm2m__api.md#gad6e5fd4815f409ad59ad631b03199333 "Set resource (instance) validation callback.") instead.

Global [lwm2m\_engine\_send](group__lwm2m__api.md#ga5a0eed7bf3593f698194e5e047b07fa8) (struct [lwm2m\_ctx](structlwm2m__ctx.md "LwM2M context structure to maintain information for a single LwM2M connection.") \*ctx, char const \*path\_list[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, bool confirmation\_request)
:   Use [lwm2m\_send\_cb()](group__lwm2m__api.md#ga026cc9288d2de17ec557e08b9b987ebc) instead.

Global [lwm2m\_engine\_set\_bool](group__lwm2m__api.md#ga8c82346313a9bf1234f72d71a5db34f5) (const char \*pathstr, bool value)
:   Use [lwm2m\_set\_bool()](group__lwm2m__api.md#ga9ef21d06bef8a97b7666c0aa7fa753b4 "Set resource (instance) value (bool).") instead.

Global [lwm2m\_engine\_set\_float](group__lwm2m__api.md#gae85eb5da495b7d42b10cf01c0d826632) (const char \*pathstr, const double \*value)
:   Use [lwm2m\_set\_f64()](group__lwm2m__api.md#ga3386d3f2ad8d9713fc2283ed6921c2fc "Set resource (instance) value (double).") instead.

Global [lwm2m\_engine\_set\_objlnk](group__lwm2m__api.md#gada5007c34ce2ee72017065b32f1cee58) (const char \*pathstr, const struct [lwm2m\_objlnk](structlwm2m__objlnk.md "LWM2M Objlnk resource type structure.") \*value)
:   Use [lwm2m\_set\_objlnk()](group__lwm2m__api.md#ga04a18bd8a4eeea41a47803c16567d67b "Set resource (instance) value (Objlnk).") instead.

Global [lwm2m\_engine\_set\_opaque](group__lwm2m__api.md#ga2a891e26440f732b77ab90b979c8cb49) (const char \*pathstr, const char \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len)
:   Use [lwm2m\_set\_opaque()](group__lwm2m__api.md#gaaef33bdf3f48fd91abdb50db4d5460f9 "Set resource (instance) value (opaque buffer).") instead.

Global [lwm2m\_engine\_set\_res\_buf](group__lwm2m__api.md#ga66bdc3f3a4d0e88b036c9704abfbcafc) (const char \*pathstr, void \*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags)
:   Use [lwm2m\_set\_res\_buf()](group__lwm2m__api.md#ga56a2aecd38baedb5dc17258610c4780d "Set data buffer for a resource.") instead.

Global [lwm2m\_engine\_set\_res\_data](group__lwm2m__api.md#gabf56a29aec75675099df2d45ca802718) (const char \*pathstr, void \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags)
:   Use [lwm2m\_set\_res\_buf()](group__lwm2m__api.md#ga56a2aecd38baedb5dc17258610c4780d "Set data buffer for a resource.") instead, so you can define buffer size and data size separately.

Global [lwm2m\_engine\_set\_res\_data\_len](group__lwm2m__api.md#ga87833da93894dc5df45b91dfaebf3f91) (const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len)
:   Use [lwm2m\_set\_res\_data\_len()](group__lwm2m__api.md#ga0f2b115d231bea6622135d72b51f55ca "Update data size for a resource.") instead.

Global [lwm2m\_engine\_set\_s16](group__lwm2m__api.md#ga1dd4952af0029c94a71f74734ae3a16c) (const char \*pathstr, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) value)
:   Use [lwm2m\_set\_s16()](group__lwm2m__api.md#gad548ffedcb8328b23eb32476a97be6ee "Set resource (instance) value (s16).") instead.

Global [lwm2m\_engine\_set\_s32](group__lwm2m__api.md#ga4f45dc38b5e6a55633474ff5d5447ecb) (const char \*pathstr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value)
:   Use [lwm2m\_set\_s32()](group__lwm2m__api.md#ga327e086959fc5649a5ef14f1f2943e88 "Set resource (instance) value (s32).") instead.

Global [lwm2m\_engine\_set\_s64](group__lwm2m__api.md#ga11619cc0907010018217b8d67e9e9f7e) (const char \*pathstr, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value)
:   Use [lwm2m\_set\_s64()](group__lwm2m__api.md#ga18fcee379640c0dda32d6e3d14827260 "Set resource (instance) value (s64).") instead.

Global [lwm2m\_engine\_set\_s8](group__lwm2m__api.md#gae665c8bb81c0aef3b960b087ff0f97f8) (const char \*pathstr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) value)
:   Use [lwm2m\_set\_s8()](group__lwm2m__api.md#ga37261a4b9e54eab3d1d855a084d082aa "Set resource (instance) value (s8).") instead.

Global [lwm2m\_engine\_set\_string](group__lwm2m__api.md#ga28911733660e7ce2f2f73c8eeb87de59) (const char \*pathstr, const char \*data\_ptr)
:   Use [lwm2m\_set\_string()](group__lwm2m__api.md#ga7217f33bf705011d91ba66c86a4d5747 "Set resource (instance) value (string).") instead.

Global [lwm2m\_engine\_set\_time](group__lwm2m__api.md#gad3621c4a9ddfdc2a9e8fe2df058aefd7) (const char \*pathstr, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) value)
:   Use [lwm2m\_set\_time()](group__lwm2m__api.md#ga7194ad24842e35130d8af7f5104c0844 "Set resource (instance) value (Time).") instead.

Global [lwm2m\_engine\_set\_u16](group__lwm2m__api.md#ga4fcea78d9506822ee76df465cf71ffdf) (const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value)
:   Use [lwm2m\_set\_u16()](group__lwm2m__api.md#ga1f06bb65571efee18db5d061f95399c3 "Set resource (instance) value (u16).") instead.

Global [lwm2m\_engine\_set\_u32](group__lwm2m__api.md#ga326c722de4ecdcbc09adb52c83cf6400) (const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)
:   Use [lwm2m\_set\_u32()](group__lwm2m__api.md#ga9481e570b121404dc1be1ce23d904894 "Set resource (instance) value (u32).") instead.

Global [lwm2m\_engine\_set\_u64](group__lwm2m__api.md#ga7d04c579284369233156a0597f09ab83) (const char \*pathstr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value)
:   Use [lwm2m\_set\_u64()](group__lwm2m__api.md#ga8a751dc8384cc47f9c14d916e20ae19d "Set resource (instance) value (u64).") instead.

Global [lwm2m\_engine\_set\_u8](group__lwm2m__api.md#ga00a61b227bae53a70b0092bb94801ea8) (const char \*pathstr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)
:   Use [lwm2m\_set\_u8()](group__lwm2m__api.md#ga1aa3ff424b7190d0fbd9366626b2685c "Set resource (instance) value (u8).") instead.

Global [lwm2m\_engine\_update\_observer\_max\_period](group__lwm2m__api.md#gacb717ef5a36524e6f0f78b90cc803577) (struct [lwm2m\_ctx](structlwm2m__ctx.md "LwM2M context structure to maintain information for a single LwM2M connection.") \*client\_ctx, const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s)
:   Use [lwm2m\_update\_observer\_max\_period()](group__lwm2m__api.md#ga6acccbcd879901574aceab53a21800fc "Change an observer's pmax value.") instead.

Global [lwm2m\_engine\_update\_observer\_min\_period](group__lwm2m__api.md#ga489c8ea2eb89c7c6dc008002ab2ea836) (struct [lwm2m\_ctx](structlwm2m__ctx.md "LwM2M context structure to maintain information for a single LwM2M connection.") \*client\_ctx, const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s)
:   Use [lwm2m\_update\_observer\_min\_period()](group__lwm2m__api.md#gadd163806d70713d8349a9db484ba88bf "Change an observer's pmin value.") instead.

Global [lwm2m\_get\_u64](group__lwm2m__api.md#ga831d229d9a4b983223dff626bbde7a66) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md "LwM2M object path structure.") \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)
:   Unsigned 64bit value type does not exits. This is internally handled as a [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b). Use [lwm2m\_get\_s64()](group__lwm2m__api.md#gaaffe06ca9ee5302fb6e26164f250653e "Get resource (instance) value (s64).") instead.

Global [lwm2m\_send](group__lwm2m__api.md#gae6358ef4b4e3a1e342828ad9c429ff72) (struct [lwm2m\_ctx](structlwm2m__ctx.md "LwM2M context structure to maintain information for a single LwM2M connection.") \*ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md "LwM2M object path structure.") path\_list[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, bool confirmation\_request)
:   Use [lwm2m\_send\_cb()](group__lwm2m__api.md#ga026cc9288d2de17ec557e08b9b987ebc) instead.

Global [lwm2m\_set\_u64](group__lwm2m__api.md#ga8a751dc8384cc47f9c14d916e20ae19d) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md "LwM2M object path structure.") \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value)
:   Unsigned 64bit value type does not exits. This is internally handled as a [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b). Use [lwm2m\_set\_s64()](group__lwm2m__api.md#ga18fcee379640c0dda32d6e3d14827260 "Set resource (instance) value (s64).") instead.

Global [openthread\_set\_state\_changed\_cb](group__openthread.md#gad097b10683a67500744763fab9028450) (otStateChangedCallback cb)
:   Use [openthread\_state\_changed\_cb\_register()](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327 "Registers callbacks which will be called when certain configuration or state changes occur within Ope...") instead.

Global [pcie\_bdf\_lookup](group__pcie__host__interface.md#gaad76dbfd3d53d812db092e2029c65fea) ([pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04 "A unique PCI(e) identifier (vendor ID, device ID).") id)

Global [pcie\_probe](group__pcie__host__interface.md#ga38df5e6054de59f1bc21e89a2701e998) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb "A unique PCI(e) endpoint (bus, device, function).") bdf, [pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04 "A unique PCI(e) identifier (vendor ID, device ID).") id)

Global [PTHREAD\_BARRIER\_DEFINE](pthread_8h.md#af63f456fc30f008794402605b4e5ac9c) (name, count)
:   Use [pthread\_barrier\_init](pthread_8h.md#aecc6c99901aac517072970e153863296 "pthread_barrier_init") instead.

Global [PWM\_STM32\_COMPLEMENTARY](stm32__pwm_8h.md#ac73e020f7f8787beaa8ddf7871578c6f)
:   Use the PWM complementary [STM32\_PWM\_COMPLEMENTARY](stm32__pwm_8h.md#a8e4959803792254f90bb31e0454a4249 "PWM complementary output pin is enabled.") flag instead.

Global [smp\_add\_cmd\_ret](mgmt_2mcumgr_2smp_2smp_8h.md#abad955ba2e5e19b6f6443c8eed4f1760) (zcbor\_state\_t \*zse, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret)
:   Deprecated after Zephyr 3.4, use [smp\_add\_cmd\_err()](mgmt_2mcumgr_2smp_2smp_8h.md#a191eb8c8a5a531b158374a1071925ca7 "Appends an "err" response.") instead

Global [SPI\_DT\_SPEC\_GET](group__spi__interface.md#gaec6a8fde1c3ec6349a601a2d5f7af785) (node\_id, operation\_, delay\_)
:   Use [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403 "spi_is_ready_dt") instead.

Global [spi\_read\_async](group__spi__interface.md#ga5185c52f0c8e2e3419a16c6e24af55e1) (const struct device \*dev, const struct [spi\_config](structspi__config.md "SPI controller configuration structure.") \*config, const struct [spi\_buf\_set](structspi__buf__set.md "SPI buffer array structure.") \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig)
:   Use [spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5 "spi_read_signal") instead.

Global [spi\_transceive\_async](group__spi__interface.md#gacc26ab19d1211508691691308744350f) (const struct device \*dev, const struct [spi\_config](structspi__config.md "SPI controller configuration structure.") \*config, const struct [spi\_buf\_set](structspi__buf__set.md "SPI buffer array structure.") \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md "SPI buffer array structure.") \*rx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig)
:   Use [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc "spi_transceive_signal") instead.

Global [spi\_write\_async](group__spi__interface.md#ga37d17fa9ae3909529762c43f9409d0f0) (const struct device \*dev, const struct [spi\_config](structspi__config.md "SPI controller configuration structure.") \*config, const struct [spi\_buf\_set](structspi__buf__set.md "SPI buffer array structure.") \*tx\_bufs, struct [k\_poll\_signal](structk__poll__signal.md) \*sig)
:   Use [spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b "spi_write_signal") instead.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
