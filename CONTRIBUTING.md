# Contributing to Linux Admin Toolkit

Thank you for your interest in contributing to the Linux Admin Toolkit!

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/CamoRageaholic1/Linux-Admin-Toolkit/issues)
2. If not, create a new issue using the bug report template
3. Include:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error messages or logs

### Suggesting Features

1. Check [existing issues](https://github.com/CamoRageaholic1/Linux-Admin-Toolkit/issues) for similar requests
2. Create a new issue using the feature request template
3. Describe:
   - The problem you're trying to solve
   - Your proposed solution
   - Any alternatives you've considered

### Code Contributions

#### Before You Start

1. Fork the repository
2. Create a new branch for your feature/fix
3. Make sure you can run the existing tests
4. Read the code style guidelines below

#### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Linux-Admin-Toolkit.git
cd Linux-Admin-Toolkit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

#### Code Style

- Follow **PEP 8** style guide
- Use **type hints** where appropriate
- Write **docstrings** for all functions and classes
- Keep functions focused and single-purpose
- Use descriptive variable names

#### Security Requirements

All contributions must:

- Follow security best practices
- Not introduce vulnerabilities
- Handle errors gracefully
- Validate all user input
- Use appropriate permissions
- Document security implications

#### Testing

- Test your code on multiple Linux distributions if possible
- Test with both Python 3.8+ versions
- Include example usage in your PR
- Test in both dry-run and actual modes

#### Documentation

- Update README.md if adding new features
- Add docstrings to new functions/classes
- Update relevant docs/ files
- Add examples if appropriate
- Update CHANGELOG (if exists)

### Pull Request Process

1. **Create Pull Request**
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe what your PR does and why

2. **PR Requirements**
   - Code follows style guidelines
   - All tests pass
   - Documentation is updated
   - No merge conflicts

3. **Review Process**
   - Maintainer will review your PR
   - Address any feedback
   - Once approved, PR will be merged

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the project
- Show empathy toward others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

## Questions?

If you have questions:

1. Check the [documentation](docs/)
2. Look through [existing issues](https://github.com/CamoRageaholic1/Linux-Admin-Toolkit/issues)
3. Create a new issue with your question

## Recognition

Contributors will be:

- Listed in CONTRIBUTORS.md (if created)
- Credited in release notes
- Thanked in the community

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Linux Admin Toolkit!** 🐧

*Author: David Osisek*  
*Book: [Linux Basics and Cheat Sheets](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)*
