# modapi
A modular API framework in Python. Built on top of Flask. Use modapi to build APIs out of subcomponents and avoid writing boilerplate.

## Usage
1. Setup `config.py`. See `config.py.example`.
2. Put modules into the `modules/` folder. See [example module](https://github.com/csu/modapi/tree/master/modules/example_module).
3. Run `gen_reqs.py` to generate `requirements.{sh, txt}`. Run `requirements.sh` to install dependencies. Virtual environment recommended.
4. Run `python server.py`.