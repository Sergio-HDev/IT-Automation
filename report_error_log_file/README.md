# Report error from log file

The log file ("fishy.log") has information written in this format:

```
Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] "ERROR/INFO/WARN" "Error description"
```

The python script ("find_error.py") takes a parameter from execution which is the log file you want to search for an error. This script will ask the user for an input ```What is the error? ```

The output file pregenerated ("errors_found.log") was created with this input:

```
CRON ERROR Failed to start
```