"""File operations for creating and managing solution files."""

import re
from datetime import datetime
from pathlib import Path

from utils import get_comment_prefix, get_language_extension


def slugify(title: str) -> str:
    """
    Convert title to URL-safe slug.
    - Lowercase
    - Replace spaces with hyphens
    - Remove non-alphanumeric characters (except hyphens)
    - Collapse multiple hyphens into one
    """
    # Convert to lowercase
    slug = title.lower()
    # Replace spaces and underscores with hyphens
    slug = re.sub(r'[\s_]+', '-', slug)
    # Remove non-alphanumeric characters except hyphens
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # Collapse multiple hyphens into one
    slug = re.sub(r'-+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug


def get_comment_header(language: str, title: str, platform: str) -> str:
    """Generate language-specific comment header for solution file."""
    prefix = get_comment_prefix(language)
    date = datetime.now().strftime("%Y-%m-%d")
    
    header = f"{prefix} Solution for {title}\n"
    header += f"{prefix} Platform: {platform}\n"
    header += f"{prefix} Date: {date}\n"
    header += f"{prefix}\n"
    
    return header


def create_solution_file(platform: str, slug: str, language: str, title: str) -> Path:
    """
    Create a solution file with header comment.
    
    Args:
        platform: Platform name (e.g., "LeetCode")
        slug: File slug (e.g., "two-sum")
        language: Programming language
        title: Problem title
    
    Returns:
        Path to the created file
    """
    # Sanitize platform name for directory
    platform_dir = slugify(platform)
    
    # Create solutions directory structure
    solutions_dir = Path("solutions") / platform_dir
    solutions_dir.mkdir(parents=True, exist_ok=True)
    
    # Get file extension
    ext = get_language_extension(language)
    if not ext.startswith('.'):
        ext = f".{ext}"
    
    # Create file path
    file_path = solutions_dir / f"{slug}{ext}"
    
    # Generate header comment
    header = get_comment_header(language, title, platform)
    
    # Write file if it doesn't exist
    if not file_path.exists():
        file_path.write_text(header, encoding='utf-8')
    
    return file_path
