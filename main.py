import os
from config_loader import load_config
from path_utils import normalize_path, get_depth, is_excluded

def determine_heading_level(file_path, config, default_level):
    normalized_file_path = normalize_path(file_path)
    for custom_path, level in config.get('custom_headings', {}).items():
        normalized_custom_path = normalize_path(custom_path)
        if normalized_custom_path in normalized_file_path:
            return level
    return default_level

def process_file(file_path, config):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        char_count = len(content)
        line_count = content.count('\n') + 1
        page_count = max(1, line_count // 50)  # Assuming 50 lines per page
    return char_count, line_count, page_count, content

def write_files_to_markdown_with_custom_headings(config):
    index_content = "## Index\n\n"
    file_content = ""
    file_counter = 1

    for file_type in config['file_extensions']:
        for root, dirs, files in os.walk(config['project_directory']):
            dirs[:] = [d for d in dirs if d not in config['exclude_directories']]
            for file in sorted(files):
                if file.endswith(file_type) and not is_excluded(os.path.join(root, file), config['exclude_directories'], config['exclude_files']):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, config['project_directory'])
                    depth = get_depth(file_path, config['project_directory'])
                    heading_level = determine_heading_level(relative_path, config, max(1, depth + 1))
                    anchor_name = f"file{file_counter}"
                    char_count, line_count, page_count, content = process_file(file_path, config)
                    index_content += f"- [{relative_path}](#{anchor_name}) - {line_count} lines, {page_count} pages\n"
                    file_content += f"{'#' * heading_level} {file} <a name='{anchor_name}'></a>\n\n```{file_type}\n"
                    file_content += f"{relative_path}\n\n{content}\n```\n*Characters: {char_count}, Lines: {line_count}, Pages: {page_count}*\n\n"
                    file_counter += 1

    full_content = index_content + "\n" + file_content

    with open(config['output_markdown'], 'w', encoding='utf-8') as md_file:
        md_file.write(full_content)

if __name__ == "__main__":
    config = load_config('config.json')
    write_files_to_markdown_with_custom_headings(config)
    print(f"Markdown document '{config['output_markdown']}' has been created.")
