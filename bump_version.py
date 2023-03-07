import sys

def bump_version(current_version, commit_message):
    """
    Bump the version based on the commit message.

    Args:
        current_version (str): The current version in MAJOR.MINOR.PATCH format.
        commit_message (str): The commit message in <change-type>: <change message> format.

    Returns:
        str: The new version in MAJOR.MINOR.PATCH format.
    """
    try:
        major, minor, patch = map(int, current_version.split('.'))
    except ValueError as e:
        return None
    change_type = commit_message.split(':')[0].lower().strip()
    if change_type == 'ci':
        patch += 1
    elif change_type == 'chore':
        patch += 1
    elif change_type == 'feat' or change_type == 'feature':
        minor += 1
        patch = 0
    elif change_type == 'minor':
        minor += 1
        patch = 0
    elif change_type == 'breaking':
        major += 1
        minor = 0
        patch = 0
    elif change_type == 'major':
        major += 1
        minor = 0
        patch = 0
    else:
        patch += 1
    return f'{major}.{minor}.{patch}'

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(bump_version(sys.argv[1], sys.argv[2]))