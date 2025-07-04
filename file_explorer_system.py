"""
File System Explorer

This module provides functions for recursively exploring file systems,
searching for files, and analyzing file metadata.
"""

# Sample file system structure for demonstration
def create_sample_file_system():
    """
    Create a sample file system structure for demonstration purposes.
    
    Returns:
        dict: A dictionary representing a file system structure with sizes
    """
    return {
        "Documents": {
            "Projects": {
                "project1.docx": 2500000,
                "project2.docx": 1800000,
                "notes.txt": 15000,
                "data.csv": 350000,
            },
            "Personal": {
                "resume.pdf": 520000,
                "budget.xlsx": 480000,
                "Photos": {
                    "vacation.jpg": 3500000,
                    "family.jpg": 2800000,
                    "graduation.png": 4200000,
                }
            },
            "report.pdf": 750000,
        },
        "Downloads": {
            "program.exe": 15000000,
            "Library": {
                "book1.pdf": 12000000,
                "book2.pdf": 9500000,
            },
            "song.mp3": 8000000,
            "video.mp4": 35000000,
        },
        "temp.txt": 2000,
    }

# Directory traversal functions
def list_all_files(directory, file_system=None, path_prefix=""):
    """
    Recursively list all files in a directory structure.
    
    Args:
        directory (str): The directory to list files from
        file_system (dict): The simulated file system structure
        path_prefix (str): Path prefix for constructing full file paths
        
    Returns:
        list: List of all file paths in the directory structure
        
    Base case:
        When we reach a file (value is an integer representing size)
        
    Recursive case:
        When we encounter a directory (dict), process each item inside it
    """
    # Use the sample file system if none provided
    if file_system is None:
        file_system = create_sample_file_system()
    
    # Check if file_system is a valid dictionary
    if not isinstance(file_system, dict):
        raise TypeError("File system must be a dictionary")
    
    # Initialize result list
    files = []
    
    # Navigate to target directory if specified
    parts = directory.split("/") if directory else []
    current = file_system
    
    # Navigate through path
    for part in parts:
        if part and part in current and isinstance(current[part], dict):
            current = current[part]
        elif part:
            # Path not found, return empty list
            return []
    
    # Process all items in current directory
    for name, value in current.items():
        # Base case: When value is integer (file)
        if isinstance(value, int):
            # Construct file path
            if path_prefix:
                file_path = f"{path_prefix}/{name}"
            else:
                file_path = name
            files.append(file_path)
        
        # Recursive case: When value is dictionary (directory)
        elif isinstance(value, dict):
            # Construct directory path
            if path_prefix:
                new_prefix = f"{path_prefix}/{name}"
            else:
                new_prefix = name
            # Recursive call
            files.extend(list_all_files("", value, new_prefix))
    
    return files

def calculate_directory_size(directory, file_system=None):
    """
    Recursively calculate the total size of all files in a directory.
    
    Args:
        directory (str): The directory to calculate size for
        file_system (dict): The simulated file system structure
        
    Returns:
        int: Total size in bytes of all files in the directory
        
    Base case:
        When we reach a file (value is an integer representing size)
        
    Recursive case:
        When we encounter a directory (dict), sum the sizes of all its contents
    """
    # Use the sample file system if none provided
    if file_system is None:
        file_system = create_sample_file_system()
    
    # Check if file_system is a valid dictionary
    if not isinstance(file_system, dict):
        raise TypeError("File system must be a dictionary")
    
    # Navigate to target directory if specified
    parts = directory.split("/") if directory else []
    current = file_system
    
    # Navigate through path
    for part in parts:
        if part and part in current and isinstance(current[part], dict):
            current = current[part]
        elif part:
            # Path not found, return 0
            return 0
    
    # Initialize total size
    total_size = 0
    
    # Process all items in current directory
    for name, value in current.items():
        # Base case: When value is integer (file)
        if isinstance(value, int):
            total_size += value
        
        # Recursive case: When value is dictionary (directory)
        elif isinstance(value, dict):
            # Recursive call
            total_size += calculate_directory_size("", value)
    
    return total_size

