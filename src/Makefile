dev-start:
	python manage.py runserver --settings=recipe_project.settings.dev
prod-start:
	python manage.py runserver --settings=recipe_project.settings.prod
dev-migrate:
	python manage.py migrate --settings=recipe_project.settings.dev
dev-makemigrations:
	python manage.py makemigrations --settings=recipe_project.settings.dev
dev-test:
	python manage.py test --settings=recipe_project.settings.dev
# add prod
install-dev:
	pip install -r requirements/dev.txt