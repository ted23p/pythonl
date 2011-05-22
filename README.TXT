== Features ==

Reads the hashbang of a script so that you don't have to manually switch between Python 2.x and 3.x

Keep the CMD shell open so you can see the result and re-run commands

Works on Double-click and Open with IDLE


== Usage ==

This script makes Python 3 the default executable.

To run under Python 2, add this to the first line of your script:
#!/usr/bin/env python2


== Install ==

Double-click on pythonl.reg and allow it to be added to the registry.

Put pythonl.bat and pythonl.py in your Python 3 install folder.

You can now:
Double-click a .py or .pyw
Right-click -> Open with IDLE

If you want to be able to call pythonl with arguments, Python 3 must be in PATH.
There is a tool to do that for you included in Python:
Tools\Scripts\win_add2path.py


== How To Uninstall ==

Double-click on pythonl_restore.reg and allow it to be added to the registry.

Remove pythonl.bat and pythonl.py from you Python 3 install folder.