def find_by_extension(directory, extension, file_system=None, path_prefix=""):
    """
    Recursively find all files with a specific extension.
    
    Args:
        directory (str): The directory to search in
        extension (str): The file extension to search for (e.g., 'pdf')
        file_system (dict): The simulated file system structure
        path_prefix (str): Path prefix for constructing full file paths
        
    Returns:
        list: List of paths to files with the specified extension
        
    Base case:
        When we reach a file, check if it has the target extension
        
    Recursive case:
        When we encounter a directory, search each item inside it
    """
    # Use the sample file system if none provided
    if file_system is None:
        file_system = create_sample_file_system()
    
    # Check if file_system is a valid dictionary
    if not isinstance(file_system, dict):
        raise TypeError("File system must be a dictionary")
    
    # Convert extension to string and lowercase
    extension = str(extension).lower()
    
    # Initialize result list
    matching_files = []
    
    # Navigate to target directory if specified
    parts = directory.split("/") if directory else []
    current = file_system
    
    # Navigate through path
    for part in parts:
        if part and part in current and isinstance(current[part], dict):
            current = current[part]
        elif part:
            # Path not found, return empty list
            return []
    
    # Process all items in current directory
    for name, value in current.items():
        # Base case: When value is integer (file)
        if isinstance(value, int):
            # Extract file extension
            file_ext = name.split('.')[-1].lower() if '.' in name else ""
            # Check extension match
            if file_ext == extension:
                # Construct file path
                if path_prefix:
                    file_path = f"{path_prefix}/{name}"
                else:
                    file_path = name
                matching_files.append(file_path)
        
        # Recursive case: When value is dictionary (directory)
        elif isinstance(value, dict):
            # Construct directory path
            if path_prefix:
                new_prefix = f"{path_prefix}/{name}"
            else:
                new_prefix = name
            # Recursive call
            matching_files.extend(find_by_extension("", extension, value, new_prefix))
    
    return matching_files

def find_by_name(directory, pattern, file_system=None, path_prefix=""):
    """
    Recursively find all files whose names contain a specific pattern.
    
    Args:
        directory (str): The directory to search in
        pattern (str): The name pattern to search for
        file_system (dict): The simulated file system structure
        path_prefix (str): Path prefix for constructing full file paths
        
    Returns:
        list: List of paths to files matching the name pattern
        
    Base case:
        When we reach a file, check if its name contains the pattern
        
    Recursive case:
        When we encounter a directory, search each item inside it
    """
    # Use the sample file system if none provided
    if file_system is None:
        file_system = create_sample_file_system()
    
    # Check if file_system is a valid dictionary
    if not isinstance(file_system, dict):
        raise TypeError("File system must be a dictionary")
    
    # Convert pattern to string and lowercase
    pattern = str(pattern).lower()
    
    # Initialize result list
    matching_files = []
    
    # Navigate to target directory if specified
    parts = directory.split("/") if directory else []
    current = file_system
    
    # Navigate through path
    for part in parts:
        if part and part in current and isinstance(current[part], dict):
            current = current[part]
        elif part:
            # Path not found, return empty list
            return []
    
    # Process all items in current directory
    for name, value in current.items():
        # Base case: When value is integer (file)
        if isinstance(value, int):
            # Check pattern match
            if pattern in name.lower():
                # Construct file path
                if path_prefix:
                    file_path = f"{path_prefix}/{name}"
                else:
                    file_path = name
                matching_files.append(file_path)
        
        # Recursive case: When value is dictionary (directory)
        elif isinstance(value, dict):
            # Construct directory path
            if path_prefix:
                new_prefix = f"{path_prefix}/{name}"
            else:
                new_prefix = name
            # Recursive call
            matching_files.extend(find_by_name("", pattern, value, new_prefix))
    
    return matching_files

def count_files_by_type(directory, file_system=None):
    """
    Recursively count files by their extension.
    
    Args:
        directory (str): The directory to analyze
        file_system (dict): The simulated file system structure
        
    Returns:
        dict: Dictionary with extensions as keys and counts as values
        
    Base case:
        When we reach a file, increment the count for its extension
        
    Recursive case:
        When we encounter a directory, count files in all its subdirectories
    """
    # Use the sample file system if none provided
    if file_system is None:
        file_system = create_sample_file_system()
    
    # Check if file_system is a valid dictionary
    if not isinstance(file_system, dict):
        raise TypeError("File system must be a dictionary")
    
    # Initialize result dictionary
    type_counts = {}
    
    # Navigate to target directory if specified
    parts = directory.split("/") if directory else []
    current = file_system
    
    # Navigate through path
    for part in parts:
        if part and part in current and isinstance(current[part], dict):
            current = current[part]
        elif part:
            # Path not found, return empty dict
            return {}
    
    # Process all items in current directory
    for name, value in current.items():
        # Base case: When value is integer (file)
        if isinstance(value, int):
            # Extract file extension
            extension = name.split('.')[-1].lower() if '.' in name else "no_extension"
            # Increment count
            type_counts[extension] = type_counts.get(extension, 0) + 1
        
        # Recursive case: When value is dictionary (directory)
        elif isinstance(value, dict):
            # Recursive call
            sub_counts = count_files_by_type("", value)
            # Merge dictionaries
            for ext, count in sub_counts.items():
                type_counts[ext] = type_counts.get(ext, 0) + count
    
    return type_counts

