from collections import defaultdict
import time

requests = defaultdict(list)

def check_rate_limit(user):
    now = time.time()
    requests[user] = [t for t in requests[user] if now - t < 60]

    if len(requests[user]) > 5:
        return False

    requests[user].append(now)
    return True

from time import time

# Store request timestamps per user
user_requests = {}

def check_rate_limit(user: str, limit: int = 5, window: int = 60) -> bool:
    current_time = time()

    # Initialize user if not exists
    if user not in user_requests:
        user_requests[user] = []

    # Remove old requests outside window
    user_requests[user] = [
        t for t in user_requests[user]
        if current_time - t < window
    ]

    # Check limit
    if len(user_requests[user]) >= limit:
        return False

    # Add new request
    user_requests[user].append(current_time)

    return True