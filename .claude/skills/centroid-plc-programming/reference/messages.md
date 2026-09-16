# Operator Messages — `MSG`

Source: `docs/official/centroid_plc_programming_manual.pdf` (PLC Manual, rev8 07/24/26). The
manual prints no page numbers; citations below are PDF page numbers, verified with
`pdftotext -layout -f N -l N docs/official/centroid_plc_programming_manual.pdf -`.

---

## Message types

There are two kinds of PLC message (PLC Manual, PDF p.18):

- **Synchronous** — displayed only while `SV_STOP` is SET, sent from a dedicated Stage that is
  the last Stage in the program and is SET only when a message needs to be printed.
- **Asynchronous** — printed immediately, usually inline with the rest of the code.

Only one message can be displayed per pass of the PLC program; a new `MSG` overwrites whatever
was displayed before, and there is no queue (PLC Manual, PDF p.18). To show the same message
again, a different message number of the same type (Sync or Async) must be sent first —
for Synchronous messages, that different number must also be nonzero — or the program will sit
in the fault state with no message displayed (PLC Manual, PDF p.18). Sending a message
requires a Word variable: `IF 1==1 THEN MSG W1` (PLC Manual, PDF p.18).

## Encoding formula

```
Word Value = type + 256 x MessageNumber
```

`type` is `1` for Synchronous or `2` for Asynchronous; `MessageNumber` is the entry number in
the first column of `plcmsg.txt` (PLC Manual, PDF p.18).

| Message Number | Type | Word Value | Notes |
|---|---|---|---|
| 1 | Synchronous | 257 | `1 + 1*256` |
| 2 | Asynchronous | 514 | `2 + 2*256` |
| 25 | Synchronous | 6401 | `1 + 25*256` |
| 50 | Asynchronous | 12802 | `2 + 50*256` |

(PLC Manual, PDF p.18)

It is easiest, and less error-prone, to define a Constant for the message number once and store
it to a Word before sending it (PLC Manual, PDF p.18):

```
INP13_GREEN_MSG IS (2 + 1*256)   ;258   — PLC Manual, PDF p.18
INP13_RED_MSG   IS (2 + 2*256)   ;514   — PLC Manual, PDF p.18
```

---

## Worked example

The manual's own example program (PLC Manual, PDF p.18-19) defines Sync and Async message
constants, an Input for each, and a `SetErrorStage` that sends the Synchronous message:

```
INP13_GREEN_MSG IS (2 + 1*256)           ;258
INP13_RED_MSG   IS (2 + 2*256)           ;514
INP14_GREEN_MSG IS (1 + 3*256)   ;769
NO_SYNC_MSG     IS (1 + 99*256) ;25345
NO_ASYNC_MSG    IS (2 + 100*256) ;25602

Async_I         IS INP13
Sync_I          IS INP14

Async_O         IS OUT13
Sync_O          IS OUT14

Sync_Cleared_M  IS MEM1

Sync_W          IS W1
Async_W         IS W2

;=============================================================================
InitialStage
;=============================================================================
IF 1==1 THEN Sync_W = NO_SYNC_MSG, Async_W = NO_ASYNC_MSG,
             RST InitialStage, SET MainStage

;=============================================================================
                     MainStage
;=============================================================================
;sync
IF Sync_I THEN Sync_W = INP14_GREEN_MSG, SET SV_STOP, SET SetErrorStage, SET Sync_O
IF !Sync_I && Sync_O THEN SET Sync_Cleared_M

;async
IF Async_I THEN Async_W = INP13_GREEN_MSG, MSG Async_W, SET Async_O
IF !Async_I THEN Async_W = INP13_RED_MSG , MSG Async_W, RST Async_O

;=============================================================================
                     SetErrorStage
;=============================================================================
IF 1==1 THEN MSG Sync_W
IF Sync_W == NO_SYNC_MSG && Sync_Cleared_M THEN RST SetError
```

(PLC Manual, PDF p.19; trimmed to the message-relevant lines.)

The corresponding `plcmsg.txt` for this example (PLC Manual, PDF p.19-20):

```
1   9001 Input 13 Green
2   9002 Input 13 Red
3   9003 Input 14 Green
99 9099 No SYNC Message
100 9010 No ASYNC Message
```

The `Async_W` values sent by the example (`258`, `514`) decode with the formula above to
message numbers `1` and `2` — the same numbers as the `plcmsg.txt` entries `1` and `2`
(PLC Manual, PDF p.18-20).

---

## `plcmsg.txt` format

`plcmsg.txt` lists every message the PLC program can send to CNC12. Typical (stock) messages
should not be overwritten; new custom messages are added as new numbers instead
(PLC Manual, PDF p.20). Each line has three space-separated fields, with no comments allowed
since all text to the end of the line is the message itself (PLC Manual, PDF p.20):

```
MessageNumber MessageLogNumber Message
```

- **MessageNumber** — is the same number as the one encoded in the `MSG` Word
  (PLC Manual, PDF p.20).
- **MessageLogNumber** — logs the message to `msglog.txt` when parameter 140's Log Level is set
  to 4; the `9xxx` series is reserved for PLC program usage (PLC Manual, PDF p.20).
- **Message** — the text displayed on the CNC12 screen, extending to end of line
  (PLC Manual, PDF p.20).
