""" VSTS Worker Testing Package """
import pytest
from vsts import VstsWorker
from mock import patch


@pytest.fixture(scope='module')
def vsts_setup():
    """ Setup Fixture """
    return VstsWorker('http://test.com/', 'user1', 'hemmligIkkeDel',
                      'project')


def test_init(vsts_setup):
    """ Create init """
    assert vsts_setup.base_url == 'http://test.com/'
    assert vsts_setup.username == 'user1'
    assert vsts_setup.pat == 'hemmligIkkeDel'
    assert vsts_setup.project == 'project'


@patch('base64.encodestring')
@patch('urllib2.urlopen')
@patch('urllib2.Request')
def test_create_request_no_data(urllib2_request, urllib2_urlopen, base64_encodestring, vsts_setup):
    """ Create Request if data none """
    url = 'http://setmeup.com'
    vsts_setup.create_request(url)
    urllib2_request.assert_called_with(url)
    urllib2_urlopen.assert_called_once()
    base64_encodestring.assert_called_once()


@patch('base64.encodestring')
@patch('urllib2.urlopen')
@patch('urllib2.Request')
def test_create_request_data(urllib2_request, urllib2_urlopen, base64_encodestring, vsts_setup):
    """ Create Request if data """
    url = 'http://setmeup.com'
    data = {'a': 1, 'b': 3}
    vsts_setup.create_request(url, data)
    urllib2_request.assert_called_with(url, data,
                                       {'Content-Type': 'application/json'})
    urllib2_urlopen.assert_called_once()
    base64_encodestring.assert_called_once()


@patch('json.load')
@patch('vsts.VstsWorker.create_request')
def test_create_wit_calls_create_request(request_mock, json_mock, vsts_setup):
    """ Test the create_wit calls create_request """
    vsts_setup.create_wit('testproj', 'test_wit')
    request_mock.assert_called_with(
        'http://test.com/DefaultCollection/testproj/_apis/wit/workitems/' +
        '$test_wit?api-version=2.0')
    json_mock.assert_called_once()


def test_create_training_data_returns_json_object(vsts_setup):
    """ Test the create_wit calls create_request """
    users = [{
        'firstname': 'Test',
        'lastname': 'User'
    }]
    data = vsts_setup.create_training_data(1, users, ['Wk1', 'Wk2'])
    assert 'Sprint 1' in data
    assert 'Test User' in data
    assert 'Test Wk1 training' in data
    assert 'Test Wk2 training' in data
    assert 'Test User' in data
    data = vsts_setup.create_training_data(5, users, ['Wk1', 'Wk2'])
    assert 'Sprint 5' in data


@patch('json.load')
@patch('vsts.VstsWorker.create_request')
def test_get_iterations_returns_json_object(request_mock, json_mock, vsts_setup):
    data = vsts_setup.get_iterations()
    request_mock.assert_called_with(
        'http://test.com/DefaultCollection/project/_apis/wit/'+
        'classificationNodes/iterations?$depth=2&api-version=2.0')
    json_mock.assert_called_once()