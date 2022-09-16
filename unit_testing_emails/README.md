# Unit Testing for Email finding on CSV

The "user_emails.csv" contains a dictionary with user names and their respective email addresses. Python script called "emails.py" searches the email that belongs to the user name passed as argument. "emails_test.py" has tests for checking the proper execution of "emails.py".

Supported test cases are:

- Normal use with two arguments and existing user
- Only one parameter (prints ```Missing parameters```)
- User not found on CSV (prints ```No email address found```)

## Examples of execution

### Proper use

```bash
python3 emails.py Blossom Gill
```

prints

```text
blossom@abc.edu
```

### Missing parameters

```bash
python3 emails.py Kirk
```

prints

```text
Missing parameters
```

### Non existing user

```bash
python3 emails.py Roy Cooper
```

prints

```text
No email address found
```
