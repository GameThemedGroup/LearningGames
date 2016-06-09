# We use an underscore to hide the "GameWindow" when this module is imported.
from SS_API import *
from Engine import GameWindow as _GameWindow
from SpaceSmasher import SpaceSmasher


class CustomSpaceMaker(SpaceSmasherFunctionalAPI):
    # Here we have methods/functions to be called (these are actually just references).
    doBlockSetInitialize = None
    
    def blockSetInitialize(self):
        """Initialize the blocks."""
        # The "CustomSpaceMaker.doBlockSetInitialize(self)" could actually be shortened
        # to just "self.doBlockSetInitialize()". But this way we have the opportunity to
        # use another parameter than just as reference to "self" (e.g. "blockSet").
        if CustomSpaceMaker.doBlockSetInitialize is not None:
            CustomSpaceMaker.doBlockSetInitialize(self)

# This function will later be used as an annotation. It sets the function to be called
# in order to initialize the block set.
#
# Example usage:
#
# | @initializeBlockSet
# | def my_init(spaceMaker):
# |     <do something here>
#
# Python will translate this to:
#
# | def my_init(spaceMaker):
# |     <do something here>
# | my_init = initializeBlockSet(my_init)
def initializeBlockSet(f):
    """Set a function to be used to initialize the block set."""
    CustomSpaceMaker.doBlockSetInitialize = f
    return f

# Again, we use an underscore to make this class "private".
class _Main(_GameWindow):

    def __init__(self):
        super(_GameWindow, self).__init__()
        self.spaceMaker = CustomSpaceMaker()
        self.setRunner(self.spaceMaker)

def startProgram(showFlashScreen = False):
    """Start the program."""
    SpaceSmasher.SetShowFlashScreen(showFlashScreen)
    m = _Main()
    m.startProgram()
