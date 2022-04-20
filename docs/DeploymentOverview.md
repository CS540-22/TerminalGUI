# Deployment Overview
## How to Deploy TerminalGUI
1. Ensure the user system has all requirements: MacOS, python3, Tkinter (should be included with standard MacOS python installations).
2. Clone the repo.
3. While in the TerminalGUI directory, run: "python src/main.py".

## Current Limitations
- The user must have experience with the terminal, their OS must be MacOS, and they must be able to clone our repo.
- Even if the user has MacOS, there may be differences between specific versions. ChaoHui's Mac runs our software as intended, but Hunter's Mac does not (display is off center).

## Future Goals for Deployment/Development
- Fix the issue between different operating environments within the same OS and expand operating systems supported.
- Ultimately, a packaged executable would be desirable instead of launching the overlay from within the terminal.
  - One possibility is to use pyinstaller (a package for converting a python app into a single package), however, a preliminary test was non-functional.
  - This is likely due to the directory structure and should be easily addressable with tweaks to the source code (though we know these modifications can wreck original functionality as discussed in lecture and thus it must still be done with care).
  - Additionally, requirements would not change should pyinstaller be utilized and thus the user environment remains a large factor in successful operation.
