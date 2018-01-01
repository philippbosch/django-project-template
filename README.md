# {{ project_name }}

## Development environment set-up

```shell
$ git clone git@github.com:philippbosch/{{ project_name }}.git
$ touch .env
$ docker-compose build
$ docker-compose up
$ docker-compose run --rm web python manage.py migrate
$ docker-compose run --rm web python manage.py createsuperuser
```

## Running the development stack

```shell
$ docker-compose up
```

## Styles development

Ensure that all required npm packages are installed with `npm install` and
that the Django development server is running, then run the `dev` command.

```shell
$ npm install
$ npm run dev
```

The site will be proxied by BrowserSync at [`http://localhost:3000`](http://localhost:3000).

The `npm run dev` command runs in watch mode, rebuilding the styles and
automatically refreshing the site whenever changes are detected.

See [STYLEGUIDE.md](STYLEGUIDE.md) for an introduction to the styles system.
