# Project Name

 Password Locker
---

## Description
---
Password Locker is a python project that allows users to store their details such as:- passwords after creating accounts

## Created by
Shadrack Anayo

---

## Live demo

</>

---
## User Stories
As a user I want to, 
1. Create a password locker account with my details, a login username and password.
2. Store my already existing account credentials in the application.e.g store name and password in the application of the account created.
3. Create new account credentials in the application.e.g for facebook
4. Have an option of putting in a password that I want to use for the new credential account.i.e use generated password or create my own
5. View my various account credentials and their passwords in the application.
6. Delete a credentials account that I no longer need in the application.
 ---
## Specifications
BDD | Input | Output
----------| ------|------
Run the application| Do, **$ ./pass_locker.py**| Welcome note and shortcuts to do your tasks
To create an account| Select 1 | Prompted to give your fullname, username and password
To Login | Select 2 | Prompted to enter username and password
If pass | Success message| New prompts to create credentials 
To create Credential | Select 1 | Prompted to give username, site name and password
To Display Credential | Select 2 | Credentials are displayed out
To Login | Select 3 | Prompted to enter username and password
IF pass | Success Message | 
To Delete Credential | Select 4| Credential selected is deleted
To go back | Select 5| Takes you back to Create an account, login or exit
If you want to exit when in first stage| Select 3| Exits the application 
---
## SetUp Requirements
To set up or to install you need:
 * python3.6
 * pip
 * pyperclip module
 ---
## Cloning
To clone, on your terminal
* $ git clone https://github.com/shack1234/Password-Locker/
* $ cd Password-Locker
---
## Testing the Application
To run the tests, on your terminal:

  * $ python3.6 test.py
---
## Run the Application
To run the application, in your terminal:

* $ chmod +x pass_locker.py
* $ ./pass_locker.py
---
## Licence
MIT © 2020, Shadrack Anayo