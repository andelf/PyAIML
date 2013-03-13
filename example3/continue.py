import sys
sys.path.insert(0, "../")
import shelve

import aiml
import copy

# use any dict like obj here
db = copy.deepcopy(dict(shelve.open("session.db", "c")))
# The Kernel object is the public interface to
# the AIML interpreter.

k = aiml.Kernel(sessionStore=db)

# load from a saved brain
k.restoreBrain("brain.sav")

# Loop forever, reading user input from the command
# line and printing responses.
while True:
    print k.respond(raw_input("> "))
    #db.sync()
