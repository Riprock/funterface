"""Tests for funterface."""

import pytest

import funterface


@pytest.fixture
def implementation():
    """Make a new funterface implementation."""
    @funterface.method('hey')
    def new_implementation(wot, hmm):
        """Just return 'woo'."""
        return '{0} {1}'.format(wot, hmm)
    return new_implementation


def test_add_method(implementation):
    """Test method decorator makes something with the named attr."""
    assert hasattr(implementation, 'hey')


@pytest.mark.parametrize(
    'init_args,call_args',
    [
        ((), ('woo', 'yeah')),
        (('woo', 'yeah'), ()),
        (('woo',), ('yeah',)),
    ]
)
def test_instance_call(implementation, init_args, call_args):
    """Test calling on a new instance."""
    assert implementation(*init_args).hey(*call_args) == 'woo yeah'


def test_class_call(implementation):
    """Test calling on just a class."""
    assert implementation.hey('woo', 'yeah') == 'woo yeah'


def test_partial(implementation):
    """Test partial adds arguments and returns instance."""
    assert funterface.partial(implementation, 'woo').hey('yeah') == 'woo yeah'
