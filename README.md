CLEAR RELATIVE TRANSFORM BLENDER ADDON
--------------------------------------

Blender has a weird issue when objects are attached to each other. Instead of change the object's transform to be relative to the parent's identity, it uses an internal property as an base transform and keeps the values of the old transform. It's impossible to actual see the transform relative to the parent in the editor's panels.

This addon tries to fix that. The command "Clear Relative Transform" fixes the transforms of the selected objects.

Implementation is based on this forum thread: https://blenderartists.org/t/parenting-with-inverse-parenting-cleared-keep-worldtransformation/647969