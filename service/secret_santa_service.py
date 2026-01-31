from typing import List, Dict, Any
import random
import copy

class SecretSantaService:
    """
    Service to handle Secret Santa game logic.
    """
    
    @staticmethod
    def assign_secret_santa(employees: List[Dict[str, Any]], last_year_data: List[Dict[str, Any]] = None) -> List[Dict[str, str]]:
        """
        Assigns Secret Santas to employees based on constraints.
        
        Constraints:
        1. An employee cannot choose themselves.
        2. An employee cannot be assigned the same child as last year.
        3. Each employee has exactly one child.
        4. Each child has exactly one Santa.
        
        Args:
            employees (List[Dict[str, Any]]): List of current employees.
            last_year_data (List[Dict[str, Any]], optional): List of last year's assignments.
            
        Returns:
            List[Dict[str, str]]: A list of dictionaries with assignment details.
        """
        if not employees:
            return []

        n = len(employees)
        
        # Map email to index for graph processing
        idx_to_email = {i: emp['Employee_EmailID'] for i, emp in enumerate(employees)}

        # Build lookup for previous assignments
        previous_assignments = set()
        if last_year_data:
            for entry in last_year_data:
                santa = entry.get('Employee_EmailID')
                child = entry.get('Secret_Child_EmailID')
                if santa and child:
                    previous_assignments.add((santa, child))

        # Build Adjacency List (Directed Graph)
        # Left side: Santas (0 to n-1), Right side: Children (0 to n-1)
        # Edge u -> v means u CAN give to v
        adj = [[] for _ in range(n)]
        
        for u in range(n):
            santa_email = idx_to_email[u]
            for v in range(n):
                child_email = idx_to_email[v]
                
                # Constraint 1: Not self
                if u == v:
                    continue
                
                # Constraint 2: Not same as last year
                if (santa_email, child_email) in previous_assignments:
                    continue
                
                adj[u].append(v)

        # Maximum Bipartite Matching (using DFS based approach / Kuhn's algorithm)
        # match[v] stores the santa assigned to child v
        match = [-1] * n 
        
        def dfs(u: int, visited: List[bool]) -> bool:
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if match[v] < 0 or dfs(match[v], visited):
                        match[v] = u
                        return True
            return False

        # Try to find a match for every santa
        matches_found = 0
        for u in range(n):
            visited = [False] * n
            if dfs(u, visited):
                matches_found += 1
        
        if matches_found < n:
            print("Error: Could not find a valid assignment for all employees due to strict constraints.")
            return []

        # Construct result
        assignments = []
        for child_idx, santa_idx in enumerate(match):
            santa = employees[santa_idx]
            child = employees[child_idx]
            assignments.append({
                'Employee_Name': santa['Employee_Name'],
                'Employee_EmailID': santa['Employee_EmailID'],
                'Secret_Child_Name': child['Employee_Name'],
                'Secret_Child_EmailID': child['Employee_EmailID']
            })
            
        return assignments
