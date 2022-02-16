# TerminalGui

Ankush & ChaoHui & Hunter


  * [Introduction](#introduction)
  * [Customer Value](#customer-value)
  * [Proposed Solution & Technology](#proposed-solution---technology)
  * [Team](#team)
  * [Project Management](#project-management)



## Introduction




## Customer Value

Customer Need
 - Primary customer: everyday programmers and unix-based terminal users.
 - Desire: a streamlined, interactive terminal experience that has a flexible memory and personal customization.
 - Rationale: the terminal's history is limited on its own and generally consists of cycling up previously issued commands to find what they might need to execute again. Each user will have their own unique set of frequently used commands and command archetypes and so tailoring the terminal experience to these needs can improve productivity.
 - Market context: this tool will not likely be used in a corporate environment unless it first develops a substantial independent user-base. Most corporations already have a work environment already set up for all workers whereas independent users have flexibility in their choice of terminal environment.

Proposed Solution
 - Customer expectation: a streamlined terminal experience.
 - Benefits: improved productivity.
 - Novelty: the UI and expanded history services are arguably an improvement on ease of use.
 - Test status: untested.

Measures of Success
 - User surveys and reviews.
 - If possible, a user study with case and control volunteers to gauge productivity gains/losses and overall ease-of-use.


## Proposed Solution & Technology

Our software can be broken down into three parts:
  - The user interface that allows users interactively to select, search, click, execute, add, and remove commands.
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


Finally, Python's `subprocess` module can invoke shell command and capture the stdout and stderr and render it in the user interface. 




## Team
  - ChaoHui: czheng4@vols.utk.edu
  - Hunter: hleef@vols.utk.edu
  - Ankush: apatel79@vols.utk.edu



## Project Management
  

Each sprint is a two-week period. 



  - `Sprint 1:` Write the proposal.
  - `Sprint 2:` Design, and implement the non-active user interface, and collect the most frequent-used command lines.
  - `Sprint 3:` Implement events in our user interface (click a button, select an item from the menu, etc).
  - `Sprint 4:` Implement search box to search for command line based on the description. Implement the backend where users can add their own commands.
  - `Sprint 5:` Show the outputs of each command among pipes.
  - `Sprint 6:` Shortcuts for executing commands.
  - `Sprint 7:` Makefile auto generator (if time allows).

  
## Development Process

- Our team has elected to use the agile development method as it is an iterative and flexible
approach. Our team is already familiar with this approach and thus we all feel most
comfortable with it plus we already have an overall picture of how our software should work
to serve our customer. This contrasts with two other methods we considered: waterfall and
extreme programming.
- The waterfall method is too strict and linear for our team dynamic not
to mention that it the planning stage can take up a significant time if not organized properly.
Our team does not feel a need to spend so much time planning, as I mentioned we have a overall
picture of how things should work out and thus having the freedom provided by the agile method
is perferred.
- Extreme programming could fit our project as it is arguably as flexible as agile,
however with our team size being 3 members strong it seems like it would be a challenge (mainly
regarding pair programming). Extreme programming can lead to cleaner coding, but as our team
is small and we know we can work well together it becomes less of concern and so ultimately
agile remains our choice due to familiarity.

