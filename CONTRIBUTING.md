# Contributing to project

We love your input! We want to make contributing to this project as easy and
transparent as possible.

## Commit message conventions
Commit messages should be clear and follow a certain format.
We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) & [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit). We also use some emojis to make the commit
messages more expressive.
Some of the emojis are borrowed from [Gitmoji](https://gitmoji.dev/).

### Commit message format
The commit messages have a specific format, which includes a header, and optional body, and footer.

```bash
<type>(<scope>): <subject>

<body>

<footer>
```

#### Header

**type**: it describes the kind of change that the commit is introducing.
The types included are:

- `feat` (Feature) :sparkles: ✨
- `doc` (Documentation) :books: 
- `bug` (Bug fix) :bug: 🐛
- `init` (Initialization) :tada: 🎉
- `update` (Update) :mushroom: 🍄
- `refactor` (Refactor) :hammer: 🔨
- `style` (Style) :artist_palette: 🎨
- `test` (Test) :test_tube: 🧪
- `perf` (Performance) :zap:⚡️
- `release` (Release) :rocket: 🚀
- `notebook` (Notebook) :notebook: 📓

**scope**: This is optional and refers to the specific part of the codebase
that the changes affect (e.g. train, validation, data).

**subject**: This is a short description of the change. Use imperative, present
tense: "change" not "changed" nor "changes".

#### Body
The body is used to explain the waht and why of the commit, as opposed to the 
how. It should provide a meaningful context and motivation for the changes and
can be as detailed as necessary.

#### Footer
The footer is used to reference Github (Gitlab) issues, pull requests, or
breaking changes. For instance, Closes #123, Fixes #456.

Example

```bash 
✨ feat(train): Add train model

Add a new training script for training a model on a new dataset

Closes #123
```

## Docstrings
For python docstrings, we adhere to the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
This includes conventions for writing clear, understandable code and comprehensive docstrings.
Please ensure your code follows these guidelines. Here is an example.

```python

def square_root(n: int):
    """What the function does. Calculate the square root of a number

    Args:
        n: The description of the first argument. The number to calculate the square root of.
    
    Returns:
        ret1: Waht the function returns. Empty if nothing is returned. The square root of the number
    
    Raises:
        Exception Class: When and why this exception can be raised by the function.
        ValueError: If the number is negative

    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number.")
    return math.sqrt(n)
```

