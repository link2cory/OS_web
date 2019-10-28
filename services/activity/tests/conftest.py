import os
import pytest

@pytest.fixture(scope='session')
def docker_compose_files(pytestconfig):
    return [os.path.join(str(pytestconfig.rootdir), 'docker-compose.yml'),
            os.path.join(str(pytestconfig.rootdir), 'docker-compose-dev.yml')]

@pytest.fixture(scope='session')
def docker_web(docker_services):
    docker_services.start('web')
    public_port = docker_services.wait_for_service("web", 5000)
    endpoint = 'api/activity'
    url = "http://{docker_services.docker_ip}:{public_port}/{endpoint}".format(**locals())
    return url
