dev-start:
	python manage.py runserver --settings=recipe_project.settings.dev
dev-migrate:
	python manage.py migrate --settings=recipe_project.settings.dev
dev-makemigrations:
	python manage.py makemigrations --settings=recipe_project.settings.dev
dev-test:
	python manage.py test --settings=recipe_project.settings.dev

#production
prod-start:
	python manage.py runserver --settings=recipe_project.settings.prod
prod-migrate:
	python manage.py migrate --settings=recipe_project.settings.prod
prod-makemigrations:
	python manage.py makemigrations --settings=recipe_project.settings.prod
prod-test:
	python manage.py test --settings=recipe_project.settings.prod

install-dev:
	pip install -r requirements/dev.txt