import os
import re
import argparse
import sys

# ==============================================================================
# SCRIPT INSTRUCTIONS
#
# This script intelligently splits a master file into separate, well-formatted
# Obsidian notes.
#
# How to Format Your Input File:
# 1. Use "split_here" on its own line to separate each note.
# 2. The first line of each section MUST be the note's title.
# 3. The second line is OPTIONAL. If it starts with "Tags:", it will be
#    processed as tags. Otherwise, it's treated as normal content.
#
# Example Format in your_notes_file.txt:
#   8086 Architecture - BIU and EU
#   Tags: 8086, architecture, biu, eu
#   The internal architecture of the 8086 is divided into two...
#   split_here
#   8086 Memory Segmentation
#   Tags: 8086, memory
#   The 8086 uses a segmented memory architecture...
#
# How to Run From Your Terminal:
#   python splitter_final.py your_notes_file.md --output_dir "your/folder"
#
# ==============================================================================

def sanitize_filename(name):
    """Takes a string and returns a filesystem-safe version."""
    sanitized = re.sub(r'[<>:"/\\|?*]', '', name).strip()
    return sanitized

def create_markdown_files(master_content, output_dir):
    """
    Splits the master content and creates individual, formatted markdown files.
    """
    os.makedirs(output_dir, exist_ok=True)

    note_chunks = master_content.split('split_here')

    if not any(chunk.strip() for chunk in note_chunks):
        print("No content found or separator 'split_here' is missing.")
        return

    print(f"Splitting into {len(note_chunks)} notes...")
    for chunk in note_chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        try:
            lines = chunk.split('\n')
            title = lines[0].strip()
            tags = []
            content_lines = []

            # Check if the second line is a tags line
            if len(lines) > 1 and lines[1].strip().lower().startswith("tags:"):
                tag_line = lines[1].strip()[5:].strip()
                # Format for Obsidian's tag syntax (e.g., #8086 #architecture)
                tags = [f"#{tag.strip()}" for tag in tag_line.split(',')]
                # The rest of the content starts from the third line
                content_lines = lines[2:]
            else:
                # No tags line found, content starts from the second line
                content_lines = lines[1:]

            # --- Build the final content for the new .md file ---
            # 1. Add the H1 Title
            final_content = f"# {title}\n\n"

            # 2. Add the formatted tags if they exist
            if tags:
                final_content += f"**Tags:** {' '.join(tags)}\n\n"

            # 3. Add the rest of the content
            final_content += "\n".join(content_lines).strip()


            filename = sanitize_filename(title) + ".md"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"  -> Successfully created '{filepath}'")

        except Exception as e:
            print(f"Warning: Could not process a chunk. Error: {e}\nChunk start: {chunk[:100]}...")


    print(f"\n✅ Done! All notes are in the '{output_dir}' directory.")

def main():
    """Main function to parse arguments and run the script."""
    parser = argparse.ArgumentParser(
        description="Splits a large text file into formatted .md notes for Obsidian using 'split_here'.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_file", help="Path to the large text file.")
    parser.add_argument(
        "--output_dir",
        default="notes",
        help="The directory to save the new notes into (default: 'notes')."
    )
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            master_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.input_file}' was not found.", file=sys.stderr)
        sys.exit(1)

    create_markdown_files(master_content, args.output_dir)

if __name__ == "__main__":
    main()

