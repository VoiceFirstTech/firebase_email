## Setup and Running

1. Execute the command `sudo apt update && sudo apt upgrade`.
2. Install python3 by executing `sudo apt install python3`.
3. Install python3-venv by executing `sudo apt install python3-venv`.
4. Clone the Repository
5. Go into the repo dir by executing `cd firebase_email`.
6. Create virtual environment by executing `python3 -m venv venv`.
7. Create a new screen by executing `screen -S app`.
7. Activate the virtual env by executing `source venv/bin/activate`.
8. Install libraries by executing `pip install -r requirements.txt`.
9. Run the app by executing `python app.py`.
10. Press `Ctrl+A+D` to detach from screen and exit the terminal.
11. To close the app, reattach to screen by executing `screen -r app` and press `Ctrl+C`.


## Running (Already Setup)

If your app is already setup by following previous steps, follow these steps -
1. SSH into the terminal or activate cloud shell.
2. Create the screen by executing `screen -S app`.
3. Go into app dir `firebase_email`.
4. Activate virtual env by `source venv/bin/activate`.
5. Run the app by `python app.py`.
6. Press `Ctrl+A+D` to detach from screen and exit the terminal.
