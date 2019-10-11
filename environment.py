#  This script should generate environment variables for allure reports,
#  which will depend on GitLab pipeline configuration and test instance.
#  All environment variables will be stored in the environment.properties file:
#  "InstanceType"="Instance"
#  "Host"="http://localhost"
#  "Port"="8081"

from os import environ
from pyhocon import ConfigFactory
import requests


conf = ConfigFactory.parse_file("reference.conf")
HOST = environ.get("TEST_STAND_HOST", conf.get_string("test_host"))
PORT = environ.get("TEST_STAND_PORT", conf.get_string("test_port"))


def get_runner_type():
    if HOST == "https://your_host":
        return "EgInstance"
    elif HOST == "https://localhost":
        return "LocalInstance"
    else:
        return "Something Else"


API = requests.get(
    "{}:{}/version/software/".format(HOST, PORT)
).text
API_VERSION = '"Version"={}\n'.format(API)
RUNNER_TYPE = '"Type"="{}"\n'.format(get_runner_type())
HOST = '"Host"="{}"\n'.format(HOST)
PORT = '"Port"="{}"\n'.format(PORT)


def main():
    with open("environment.properties", "a+") as f:
        f.write(RUNNER_TYPE)
        f.write(HOST)
        f.write(PORT)
        f.write(API_VERSION)
        f.close()


if __name__ == "__main__":
    main()
