"""Utility functions and constants for CP Tracker."""

# Language to file extension mapping
LANGUAGE_EXTENSIONS = {
    "cpp": ".cpp",
    "c++": ".cpp",
    "cplusplus": ".cpp",
    "python": ".py",
    "py": ".py",
    "java": ".java",
    "javascript": ".js",
    "js": ".js",
    "typescript": ".ts",
    "ts": ".ts",
    "go": ".go",
    "rust": ".rs",
    "c": ".c",
    "csharp": ".cs",
    "cs": ".cs",
    "kotlin": ".kt",
    "swift": ".swift",
    "ruby": ".rb",
    "php": ".php",
}

# Difficulty color mapping for Rich
DIFFICULTY_COLORS = {
    "Easy": "green",
    "Medium": "yellow",
    "Hard": "red",
}

# Comment prefixes by language
COMMENT_PREFIXES = {
    "cpp": "//",
    "c++": "//",
    "cplusplus": "//",
    "c": "//",
    "java": "//",
    "javascript": "//",
    "js": "//",
    "typescript": "//",
    "ts": "//",
    "csharp": "//",
    "cs": "//",
    "go": "//",
    "rust": "//",
    "kotlin": "//",
    "swift": "//",
    "python": "#",
    "py": "#",
    "ruby": "#",
    "php": "//",
}


def normalize_language(language: str) -> str:
    """Normalize language name to lowercase for consistent matching."""
    return language.lower().strip()


def get_language_extension(language: str) -> str:
    """Get file extension for a given language name (case-insensitive)."""
    normalized = normalize_language(language)
    return LANGUAGE_EXTENSIONS.get(normalized, f".{normalized}")


def get_comment_prefix(language: str) -> str:
    """Get comment prefix for a given language (case-insensitive)."""
    normalized = normalize_language(language)
    return COMMENT_PREFIXES.get(normalized, "//")


def get_difficulty_color(difficulty: str) -> str:
    """Get color code for difficulty level."""
    return DIFFICULTY_COLORS.get(difficulty, "white")
