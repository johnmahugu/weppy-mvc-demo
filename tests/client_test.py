from weppy_mvc_demo import User, db
from weppy_mvc_demo import utils
from .fixtures import client, admin_client, logged_client, TEST_USER


def test_welcome_page_access(client):
    resp = client.get('/')
    assert 'Welcome to Weppy Mvc Demo' in resp.data


def test_error_404(client):
    resp = client.get(utils.get_cryptogen_string())
    assert "<title>Weppy Mvc Demo-404</title>" in resp.data


def test_account_page_access(client):
    resp = client.get('/account/login')
    assert "Weppy Mvc Demo | Account" in resp.data


def test_users_page_access(client):
    resp = client.get('/users/')
    assert "Weppy Mvc Demo-403" in resp.data


def test_admin_users_page_access(admin_client):
    resp = admin_client.get('/users/')
    assert "Weppy Mvc Demo | Users" in resp.data


def test_login_page(logged_client):
    resp = logged_client.get('/account/profile')
    assert 'Profile' in resp.data


def test_profile_page(logged_client):
    db._adapter.reconnect()
    rows = db(User.email == TEST_USER.email).select()
    test_user_id = rows[0].id
    resp = logged_client.get('/user/{}'.format(test_user_id))
    assert TEST_USER.first_name in resp.data
    assert TEST_USER.last_name in resp.data


def test_maintenance_page(client):
    resp = client.get("/maintenance_check")
    assert "Weppy Mvc Demo | Maintenance" in resp.data


def test_tour_page(client):
    resp = client.get("/tour")
    assert "Weppy Mvc Demo | Tour" in resp.data


def test_health_check_page(client):
    # TODO: Move to api endpoint
    resp = client.get("/health-check")
    assert "Status OK" in resp.data
