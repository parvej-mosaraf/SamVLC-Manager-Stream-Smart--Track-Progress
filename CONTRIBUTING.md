# Contributing to SamOnline FTP Link Extractor & Player

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

Before creating an issue, please:
1. Check if the issue already exists
2. Search through closed issues for similar problems
3. Ensure you're using the latest version

When creating an issue, include:
- **Clear title**: Brief description of the problem
- **Description**: Detailed explanation of the issue
- **Steps to reproduce**: How to recreate the problem
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, browser, etc.
- **Screenshots**: If applicable

### Suggesting Enhancements

For feature requests:
1. Check if the feature already exists
2. Explain the use case and benefits
3. Provide mockups or examples if possible
4. Consider implementation complexity

### Code Contributions

#### Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/samvlc-manager.git
   cd samvlc-manager
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### Development Guidelines

##### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

##### Testing
- Test your changes thoroughly
- Test with different show configurations
- Verify VLC integration works
- Check web interface functionality

##### Documentation
- Update relevant documentation files
- Add docstrings to new functions
- Update README.md if needed
- Include examples for new features

#### Pull Request Process

1. **Ensure your code works**:
   - Test all functionality
   - Check for syntax errors
   - Verify no regressions

2. **Update documentation**:
   - Update README.md if needed
   - Add comments to code
   - Update user manual if applicable

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**:
   - Use a clear, descriptive title
   - Explain what changes you made
   - Reference any related issues
   - Include screenshots if applicable

## 🏗️ Development Setup

### Prerequisites
- Python 3.7+
- Git
- VLC Media Player
- Code editor (VS Code, PyCharm, etc.)

### Local Development

1. **Clone and setup**:
   ```bash
   git clone https://github.com/yourusername/samvlc-manager.git
   cd samvlc-manager
   pip install -r requirements.txt
   ```

2. **Create test data**:
   ```bash
   mkdir "shows/Test Show"
   echo "http://example.com/video1.m3u8" > "shows/Test Show/extracted_links.txt"
   echo '{"0": false}' > "shows/Test Show/data.json"
   ```

3. **Run the application**:
   ```bash
   cd web-player
   python app.py
   ```

4. **Test link extraction**:
   ```bash
   python samvlc-extractor.py
   ```

### Project Structure

```
samvlc-manager/
├── samvlc-extractor.py      # Link extraction
├── web-player/
│   ├── app.py              # Flask web server
│   └── templates/
│       └── index.html      # Web interface
├── shows/                   # Test data storage
├── requirements.txt         # Dependencies
└── docs/                   # Documentation
```

## 🎯 Areas for Contribution

### High Priority
- **Error Handling**: Improve error messages and recovery
- **UI/UX**: Enhance the web interface design
- **Configuration**: Make paths configurable via config file
- **Testing**: Add unit tests and integration tests

### Medium Priority
- **Performance**: Optimize for large show collections
- **Features**: Add search, filtering, sorting
- **Compatibility**: Support more video formats
- **Documentation**: Improve code documentation

### Low Priority
- **Themes**: Add dark/light mode support
- **Mobile**: Improve mobile responsiveness
- **API**: Add REST API endpoints
- **Database**: Add database support option

## 📋 Coding Standards

### Python Code
```python
def example_function(param1, param2):
    """
    Brief description of the function.
    
    Args:
        param1 (str): Description of parameter
        param2 (int): Description of parameter
        
    Returns:
        bool: Description of return value
    """
    # Implementation here
    return True
```

### HTML/CSS
- Use semantic HTML elements
- Follow BEM naming convention for CSS
- Keep styles organized and commented
- Ensure responsive design

### JavaScript
- Use modern ES6+ features
- Add JSDoc comments for functions
- Handle errors gracefully
- Keep functions small and focused

## 🐛 Bug Reports

When reporting bugs, please include:

### Required Information
- **OS and version**: Windows 10, macOS 12, Ubuntu 20.04, etc.
- **Python version**: `python --version`
- **Browser**: Chrome 95, Firefox 94, etc.
- **Steps to reproduce**: Detailed steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Error messages**: Full error text

### Optional Information
- **Screenshots**: Visual evidence
- **Log files**: Any relevant logs
- **Configuration**: Custom settings used
- **Workaround**: Any temporary fixes found

## 💡 Feature Requests

### Before Submitting
1. Check existing issues and PRs
2. Consider if it fits the project scope
3. Think about implementation complexity
4. Consider user impact

### When Submitting
- **Clear title**: Brief, descriptive
- **Detailed description**: What and why
- **Use cases**: Real-world scenarios
- **Mockups**: Visual examples if applicable
- **Alternatives**: Other solutions considered

## 📚 Documentation

### Types of Documentation
- **Code comments**: Inline documentation
- **Docstrings**: Function/class documentation
- **README**: Project overview and setup
- **User Manual**: End-user instructions
- **API docs**: Technical reference

### Writing Guidelines
- Use clear, simple language
- Include examples and code snippets
- Keep it up-to-date with code changes
- Use consistent formatting

## 🔒 Security

### Security Considerations
- Never commit sensitive information
- Validate all user inputs
- Use secure coding practices
- Report security issues privately

### Reporting Security Issues
For security-related issues:
1. **Don't create public issues**
2. **Email security concerns privately**
3. **Include detailed reproduction steps**
4. **Wait for response before disclosure**

## 📞 Getting Help

### Community Support
- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and ideas
- **Pull Requests**: For code contributions

### Development Questions
- Check existing documentation
- Search through issues and discussions
- Ask specific, detailed questions
- Provide context and examples

## 🎉 Recognition

Contributors will be recognized in:
- **README.md**: Contributor list
- **Release notes**: Feature acknowledgments
- **GitHub**: Commit history and contributions

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for contributing to SamVLC Manager! 🚀
