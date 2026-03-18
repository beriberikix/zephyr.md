---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/audio/media.html
original_path: connectivity/bluetooth/api/audio/media.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth Media

## API Reference

### Media Control Service

*group* Media Control Service (MCS)
:   Media Control Service (MCS).

    Definitions and types related to the Media Control Service and Media Control Profile specifications.

    **Since**
    :   3.0

    **Version**
    :   0.8.0

    Playback speeds

    The playback speed (s) is calculated by the value of 2 to the power of p divided by 64.

    All values from -128 to 127 allowed, only some examples defined.

    BT\_MCS\_PLAYBACK\_SPEED\_MIN
    :   Minimum playback speed, resulting in 25 % speed.

    BT\_MCS\_PLAYBACK\_SPEED\_QUARTER
    :   Quarter playback speed, resulting in 25 % speed.

    BT\_MCS\_PLAYBACK\_SPEED\_HALF
    :   Half playback speed, resulting in 50 % speed.

    BT\_MCS\_PLAYBACK\_SPEED\_UNITY
    :   Unity playback speed, resulting in 100 % speed.

    BT\_MCS\_PLAYBACK\_SPEED\_DOUBLE
    :   Double playback speed, resulting in 200 % speed.

    BT\_MCS\_PLAYBACK\_SPEED\_MAX
    :   Max playback speed, resulting in 395.7 % speed (nearly 400 %).

    Seeking speed

    The allowed values for seeking speed are the range -64 to -4 (endpoints included), the value 0, and the range 4 to 64 (endpoints included).

    BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MAX
    :   Maximum seeking speed - Can be negated.

    BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MIN
    :   Minimum seeking speed - Can be negated.

    BT\_MCS\_SEEKING\_SPEED\_FACTOR\_ZERO
    :   No seeking.

    Playing orders

    BT\_MCS\_PLAYING\_ORDER\_SINGLE\_ONCE
    :   A single track is played once; there is no next track.

    BT\_MCS\_PLAYING\_ORDER\_SINGLE\_REPEAT
    :   A single track is played repeatedly; the next track is the current track.

    BT\_MCS\_PLAYING\_ORDER\_INORDER\_ONCE
    :   The tracks within a group are played once in track order.

    BT\_MCS\_PLAYING\_ORDER\_INORDER\_REPEAT
    :   The tracks within a group are played in track order repeatedly.

    BT\_MCS\_PLAYING\_ORDER\_OLDEST\_ONCE
    :   The tracks within a group are played once only from the oldest first.

    BT\_MCS\_PLAYING\_ORDER\_OLDEST\_REPEAT
    :   The tracks within a group are played from the oldest first repeatedly.

    BT\_MCS\_PLAYING\_ORDER\_NEWEST\_ONCE
    :   The tracks within a group are played once only from the newest first.

    BT\_MCS\_PLAYING\_ORDER\_NEWEST\_REPEAT
    :   The tracks within a group are played from the newest first repeatedly.

    BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_ONCE
    :   The tracks within a group are played in random order once.

    BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_REPEAT
    :   The tracks within a group are played in random order repeatedly.

    Playing orders supported

    A bitmap, in the same order as the playing orders above.

    Note that playing order 1 corresponds to bit 0, and so on.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE
    :   A single track is played once; there is no next track.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT
    :   A single track is played repeatedly; the next track is the current track.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE
    :   The tracks within a group are played once in track order.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT
    :   The tracks within a group are played in track order repeatedly.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE
    :   The tracks within a group are played once only from the oldest first.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT
    :   The tracks within a group are played from the oldest first repeatedly.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE
    :   The tracks within a group are played once only from the newest first.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT
    :   The tracks within a group are played from the newest first repeatedly.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE
    :   The tracks within a group are played in random order once.

    BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT
    :   The tracks within a group are played in random order repeatedly.

    Media states

    BT\_MCS\_MEDIA\_STATE\_INACTIVE
    :   The current track is invalid, and no track has been selected.

    BT\_MCS\_MEDIA\_STATE\_PLAYING
    :   The media player is playing the current track.

    BT\_MCS\_MEDIA\_STATE\_PAUSED
    :   The current track is paused.

        The media player has a current track, but it is not being played

    BT\_MCS\_MEDIA\_STATE\_SEEKING
    :   The current track is fast forwarding or fast rewinding.

    Media control point opcodes

    BT\_MCS\_OPC\_PLAY
    :   Start playing the current track.

    BT\_MCS\_OPC\_PAUSE
    :   Pause playing the current track.

    BT\_MCS\_OPC\_FAST\_REWIND
    :   Fast rewind the current track.

    BT\_MCS\_OPC\_FAST\_FORWARD
    :   Fast forward the current track.

    BT\_MCS\_OPC\_STOP
    :   Stop current activity and return to the paused state and set the current track position to the start of the current track.

    BT\_MCS\_OPC\_MOVE\_RELATIVE
    :   Set a new current track position relative to the current track position.

    BT\_MCS\_OPC\_PREV\_SEGMENT
    :   Set the current track position to the starting position of the previous segment of the current track.

    BT\_MCS\_OPC\_NEXT\_SEGMENT
    :   Set the current track position to the starting position of the next segment of the current track.

    BT\_MCS\_OPC\_FIRST\_SEGMENT
    :   Set the current track position to the starting position of the first segment of the current track.

    BT\_MCS\_OPC\_LAST\_SEGMENT
    :   Set the current track position to the starting position of the last segment of the current track.

    BT\_MCS\_OPC\_GOTO\_SEGMENT
    :   Set the current track position to the starting position of the nth segment of the current track.

    BT\_MCS\_OPC\_PREV\_TRACK
    :   Set the current track to the previous track based on the playing order.

    BT\_MCS\_OPC\_NEXT\_TRACK
    :   Set the current track to the next track based on the playing order.

    BT\_MCS\_OPC\_FIRST\_TRACK
    :   Set the current track to the first track based on the playing order.

    BT\_MCS\_OPC\_LAST\_TRACK
    :   Set the current track to the last track based on the playing order.

    BT\_MCS\_OPC\_GOTO\_TRACK
    :   Set the current track to the nth track based on the playing order.

    BT\_MCS\_OPC\_PREV\_GROUP
    :   Set the current group to the previous group in the sequence of groups.

    BT\_MCS\_OPC\_NEXT\_GROUP
    :   Set the current group to the next group in the sequence of groups.

    BT\_MCS\_OPC\_FIRST\_GROUP
    :   Set the current group to the first group in the sequence of groups.

    BT\_MCS\_OPC\_LAST\_GROUP
    :   Set the current group to the last group in the sequence of groups.

    BT\_MCS\_OPC\_GOTO\_GROUP
    :   Set the current group to the nth group in the sequence of groups.

    Media control point supported opcodes values

    BT\_MCS\_OPC\_SUP\_PLAY
    :   Support the Play opcode.

    BT\_MCS\_OPC\_SUP\_PAUSE
    :   Support the Pause opcode.

    BT\_MCS\_OPC\_SUP\_FAST\_REWIND
    :   Support the Fast Rewind opcode.

    BT\_MCS\_OPC\_SUP\_FAST\_FORWARD
    :   Support the Fast Forward opcode.

    BT\_MCS\_OPC\_SUP\_STOP
    :   Support the Stop opcode.

    BT\_MCS\_OPC\_SUP\_MOVE\_RELATIVE
    :   Support the Move Relative opcode.

    BT\_MCS\_OPC\_SUP\_PREV\_SEGMENT
    :   Support the Previous Segment opcode.

    BT\_MCS\_OPC\_SUP\_NEXT\_SEGMENT
    :   Support the Next Segment opcode.

    BT\_MCS\_OPC\_SUP\_FIRST\_SEGMENT
    :   Support the First Segment opcode.

    BT\_MCS\_OPC\_SUP\_LAST\_SEGMENT
    :   Support the Last Segment opcode.

    BT\_MCS\_OPC\_SUP\_GOTO\_SEGMENT
    :   Support the Goto Segment opcode.

    BT\_MCS\_OPC\_SUP\_PREV\_TRACK
    :   Support the Previous Track opcode.

    BT\_MCS\_OPC\_SUP\_NEXT\_TRACK
    :   Support the Next Track opcode.

    BT\_MCS\_OPC\_SUP\_FIRST\_TRACK
    :   Support the First Track opcode.

    BT\_MCS\_OPC\_SUP\_LAST\_TRACK
    :   Support the Last Track opcode.

    BT\_MCS\_OPC\_SUP\_GOTO\_TRACK
    :   Support the Goto Track opcode.

    BT\_MCS\_OPC\_SUP\_PREV\_GROUP
    :   Support the Previous Group opcode.

    BT\_MCS\_OPC\_SUP\_NEXT\_GROUP
    :   Support the Next Group opcode.

    BT\_MCS\_OPC\_SUP\_FIRST\_GROUP
    :   Support the First Group opcode.

    BT\_MCS\_OPC\_SUP\_LAST\_GROUP
    :   Support the Last Group opcode.

    BT\_MCS\_OPC\_SUP\_GOTO\_GROUP
    :   Support the Goto Group opcode.

    Media control point notification result codes

    BT\_MCS\_OPC\_NTF\_SUCCESS
    :   Action requested by the opcode write was completed successfully.

    BT\_MCS\_OPC\_NTF\_NOT\_SUPPORTED
    :   An invalid or unsupported opcode was used for the Media Control Point write.

    BT\_MCS\_OPC\_NTF\_PLAYER\_INACTIVE
    :   The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive.

    BT\_MCS\_OPC\_NTF\_CANNOT\_BE\_COMPLETED
    :   The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player.

    Search control point type values

    Reference: Media Control Service spec v1.0 section 3.20.2

    BT\_MCS\_SEARCH\_TYPE\_TRACK\_NAME
    :   Search for Track Name.

    BT\_MCS\_SEARCH\_TYPE\_ARTIST\_NAME
    :   Search for Artist Name.

    BT\_MCS\_SEARCH\_TYPE\_ALBUM\_NAME
    :   Search for Album Name.

    BT\_MCS\_SEARCH\_TYPE\_GROUP\_NAME
    :   Search for Group Name.

    BT\_MCS\_SEARCH\_TYPE\_EARLIEST\_YEAR
    :   Search for Earliest Year.

    BT\_MCS\_SEARCH\_TYPE\_LATEST\_YEAR
    :   Search for Latest Year.

    BT\_MCS\_SEARCH\_TYPE\_GENRE
    :   Search for Genre.

    BT\_MCS\_SEARCH\_TYPE\_ONLY\_TRACKS
    :   Search for Tracks only.

    BT\_MCS\_SEARCH\_TYPE\_ONLY\_GROUPS
    :   Search for Groups only.

    Search notification result codes

    Reference: Media Control Service spec v1.0 section 3.20.2

    BT\_MCS\_SCP\_NTF\_SUCCESS
    :   Search request was accepted; search has started.

    BT\_MCS\_SCP\_NTF\_FAILURE
    :   Search request was invalid; no search started.

    Group object object types

    Reference: Media Control Service spec v1.0 section 4.4.1

    BT\_MCS\_GROUP\_OBJECT\_TRACK\_TYPE
    :   Group object type is track.

    BT\_MCS\_GROUP\_OBJECT\_GROUP\_TYPE
    :   Group object type is group.

    Defines

    BT\_MCS\_ERR\_LONG\_VAL\_CHANGED
    :   A characteristic value has changed while a Read Long Value Characteristic sub-procedure is in progress.

    BT\_MCS\_OPCODES\_SUPPORTED\_LEN
    :   Media control point supported opcodes length.

    SEARCH\_LEN\_MIN
    :   Search control point minimum length.

        At least one search control item (SCI), consisting of the length octet and the type octet. (The \* parameter field may be empty.)

    SEARCH\_LEN\_MAX
    :   Search control point maximum length.

    SEARCH\_SCI\_LEN\_MIN
    :   Search control point item (SCI) minimum length.

        An SCI length can be as little as one byte, for an SCI that has only the type field. (The SCI len is the length of type + param.)

    SEARCH\_PARAM\_MAX
    :   Search parameters maximum length.

