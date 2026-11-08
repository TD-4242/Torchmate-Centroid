+ Torchmate router on Centroid Acorn, CNC12 Router (inch), for VCarve Pro 12.5.
+ Every tool, including the first, gets T_ M6 (mfunc6.mac parks, prompts and re-measures) then G43 H_.
+ #300 carries the tool name to the mfunc76.mac prompt; CNC12 strings can't hold a double quote.

POST_NAME = "Torchmate Centroid (inch) (*.nc)"

FILE_EXTENSION = "nc"

UNITS = "INCHES"

LINE_ENDING = "[13][10]"

SUBSTITUTE = "[34]'"

+ Run TOOLCHANGE and NEW_SEGMENT for the first toolpath too, so the first tool is measured.
FIRST_TOOLPATH_NEW_SEGMENT = YES

+ X, Y and Z always output: after M6 the machine is at the touch-off, not where Vectric last left it.
VAR SPINDLE_SPEED = [S|A|S|1.0]
VAR FEED_RATE = [F|C|F|1.1]
VAR CUT_RATE = [FC|C|F|1.1]
VAR PLUNGE_RATE = [FP|C|F|1.1]
VAR X_POSITION = [X|A|X|1.4]
VAR Y_POSITION = [Y|A|Y|1.4]
VAR Z_POSITION = [Z|A|Z|1.4]
VAR ARC_CENTRE_I_INC_POSITION = [I|A|I|1.4]
VAR ARC_CENTRE_J_INC_POSITION = [J|A|J|1.4]
VAR X_HOME_POSITION = [XH|A|X|1.4]
VAR Y_HOME_POSITION = [YH|A|Y|1.4]
VAR DWELL_TIME = [DWELL|A|P|1.2]

begin HEADER

"; [TP_FILENAME]  [DATE] [TIME]"
"; Tools: [TOOLS_USED]"
"G20 G17 G40 G49 G80 G90 G94"
"G54"
"M25"

begin TOOLCHANGE

"M5"
"#300 = [34][TOOLNAME][34]"
"T[T] M6"
"G43 H[T]"

+ Also runs after every TOOLCHANGE. The trim router has no speed control; G4 gives it time to spin up.
begin NEW_SEGMENT

"; [TOOLPATH_NAME]"
"[S] M3"
"G4 P3"

begin INITIAL_RAPID_MOVE

"G0 [X] [Y]"
"G0 [Z]"

begin RAPID_MOVE

"G0 [X] [Y] [Z]"

begin FEED_MOVE

"G1 [X] [Y] [Z] [F]"

begin CW_ARC_MOVE

"G2 [X] [Y] [Z] [I] [J] [F]"

begin CCW_ARC_MOVE

"G3 [X] [Y] [Z] [I] [J] [F]"

begin FIRST_CW_HELICAL_ARC_PLUNGE_MOVE

"G2 [X] [Y] [Z] [I] [J] [F]"

begin FIRST_CCW_HELICAL_ARC_PLUNGE_MOVE

"G3 [X] [Y] [Z] [I] [J] [F]"

begin CW_HELICAL_ARC_MOVE

"G2 [X] [Y] [Z] [I] [J] [F]"

begin CCW_HELICAL_ARC_MOVE

"G3 [X] [Y] [Z] [I] [J] [F]"

begin DWELL_MOVE

"G4 [DWELL]"

begin FOOTER

"M5"
"M25"
"G49"
"G0 [XH] [YH]"
"M30"
