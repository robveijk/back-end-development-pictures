# Python Starter Template
Quick start for a new Python project. Currently, this just adds the `pre-commit-config.yaml` and provides a checklist for basic set up.

### TO DO
- [ ] Run `pre-commit autoupdate` on the [python_starter](https://github.com/robveijk/python_starter) repository (see https://pre-commit.com/#updating-hooks-automatically)
- [ ] Create a new Repo using this repo as Template (from [github.com](https://github.com/robveijk?tab=repositories))
- [ ] Create a new virtual environment: `make_venv <python_version> <optional suffix>`
  - List available Python versions using `uv python list`
  - Note: Include patch version in order to include the full version in the venv name (i.e., use `3.13.0` instead of `3.13`)
- [ ] Create `.envrc` file: `echo_envrc <python_version> <optional suffix> > .envrc`
- [ ] Initialize project to create `pyproject.toml`: `uv init`
- [ ] Add pre-commit dependencies: `uv add --dev pre-commit`
   - Since we're using remote hook repositories, we don't need to add other dependencies
- [ ] Install pre-commit hooks: `pre-commit install`
  - Install globally using `uv tool install pre-commit`
- [ ] Test pre-commit hooks: `pre-commit run --all`
  - It's likely additional dependencies must be added, depending on the specifics of the project
  - **Uncomment the pytest hook** after you've added tests (it fails when no tests are found)
- [ ] Remove the contents of this file and update for the project

If you're using Jupyter Notebooks _and_ want to use a separate virtual environment
- [ ] Create separate virtual env: `cd notebooks; make_venv <python_version> $(basename $(dirname $(pwd)))`
  - To append the basefolder as suffix
- [ ] Add Jupyter dependency `uv add --group eda jupyter`
- [ ] Export dependencies: `uv export --all-groups > notebooks/requirements.txt`
  - Note: Should not be necessary (in the future; also see https://github.com/astral-sh/uv/issues/8590)
  - Let's try `uv sync --all-groups`
- [ ] Install dependencies
