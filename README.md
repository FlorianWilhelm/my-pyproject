# 🤜 Brutally simple Python package 🤛

True to the motto, friends don't let friends fiddle with the PYTHONPATH,
this repository shows how easy it is with a minimal [pyproject.toml](pyroject.toml)
to create an installable Python package. So to test this:

1. clone this repository `git clone https://github.com/FlorianWilhelm/my_pyproject.git`,
2. type `pip install -e .` to install this skeleton python package,
3. run `python -c "from  my_pyproject.my_module import fib; print(fib(42))"` to see that it really works 🎉

If you even wanted to build a proper sdist or wheel file you can do that with `pip install build` followed by `python -m build`. 

That's it, nothing more to see here. Use and modify [pyproject.toml](pyroject.toml) for your own projects or even better,
if you are interested in a really professional Python project setup, check out [The Hatchlor](https://github.com/FlorianWilhelm/the-hatchlor) 🌹 
