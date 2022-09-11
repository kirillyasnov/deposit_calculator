from fastapi.testclient import TestClient
import pytest

from app.main import app


@pytest.fixture()
def test_app():
    return TestClient(app)


def test_deposits_success(test_app):
    response = test_app.post(url='/deposits',
                             json={'date': '31.01.2021',
                                   'periods': 3,
                                   'amount': 10000,
                                   'rate': 6})
    assert response.status_code == 200
    assert response.json() == {
        '31.01.2021': 10050,
        '28.02.2021': 10100.25,
        '31.03.2021': 10150.75
    }


@pytest.mark.parametrize('test_app, not_valid_request', [
    (test_app, {'date': '31.01.21',
                'periods': 3,
                'amount': 10000,
                'rate': 6}),
    (test_app, {'date': '31.01.2021',
                'periods': 61,
                'amount': 10000,
                'rate': 6}),
    (test_app, {'date': '31.01.2021',
                'periods': 3,
                'amount': 9999,
                'rate': 6}),
    (test_app, {'date': '31.01.2021',
                'periods': 3,
                'amount': 10000,
                'rate': 10})
])
def test_deposits_validation_error(test_app, not_valid_request):
    test_app = TestClient(app)
    response = test_app.post(url='/deposits', json=not_valid_request)
    assert response.status_code == 400
    assert response.json().get('error') is not None
