## Description

A simple browser chat app made with Django and HTML.

A standard Django application handles http requests using a request-response lifecycle. A request is sent from the user’s browser, Django calls the relevant view which then returns a response to the user.

## Installation

- Requires python 3.6+

To install development dependncies:

```
$ pip3 install -r requirements.txt
```
## Usage

```python
python3 manage.py runserver
```
## Virtualenv

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This means that each project can have its own dependencies, regardless of what dependencies every other project has. We use a module named `virtualenv` which is a tool to create isolated Python environments. `virtualenv` creates a folder which contains all the necessary executables to use the packages that a Python project would need.

### Installing virtualenv

```bash
$ pip3 install virtualenv
```

### Test your installation

```bash
$ virtualenv --version
```

### Using virtualenv

You can create a virtualenv using the following command:

```bash
$ virtualenv virtualenv_name
```

After running this command, a directory named my_name will be created. This is the directory which contains all the necessary executables to use the packages that a Python project would need. This is where Python packages will be installed.

Now after creating virtual environment, you need to activate it. Remember to activate the relevant virtual environment every time you work on the project. This can be done using the following command:

```
$ source virtualenv_name/bin/activate
```

Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal. This will let you know that the virtual environment is currently active.
Now you can install dependencies related to the project in this virtual environment. For example if you are using Django 1.9 for a project, you can install it like you install other packages.

```
(virtualenv_name) $ pip install Django==1.9
```

Once you are done with the work, you can deactivate the virtual environment by the following command:

```
(virtualenv_name) $ deactivate
```

Now you will be back to system’s default Python installation.


