# Numbers written in words

This django application converts numbers into words. It supports polish language only.

## Installing

Required packages:

* git
* Docker
* docker-compose

```
git clone https://github.com/DawidMakar/numbers-written-in-words.git
cd numbers-written-in-words
docker-compose up -d --build
```

## Running the tests

1. While docker container is up, run following command to access app terminal:
```
docker exec -it numbers-written-in-words_web_1 /bin/bash
```
2. Run 'test' command:
```
python3 manage.py test core
```

Tests check request methods (get/post) for the main view as well as correctness of converting function's output results.

Example:

```
def test_thousands(self):
    # (...)
    self.assertEqual(convert_number_to_words('145712'),
                     'sto czterdzieści pięć tysięcy siedemset dwanaście')
```

## Built With

* [Python 3](https://docs.python.org/3/)
* [Django 2](https://docs.djangoproject.com/en/2.1/) - The web framework used


## Authors

* **Dawid Makar** - *Initial work* - [DawidMakar](https://github.com/DawidMakar)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
