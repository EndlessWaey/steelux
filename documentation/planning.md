# Planning

I use this file for planning and tracking features I wish to implement.

Features that need implementing:

- Native way to gain write access to the mouse / Eliminating the need to run a shell command in order to gain necessary permissions to the mouse on the OS level. Find a way to do it in python natively. _Subprocess_ should probably do the trick.
- Make a proper package out of this software that can be installed via a package manager and/or pip. A pyproject.toml was already created but it doesn't work currently. Nice.
- Proper Logging. Stop printing a shitload of information to the stdout. Do proper printing of errors to stderr and give users an option to explicitly ask for verbose output, otherwise: talk as little as possible.