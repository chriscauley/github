Homer Coding Test
=======

Run the folloging bash commands:

```
pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver
```

The app should now be running on localhost:8000

Important Files
=======

* `github/models.py` - Repository model

* `github/forms.py` - Form for saving and validating repositories

* `main/views.py` - Basically just glue to hold the python and html together

* `main/templates/index.html` - The form and script tags

* `main/static/github.tag` - Riot tag `<repository-viewer>`, which generates the buttons and the graph

* `main/static/less/homer.less` - Styling for the graph (included here as `main/static/less/homer.css` because less.js is hard to install on some operating systems)
