syncdb:
	python manage.py syncdb --noinput
migrate:
	python manage.py migrate
test:
	python manage.py  test test_cup
run:
	python manage.py runserver
