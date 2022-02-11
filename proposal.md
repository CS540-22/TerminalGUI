# TerminalGui

Ankush & ChaoHui & Hunter


  * [Introduction](#introduction)
  * [Customer Value](#customer-value)
  * [Proposed Solution & Technology](#proposed-solution---technology)
  * [Team](#team)
  * [Project Management](#project-management)



## Introduction




## Customer Value




## Proposed Solution & Technology

Our software can be broken down into three parts:
  - The user interface allows users interactively to select, search, click, execute, add, and remove commands.
  - The filesystem or server to store the commands.
  - The ability to execute arbitrary shell commands.


To accomplish this, we decide to choose `Python` as our primary language for several reasons.
  - `Python` has well-developed `GUI` libraries, such as `PyQt5`, `Tkinter`, etc.
  - `Python` can execute an arbitrary shell command and capture the output.
  - All of our team members have experience with `Python`


Our team has decided that `Tkinter` is the best choice to render the user interface. For the user interface display, a drop-down menu, radio button, checkbox, regular button, and text box widgets are mainly used. `Tkinter` is a cross-platform GUI library and supports a variety of widgets. These widgets also offer customizability. For example, we can easily emphasize the text by coloring it.

We can either use the filesystem or database to store the commands. For the simplicity of our project and limited time, we decide to go with the filesystem and use the `JSON` format. This file will store an array of `JSON` commands. One of the examples is shown below.

```json
{
  "command_name": "g++",
  "categories": {
    "C++ Version": {
      "widget_type": "radio_button",
      "options": ["--std=c++98", "--std=c++11", "--std=c++20"],
      "description": ["Use c++98", "Use c++11", "Use c++20"]
    },
    "Output": {
      "widget_type": "text",
      "description": "The name of the executable"
    },
    "Optimization": {
      "widget_type": "radio_button",
      "options": ["-O1", "-O2", "-O3"],
      "description": ["Optimize", "Optimize", "Optimize"]
    },
    "Warnings": {
      "widget_type": "checkbox",
      "options": ["-Werror", "-Wall"],
      "description": ["Make all warnings into errors", "Show all warnings"]
    }
  }
}
```


Finally,




## Team
  - ChaoHui: czheng4@vols.utk.edu
  - Hunter: hleef@vols.utk.edu
  - Ankush: apatel79@vols.utk.edu



## Project Management