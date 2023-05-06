# elements_slot_reserver
A simple tool to automatically register for a slot in a selected studio for the next day.

The script is scheduled for every day at 13:30 UTC time.

## Variables
The tool is configured through GitHub secrets that
[you need to set in your forked repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

### Studio

The `STUDIO_NAME` holds the name of the studio where you want to reserve.

Choices are ...
1. "Balanstraße"
2. "Donnersbergerbrücke"
3. "Eschborn"
4. "Eschenheimer Turm"
5. "Henninger Turm"
6. "Paulinenbrücke"
7. "Siemensallee"

It defaults to "Donnersbergerbrücke".

### Credentials
The `EMAIL` and `PASSWORD` you use to sign in to the registration site.