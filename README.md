# BRUSH_MANAGER
This addon does the following:

1. It auto-loads custom brushes from blend files found in blender/bin/2.81/datafiles/brushes on Windows and Blender.app/Contents/Resources/2.81/datafiles/brushes on MacOS
- If for some reason you add a custom brush while blender is running, you can click on File->Reload Custom Brushes so that it can pickup the new brushes
2. It adds a save option under the brush_context_menu (small arrow next to the icon of the brush in the properties window)
- Each brush is saved as an individual file so it can be shared.
- To share more than one, just zip them
3. Finally, it enables a custom quick-menu (like the brush selector in zBrush) that shows all the builtin and custom brushes for quick access. (Shift-Space)

That's it! I do have more plans for the addon like: 1) Put the save option as an icon next to the "Add brush" option and just below the brush icon in the properties section. 2) Incorporate the quick menu into the actual toolbar instead of making my own menu.

Enjoy!

Abinadi
