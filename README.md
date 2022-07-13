1. Cream repository-ul `learning-mvt-architecture` pe GitHub
2. Il clonam local in folder-ul `finalProjects`
3. Ne cream un nou environment urmand pasii: [File -> New Project -> Selectam finalProjects -> OK -> Create]
4. Instalam `Django`, `pip` si `ipython` urmand pasii de mai jos:
    [file -> settings -> Project: finalProjects -> Python Interpreter -> dam install la fiecare in parte]
5. `cd learning-mvt-architecture`
6. `django-admin startproject ssm_project`
7. `cd ssm_project` 
8. `python manage.py startapp ssm_app`
9. [settings.py -> INSTALLED_APPS -> adaugam 'ssm_app']
10. `python manage.py runserver` 
    Dupa rularea acestei comnenzi vom primi mesajul:
    "You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them."
11. `python manage.py migrate`   ->  Apply all migrations: admin, auth, contenttypes, sessions
12. `python manage.py createsuperuser`
     username
     email address
     password
     password (again)
13. Mergem pe ruta `http://127.0.0.1:8000/admin/` -> introducem userul si parola -> ne logam la admin panel-ul oferit de Django
14. Cream in `models.py` tabelele Playlist, Album, Genre, Artist, Song 
15. `python manage.py makemigrations` 
16. `python manage.py migrate`
17. In `admin.py` adaugam pentru fiecare tabela `admin.site.register(Playlist)`
18. Mergem pe ruta `http://127.0.0.1:8000/admin/` si ne populam baza de date. 
    Putem sa facem asta si din [python manage.py shell -> from ssm_app.models import *]
19. In `ssm_app` cream folderul `templates -> base.html -> homepage.html` (cu view-ul si template-ul aferent)
20. Cream folderul `static`  -> media unde punem _pozele_
                             -> css -> style.css

