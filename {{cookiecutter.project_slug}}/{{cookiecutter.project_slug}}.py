from app import create_app

# Import models that need to be migrated
from app.user.model import blacklist_model, user_model

app = create_app()