### Media Proxy

*group* Media Proxy
:   Media proxy module.

    The media proxy module is the connection point between media players and media controllers.

    **Since**
    :   3.0

    **Version**
    :   0.8.0

    A media player has (access to) media content and knows how to navigate and play this content. A media controller reads or gets information from a player and controls the player by setting player parameters and giving the player commands.

    The media proxy module allows media player implementations to make themselves available to media controllers. And it allows controllers to access, and get updates from, any player.

    The media proxy module allows both local and remote control of local player instances: A media controller may be a local application, or it may be a Media Control Service relaying requests from a remote Media Control Client. There may be either local or remote control, or both, or even multiple instances of each.

    Playback speed parameters

    All values from -128 to 127 allowed, only some defined

    MEDIA\_PROXY\_PLAYBACK\_SPEED\_MIN
    :   Minimum playback speed, resulting in 25 % speed.

    MEDIA\_PROXY\_PLAYBACK\_SPEED\_QUARTER
    :   Quarter playback speed, resulting in 25 % speed.

    MEDIA\_PROXY\_PLAYBACK\_SPEED\_HALF
    :   Half playback speed, resulting in 50 % speed.

    MEDIA\_PROXY\_PLAYBACK\_SPEED\_UNITY
    :   Unity playback speed, resulting in 100 % speed.

    MEDIA\_PROXY\_PLAYBACK\_SPEED\_DOUBLE
    :   Double playback speed, resulting in 200 % speed.

    MEDIA\_PROXY\_PLAYBACK\_SPEED\_MAX
    :   Max playback speed, resulting in 395.7 % speed (nearly 400 %).

    Seeking speed factors

    The allowed values for seeking speed are the range -64 to -4 (endpoints included), the value 0, and the range 4 to 64 (endpoints included).

    MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MAX
    :   Maximum seeking speed - Can be negated.

    MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MIN
    :   Minimum seeking speed - Can be negated.

    MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_ZERO
    :   No seeking.

    Playing orders

    MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_ONCE
    :   A single track is played once; there is no next track.

    MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_REPEAT
    :   A single track is played repeatedly; the next track is the current track.

    MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_ONCE
    :   The tracks within a group are played once in track order.

    MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_REPEAT
    :   The tracks within a group are played in track order repeatedly.

    MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_ONCE
    :   The tracks within a group are played once only from the oldest first.

    MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_REPEAT
    :   The tracks within a group are played from the oldest first repeatedly.

    MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_ONCE
    :   The tracks within a group are played once only from the newest first.

    MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_REPEAT
    :   The tracks within a group are played from the newest first repeatedly.

    MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_ONCE
    :   The tracks within a group are played in random order once.

    MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_REPEAT
    :   The tracks within a group are played in random order repeatedly.

    Playing orders supported

    A bitmap, in the same order as the playing orders above.

    Note that playing order 1 corresponds to bit 0, and so on.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE
    :   A single track is played once; there is no next track.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT
    :   A single track is played repeatedly; the next track is the current track.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE
    :   The tracks within a group are played once in track order.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT
    :   The tracks within a group are played in track order repeatedly.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE
    :   The tracks within a group are played once only from the oldest first.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT
    :   The tracks within a group are played from the oldest first repeatedly.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE
    :   The tracks within a group are played once only from the newest first.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT
    :   The tracks within a group are played from the newest first repeatedly.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE
    :   The tracks within a group are played in random order once.

    MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT
    :   The tracks within a group are played in random order repeatedly.

    Media player states

    MEDIA\_PROXY\_STATE\_INACTIVE
    :   The current track is invalid, and no track has been selected.

    MEDIA\_PROXY\_STATE\_PLAYING
    :   The media player is playing the current track.

    MEDIA\_PROXY\_STATE\_PAUSED
    :   The current track is paused.

        The media player has a current track, but it is not being played

    MEDIA\_PROXY\_STATE\_SEEKING
    :   The current track is fast forwarding or fast rewinding.

    MEDIA\_PROXY\_STATE\_LAST
    :   Used internally as the last state value.

    Media player command opcodes

    MEDIA\_PROXY\_OP\_PLAY
    :   Start playing the current track.

    MEDIA\_PROXY\_OP\_PAUSE
    :   Pause playing the current track.

    MEDIA\_PROXY\_OP\_FAST\_REWIND
    :   Fast rewind the current track.

    MEDIA\_PROXY\_OP\_FAST\_FORWARD
    :   Fast forward the current track.

    MEDIA\_PROXY\_OP\_STOP
    :   Stop current activity and return to the paused state and set the current track position to the start of the current track.

    MEDIA\_PROXY\_OP\_MOVE\_RELATIVE
    :   Set a new current track position relative to the current track position.

    MEDIA\_PROXY\_OP\_PREV\_SEGMENT
    :   Set the current track position to the starting position of the previous segment of the current track.

    MEDIA\_PROXY\_OP\_NEXT\_SEGMENT
    :   Set the current track position to the starting position of the next segment of the current track.

    MEDIA\_PROXY\_OP\_FIRST\_SEGMENT
    :   Set the current track position to the starting position of the first segment of the current track.

    MEDIA\_PROXY\_OP\_LAST\_SEGMENT
    :   Set the current track position to the starting position of the last segment of the current track.

    MEDIA\_PROXY\_OP\_GOTO\_SEGMENT
    :   Set the current track position to the starting position of the nth segment of the current track.

    MEDIA\_PROXY\_OP\_PREV\_TRACK
    :   Set the current track to the previous track based on the playing order.

    MEDIA\_PROXY\_OP\_NEXT\_TRACK
    :   Set the current track to the next track based on the playing order.

    MEDIA\_PROXY\_OP\_FIRST\_TRACK
    :   Set the current track to the first track based on the playing order.

    MEDIA\_PROXY\_OP\_LAST\_TRACK
    :   Set the current track to the last track based on the playing order.

    MEDIA\_PROXY\_OP\_GOTO\_TRACK
    :   Set the current track to the nth track based on the playing order.

    MEDIA\_PROXY\_OP\_PREV\_GROUP
    :   Set the current group to the previous group in the sequence of groups.

    MEDIA\_PROXY\_OP\_NEXT\_GROUP
    :   Set the current group to the next group in the sequence of groups.

    MEDIA\_PROXY\_OP\_FIRST\_GROUP
    :   Set the current group to the first group in the sequence of groups.

    MEDIA\_PROXY\_OP\_LAST\_GROUP
    :   Set the current group to the last group in the sequence of groups.

    MEDIA\_PROXY\_OP\_GOTO\_GROUP
    :   Set the current group to the nth group in the sequence of groups.

    Unnamed Group

    MEDIA\_PROXY\_OP\_SUP\_PLAY
    :   Media player supported command opcodes.

        Support the Play opcode

    MEDIA\_PROXY\_OP\_SUP\_PAUSE
    :   Support the Pause opcode.

    MEDIA\_PROXY\_OP\_SUP\_FAST\_REWIND
    :   Support the Fast Rewind opcode.

    MEDIA\_PROXY\_OP\_SUP\_FAST\_FORWARD
    :   Support the Fast Forward opcode.

    MEDIA\_PROXY\_OP\_SUP\_STOP
    :   Support the Stop opcode.

    MEDIA\_PROXY\_OP\_SUP\_MOVE\_RELATIVE
    :   Support the Move Relative opcode.

    MEDIA\_PROXY\_OP\_SUP\_PREV\_SEGMENT
    :   Support the Previous Segment opcode.

    MEDIA\_PROXY\_OP\_SUP\_NEXT\_SEGMENT
    :   Support the Next Segment opcode.

    MEDIA\_PROXY\_OP\_SUP\_FIRST\_SEGMENT
    :   Support the First Segment opcode.

    MEDIA\_PROXY\_OP\_SUP\_LAST\_SEGMENT
    :   Support the Last Segment opcode.

    MEDIA\_PROXY\_OP\_SUP\_GOTO\_SEGMENT
    :   Support the Goto Segment opcode.

    MEDIA\_PROXY\_OP\_SUP\_PREV\_TRACK
    :   Support the Previous Track opcode.

    MEDIA\_PROXY\_OP\_SUP\_NEXT\_TRACK
    :   Support the Next Track opcode.

    MEDIA\_PROXY\_OP\_SUP\_FIRST\_TRACK
    :   Support the First Track opcode.

    MEDIA\_PROXY\_OP\_SUP\_LAST\_TRACK
    :   Support the Last Track opcode.

    MEDIA\_PROXY\_OP\_SUP\_GOTO\_TRACK
    :   Support the Goto Track opcode.

    MEDIA\_PROXY\_OP\_SUP\_PREV\_GROUP
    :   Support the Previous Group opcode.

    MEDIA\_PROXY\_OP\_SUP\_NEXT\_GROUP
    :   Support the Next Group opcode.

    MEDIA\_PROXY\_OP\_SUP\_FIRST\_GROUP
    :   Support the First Group opcode.

    MEDIA\_PROXY\_OP\_SUP\_LAST\_GROUP
    :   Support the Last Group opcode.

    MEDIA\_PROXY\_OP\_SUP\_GOTO\_GROUP
    :   Support the Goto Group opcode.

    Media player command result codes

    MEDIA\_PROXY\_CMD\_SUCCESS
    :   Action requested by the opcode write was completed successfully.

    MEDIA\_PROXY\_CMD\_NOT\_SUPPORTED
    :   An invalid or unsupported opcode was used for the Media Control Point write.

    MEDIA\_PROXY\_CMD\_PLAYER\_INACTIVE
    :   The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive.

    MEDIA\_PROXY\_CMD\_CANNOT\_BE\_COMPLETED
    :   The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player.

    Search operation type values

    MEDIA\_PROXY\_SEARCH\_TYPE\_TRACK\_NAME
    :   Search for Track Name.

    MEDIA\_PROXY\_SEARCH\_TYPE\_ARTIST\_NAME
    :   Search for Artist Name.

    MEDIA\_PROXY\_SEARCH\_TYPE\_ALBUM\_NAME
    :   Search for Album Name.

    MEDIA\_PROXY\_SEARCH\_TYPE\_GROUP\_NAME
    :   Search for Group Name.

    MEDIA\_PROXY\_SEARCH\_TYPE\_EARLIEST\_YEAR
    :   Search for Earliest Year.

    MEDIA\_PROXY\_SEARCH\_TYPE\_LATEST\_YEAR
    :   Search for Latest Year.

    MEDIA\_PROXY\_SEARCH\_TYPE\_GENRE
    :   Search for Genre.

    MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_TRACKS
    :   Search for Tracks only.

    MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_GROUPS
    :   Search for Groups only.

    Search notification result codes

    MEDIA\_PROXY\_SEARCH\_SUCCESS
    :   Search request was accepted; search has started.

    MEDIA\_PROXY\_SEARCH\_FAILURE
    :   Search request was invalid; no search started.

    Group object object types

    MEDIA\_PROXY\_GROUP\_OBJECT\_TRACK\_TYPE
    :   Group object type is track.

    MEDIA\_PROXY\_GROUP\_OBJECT\_GROUP\_TYPE
    :   Group object type is group.

    Defines

    MEDIA\_PROXY\_OPCODES\_SUPPORTED\_LEN
    :   Media player supported opcodes length.

    Functions

    int media\_proxy\_ctrl\_register(struct [media\_proxy\_ctrl\_cbs](#c.media_proxy_ctrl_cbs) \*ctrl\_cbs)
    :   Register a controller with the media\_proxy.

        Parameters:
        :   - **ctrl\_cbs** – Callbacks to the controller

        Returns:
        :   0 if success, errno on failure

    int media\_proxy\_ctrl\_discover\_player(struct bt\_conn \*conn)
    :   Discover a remote media player.

        Discover a remote media player instance. The remote player instance will be discovered, and accessed, using Bluetooth, via the media control client and a remote media control service. This call will start a GATT discovery of the Media Control Service on the peer, and setup handles and subscriptions.

        This shall be called once before any other actions can be executed for the remote player. The remote player instance will be returned in the discover\_player() callback.

        Parameters:
        :   - **conn** – The connection to do discovery for

        Returns:
        :   0 if success, errno on failure

    int media\_proxy\_ctrl\_get\_player\_name(struct media\_player \*player)
    :   Read Media Player Name.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_icon\_id(struct media\_player \*player)
    :   Read Icon Object ID.

        Get an ID (48 bit) that can be used to retrieve the Icon Object from an Object Transfer Service

        See the Media Control Service spec v1.0 sections 3.2 and 4.1 for a description of the Icon Object.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_icon\_url(struct media\_player \*player)
    :   Read Icon URL.

        Get a URL to the media player’s icon.

        Parameters:
        :   - **player** – Media player instance pointer

    int media\_proxy\_ctrl\_get\_track\_title(struct media\_player \*player)
    :   Read Track Title.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_track\_duration(struct media\_player \*player)
    :   Read Track Duration.

        The duration of a track is measured in hundredths of a second.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_track\_position(struct media\_player \*player)
    :   Read Track Position.

        The position of the player (the playing position) is measured in hundredths of a second from the beginning of the track

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_set\_track\_position(struct media\_player \*player, int32\_t position)
    :   Set Track Position.

        Set the playing position of the media player in the current track. The position is given in hundredths of a second, from the beginning of the track of the track for positive values, and (backwards) from the end of the track for negative values.

        Parameters:
        :   - **player** – Media player instance pointer
            - **position** – The track position to set

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_playback\_speed(struct media\_player \*player)
    :   Get Playback Speed.

        The playback speed parameter is related to the actual playback speed as follows: actual playback speed = 2^(speed\_parameter/64)

        A speed parameter of 0 corresponds to unity speed playback (i.e. playback at “normal” speed). A speed parameter of -128 corresponds to playback at one fourth of normal speed, 127 corresponds to playback at almost four times the normal speed.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_set\_playback\_speed(struct media\_player \*player, int8\_t speed)
    :   Set Playback Speed.

        See the get\_playback\_speed() function for an explanation of the playback speed parameter.

        Note that the media player may not support all possible values of the playback speed parameter. If the value given is not supported, and is higher than the current value, the player should set the playback speed to the next higher supported value. (And correspondingly to the next lower supported value for given values lower than the current value.)

        Parameters:
        :   - **player** – Media player instance pointer
            - **speed** – The playback speed parameter to set

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_seeking\_speed(struct media\_player \*player)
    :   Get Seeking Speed.

        The seeking speed gives the speed with which the player is seeking. It is a factor, relative to real-time playback speed - a factor four means seeking happens at four times the real-time playback speed. Positive values are for forward seeking, negative values for backwards seeking.

        The seeking speed is not settable - a non-zero seeking speed is the result of “fast rewind” of “fast forward” commands.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_track\_segments\_id(struct media\_player \*player)
    :   Read Current Track Segments Object ID.

        Get an ID (48 bit) that can be used to retrieve the Current Track Segments Object from an Object Transfer Service

        See the Media Control Service spec v1.0 sections 3.10 and 4.2 for a description of the Track Segments Object.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_current\_track\_id(struct media\_player \*player)
    :   Read Current Track Object ID.

        Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

        See the Media Control Service spec v1.0 sections 3.11 and 4.3 for a description of the Current Track Object.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_set\_current\_track\_id(struct media\_player \*player, uint64\_t id)
    :   Set Current Track Object ID.

        Change the player’s current track to the track given by the ID. (Behaves similarly to the goto track command.)

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer
            - **id** – The ID of a track object

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_next\_track\_id(struct media\_player \*player)
    :   Read Next Track Object ID.

        Get an ID (48 bit) that can be used to retrieve the Next Track Object from an Object Transfer Service

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_set\_next\_track\_id(struct media\_player \*player, uint64\_t id)
    :   Set Next Track Object ID.

        Change the player’s next track to the track given by the ID.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer
            - **id** – The ID of a track object

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_parent\_group\_id(struct media\_player \*player)
    :   Read Parent Group Object ID.

        Get an ID (48 bit) that can be used to retrieve the Parent Track Object from an Object Transfer Service

        The parent group is the parent of the current group.

        See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Track Object.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_current\_group\_id(struct media\_player \*player)
    :   Read Current Group Object ID.

        Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

        See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Group Object.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_set\_current\_group\_id(struct media\_player \*player, uint64\_t id)
    :   Set Current Group Object ID.

        Change the player’s current group to the group given by the ID, and the current track to the first track in that group.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer
            - **id** – The ID of a group object

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_playing\_order(struct media\_player \*player)
    :   Read Playing Order.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_set\_playing\_order(struct media\_player \*player, uint8\_t order)
    :   Set Playing Order.

        Set the media player’s playing order

        Parameters:
        :   - **player** – Media player instance pointer
            - **order** – The playing order to set

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_playing\_orders\_supported(struct media\_player \*player)
    :   Read Playing Orders Supported.

        Read a bitmap containing the media player’s supported playing orders.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_media\_state(struct media\_player \*player)
    :   Read Media State.

        Read the media player’s state

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_send\_command(struct media\_player \*player, const struct [mpl\_cmd](#c.mpl_cmd) \*command)
    :   Send Command.

        Send a command to the media player. Commands may cause the media player to change its state May result in two callbacks - one for the actual sending of the command to the player, one for the result of the command from the player.

        Parameters:
        :   - **player** – Media player instance pointer
            - **command** – The command to send

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_commands\_supported(struct media\_player \*player)
    :   Read Commands Supported.

        Read a bitmap containing the media player’s supported command opcodes.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_send\_search(struct media\_player \*player, const struct [mpl\_search](#c.mpl_search) \*search)
    :   Set Search.

        Write a search to the media player. If the search is successful, the search results will be available as a group object in the Object Transfer Service (OTS).

        May result in up to three callbacks

        - one for the actual sending of the search to the player
        - one for the result code for the search from the player
        - if the search is successful, one for the search results object ID in the OTs

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer
            - **search** – The search to write

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_ctrl\_get\_search\_results\_id(struct media\_player \*player)
    :   Read Search Results Object ID.

        Get an ID (48 bit) that can be used to retrieve the Search Results Object from an Object Transfer Service

        The search results object is a group object. The search results object only exists if a successful search operation has been done.

        Requires Object Transfer Service

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    uint8\_t media\_proxy\_ctrl\_get\_content\_ctrl\_id(struct media\_player \*player)
    :   Read Content Control ID.

        The content control ID identifies a content control service on a device, and links it to the corresponding audio stream.

        Parameters:
        :   - **player** – Media player instance pointer

        Returns:
        :   0 if success, errno on failure.

    int media\_proxy\_pl\_register(struct [media\_proxy\_pl\_calls](#c.media_proxy_pl_calls) \*pl\_calls)
    :   Register a player with the media proxy.

        Register a player with the media proxy module, for use by media controllers.

        The media proxy may call any non-NULL function pointers in the supplied [media\_proxy\_pl\_calls](#structmedia__proxy__pl__calls) structure.

        Parameters:
        :   - **pl\_calls** – Function pointers to the media player’s calls

        Returns:
        :   0 if success, errno on failure

    int media\_proxy\_pl\_init(void)
    :   Initialize player.

        TODO: Move to player header file

    struct bt\_ots \*bt\_mcs\_get\_ots(void)
    :   Get the pointer of the Object Transfer Service used by the Media Control Service.

        TODO: Find best location for this call, and move this one also

    void media\_proxy\_pl\_name\_cb(const char \*name)
    :   Player name changed callback.

        To be called when the player’s name is changed.

        Parameters:
        :   - **name** – The name of the player

    void media\_proxy\_pl\_icon\_url\_cb(const char \*url)
    :   Player icon URL changed callback.

        To be called when the player’s icon URL is changed.

        Parameters:
        :   - **url** – The URL of the player’s icon

    void media\_proxy\_pl\_track\_changed\_cb(void)
    :   Track changed callback.

        To be called when the player’s current track is changed

    void media\_proxy\_pl\_track\_title\_cb(char \*title)
    :   Track title callback.

        To be called when the player’s current track is changed

        Parameters:
        :   - **title** – The title of the track

    void media\_proxy\_pl\_track\_duration\_cb(int32\_t duration)
    :   Track duration callback.

        To be called when the current track’s duration is changed (e.g. due to a track change)

        The track duration is given in hundredths of a second.

        Parameters:
        :   - **duration** – The track duration

    void media\_proxy\_pl\_track\_position\_cb(int32\_t position)
    :   Track position callback.

        To be called when the media player’s position in the track is changed, or when the player is paused or similar.

        Exception: This callback should not be called when the position changes during regular playback, i.e. while the player is playing and playback happens at a constant speed.

        The track position is given in hundredths of a second from the start of the track.

        Parameters:
        :   - **position** – The media player’s position in the track

    void media\_proxy\_pl\_playback\_speed\_cb(int8\_t speed)
    :   Playback speed callback.

        To be called when the playback speed is changed.

        Parameters:
        :   - **speed** – The playback speed parameter

    void media\_proxy\_pl\_seeking\_speed\_cb(int8\_t speed)
    :   Seeking speed callback.

        To be called when the seeking speed is changed.

        Parameters:
        :   - **speed** – The seeking speed factor

    void media\_proxy\_pl\_current\_track\_id\_cb(uint64\_t id)
    :   Current track object ID callback.

        To be called when the ID of the current track is changed (e.g. due to a track change).

        Parameters:
        :   - **id** – The ID of the current track object in the OTS

    void media\_proxy\_pl\_next\_track\_id\_cb(uint64\_t id)
    :   Next track object ID callback.

        To be called when the ID of the current track is changes

        Parameters:
        :   - **id** – The ID of the next track object in the OTS

    void media\_proxy\_pl\_parent\_group\_id\_cb(uint64\_t id)
    :   Parent group object ID callback.

        To be called when the ID of the parent group is changed

        Parameters:
        :   - **id** – The ID of the parent group object in the OTS

    void media\_proxy\_pl\_current\_group\_id\_cb(uint64\_t id)
    :   Current group object ID callback.

        To be called when the ID of the current group is changed

        Parameters:
        :   - **id** – The ID of the current group object in the OTS

    void media\_proxy\_pl\_playing\_order\_cb(uint8\_t order)
    :   Playing order callback.

        To be called when the playing order is changed

        Parameters:
        :   - **order** – The playing order

    void media\_proxy\_pl\_media\_state\_cb(uint8\_t state)
    :   Media state callback.

        To be called when the media state is changed

        Parameters:
        :   - **state** – The media player’s state

    void media\_proxy\_pl\_command\_cb(const struct [mpl\_cmd\_ntf](#c.mpl_cmd_ntf) \*cmd\_ntf)
    :   Command callback.

        To be called when a command has been sent, to notify whether the command was successfully performed or not. See the MEDIA\_PROXY\_CMD\_\* result code defines.

        Parameters:
        :   - **cmd\_ntf** – The result of the command

    void media\_proxy\_pl\_commands\_supported\_cb(uint32\_t opcodes)
    :   Commands supported callback.

        To be called when the set of commands supported is changed

        Parameters:
        :   - **opcodes** – The supported commands opcodes

    void media\_proxy\_pl\_search\_cb(uint8\_t result\_code)
    :   Search callback.

        To be called when a search has been set to notify whether the search was successfully performed or not. See the MEDIA\_PROXY\_SEARCH\_\* result code defines.

        The actual results of the search, if successful, can be found in the search results object.

        Parameters:
        :   - **result\_code** – The result (success or failure) of the search

    void media\_proxy\_pl\_search\_results\_id\_cb(uint64\_t id)
    :   Search Results object ID callback.

        To be called when the ID of the search results is changed (typically as the result of a new successful search).

        Parameters:
        :   - **id** – The ID of the search results object in the OTS

    struct mpl\_cmd
    :   *#include <media\_proxy.h>*

        Media player command.

        Public Members

        uint8\_t opcode
        :   The opcode.

            See the MEDIA\_PROXY\_OP\_\* values

        bool use\_param
        :   Whether or not the [mpl\_cmd::param](#structmpl__cmd_1ade5ed4d0ff2aeb192b8ed6b586c9bc9e) is used.

        int32\_t param
        :   A 32-bit signed parameter.

            The parameter value depends on the [mpl\_cmd::opcode](#structmpl__cmd_1a5cb29ca9e5a6b8249c69cc975b345e2f)

    struct mpl\_cmd\_ntf
    :   *#include <media\_proxy.h>*

        Media command notification.

        Public Members

        uint8\_t requested\_opcode
        :   The opcode that was sent.

        uint8\_t result\_code
        :   The result of the operation.

    struct mpl\_sci
    :   *#include <media\_proxy.h>*

        Search control item.

        Public Members

        uint8\_t len
        :   Length of type and parameter.

        uint8\_t type
        :   MEDIA\_PROXY\_SEARCH\_TYPE\_<…>.

        char param[62]
        :   Search parameter.

    struct mpl\_search
    :   *#include <media\_proxy.h>*

        Search.

        Public Members

        uint8\_t len
        :   The length of the [mpl\_search::search](#structmpl__search_1aa2332c1802786e2ef0486ede1c3a24c7) value.

        char search[64]
        :   Concatenated search control items - (type, length, param).

    struct media\_proxy\_ctrl\_cbs
    :   *#include <media\_proxy.h>*

        Callbacks to a controller, from the media proxy.

        Given by a controller when registering

        Public Members

        void (\*local\_player\_instance)(struct media\_player \*player, int err)
        :   Media Player Instance callback.

            Called when the local Media Player instance is registered or read (TODO). Also called if the local player instance is already registered when the controller is registered. Provides the controller with the pointer to the local player instance.

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, or errno on negative value.

        void (\*player\_name\_recv)(struct media\_player \*player, int err, const char \*name)
        :   Media Player Name receive callback.

            Called when the Media Player Name is read or changed See also media\_proxy\_ctrl\_name\_get()

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param name:
            :   The name of the media player

        void (\*icon\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)
        :   Media Player Icon Object ID receive callback.

            Called when the Media Player Icon Object ID is read See also [media\_proxy\_ctrl\_get\_icon\_id()](#group__bt__media__proxy_1ga5efccb39cdb97eed476e0c0bff461ec1)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID of the Icon object in the Object Transfer Service (48 bits)

        void (\*icon\_url\_recv)(struct media\_player \*player, int err, const char \*url)
        :   Media Player Icon URL receive callback.

            Called when the Media Player Icon URL is read See also [media\_proxy\_ctrl\_get\_icon\_url()](#group__bt__media__proxy_1gab6df6fe71c8273eca855eb3be27290dd)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param url:
            :   The URL of the icon

        void (\*track\_changed\_recv)(struct media\_player \*player, int err)
        :   Track changed receive callback.

            Called when the Current Track is changed

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

        void (\*track\_title\_recv)(struct media\_player \*player, int err, const char \*title)
        :   Track Title receive callback.

            Called when the Track Title is read or changed See also [media\_proxy\_ctrl\_get\_track\_title()](#group__bt__media__proxy_1gabfbb49e79204130cb004f217af771b80)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param title:
            :   The title of the current track

        void (\*track\_duration\_recv)(struct media\_player \*player, int err, int32\_t duration)
        :   Track Duration receive callback.

            Called when the Track Duration is read or changed See also [media\_proxy\_ctrl\_get\_track\_duration()](#group__bt__media__proxy_1ga488441418a8f2d358092019bbfe16788)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param duration:
            :   The duration of the current track

        void (\*track\_position\_recv)(struct media\_player \*player, int err, int32\_t position)
        :   Track Position receive callback.

            Called when the Track Position is read or changed See also [media\_proxy\_ctrl\_get\_track\_position()](#group__bt__media__proxy_1gae0bb75feb49a68b495150c6fba2f21a7) and [media\_proxy\_ctrl\_set\_track\_position()](#group__bt__media__proxy_1ga776bb5f16cf1f4f6cc3842aabd86b781)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param position:
            :   The player’s position in the track

        void (\*track\_position\_write)(struct media\_player \*player, int err, int32\_t position)
        :   Track Position write callback.

            Called when the Track Position is written See also [media\_proxy\_ctrl\_set\_track\_position()](#group__bt__media__proxy_1ga776bb5f16cf1f4f6cc3842aabd86b781).

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param position:
            :   The position given attempted to write

        void (\*playback\_speed\_recv)(struct media\_player \*player, int err, int8\_t speed)
        :   Playback Speed receive callback.

            Called when the Playback Speed is read or changed See also [media\_proxy\_ctrl\_get\_playback\_speed()](#group__bt__media__proxy_1ga2d64a23b3f881579a603a04baeb64088) and [media\_proxy\_ctrl\_set\_playback\_speed()](#group__bt__media__proxy_1gabafbc857c3e6befe98e339acb58f17fb)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param speed:
            :   The playback speed parameter

        void (\*playback\_speed\_write)(struct media\_player \*player, int err, int8\_t speed)
        :   Playback Speed write callback.

            Called when the Playback Speed is written See also [media\_proxy\_ctrl\_set\_playback\_speed()](#group__bt__media__proxy_1gabafbc857c3e6befe98e339acb58f17fb)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param speed:
            :   The playback speed parameter attempted to write

        void (\*seeking\_speed\_recv)(struct media\_player \*player, int err, int8\_t speed)
        :   Seeking Speed receive callback.

            Called when the Seeking Speed is read or changed See also [media\_proxy\_ctrl\_get\_seeking\_speed()](#group__bt__media__proxy_1ga817ca4ab611e214493fbc918036def0f)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param speed:
            :   The seeking speed factor

        void (\*track\_segments\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)
        :   Track Segments Object ID receive callback.

            Called when the Track Segments Object ID is read See also [media\_proxy\_ctrl\_get\_track\_segments\_id()](#group__bt__media__proxy_1ga1afcc097cb36c4f11141b82ce28e8126)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID of the track segments object in Object Transfer Service (48 bits)

        void (\*current\_track\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)
        :   Current Track Object ID receive callback.

            Called when the Current Track Object ID is read or changed See also [media\_proxy\_ctrl\_get\_current\_track\_id()](#group__bt__media__proxy_1gaebe7e3683041e28bef40df75cc991dea) and [media\_proxy\_ctrl\_set\_current\_track\_id()](#group__bt__media__proxy_1gaea6adacedaded10f7c2c0f91b7159f74)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID of the current track object in Object Transfer Service (48 bits)

        void (\*current\_track\_id\_write)(struct media\_player \*player, int err, uint64\_t id)
        :   Current Track Object ID write callback.

            Called when the Current Track Object ID is written See also [media\_proxy\_ctrl\_set\_current\_track\_id()](#group__bt__media__proxy_1gaea6adacedaded10f7c2c0f91b7159f74)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID (48 bits) attempted to write

        void (\*next\_track\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)
        :   Next Track Object ID receive callback.

            Called when the Next Track Object ID is read or changed See also [media\_proxy\_ctrl\_get\_next\_track\_id()](#group__bt__media__proxy_1gae32da32bd504061801730805729242e1) and [media\_proxy\_ctrl\_set\_next\_track\_id()](#group__bt__media__proxy_1ga43b797717fb9b36b94a606dfabeb0fa7)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID of the next track object in Object Transfer Service (48 bits)

        void (\*next\_track\_id\_write)(struct media\_player \*player, int err, uint64\_t id)
        :   Next Track Object ID write callback.

            Called when the Next Track Object ID is written See also [media\_proxy\_ctrl\_set\_next\_track\_id()](#group__bt__media__proxy_1ga43b797717fb9b36b94a606dfabeb0fa7)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID (48 bits) attempted to write

        void (\*parent\_group\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)
        :   Parent Group Object ID receive callback.

            Called when the Parent Group Object ID is read or changed See also [media\_proxy\_ctrl\_get\_parent\_group\_id()](#group__bt__media__proxy_1ga12dc878be39814660900ba875e13e537)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID of the parent group object in Object Transfer Service (48 bits)

        void (\*current\_group\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)
        :   Current Group Object ID receive callback.

            Called when the Current Group Object ID is read or changed See also [media\_proxy\_ctrl\_get\_current\_group\_id()](#group__bt__media__proxy_1ga2ae50a1988305b4247ff0af796b6d93e) and [media\_proxy\_ctrl\_set\_current\_group\_id()](#group__bt__media__proxy_1gae496885d0124f4e3fc2c0f203fcff118)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID of the current group object in Object Transfer Service (48 bits)

        void (\*current\_group\_id\_write)(struct media\_player \*player, int err, uint64\_t id)
        :   Current Group Object ID write callback.

            Called when the Current Group Object ID is written See also [media\_proxy\_ctrl\_set\_current\_group\_id()](#group__bt__media__proxy_1gae496885d0124f4e3fc2c0f203fcff118)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID (48 bits) attempted to write

        void (\*playing\_order\_recv)(struct media\_player \*player, int err, uint8\_t order)
        :   Playing Order receive callback.

            Called when the Playing Order is read or changed See also [media\_proxy\_ctrl\_get\_playing\_order()](#group__bt__media__proxy_1ga2f93bcde2460c6638880f8e6631eb68e) and [media\_proxy\_ctrl\_set\_playing\_order()](#group__bt__media__proxy_1gaa4040e97100f6e70527e6ad201309bbe)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param order:
            :   The playing order

        void (\*playing\_order\_write)(struct media\_player \*player, int err, uint8\_t order)
        :   Playing Order write callback.

            Called when the Playing Order is written See also [media\_proxy\_ctrl\_set\_playing\_order()](#group__bt__media__proxy_1gaa4040e97100f6e70527e6ad201309bbe)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param order:
            :   The playing order attempted to write

        void (\*playing\_orders\_supported\_recv)(struct media\_player \*player, int err, uint16\_t orders)
        :   Playing Orders Supported receive callback.

            Called when the Playing Orders Supported is read See also [media\_proxy\_ctrl\_get\_playing\_orders\_supported()](#group__bt__media__proxy_1ga030899757b79251f1d5a1055f65fe989)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param orders:
            :   The playing orders supported

        void (\*media\_state\_recv)(struct media\_player \*player, int err, uint8\_t state)
        :   Media State receive callback.

            Called when the Media State is read or changed See also [media\_proxy\_ctrl\_get\_media\_state()](#group__bt__media__proxy_1ga9433aaf24776c30557ea694795e75b3e) and [media\_proxy\_ctrl\_send\_command()](#group__bt__media__proxy_1ga590762e7272b99fb8ac50a7841424670)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param state:
            :   The media player state

        void (\*command\_send)(struct media\_player \*player, int err, const struct [mpl\_cmd](#c.mpl_cmd) \*cmd)
        :   Command send callback.

            Called when a command has been sent See also [media\_proxy\_ctrl\_send\_command()](#group__bt__media__proxy_1ga590762e7272b99fb8ac50a7841424670)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param cmd:
            :   The command sent

        void (\*command\_recv)(struct media\_player \*player, int err, const struct [mpl\_cmd\_ntf](#c.mpl_cmd_ntf) \*result)
        :   Command result receive callback.

            Called when a command result has been received See also [media\_proxy\_ctrl\_send\_command()](#group__bt__media__proxy_1ga590762e7272b99fb8ac50a7841424670)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param result:
            :   The result received

        void (\*commands\_supported\_recv)(struct media\_player \*player, int err, uint32\_t opcodes)
        :   Commands supported receive callback.

            Called when the Commands Supported is read or changed See also [media\_proxy\_ctrl\_get\_commands\_supported()](#group__bt__media__proxy_1ga15804287093b20d4a1616380729b33c8)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param opcodes:
            :   The supported command opcodes (bitmap)

        void (\*search\_send)(struct media\_player \*player, int err, const struct [mpl\_search](#c.mpl_search) \*search)
        :   Search send callback.

            Called when a search has been sent See also [media\_proxy\_ctrl\_send\_search()](#group__bt__media__proxy_1ga052c3fabac4a44ee2802ddd4a6c5c9ac)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param search:
            :   The search sent

        void (\*search\_recv)(struct media\_player \*player, int err, uint8\_t result\_code)
        :   Search result code receive callback.

            Called when a search result code has been received See also [media\_proxy\_ctrl\_send\_search()](#group__bt__media__proxy_1ga052c3fabac4a44ee2802ddd4a6c5c9ac)

            The search result code tells whether the search was successful or not. For a successful search, the actual results of the search (i.e. what was found as a result of the search)can be accessed using the Search Results Object ID. The Search Results Object ID has a separate callback - [search\_results\_id\_recv()](#structmedia__proxy__ctrl__cbs_1af067e55ef7f676ad3c05f838160ed21e).

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param result\_code:
            :   Search result code

        void (\*search\_results\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)
        :   Search Results Object ID receive callback See also [media\_proxy\_ctrl\_get\_search\_results\_id()](#group__bt__media__proxy_1ga580a0c9fa47460be59f0571ee11a41b4).

            Called when the Search Results Object ID is read or changed

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param id:
            :   The ID of the search results object in Object Transfer Service (48 bits)

        void (\*content\_ctrl\_id\_recv)(struct media\_player \*player, int err, uint8\_t ccid)
        :   Content Control ID receive callback.

            Called when the Content Control ID is read See also [media\_proxy\_ctrl\_get\_content\_ctrl\_id()](#group__bt__media__proxy_1ga23488e77985a04216ec7c7fa785f09fc)

            Param player:
            :   Media player instance pointer

            Param err:
            :   Error value. 0 on success, GATT error on positive value or errno on negative value.

            Param ccid:
            :   The content control ID

    struct media\_proxy\_pl\_calls
    :   *#include <media\_proxy.h>*

        Available calls in a player, that the media proxy can call.

        Given by a player when registering.

        Public Members

        const char \*(\*get\_player\_name)(void)
        :   Read Media Player Name.

            Return:
            :   The name of the media player

        uint64\_t (\*get\_icon\_id)(void)
        :   Read Icon Object ID.

            Get an ID (48 bit) that can be used to retrieve the Icon Object from an Object Transfer Service

            See the Media Control Service spec v1.0 sections 3.2 and 4.1 for a description of the Icon Object.

            Return:
            :   The Icon Object ID

        const char \*(\*get\_icon\_url)(void)
        :   Read Icon URL.

            Get a URL to the media player’s icon.

            Return:
            :   The URL of the Icon

        const char \*(\*get\_track\_title)(void)
        :   Read Track Title.

            Return:
            :   The title of the current track

        int32\_t (\*get\_track\_duration)(void)
        :   Read Track Duration.

            The duration of a track is measured in hundredths of a second.

            Return:
            :   The duration of the current track

        int32\_t (\*get\_track\_position)(void)
        :   Read Track Position.

            The position of the player (the playing position) is measured in hundredths of a second from the beginning of the track

            Return:
            :   The position of the player in the current track

        void (\*set\_track\_position)(int32\_t position)
        :   Set Track Position.

            Set the playing position of the media player in the current track. The position is given in hundredths of a second, from the beginning of the track of the track for positive values, and (backwards) from the end of the track for negative values.

            Param position:
            :   The player position to set

        int8\_t (\*get\_playback\_speed)(void)
        :   Get Playback Speed.

            The playback speed parameter is related to the actual playback speed as follows: actual playback speed = 2^(speed\_parameter/64)

            A speed parameter of 0 corresponds to unity speed playback (i.e. playback at “normal” speed). A speed parameter of -128 corresponds to playback at one fourth of normal speed, 127 corresponds to playback at almost four times the normal speed.

            Return:
            :   The playback speed parameter

        void (\*set\_playback\_speed)(int8\_t speed)
        :   Set Playback Speed.

            See the [get\_playback\_speed()](#structmedia__proxy__pl__calls_1ae1006d5c684e12e1e1c927f71aa93930) function for an explanation of the playback speed parameter.

            Note that the media player may not support all possible values of the playback speed parameter. If the value given is not supported, and is higher than the current value, the player should set the playback speed to the next higher supported value. (And correspondingly to the next lower supported value for given values lower than the current value.)

            Param speed:
            :   The playback speed parameter to set

        int8\_t (\*get\_seeking\_speed)(void)
        :   Get Seeking Speed.

            The seeking speed gives the speed with which the player is seeking. It is a factor, relative to real-time playback speed - a factor four means seeking happens at four times the real-time playback speed. Positive values are for forward seeking, negative values for backwards seeking.

            The seeking speed is not settable - a non-zero seeking speed is the result of “fast rewind” of “fast forward” commands.

            Return:
            :   The seeking speed factor

        uint64\_t (\*get\_track\_segments\_id)(void)
        :   Read Current Track Segments Object ID.

            Get an ID (48 bit) that can be used to retrieve the Current Track Segments Object from an Object Transfer Service

            See the Media Control Service spec v1.0 sections 3.10 and 4.2 for a description of the Track Segments Object.

            Return:
            :   Current The Track Segments Object ID

        uint64\_t (\*get\_current\_track\_id)(void)
        :   Read Current Track Object ID.

            Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

            See the Media Control Service spec v1.0 sections 3.11 and 4.3 for a description of the Current Track Object.

            Return:
            :   The Current Track Object ID

        void (\*set\_current\_track\_id)(uint64\_t id)
        :   Set Current Track Object ID.

            Change the player’s current track to the track given by the ID. (Behaves similarly to the goto track command.)

            Param id:
            :   The ID of a track object

        uint64\_t (\*get\_next\_track\_id)(void)
        :   Read Next Track Object ID.

            Get an ID (48 bit) that can be used to retrieve the Next Track Object from an Object Transfer Service

            Return:
            :   The Next Track Object ID

        void (\*set\_next\_track\_id)(uint64\_t id)
        :   Set Next Track Object ID.

            Change the player’s next track to the track given by the ID.

            Param id:
            :   The ID of a track object

        uint64\_t (\*get\_parent\_group\_id)(void)
        :   Read Parent Group Object ID.

            Get an ID (48 bit) that can be used to retrieve the Parent Track Object from an Object Transfer Service

            The parent group is the parent of the current group.

            See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Track Object.

            Return:
            :   The Current Group Object ID

        uint64\_t (\*get\_current\_group\_id)(void)
        :   Read Current Group Object ID.

            Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

            See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Group Object.

            Return:
            :   The Current Group Object ID

        void (\*set\_current\_group\_id)(uint64\_t id)
        :   Set Current Group Object ID.

            Change the player’s current group to the group given by the ID, and the current track to the first track in that group.

            Param id:
            :   The ID of a group object

        uint8\_t (\*get\_playing\_order)(void)
        :   Read Playing Order.

            return The media player’s current playing order

        void (\*set\_playing\_order)(uint8\_t order)
        :   Set Playing Order.

            Set the media player’s playing order. See the MEDIA\_PROXY\_PLAYING\_ORDER\_\* defines.

            Param order:
            :   The playing order to set

        uint16\_t (\*get\_playing\_orders\_supported)(void)
        :   Read Playing Orders Supported.

            Read a bitmap containing the media player’s supported playing orders. See the MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_\* defines.

            Return:
            :   The media player’s supported playing orders

        uint8\_t (\*get\_media\_state)(void)
        :   Read Media State.

            Read the media player’s state See the MEDIA\_PROXY\_MEDIA\_STATE\_\* defines.

            Return:
            :   The media player’s state

        void (\*send\_command)(const struct [mpl\_cmd](#c.mpl_cmd) \*command)
        :   Send Command.

            Send a command to the media player. For command opcodes (play, pause, …) - see the MEDIA\_PROXY\_OP\_\* defines.

            Param command:
            :   The command to send

        uint32\_t (\*get\_commands\_supported)(void)
        :   Read Commands Supported.

            Read a bitmap containing the media player’s supported command opcodes. See the MEDIA\_PROXY\_OP\_SUP\_\* defines.

            Return:
            :   The media player’s supported command opcodes

        void (\*send\_search)(const struct [mpl\_search](#c.mpl_search) \*search)
        :   Set Search.

            Write a search to the media player. (For the formatting of a search, see the Media Control Service spec and the mcs.h file.)

            Param search:
            :   The search to write

        uint64\_t (\*get\_search\_results\_id)(void)
        :   Read Search Results Object ID.

            Get an ID (48 bit) that can be used to retrieve the Search Results Object from an Object Transfer Service

            The search results object is a group object. The search results object only exists if a successful search operation has been done.

            Return:
            :   The Search Results Object ID

        uint8\_t (\*get\_content\_ctrl\_id)(void)
        :   Read Content Control ID.

            The content control ID identifies a content control service on a device, and links it to the corresponding audio stream.

            Return:
            :   The content control ID for the media player

### Media Control Client

*group* Media Control Client (MCC)
:   Bluetooth Media Control Client (MCC) interface.

    Updated to the Media Control Profile specification revision 1.0

    **Since**
    :   3.0

    **Version**
    :   0.8.0

    Typedefs

    typedef void (\*bt\_mcc\_discover\_mcs\_cb)(struct bt\_conn \*conn, int err)
    :   Callback function for [bt\_mcc\_discover\_mcs()](#group__bt__gatt__mcc_1gaa1f9ead03b4cccaff1e3390b8052b0f3).

        Called when a media control server is discovered

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

    typedef void (\*bt\_mcc\_read\_player\_name\_cb)(struct bt\_conn \*conn, int err, const char \*name)
    :   Callback function for [bt\_mcc\_read\_player\_name()](#group__bt__gatt__mcc_1ga724ce71fc88f1ca4bcf209c92c177f36).

        Called when the player name is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param name:
        :   Player name

    typedef void (\*bt\_mcc\_read\_icon\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t icon\_id)
    :   Callback function for [bt\_mcc\_read\_icon\_obj\_id()](#group__bt__gatt__mcc_1ga0e69de33c37957a2b5473df7d3c3f389).

        Called when the icon object ID is read

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param icon\_id:
        :   The ID of the Icon Object. This is a UINT48 in a uint64\_t

    typedef void (\*bt\_mcc\_read\_icon\_url\_cb)(struct bt\_conn \*conn, int err, const char \*icon\_url)
    :   Callback function for [bt\_mcc\_read\_icon\_url()](#group__bt__gatt__mcc_1ga38733456db6bc6558a511e104577c9c9).

        Called when the icon URL is read

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param icon\_url:
        :   The URL of the Icon

    typedef void (\*bt\_mcc\_track\_changed\_ntf\_cb)(struct bt\_conn \*conn, int err)
    :   Callback function for track changed notifications.

        Called when a track change is notified.

        The track changed characteristic is a special case. It can not be read or set, it can only be notified.

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

    typedef void (\*bt\_mcc\_read\_track\_title\_cb)(struct bt\_conn \*conn, int err, const char \*title)
    :   Callback function for [bt\_mcc\_read\_track\_title()](#group__bt__gatt__mcc_1ga7dfa14489a4cea4b00053c9aa75cf373).

        Called when the track title is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param title:
        :   The title of the track

    typedef void (\*bt\_mcc\_read\_track\_duration\_cb)(struct bt\_conn \*conn, int err, int32\_t dur)
    :   Callback function for [bt\_mcc\_read\_track\_duration()](#group__bt__gatt__mcc_1ga50a45f043bd2ae1741a120e02e9dc2f5).

        Called when the track duration is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param dur:
        :   The duration of the track

    typedef void (\*bt\_mcc\_read\_track\_position\_cb)(struct bt\_conn \*conn, int err, int32\_t pos)
    :   Callback function for [bt\_mcc\_read\_track\_position()](#group__bt__gatt__mcc_1gaf143098f5dfcfba01df3d6f06472779e).

        Called when the track position is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param pos:
        :   The Track Position

    typedef void (\*bt\_mcc\_set\_track\_position\_cb)(struct bt\_conn \*conn, int err, int32\_t pos)
    :   Callback function for [bt\_mcc\_set\_track\_position()](#group__bt__gatt__mcc_1gad324366d33bef6b1ed1c8fc881bf44cf).

        Called when the track position is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param pos:
        :   The Track Position set (or attempted to set)

    typedef void (\*bt\_mcc\_read\_playback\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)
    :   Callback function for [bt\_mcc\_read\_playback\_speed()](#group__bt__gatt__mcc_1gaa566a4c42f0ab0ab6feddf4e25845609).

        Called when the playback speed is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param speed:
        :   The Playback Speed

    typedef void (\*bt\_mcc\_set\_playback\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)
    :   Callback function for [bt\_mcc\_set\_playback\_speed()](#group__bt__gatt__mcc_1ga1382e5b6000896dc94f6489909301719).

        Called when the playback speed is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param speed:
        :   The Playback Speed set (or attempted to set)

    typedef void (\*bt\_mcc\_read\_seeking\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)
    :   Callback function for [bt\_mcc\_read\_seeking\_speed()](#group__bt__gatt__mcc_1ga366fdfaa23cef9f1c3ba7ddd36a67658).

        Called when the seeking speed is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param speed:
        :   The Seeking Speed

    typedef void (\*bt\_mcc\_read\_segments\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for [bt\_mcc\_read\_segments\_obj\_id()](#group__bt__gatt__mcc_1ga4cb0a95e91d3ec00ede64663a2b932f0).

        Called when the track segments object ID is read

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Track Segments Object ID (UINT48)

    typedef void (\*bt\_mcc\_read\_current\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for [bt\_mcc\_read\_current\_track\_obj\_id()](#group__bt__gatt__mcc_1ga5b3a8fb8e8251cf005b34e47619ae7b9).

        Called when the current track object ID is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Current Track Object ID (UINT48)

    typedef void (\*bt\_mcc\_set\_current\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for [bt\_mcc\_set\_current\_track\_obj\_id()](#group__bt__gatt__mcc_1ga8374ac230c5fe6b5a1bb7fa873fdeb49).

        Called when the current track object ID is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Object ID (UINT48) set (or attempted to set)

    typedef void (\*bt\_mcc\_read\_next\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for bt\_mcc\_read\_next\_track\_obj\_id\_obj().

        Called when the next track object ID is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Next Track Object ID (UINT48)

    typedef void (\*bt\_mcc\_set\_next\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for [bt\_mcc\_set\_next\_track\_obj\_id()](#group__bt__gatt__mcc_1gafeebcbb0c77d5d4acbe151fd9888d084).

        Called when the next track object ID is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Object ID (UINT48) set (or attempted to set)

    typedef void (\*bt\_mcc\_read\_parent\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for [bt\_mcc\_read\_parent\_group\_obj\_id()](#group__bt__gatt__mcc_1ga3ccd5961cc4c8d82fa988d300e12e1ae).

        Called when the parent group object ID is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Parent Group Object ID (UINT48)

    typedef void (\*bt\_mcc\_read\_current\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for [bt\_mcc\_read\_current\_group\_obj\_id()](#group__bt__gatt__mcc_1ga8cb43a6947df48113b082d8cc8ccf25c).

        Called when the current group object ID is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Current Group Object ID (UINT48)

    typedef void (\*bt\_mcc\_set\_current\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t obj\_id)
    :   Callback function for [bt\_mcc\_set\_current\_group\_obj\_id()](#group__bt__gatt__mcc_1gae3f385811f852d584595c6e531556aed).

        Called when the current group object ID is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param obj\_id:
        :   The Object ID (UINT48) set (or attempted to set)

    typedef void (\*bt\_mcc\_read\_playing\_order\_cb)(struct bt\_conn \*conn, int err, uint8\_t order)
    :   Callback function for [bt\_mcc\_read\_playing\_order()](#group__bt__gatt__mcc_1ga077a134ff1404fb76aa756a5531fd1d7).

        Called when the playing order is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param order:
        :   The playback order

    typedef void (\*bt\_mcc\_set\_playing\_order\_cb)(struct bt\_conn \*conn, int err, uint8\_t order)
    :   Callback function for [bt\_mcc\_set\_playing\_order()](#group__bt__gatt__mcc_1ga05295649385c3a337401765627d09553).

        Called when the playing order is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param order:
        :   The Playing Order set (or attempted to set)

    typedef void (\*bt\_mcc\_read\_playing\_orders\_supported\_cb)(struct bt\_conn \*conn, int err, uint16\_t orders)
    :   Callback function for [bt\_mcc\_read\_playing\_orders\_supported()](#group__bt__gatt__mcc_1gaf61f6fcf3f96ccb6f5a72ffaad27dec4).

        Called when the supported playing orders are read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param orders:
        :   The playing orders supported (bitmap)

    typedef void (\*bt\_mcc\_read\_media\_state\_cb)(struct bt\_conn \*conn, int err, uint8\_t state)
    :   Callback function for [bt\_mcc\_read\_media\_state()](#group__bt__gatt__mcc_1gac1b440cfa54dd4b6e23bb47bf885f88d).

        Called when the media state is read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param state:
        :   The Media State

    typedef void (\*bt\_mcc\_send\_cmd\_cb)(struct bt\_conn \*conn, int err, const struct [mpl\_cmd](#c.mpl_cmd) \*cmd)
    :   Callback function for [bt\_mcc\_send\_cmd()](#group__bt__gatt__mcc_1ga3f4a538bcf436e4e80b73ed6e077dfa0).

        Called when a command is sent, i.e. when the media control point is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param cmd:
        :   The command sent

    typedef void (\*bt\_mcc\_cmd\_ntf\_cb)(struct bt\_conn \*conn, int err, const struct [mpl\_cmd\_ntf](#c.mpl_cmd_ntf) \*ntf)
    :   Callback function for command notifications.

        Called when the media control point is notified

        Notifications for commands (i.e. for writes to the media control point) use a different parameter structure than what is used for sending commands (writing to the media control point)

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param ntf:
        :   The command notification

    typedef void (\*bt\_mcc\_read\_opcodes\_supported\_cb)(struct bt\_conn \*conn, int err, uint32\_t opcodes)
    :   Callback function for [bt\_mcc\_read\_opcodes\_supported()](#group__bt__gatt__mcc_1ga692160554947f92e8c81912c5e597086).

        Called when the supported opcodes (commands) are read or notified

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param opcodes:
        :   The supported opcodes

    typedef void (\*bt\_mcc\_send\_search\_cb)(struct bt\_conn \*conn, int err, const struct [mpl\_search](#c.mpl_search) \*search)
    :   Callback function for [bt\_mcc\_send\_search()](#group__bt__gatt__mcc_1ga324161056e03195820bbd7cc77ff287d).

        Called when a search is sent, i.e. when the search control point is set

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param search:
        :   The search set (or attempted to set)

    typedef void (\*bt\_mcc\_search\_ntf\_cb)(struct bt\_conn \*conn, int err, uint8\_t result\_code)
    :   Callback function for search notifications.

        Called when the search control point is notified

        Notifications for searches (i.e. for writes to the search control point) use a different parameter structure than what is used for sending searches (writing to the search control point)

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param result\_code:
        :   The search notification

    typedef void (\*bt\_mcc\_read\_search\_results\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)
    :   Callback function for [bt\_mcc\_read\_search\_results\_obj\_id()](#group__bt__gatt__mcc_1ga98814a516a027bdaa3250e93d55309fd).

        Called when the search results object ID is read or notified

        Note that the Search Results Object ID value may be zero, in case the characteristic does not exist on the server. (This will be the case if there has not been a successful search.)

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param id:
        :   The Search Results Object ID (UINT48)

    typedef void (\*bt\_mcc\_read\_content\_control\_id\_cb)(struct bt\_conn \*conn, int err, uint8\_t ccid)
    :   Callback function for [bt\_mcc\_read\_content\_control\_id()](#group__bt__gatt__mcc_1ga77cbf810c35d1a17efce1fae6a941963).

        Called when the content control ID is read

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param ccid:
        :   The Content Control ID

    typedef void (\*bt\_mcc\_otc\_obj\_selected\_cb)(struct bt\_conn \*conn, int err)
    :   Callback function for object selected.

        Called when an object is selected

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

    typedef void (\*bt\_mcc\_otc\_obj\_metadata\_cb)(struct bt\_conn \*conn, int err)
    :   Callback function for [bt\_mcc\_otc\_read\_object\_metadata()](#group__bt__gatt__mcc_1gadf687cb26a6d00bca73e273da583df88).

        Called when object metadata is read

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

    typedef void (\*bt\_mcc\_otc\_read\_icon\_object\_cb)(struct bt\_conn \*conn, int err, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Callback function for [bt\_mcc\_otc\_read\_icon\_object()](#group__bt__gatt__mcc_1gaba527d8f0307ab11150a5434231c0e7e).

        Called when the icon object is read

        If err is EMSGSIZE, the object contents have been truncated.

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param buf:
        :   Buffer containing the object contents

    typedef void (\*bt\_mcc\_otc\_read\_track\_segments\_object\_cb)(struct bt\_conn \*conn, int err, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Callback function for [bt\_mcc\_otc\_read\_track\_segments\_object()](#group__bt__gatt__mcc_1gac22e840b65895aa018ab1b4535a87672).

        Called when the track segments object is read

        If err is EMSGSIZE, the object contents have been truncated.

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param buf:
        :   Buffer containing the object contents

    typedef void (\*bt\_mcc\_otc\_read\_current\_track\_object\_cb)(struct bt\_conn \*conn, int err, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Callback function for [bt\_mcc\_otc\_read\_current\_track\_object()](#group__bt__gatt__mcc_1gac4b09a77df52d2681e7652591ca32bf8).

        Called when the current track object is read

        If err is EMSGSIZE, the object contents have been truncated.

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param buf:
        :   Buffer containing the object contents

    typedef void (\*bt\_mcc\_otc\_read\_next\_track\_object\_cb)(struct bt\_conn \*conn, int err, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Callback function for [bt\_mcc\_otc\_read\_next\_track\_object()](#group__bt__gatt__mcc_1ga611c9edebff5b4347ad1241ffd19f49e).

        Called when the next track object is read

        If err is EMSGSIZE, the object contents have been truncated.

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param buf:
        :   Buffer containing the object contents

    typedef void (\*bt\_mcc\_otc\_read\_parent\_group\_object\_cb)(struct bt\_conn \*conn, int err, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Callback function for [bt\_mcc\_otc\_read\_parent\_group\_object()](#group__bt__gatt__mcc_1gae001cb2d701457ce083aa8a0fd5ec518).

        Called when the parent group object is read

        If err is EMSGSIZE, the object contents have been truncated.

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param buf:
        :   Buffer containing the object contents

    typedef void (\*bt\_mcc\_otc\_read\_current\_group\_object\_cb)(struct bt\_conn \*conn, int err, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*buf)
    :   Callback function for [bt\_mcc\_otc\_read\_current\_group\_object()](#group__bt__gatt__mcc_1ga4b1ebe682ad134795f8a1b494244f8b6).

        Called when the current group object is read

        If err is EMSGSIZE, the object contents have been truncated.

        Param conn:
        :   The connection that was used to initialise the media control client

        Param err:
        :   Error value. 0 on success, GATT error or errno on fail

        Param buf:
        :   Buffer containing the object contents

    Functions

    int bt\_mcc\_init(struct [bt\_mcc\_cb](#c.bt_mcc_cb) \*cb)
    :   Initialize Media Control Client.

        Parameters:
        :   - **cb** – Callbacks to be used

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_discover\_mcs(struct bt\_conn \*conn, bool subscribe)
    :   Discover Media Control Service.

        Discover Media Control Service (MCS) on the server given by the connection Optionally subscribe to notifications.

        Shall be called once, after media control client initialization and before using other media control client functionality.

        Parameters:
        :   - **conn** – Connection to the peer device
            - **subscribe** – Whether to subscribe to notifications

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_player\_name(struct bt\_conn \*conn)
    :   Read Media Player Name.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_icon\_obj\_id(struct bt\_conn \*conn)
    :   Read Icon Object ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_icon\_url(struct bt\_conn \*conn)
    :   Read Icon Object URL.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_track\_title(struct bt\_conn \*conn)
    :   Read Track Title.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_track\_duration(struct bt\_conn \*conn)
    :   Read Track Duration.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_track\_position(struct bt\_conn \*conn)
    :   Read Track Position.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_set\_track\_position(struct bt\_conn \*conn, int32\_t pos)
    :   Set Track position.

        Parameters:
        :   - **conn** – Connection to the peer device
            - **pos** – Track position

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_playback\_speed(struct bt\_conn \*conn)
    :   Read Playback speed.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_set\_playback\_speed(struct bt\_conn \*conn, int8\_t speed)
    :   Set Playback Speed.

        Parameters:
        :   - **conn** – Connection to the peer device
            - **speed** – Playback speed

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_seeking\_speed(struct bt\_conn \*conn)
    :   Read Seeking speed.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_segments\_obj\_id(struct bt\_conn \*conn)
    :   Read Track Segments Object ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_current\_track\_obj\_id(struct bt\_conn \*conn)
    :   Read Current Track Object ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_set\_current\_track\_obj\_id(struct bt\_conn \*conn, uint64\_t id)
    :   Set Current Track Object ID.

        Set the Current Track to the track given by the `id` parameter

        Parameters:
        :   - **conn** – Connection to the peer device
            - **id** – Object Transfer Service ID (UINT48) of the track to set as the current track

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_next\_track\_obj\_id(struct bt\_conn \*conn)
    :   Read Next Track Object ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_set\_next\_track\_obj\_id(struct bt\_conn \*conn, uint64\_t id)
    :   Set Next Track Object ID.

        Set the Next Track to the track given by the `id` parameter

        Parameters:
        :   - **conn** – Connection to the peer device
            - **id** – Object Transfer Service ID (UINT48) of the track to set as the next track

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_current\_group\_obj\_id(struct bt\_conn \*conn)
    :   Read Current Group Object ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_set\_current\_group\_obj\_id(struct bt\_conn \*conn, uint64\_t id)
    :   Set Current Group Object ID.

        Set the Current Group to the group given by the `id` parameter

        Parameters:
        :   - **conn** – Connection to the peer device
            - **id** – Object Transfer Service ID (UINT48) of the group to set as the current group

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_parent\_group\_obj\_id(struct bt\_conn \*conn)
    :   Read Parent Group Object ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_playing\_order(struct bt\_conn \*conn)
    :   Read Playing Order.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_set\_playing\_order(struct bt\_conn \*conn, uint8\_t order)
    :   Set Playing Order.

        Parameters:
        :   - **conn** – Connection to the peer device
            - **order** – Playing order

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_playing\_orders\_supported(struct bt\_conn \*conn)
    :   Read Playing Orders Supported.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_media\_state(struct bt\_conn \*conn)
    :   Read Media State.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_send\_cmd(struct bt\_conn \*conn, const struct [mpl\_cmd](#c.mpl_cmd) \*cmd)
    :   Send a command.

        Write a command (e.g. “play”, “pause”) to the server’s media control point.

        Parameters:
        :   - **conn** – Connection to the peer device
            - **cmd** – The command to send

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_opcodes\_supported(struct bt\_conn \*conn)
    :   Read Opcodes Supported.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_send\_search(struct bt\_conn \*conn, const struct [mpl\_search](#c.mpl_search) \*search)
    :   Send a Search command.

        Write a search to the server’s search control point.

        Parameters:
        :   - **conn** – Connection to the peer device
            - **search** – The search

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_search\_results\_obj\_id(struct bt\_conn \*conn)
    :   Search Results Group Object ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_read\_content\_control\_id(struct bt\_conn \*conn)
    :   Read Content Control ID.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_otc\_read\_object\_metadata(struct bt\_conn \*conn)
    :   Read the current object metadata.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_otc\_read\_icon\_object(struct bt\_conn \*conn)
    :   Read the Icon Object.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_otc\_read\_track\_segments\_object(struct bt\_conn \*conn)
    :   Read the Track Segments Object.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_otc\_read\_current\_track\_object(struct bt\_conn \*conn)
    :   Read the Current Track Object.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_otc\_read\_next\_track\_object(struct bt\_conn \*conn)
    :   Read the Next Track Object.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_otc\_read\_current\_group\_object(struct bt\_conn \*conn)
    :   Read the Current Group Object.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    int bt\_mcc\_otc\_read\_parent\_group\_object(struct bt\_conn \*conn)
    :   Read the Parent Group Object.

        Parameters:
        :   - **conn** – Connection to the peer device

        Returns:
        :   0 if success, errno on failure.

    struct [bt\_ots\_client](../services.md#c.bt_ots_client "bt_ots_client") \*bt\_mcc\_otc\_inst(struct bt\_conn \*conn)
    :   Look up MCC OTC instance.

        Parameters:
        :   - **conn** – The connection to the MCC server.

        Returns:
        :   Pointer to a MCC OTC instance if found else NULL.

    struct bt\_mcc\_cb
    :   *#include <mcc.h>*

        Media control client callbacks.

        Public Members

        [bt\_mcc\_discover\_mcs\_cb](#c.bt_mcc_discover_mcs_cb) discover\_mcs
        :   Callback when discovery has finished.

        [bt\_mcc\_read\_player\_name\_cb](#c.bt_mcc_read_player_name_cb) read\_player\_name
        :   Callback when reading the player name.

        [bt\_mcc\_read\_icon\_obj\_id\_cb](#c.bt_mcc_read_icon_obj_id_cb) read\_icon\_obj\_id
        :   Callback when reading the icon object ID.

        [bt\_mcc\_read\_icon\_url\_cb](#c.bt_mcc_read_icon_url_cb) read\_icon\_url
        :   Callback when reading the icon URL.

        [bt\_mcc\_track\_changed\_ntf\_cb](#c.bt_mcc_track_changed_ntf_cb) track\_changed\_ntf
        :   Callback when getting a track changed notification.

        [bt\_mcc\_read\_track\_title\_cb](#c.bt_mcc_read_track_title_cb) read\_track\_title
        :   Callback when reading the track title.

        [bt\_mcc\_read\_track\_duration\_cb](#c.bt_mcc_read_track_duration_cb) read\_track\_duration
        :   Callback when reading the track duration.

        [bt\_mcc\_read\_track\_position\_cb](#c.bt_mcc_read_track_position_cb) read\_track\_position
        :   Callback when reading the track position.

        [bt\_mcc\_set\_track\_position\_cb](#c.bt_mcc_set_track_position_cb) set\_track\_position
        :   Callback when setting the track position.

        [bt\_mcc\_read\_playback\_speed\_cb](#c.bt_mcc_read_playback_speed_cb) read\_playback\_speed
        :   Callback when reading the playback speed.

        [bt\_mcc\_set\_playback\_speed\_cb](#c.bt_mcc_set_playback_speed_cb) set\_playback\_speed
        :   Callback when setting the playback speed.

        [bt\_mcc\_read\_seeking\_speed\_cb](#c.bt_mcc_read_seeking_speed_cb) read\_seeking\_speed
        :   Callback when reading the seeking speed.

        [bt\_mcc\_read\_segments\_obj\_id\_cb](#c.bt_mcc_read_segments_obj_id_cb) read\_segments\_obj\_id
        :   Callback when reading the segments object ID.

        [bt\_mcc\_read\_current\_track\_obj\_id\_cb](#c.bt_mcc_read_current_track_obj_id_cb) read\_current\_track\_obj\_id
        :   Callback when reading the current track object ID.

        [bt\_mcc\_set\_current\_track\_obj\_id\_cb](#c.bt_mcc_set_current_track_obj_id_cb) set\_current\_track\_obj\_id
        :   Callback when setting the current track object ID.

        [bt\_mcc\_read\_next\_track\_obj\_id\_cb](#c.bt_mcc_read_next_track_obj_id_cb) read\_next\_track\_obj\_id
        :   Callback when reading the next track object ID.

        [bt\_mcc\_set\_next\_track\_obj\_id\_cb](#c.bt_mcc_set_next_track_obj_id_cb) set\_next\_track\_obj\_id
        :   Callback when setting the next track object ID.

        [bt\_mcc\_read\_current\_group\_obj\_id\_cb](#c.bt_mcc_read_current_group_obj_id_cb) read\_current\_group\_obj\_id
        :   Callback when reading the current group object ID.

        [bt\_mcc\_set\_current\_group\_obj\_id\_cb](#c.bt_mcc_set_current_group_obj_id_cb) set\_current\_group\_obj\_id
        :   Callback when setting the current group object ID.

        [bt\_mcc\_read\_parent\_group\_obj\_id\_cb](#c.bt_mcc_read_parent_group_obj_id_cb) read\_parent\_group\_obj\_id
        :   Callback when reading the parent group object ID.

        [bt\_mcc\_read\_playing\_order\_cb](#c.bt_mcc_read_playing_order_cb) read\_playing\_order
        :   Callback when reading the playing order.

        [bt\_mcc\_set\_playing\_order\_cb](#c.bt_mcc_set_playing_order_cb) set\_playing\_order
        :   Callback when setting the playing order.

        [bt\_mcc\_read\_playing\_orders\_supported\_cb](#c.bt_mcc_read_playing_orders_supported_cb) read\_playing\_orders\_supported
        :   Callback when reading the supported playing orders.

        [bt\_mcc\_read\_media\_state\_cb](#c.bt_mcc_read_media_state_cb) read\_media\_state
        :   Callback when reading the media state.

        [bt\_mcc\_send\_cmd\_cb](#c.bt_mcc_send_cmd_cb) send\_cmd
        :   Callback when sending a command.

        [bt\_mcc\_cmd\_ntf\_cb](#c.bt_mcc_cmd_ntf_cb) cmd\_ntf
        :   Callback command notifications.

        [bt\_mcc\_read\_opcodes\_supported\_cb](#c.bt_mcc_read_opcodes_supported_cb) read\_opcodes\_supported
        :   Callback when reading the supported opcodes.

        [bt\_mcc\_send\_search\_cb](#c.bt_mcc_send_search_cb) send\_search
        :   Callback when sending the a search query.

        [bt\_mcc\_search\_ntf\_cb](#c.bt_mcc_search_ntf_cb) search\_ntf
        :   Callback when receiving a search notification.

        [bt\_mcc\_read\_search\_results\_obj\_id\_cb](#c.bt_mcc_read_search_results_obj_id_cb) read\_search\_results\_obj\_id
        :   Callback when reading the search results object ID.

        [bt\_mcc\_read\_content\_control\_id\_cb](#c.bt_mcc_read_content_control_id_cb) read\_content\_control\_id
        :   Callback when reading the content control ID.

        [bt\_mcc\_otc\_obj\_selected\_cb](#c.bt_mcc_otc_obj_selected_cb) otc\_obj\_selected
        :   Callback when selecting an object.

        [bt\_mcc\_otc\_obj\_metadata\_cb](#c.bt_mcc_otc_obj_metadata_cb) otc\_obj\_metadata
        :   Callback when receiving the current object metadata.

        [bt\_mcc\_otc\_read\_icon\_object\_cb](#c.bt_mcc_otc_read_icon_object_cb) otc\_icon\_object
        :   Callback when reading the current icon object.

        [bt\_mcc\_otc\_read\_track\_segments\_object\_cb](#c.bt_mcc_otc_read_track_segments_object_cb) otc\_track\_segments\_object
        :   Callback when reading the track segments object.

        [bt\_mcc\_otc\_read\_current\_track\_object\_cb](#c.bt_mcc_otc_read_current_track_object_cb) otc\_current\_track\_object
        :   Callback when reading the current track object.

        [bt\_mcc\_otc\_read\_next\_track\_object\_cb](#c.bt_mcc_otc_read_next_track_object_cb) otc\_next\_track\_object
        :   Callback when reading the next track object.

        [bt\_mcc\_otc\_read\_current\_group\_object\_cb](#c.bt_mcc_otc_read_current_group_object_cb) otc\_current\_group\_object
        :   Callback when reading the current group object.

        [bt\_mcc\_otc\_read\_parent\_group\_object\_cb](#c.bt_mcc_otc_read_parent_group_object_cb) otc\_parent\_group\_object
        :   Callback when reading the parent group object.