def find_largest_files(directory, n, file_system=None):
    """
    Recursively find the n largest files in a directory.
    
    Args:
        directory (str): The directory to search in
        n (int): The number of large files to find
        file_system (dict): The simulated file system structure
        
    Returns:
        list: List of tuples (path, size) for the n largest files
        
    Base case:
        When we reach a file, consider it for the largest files list
        
    Recursive case:
        When we encounter a directory, search all its subdirectories
    """
    # Validate n parameter
    try:
        n = int(n)
        if n < 0:
            return []  # Return empty list for negative n
    except (TypeError, ValueError):
        raise TypeError("n must be an integer")
    
    # Use the sample file system if none provided
    if file_system is None:
        file_system = create_sample_file_system()
    
    # Check if file_system is a valid dictionary
    if not isinstance(file_system, dict):
        raise TypeError("File system must be a dictionary")
    
    # Create helper function to collect all files
    def collect_all_files(current_dict, current_path=""):
        """Helper function to recursively collect all files with their sizes"""
        all_files = []
        
        # Process all items in current directory
        for name, value in current_dict.items():
            # Base case: If file
            if isinstance(value, int):
                # Construct path
                if current_path:
                    file_path = f"{current_path}/{name}"
                else:
                    file_path = name
                # Add tuple (path, size)
                all_files.append((file_path, value))
            
            # Recursive case: If directory
            elif isinstance(value, dict):
                # Construct path
                if current_path:
                    new_path = f"{current_path}/{name}"
                else:
                    new_path = name
                # Recursive call
                all_files.extend(collect_all_files(value, new_path))
        
        return all_files
    
    # Navigate to target directory if specified
    parts = directory.split("/") if directory else []
    current = file_system
    
    # Navigate through path
    for part in parts:
        if part and part in current and isinstance(current[part], dict):
            current = current[part]
        elif part:
            # Path not found, return empty list
            return []
    
    # Collect all files
    all_files = collect_all_files(current)
    
    # Sort by size (descending)
    all_files.sort(key=lambda x: x[1], reverse=True)
    
    # Return top n files
    return all_files[:n]

def format_file_size(size_bytes):
    """
    Format file size from bytes to human-readable format.
    
    Args:
        size_bytes (int): File size in bytes
        
    Returns:
        str: Human-readable file size (e.g., "1.23 MB")
    """
    try:
        size = float(size_bytes)
    except (TypeError, ValueError):
        raise TypeError("Size must be a number")
    
    # Handle negative sizes
    if size < 0:
        return f"-{format_file_size(-size)}"
    
    # Define size units
    units = ["B", "KB", "MB", "GB", "TB"]
    unit_index = 0
    
    # Convert to appropriate unit
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    
    # Format result
    if unit_index == 0:
        return f"{int(size)} {units[unit_index]}"
    else:
        return f"{size:.2f} {units[unit_index]}"

def main():
    """
    Main function demonstrating the file system explorer.
    """
    print("===== FILE SYSTEM EXPLORER =====")
    file_system = create_sample_file_system()
    
    # Directory Summary
    print("\n----- DIRECTORY SUMMARY -----")
    all_files = list_all_files("", file_system)
    total_size = calculate_directory_size("", file_system)
    formatted_size = format_file_size(total_size)
    print(f"Total files: {len(all_files)}")
    print(f"Total size: {formatted_size}")
    
    # File Type Distribution
    print("\n----- FILE TYPE DISTRIBUTION -----")
    type_counts = count_files_by_type("", file_system)
    for file_type, count in type_counts.items():
        print(f"{file_type}: {count} files")
    
    # Search by Extension
    print("\n----- SEARCH BY EXTENSION -----")
    pdf_files = find_by_extension("", "pdf", file_system)
    print(f"PDF files found: {len(pdf_files)}")
    for pdf_file in pdf_files:
        print(f"  {pdf_file}")
    
    # Search by Name
    print("\n----- SEARCH BY NAME -----")
    project_files = find_by_name("", "project", file_system)
    print(f"Project files found: {len(project_files)}")
    for project_file in project_files:
        print(f"  {project_file}")
    
    # Largest Files
    print("\n----- LARGEST FILES -----")
    largest_files = find_largest_files("", 5, file_system)
    for path, size in largest_files:
        print(f"{path}: {format_file_size(size)}")
    
    # Specific Directory Analysis
    print("\n----- SPECIFIC DIRECTORY ANALYSIS -----")
    photos_files = list_all_files("Documents/Personal/Photos", file_system)
    photos_size = calculate_directory_size("Documents/Personal/Photos", file_system)
    print(f"Photos directory contains {len(photos_files)} files")
    print(f"Photos directory total size: {format_file_size(photos_size)}")

if __name__ == "__main__":
    main()