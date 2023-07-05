from app import app
from app.models import User, Artwork

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Artwork': Artwork}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
