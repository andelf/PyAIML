import sys
sys.path.insert(0, "../")
import shelve

import aiml


# use any dick like obj here
db = shelve.open("session.db", "c", writeback=True)
# The Kernel object is the public interface to
# the AIML interpreter.

k = aiml.Kernel(sessionStore=db)

# load from a saved brain
k.loadBrain("brain.sav")

# Loop forever, reading user input from the command
# line and printing responses.
while True:
    print k.respond(raw_input("> "))
    db.sync()
