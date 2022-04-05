cd /web/goplaciz-backend &&
source .venv/bin/activate &&
source conf &&
gunicorn -b 0.0.0.0:8070 goplaciz.wsgi:application --workers 4