Use Case 1 -- Moving the curser after typing a command.

- Actor: TerminalGUI user.

- Basic flow: One moment the user is typing in a command they want to
execute in the first window of the TerminalGUI app which is similar
to the default terminal. However, the user notices a typo in the middle of
the command they have typed so they want to move the cursor quickly to
that specific spot. The user clicks on the location of the typo and thus the
cursor is where they need it to be. The user then fixes the typo and
executes the corrected command.

Use Case 2 -- Visually selecting command.

- Actor: TerminalGUI user.

- Basic flow: The user is on the second window of the TerminalGUI app and
wants to execute a common compilation command, "g++ -std=c++98 -Wall -Werror
-o". First they click on the "filters" dropdown just below the window bar and
select "compilation". Next they click on "g++" which then fills the current
window with common flags associated with "g++". The user selects each of the
flags they desire, and then clicks the "execute" button on the bottom right
of the window. This brings the user to the first window where they can
type in the remainder of the command: the executable name and name of the
cpp source. The user then hits enter and their code is compiled.
