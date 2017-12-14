[![Coverage Status](https://coveralls.io/repos/github/dwavesystems/homebase/badge.svg?branch=master)](https://coveralls.io/github/dwavesystems/homebase?branch=master)
[![Build Status](https://travis-ci.org/dwavesystems/homebase.svg?branch=master)](https://travis-ci.org/dwavesystems/homebase)
# homebase


A place for your app to call home.

*homebase* provides a platform independent API for querying paths in which applications can write caches, data, configs, and
other information.


## rationale 

Since each operating system expects applications to write their data to OS dependant paths, managing cache writing
on portable applications can become difficult.

For example, on macOS:

    ~/Library/Application Support/app_name

while on Linux it may be:

    ~/.local/share/app_name
    
and on Windows:
    
    c:\users\<user_name>\AppData\Local/app_name

and the problem gets worse if you are running inside of a [virtualenv](https://virtualenv.pypa.io/en/stable/)

A similar issue happens for other forms of data, like caches, logs, configuration files, or application state.

## Installation

```bash
python setup.py install
```


## Usage

```python
import homebase

app_name = "my_app"
app_author = "nakatomi-corp"
user_data_dir = homebase.user_data_dir(app_name=app_name, app_author=app_author)
user_cache_dir = homebase.user_cache_dir(app_name=app_name, app_author=app_author)
user_logs_dir = homebase.user_logs_dir(app_name=app_name, app_author=app_author)
user_config_dir = homebase.user_config_dir(app_name=app_name, app_author=app_author)
user_state_dir = homebase.user_state_dir(app_name=app_name, app_author=app_author)

# site specific directories, e.g. /usr/share
site_data_dir = homebase.site_data_dir(app_name=app_name, app_author=app_author)
site_config_dir = homebase.site_config_dir(app_name=app_name, app_author=app_author)
```

If you are running inside of a virtualenv, *homebase* will return paths that are relative to that environment.
If you still want the user path, pass `use_virtualenv=False` in the call.

For example, suppose you have set up a virtual environment in `/home/username/env` on linux

```python
import homebase

app_name = "my_app"
app_author = "nakatomi-corp"
user_data_dir = homebase.user_data_dir(app_name=app_name, app_author=app_author)
# /home/username/env/data/my_app
user_data_dir = homebase.user_data_dir(app_name=app_name, app_author=app_author, use_virtualenv=False)
# /home/username/.local/share/my_app.
```

See the [documentation](# TODO) for more details and examples.

## License

See [LICENSE.txt](LICENSE.txt)


## Acknowledgement

This project is inspired by and is derived from [appdirs](https://github.com/ActiveState/appdirs)
