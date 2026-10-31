#!/bin/bash

HTML_FILE="index.html" 

TODO_TASKS=$(awk '/^Done Tasks:/ {exit} !/^ToDo Tasks:[[:space:]]*$/ {print}' "$1")
DONE_TASKS=$(awk '/^Done Tasks:[[:space:]]*$/ {found=1; next} found && /^[[:space:]]*$/ {exit} found {print}' "$1")
UNIT_TEST_RESULTS=$(cat "$2")

update_pre() {
    HTML_ID="$1" CONTENT="$2" perl -0777 -i -pe \
    's{(<pre id="\Q$ENV{HTML_ID}\E">).*?(</pre>)}{$1\n$ENV{CONTENT}\n$2}gs' "$3"
}

update_pre "pending" "$TODO_TASKS" "$HTML_FILE" 
update_pre "completed" "$DONE_TASKS" "$HTML_FILE" 
update_pre "unittest" "$UNIT_TEST_RESULTS" "$HTML_FILE"

#git config --global user.email "github-actions@users.noreply.github.com" 
#git add "$HTML_FILE"
#git commit -m "Update $HTML_FILE with new task and test data" 
#git push

