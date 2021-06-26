from website import create_app

app = create_app()

# only if main.py is run, will we run the web server
if __name__ == "__main__":
    app.run(debug=True) # every change to code, will automatically rerun, not for production
