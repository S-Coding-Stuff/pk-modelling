# Pharmacokinetic Modelling — Python Library

**SAIN** project to develop an extensible Python library for defining, simulating and visualising compartmental pharmacokinetic (PK) models. Pharmacokinetics describes how drugs are absorbed, distributed, metabolised and eliminated (ADME). The project focuses on PK models; pharmacodynamic (PD) models are outside its scope.

**Status: initial development.** The repository currently contains a standalone two-compartment simulation in `prototype.py`, a package skeleton and basic tests. The library interface described below is planned work.

## Repository structure

The current source and configuration files are shown below; Git internals, generated files and operating-system metadata are omitted.

```text
pk-modelling/
├── .flake8
├── .gitignore
├── LICENSE
├── README.md
├── prototype.py
├── setup.py
└── pkmodel/
    ├── __init__.py
    ├── model.py
    ├── protocol.py
    ├── solution.py
    ├── version_info.py
    └── tests/
        ├── __init__.py
        ├── test_model.py
        ├── test_protocol.py
        └── test_solution.py
```

`pyproject.toml` defines the `pkmodel` distribution, its dependencies, development tools and test configuration. `pkmodel/__init__.py` exports the three placeholder classes and version information. The tests check the default value stored by each class.

## Installation

Clone the repository and install from its root directory, preferably in a virtual environment:

```bash
git clone https://github.com/SAIN-ENAIBLE/pk-modelling.git
cd pk-modelling
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. Use `python3` in place of `python` if that is how Python 3 is installed on your system.

Use Python 3.11 or later; CI uses Python 3.12. The editable installation installs NumPy, SciPy and Matplotlib using the dependencies in `pyproject.toml`.

For development, install the configured `dev` extra, which adds pytest, coverage tools, Ruff and the package build tool:

```bash
python -m pip install -e ".[dev]"
```

There is no documentation source directory or Sphinx build configuration yet. Installation here is from source; no PyPI release is assumed.

## Usage

### Existing prototype

After installing the dependencies, run from the repository root:

```bash
python prototype.py
```

The script solves the two-compartment equations using `solve_ivp` and plots central and peripheral drug quantities for two parameter sets. Both start with zero drug quantity and receive a constant input of 1 ng/h over 0–1 h. They differ in intercompartmental flow: 1 and 2 mL/h. All compartment volumes are 1 mL and clearance is 1 mL/h. The plot contains four labelled curves.

The script uses `plt.show()` to display a figure and does not save results to disk. A graphical Matplotlib backend is needed to view the plot interactively. For a non-interactive execution check on a headless system:

```bash
MPLBACKEND=Agg python prototype.py
```

### Proposed API — not yet implemented

The intended workflow is to define a `Model`, create an independent `Protocol`, combine them in a `Simulation`, and obtain a `Solution` for analysis and visualisation. Constructor arguments and method names for this workflow have not been established. The current placeholder classes cannot run simulations.

## Testing and code quality

After installing the `dev` extra, run the tests, linting, formatting check and package build from the repository root:

```bash
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
python -m build
```

The three current tests check placeholder construction only. They do not validate the numerical model, dosing behaviour or simulation results.

To format your changes automatically:

```bash
python -m ruff format .
```

Ruff and pytest settings are in `pyproject.toml`; tests live in `pkmodel/tests/`.

## Branch workflow and continuous integration

Each contributor works on a branch in the shared repository:

```bash
git switch main
git pull --ff-only
git switch -c feature/my-change
# Edit code and run the checks above.
git add path/to/changed-file.py
git commit -m "Describe the change"
git push -u origin feature/my-change
```

Open a pull request targeting `main` and request a teammate's review. After merging, update your local `main` before starting another branch.

`.github/workflows/ci.yml` runs tests, linting, formatting checks and a package build on every branch push and on pull requests to `main`. It also supports manual runs from the Actions tab once the workflow is on the default branch. New commits cancel older runs for the same branch or pull request. CI installs `.[dev]` from `pyproject.toml`; it does not use `requirements.txt`.

Commit and push the workflow, `pyproject.toml` and the accompanying code changes to activate these checks on your branch, then merge the pull request into `main`. Check results appear in the repository's Actions tab and on pull requests.

To enforce review and passing checks before merging, a repository administrator can create a branch ruleset in **Settings → Rules → Rulesets** targeting `main`. Require a pull request, one approval and the `checks` status check after its first run. Availability depends on repository visibility and the organization's GitHub plan. The workflow runs checks; repository rules enforce merge requirements.

## Acknowledgements and licence

This project was created from the
[SABS-R3 software engineering PK starter repository](https://github.com/sabs-r3/software-engineering-projects-pk)
and has an independent Git history. The starter code provides the initial
prototype, package skeleton and tests.

The project is licensed under the [MIT License](LICENSE). The existing licence
retains **Copyright (c) 2020 SABS-R3**; its copyright and permission notices must
be preserved in copies or substantial portions of the software.
