# Weppy Mvc Demo 
[![Build Status](https://travis-ci.org/mijdavis2/weppy-mvc-demo.svg?branch=master)](https://travis-ci.org/mijdavis2/weppy_mvc_demo)
[![Coverage Status](https://coveralls.io/repos/github/mijdavis2/weppy-mvc-demo/badge.svg?branch=master)](https://coveralls.io/github/mijdavis2/weppy_mvc_demo?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/da6e4e83204b46eb88f83758ef27cd12)](https://www.codacy.com/app/mijdavis2/weppy-mvc-demo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mijdavis2/weppy-mvc-demo&amp;utm_campaign=Badge_Grade)

Weppy Mvc Demo is a full stack python application built with generator-weppy-mvc.
Generator-weppy-mvc is based on the starter-weppy project.

>Starter Weppy is a python web application starter kit built on the [weppy framework](https://github.com/gi0baro/weppy). 
>Current version is based on Weppy 0.6 with an MVC scaffolding. 
>An api module, dev mode, and 100% test coverage are included out of the box.

## Run

**Requirements**:
- Python 3.4+ or 3.5+

For automated pip and virtual env setup and creation, 
clone this repository and in your terminal do:

```
. ./setup.sh
python run.py
```

Otherwise, do:

```
pip install -r requirements.txt
python run.py
```

### Docker

To make your application available at ```http://localhost/```:

```
docker build -t weppy_mvc_demo .
docker run -it -p 80:8000 --rm --name weppy_mvc_demo weppy_mvc_demo
```


## Develop

Running in development mode will enable debug pages,
automatically create test, users in multiple states,
and upon killing the app, those test users will automatically be 
deleted from the DB.

To start the app in development mode, do:

```
python run.py --dev
```

See ```weppy_mvc_demo/cli.py``` for cli commands. 

## Test

```
py.test -v -s --cov-report term-missing --cov=weppy_mvc_demo -r w tests
```


## License

MIT © [mijdavis2](http://mdavisinsc.com)


[npm-image]: https://badge.fury.io/js/generator-weppy-mvc.svg
[npm-url]: https://npmjs.org/package/generator-weppy-mvc
[travis-image]: https://travis-ci.org/mijdavis2/generator-weppy-mvc.svg?branch=master
[travis-url]: https://travis-ci.org/mijdavis2/generator-weppy-mvc
[daviddm-image]: https://david-dm.org/mijdavis2/generator-weppy-mvc.svg?theme=shields.io
[daviddm-url]: https://david-dm.org/mijdavis2/generator-weppy-mvc
[coveralls-image]: https://coveralls.io/repos/mijdavis2/generator-weppy-mvc/badge.svg
[coveralls-url]: https://coveralls.io/r/mijdavis2/generator-weppy-mvc
