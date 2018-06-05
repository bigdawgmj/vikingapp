""" VSTS Worker Testing Package """
import pytest
from vsts import VstsWorker
from mock import patch


@pytest.fixture(scope='module')
def vsts_setup():
    """ Setup Fixture """
    return VstsWorker('http://test.com', 'user1', 'hemmligIkkeDel',
                      'project')


def test_init(vsts_setup):
    """ Create init """
    assert vsts_setup.base_url == 'http://test.com'
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
