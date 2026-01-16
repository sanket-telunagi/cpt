"""CP Tracker CLI - Manage competitive programming solutions."""

import typer
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import print as rprint

from database import ProblemDB
from file_ops import create_solution_file, slugify
from utils import get_difficulty_color, normalize_language

app = typer.Typer()
console = Console()


@app.command()
def add():
    """Add a new solution or add a solution to an existing problem."""
    db = ProblemDB()
    
    # Prompt for basic information
    platform = Prompt.ask("Platform", default="LeetCode")
    title = Prompt.ask("Title")
    language = Prompt.ask("Language", default="python")
    
    # Auto-generate slug and allow override
    auto_slug = slugify(title)
    slug = Prompt.ask("Slug (for filename)", default=auto_slug)
    
    # Normalize platform and title for comparison
    normalized_platform = platform.strip()
    normalized_title = title.strip()
    
    # Check if problem exists
    existing_problem = db.find_problem(normalized_title, normalized_platform)
    
    if existing_problem:
        # Existing problem - add new language solution
        normalized_lang = normalize_language(language)
        
        if db.problem_has_language(existing_problem, normalized_lang):
            rprint(f"[red]Error:[/red] Solution in {language} already exists for this problem.")
            raise typer.Exit(1)
        
        # Create file
        file_path = create_solution_file(
            normalized_platform, 
            slug, 
            normalized_lang, 
            normalized_title
        )
        
        # Add solution to existing problem
        solutions = existing_problem.get('solutions', [])
        solutions.append({
            "language": normalized_lang,
            "path": str(file_path),
            "date": datetime.now().isoformat()
        })
        
        doc_id = existing_problem.get('doc_id')
        if doc_id is None:
            rprint("[red]Error:[/red] Could not retrieve document ID.")
            raise typer.Exit(1)
        db.update_problem(doc_id, {"solutions": solutions})
        
        rprint(f"[green]✓[/green] Added {language} solution to existing problem: {normalized_title}")
        rprint(f"[dim]File: {file_path}[/dim]")
    
    else:
        # New problem - prompt for additional info
        difficulty = Prompt.ask(
            "Difficulty", 
            choices=["Easy", "Medium", "Hard"],
            default="Easy"
        )
        
        tags_input = Prompt.ask("Tags (comma-separated)", default="")
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else []
        
        # Create file
        normalized_lang = normalize_language(language)
        file_path = create_solution_file(
            normalized_platform,
            slug,
            normalized_lang,
            normalized_title
        )
        
        # Create problem document
        problem_data = {
            "title": normalized_title,
            "slug": slug,
            "platform": normalized_platform,
            "difficulty": difficulty,
            "tags": tags,
            "solutions": [{
                "language": normalized_lang,
                "path": str(file_path),
                "date": datetime.now().isoformat()
            }]
        }
        
        db.add_problem(problem_data)
        
        rprint(f"[green]✓[/green] Created new problem: {normalized_title}")
        rprint(f"[dim]File: {file_path}[/dim]")


@app.command()
def list():
    """List all problems with their details."""
    db = ProblemDB()
    problems = db.get_all_problems()
    
    if not problems:
        rprint("[yellow]No problems found. Use 'add' to create your first problem.[/yellow]")
        return
    
    # Create table
    table = Table(title="CP Tracker - Problems", show_header=True, header_style="bold magenta")
    table.add_column("Title", style="cyan", no_wrap=True)
    table.add_column("Platform", style="blue")
    table.add_column("Difficulty", style="bold")
    table.add_column("Solved In", style="green")
    
    for problem in problems:
        title = problem.get("title", "N/A")
        platform = problem.get("platform", "N/A")
        difficulty = problem.get("difficulty", "N/A")
        
        # Get languages from solutions
        solutions = problem.get("solutions", [])
        languages = [sol.get("language", "").upper() for sol in solutions]
        solved_in = ", ".join(languages) if languages else "None"
        
        # Color code difficulty
        color = get_difficulty_color(difficulty)
        difficulty_display = f"[{color}]{difficulty}[/{color}]"
        
        table.add_row(title, platform, difficulty_display, solved_in)
    
    console.print(table)


@app.command()
def stats():
    """Show statistics about solved problems."""
    db = ProblemDB()
    problems = db.get_all_problems()
    
    if not problems:
        rprint("[yellow]No problems found. Use 'add' to create your first problem.[/yellow]")
        return
    
    # Calculate statistics
    total_problems = len(problems)
    
    # Count solutions by language
    language_counts = {}
    for problem in problems:
        solutions = problem.get("solutions", [])
        for solution in solutions:
            lang = solution.get("language", "unknown").upper()
            language_counts[lang] = language_counts.get(lang, 0) + 1
    
    # Build stats text
    stats_text = f"[bold cyan]Total Problems Solved:[/bold cyan] {total_problems}\n\n"
    
    if language_counts:
        stats_text += "[bold cyan]Solutions by Language:[/bold cyan]\n"
        # Sort by count (descending)
        sorted_langs = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
        for lang, count in sorted_langs:
            stats_text += f"  • {lang}: {count}\n"
    else:
        stats_text += "[dim]No solutions recorded.[/dim]\n"
    
    # Display in panel
    panel = Panel(stats_text, title="[bold green]CP Tracker Statistics[/bold green]", border_style="green")
    console.print(panel)


if __name__ == "__main__":
    app()
