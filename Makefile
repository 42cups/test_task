syncdb:
	python manage.py syncdb --noinput
migrate:
	python manage.py migrate
syncdb:
	python manage.py collectstatic --noinput
test:
	python manage.py  test test_cup
run:
	python manage.py runserver
