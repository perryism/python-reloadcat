# Description

This project is designed to facilitate test-driven development by automatically watching over the test files you are writing and continuously running them. It provides a convenient way to ensure that your tests are always up-to-date and running smoothly. By using the `reloadcat` module, you can easily automate the process of running tests and get instant feedback on any changes you make. This helps to streamline your development workflow and improve the overall quality of your code. 


# Installation

```
pip install git+https://github.com/perryism/python-reloadcat.git
```

# Get Started

To use `reloadcat`, simply run the following command in your terminal:

```
reloadcat
```

Additionally, you can specify which files to watch by editing the `reloadcat.yaml` file and adding the desired file patterns under the `patterns` section. For example, if you want to watch all Python test files in the `tests` and `my_project` directories, you can add the following patterns:

```yaml
patterns:
  - ./tests/*.py
  - ./my_project/*.py
```
