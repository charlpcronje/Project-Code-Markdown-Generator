# Project Code Markdown Generator

- README.md
```md
# Project Code Markdown Generator

This project contains a set of Python scripts that work together to generate a Markdown document from a project's source code. The scripts are designed to be modular, enhancing readability and maintainability.

## Modules

- `config_loader.py`: Handles loading of configuration from a JSON file.
- `path_utils.py`: Provides utilities for path normalization and depth calculation.
- `markdown_generator.py`: The main script that generates the Markdown document.

## Configuration

Edit `config.json` to specify project details and custom heading levels for specific paths.

```json
{
  "root_path": "/path/to/your/project",
  "output_path": "project_code.md",
  "file_extensions": [".java", ".js", ".html", ".css"],
  "custom_headings_depths": {
    "relative/path/to/specific/directory": 2,
    "relative/another/path": 3
  }
}
```

## Usage

1. Update `config.json` with your project details.
2. Run the main script: `python markdown_generator.py`.
3. The Markdown document will be generated in the specified output location.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
