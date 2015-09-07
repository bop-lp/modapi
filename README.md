# modapi
A modular API framework in Python.

## Usage
1. Setup `config.py`. See `config.py.example`.
2. Put modules into the `modules/` folder. See [example module](https://github.com/csu/modapi/tree/master/modules/example_module).
3. Run `gen_reqs.py` to generate `requirements.{sh, txt}`. Run `pip install -r requirements.txt` or `requirements.sh` to install dependencies. Run in a virtual environment, if you want.
4. Run `python server.py`.