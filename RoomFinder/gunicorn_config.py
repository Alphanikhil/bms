import os

# Bind to 0.0.0.0 to access the server from outside
bind = f"0.0.0.0:{os.environ.get('PORT', '10000')}"

# Worker configuration
workers = 4
worker_class = 'sync'

# Timeout configuration
timeout = 120

# Logging
accesslog = '-'
errorlog = '-'
