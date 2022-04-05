# TerminalGUI


Extended GUI for Terminal/Command Line

This gui will allow users to quickly select/search from a variety
of well-known commands and subsequently execute them in the terminal.

The aim of this tool is to alleviate the stress of recalling previously
used commands and having to type them out by creating a more visual
and interactive terminal experience.

Take, for example, compiling C++ code. Simpler compilation commands are
easy to remember, but ultimately there are a multitude of flags that can
change the compilation result and it can be hard to recall them
whenever a particular set of flags may be needed.

This interface will have categories of possible commands to execute
as well as sub-categories for things such as flags and other variables.

Team:
  - ChaoHui: czheng4@vols.utk.edu
  - Hunter: hleef@vols.utk.edu
  - Ankush: apatel79@vols.utk.edu


# How to run code
```
python src/main.py
```


# Static analysis
```
pylint src/main.py
************* Module main
src/main.py:7:37: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:63:0: C0301: Line too long (104/100) (line-too-long)
src/main.py:64:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:68:0: C0301: Line too long (106/100) (line-too-long)
src/main.py:72:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:122:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:136:0: C0301: Line too long (104/100) (line-too-long)
src/main.py:144:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:157:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:162:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:207:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:214:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:218:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:219:0: C0301: Line too long (101/100) (line-too-long)
src/main.py:252:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:280:50: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:283:0: C0301: Line too long (108/100) (line-too-long)
src/main.py:298:0: C0301: Line too long (131/100) (line-too-long)
src/main.py:342:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:345:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:346:0: C0301: Line too long (114/100) (line-too-long)
src/main.py:348:0: C0301: Line too long (111/100) (line-too-long)
src/main.py:372:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:373:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:381:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:386:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:387:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:398:0: C0303: Trailing whitespace (trailing-whitespace)
src/main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/main.py:4:0: W0401: Wildcard import tkinter (wildcard-import)
src/main.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:30:0: C0115: Missing class docstring (missing-class-docstring)
src/main.py:36:4: C0103: Method name "addTab" doesn't conform to snake_case naming style (invalid-name)
src/main.py:36:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:41:4: C0103: Method name "getTabByName" doesn't conform to snake_case naming style (invalid-name)
src/main.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:44:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:47:0: C0115: Missing class docstring (missing-class-docstring)
src/main.py:58:4: C0103: Method name "enterCallback" doesn't conform to snake_case naming style (invalid-name)
src/main.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:69:8: W0702: No exception type(s) specified (bare-except)
src/main.py:77:39: C0321: More than one statement on a single line (multiple-statements)
src/main.py:85:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:86:8: C0103: Variable name "fp" doesn't conform to snake_case naming style (invalid-name)
src/main.py:85:34: W0613: Unused argument 'event' (unused-argument)
src/main.py:91:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:91:36: W0613: Unused argument 'event' (unused-argument)
src/main.py:95:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:99:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:99:27: W0613: Unused argument 'event' (unused-argument)
src/main.py:105:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:124:4: C0103: Method name "newCommand" doesn't conform to snake_case naming style (invalid-name)
src/main.py:124:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:114:8: W0201: Attribute 'frame' defined outside __init__ (attribute-defined-outside-init)
src/main.py:120:8: W0201: Attribute 'canvas' defined outside __init__ (attribute-defined-outside-init)
src/main.py:143:0: C0115: Missing class docstring (missing-class-docstring)
src/main.py:143:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
src/main.py:155:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
src/main.py:155:43: C0103: Variable name "f" doesn't conform to snake_case naming style (invalid-name)
src/main.py:158:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:159:8: C0103: Variable name "fp" doesn't conform to snake_case naming style (invalid-name)
src/main.py:158:34: W0613: Unused argument 'event' (unused-argument)
src/main.py:164:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:164:36: W0613: Unused argument 'event' (unused-argument)
src/main.py:168:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:172:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:172:27: W0613: Unused argument 'event' (unused-argument)
src/main.py:177:25: W0622: Redefining built-in 'id' (redefined-builtin)
src/main.py:177:4: C0103: Method name "getCommand" doesn't conform to snake_case naming style (invalid-name)
src/main.py:177:25: C0103: Argument name "id" doesn't conform to snake_case naming style (invalid-name)
src/main.py:177:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:181:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:182:14: E1101: Instance of 'UserCommands' has no 'var' member (no-member)
src/main.py:183:8: W0107: Unnecessary pass statement (unnecessary-pass)
src/main.py:188:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:191:22: W0622: Redefining built-in 'id' (redefined-builtin)
src/main.py:191:22: C0103: Argument name "id" doesn't conform to snake_case naming style (invalid-name)
src/main.py:191:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:195:12: C0103: Variable name "f" doesn't conform to snake_case naming style (invalid-name)
src/main.py:196:44: C0321: More than one statement on a single line (multiple-statements)
src/main.py:210:4: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:210:4: R0914: Too many local variables (20/15) (too-many-locals)
src/main.py:230:8: C0103: Variable name "fp" doesn't conform to snake_case naming style (invalid-name)
src/main.py:241:12: C0103: Variable name "f" doesn't conform to snake_case naming style (invalid-name)
src/main.py:244:12: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
src/main.py:251:41: C0321: More than one statement on a single line (multiple-statements)
src/main.py:254:16: C0103: Variable name "f" doesn't conform to snake_case naming style (invalid-name)
src/main.py:271:28: C0103: Variable name "rb" doesn't conform to snake_case naming style (invalid-name)
src/main.py:283:24: C0103: Variable name "cb" doesn't conform to snake_case naming style (invalid-name)
src/main.py:295:12: C0103: Variable name "f" doesn't conform to snake_case naming style (invalid-name)
src/main.py:210:4: R0915: Too many statements (59/50) (too-many-statements)
src/main.py:222:8: W0201: Attribute 'frame' defined outside __init__ (attribute-defined-outside-init)
src/main.py:228:8: W0201: Attribute 'canvas' defined outside __init__ (attribute-defined-outside-init)
src/main.py:361:0: C0116: Missing function or method docstring (missing-function-docstring)
src/main.py:4:0: W0614: Unused import(s) enum, sys, TclError, re, wantobjects, TkVersion, TclVersion, READABLE, WRITABLE, EXCEPTION, EventType, Event, NoDefaultRoot, Variable, StringVar, IntVar, DoubleVar, BooleanVar, mainloop, getint, getdouble, getboolean, Misc, CallWrapper, XView, YView, Wm, Tk, Tcl, Pack, Place, Grid, BaseWidget, Widget, Toplevel, Button, Canvas, Checkbutton, Entry, Frame, Label, Listbox, Menu, Menubutton, Message, Radiobutton, Scale, Scrollbar, Text, OptionMenu, Image, PhotoImage, BitmapImage, image_names, image_types, Spinbox, LabelFrame, PanedWindow, NO, FALSE, OFF, YES, TRUE, ON, N, S, W, E, NW, SW, NE, SE, NS, EW, NSEW, CENTER, NONE, X, Y, BOTH, LEFT, TOP, RIGHT, BOTTOM, RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID, HORIZONTAL, VERTICAL, NUMERIC, CHAR, WORD, BASELINE, INSIDE, OUTSIDE, SEL, SEL_FIRST, SEL_LAST, INSERT, CURRENT, ANCHOR, ALL, NORMAL, DISABLED, ACTIVE, HIDDEN, CASCADE, CHECKBUTTON, COMMAND, RADIOBUTTON, SEPARATOR, SINGLE, BROWSE, MULTIPLE, EXTENDED, DOTBOX, UNDERLINE, PIESLICE, CHORD, ARC, FIRST, LAST, BUTT, PROJECTING, ROUND, BEVEL, MITER, MOVETO, SCROLL, UNITS and PAGES from wildcard import of tkinter (unused-wildcard-import)
src/main.py:4:0: C0412: Imports from package tkinter are not grouped (ungrouped-imports)

------------------------------------------------------------------
Your code has been rated at 4.83/10 (previous run: 4.83/10, +0.00)

```