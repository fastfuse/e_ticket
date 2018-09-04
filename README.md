## Public Transport E-Ticketing System backend

### Development

* Install requirements:
```sh
$> pip install -r requirements.txt
```

* Export environment variables:
```sh
$> export FLASK_APP="application/__init__.py"
$> export APP_SETTINGS="config.DevelopmentConfig"
$> export FLASK_ENV="development"
```

* Fire up DB:
```sh
$> docker-compose up -d postgres
```

* Migrate database:
```sh
$> flask db init
$> flask db migrate
$> flask db upgrade
```

* Run development server:
```sh
$> flask run
```