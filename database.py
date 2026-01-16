"""Database operations for CP Tracker using TinyDB."""

from pathlib import Path
from tinydb import TinyDB, Query
from typing import Optional, List, Dict, Any


class ProblemDB:
    """Wrapper class for TinyDB operations on problem documents."""
    
    def __init__(self, db_path: str = "data.json"):
        """Initialize database connection."""
        self.db_path = Path(db_path)
        self.db = TinyDB(str(self.db_path))
        self.problems = self.db.table('problems')
        self.Problem = Query()
    
    def find_problem(self, title: str, platform: str) -> Optional[Dict[str, Any]]:
        """
        Find a problem by title and platform.
        
        Returns:
            Problem document with doc_id key if found, None otherwise
        """
        # Search for matching documents
        condition = (self.Problem.title == title) & (self.Problem.platform == platform)
        results = self.problems.search(condition)
        
        if not results:
            return None
        
        # Find the doc_id by checking each document
        # TinyDB uses integer doc_ids starting from 1
        doc = results[0]
        # We need to find which doc_id corresponds to this document
        # Use get() to retrieve by doc_id and compare
        all_docs = self.problems.all()
        max_id = len(all_docs) + 10  # Small buffer for safety
        
        for doc_id in range(1, max_id + 1):
            try:
                retrieved = self.problems.get(doc_id=doc_id)
                if retrieved and retrieved.get('title') == title and retrieved.get('platform') == platform:
                    result = doc.copy()
                    result['doc_id'] = doc_id
                    return result
            except (KeyError, ValueError):
                continue
        
        # Fallback: return document without doc_id (shouldn't happen)
        result = doc.copy()
        return result
    
    def add_problem(self, problem_data: Dict[str, Any]) -> int:
        """
        Add a new problem to the database.
        
        Args:
            problem_data: Dictionary containing problem information
        
        Returns:
            Document ID of the inserted problem
        """
        return self.problems.insert(problem_data)
    
    def update_problem(self, doc_id: int, updates: Dict[str, Any]) -> None:
        """
        Update an existing problem document.
        
        Args:
            doc_id: Document ID to update
            updates: Dictionary of fields to update
        """
        self.problems.update(updates, doc_ids=[doc_id])
    
    def get_all_problems(self) -> List[Dict[str, Any]]:
        """
        Retrieve all problems from the database.
        
        Returns:
            List of all problem documents
        """
        return self.problems.all()
    
    def problem_has_language(self, problem: Dict[str, Any], language: str) -> bool:
        """
        Check if a problem already has a solution in the given language.
        
        Args:
            problem: Problem document
            language: Language to check
        
        Returns:
            True if language solution exists, False otherwise
        """
        solutions = problem.get('solutions', [])
        normalized_lang = language.lower().strip()
        return any(
            sol.get('language', '').lower() == normalized_lang 
            for sol in solutions
        )
