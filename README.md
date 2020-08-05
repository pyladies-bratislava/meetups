# pybratislava

Repository for the PyLadies Bratislava Meetups.

To run the code from a meetup do the following:
1. Create a virtual environment inside the meetup's directory > `python3 -m venv .venv`
In this example the virtualenv will be located in the `.venv` directory.
2. Activate the environment > `source .venv/bin/activate` (linux/mac) or `.\.venv\Scripts\activate.bat` (windows)
3. Check if there is a `requirements.txt` file. If so install them > `pip install -r requirements.txt`
4. Check which python files exist in the folder and run them.

To add code to the repo follow these steps:
1. Clone the repository
2. Create a branch and make some changes > `git checkout -b <branch-name>`
3. Commit your changes and write a nice commit message (locally) > `git commit -m "Code for database access"`
4. Push your branch to github > `git push origin <branch-name>`
5. Make a Pull Request to `meetups:master` (in github using your account)
6. Wait for the review and the merge of your changes.
7. For questions use our slack channel > `#city-bratislava` ( [Join pyladies on slack](https://slackin.pyladies.com/) )

Happy coding :)

