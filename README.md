# Project Code Markdown Generator

This project consists of a set of Python scripts designed to generate a Markdown document from a project's source code. The scripts are modular and focus on enhancing readability and maintainability of the codebase documentation.

## Features

1. **Modular Script Design**:
   - The project is divided into distinct modules, each handling specific functionalities.

2. **Depth Calculation and Heading Assignment**:
   - Calculates the depth of each file in the project directory.
   - Assigns heading levels in the Markdown document based on the depth, providing a visual hierarchy.

3. **Customizable Heading Levels**:
   - Allows overriding automatically assigned heading levels using the `config.json` file for specified paths.

4. **Path Normalization**:
   - Normalizes all paths (both relative and absolute) for consistency across different operating systems.

5. **Exclusion of Specific Directories and Files**:
   - Can exclude specified directories and files from being processed, as defined in the `config.json`.

6. **Line, Character, and Page Count**:
   - Counts the number of characters, lines, and calculates pages for each file, appending this information at the end of each code block.

7. **Index Generation with File Details**:
   - Creates an index at the beginning of the Markdown document.
   - Lists each file with links, line counts, and page counts for easy navigation.

8. **Configurable File Extensions**:
   - Processes files based on specified extensions in `config.json`, allowing customization for different projects.

## Modules

- `config_loader.py`: Handles the loading of configuration settings from a JSON file.
- `path_utils.py`: Provides utilities for path normalization and calculating directory depth.
- `main.py`: The main script for generating the Markdown document, incorporating all features listed above.

## Configuration

Configure the script using `config.json`:

```json
{
  "project_directory": "/path/to/your/project",
  "output_markdown": "project_code.md",
  "file_extensions": [".java", ".js", ".html", ".css"],
  "exclude_directories": ["dir_to_exclude1", "dir_to_exclude2"],
  "exclude_files": ["file_to_exclude1.js", "file_to_exclude2.css"],
  "custom_headings": {
    "relative/path/to/specific/directory": 2,
    "relative/another/path": 3
  }
}
```

## Usage

1. Update `config.json` with the details of your project.
2. Run `python main.py`.
3. The Markdown document, structured with headings, indices, and file details, will be generated.

## Requirements

- Python installation.
- No additional Python packages are required.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE.md) file for details.
