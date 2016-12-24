"""Provide a decorator for writing one method classes as a function."""

from functools import partial as functools_partial


def vagemethod_get(func, dummy_self, obj, objtype):
    """Return a partial function bound to the instance or class."""
    if obj is None:
        return functools_partial(func, objtype)
    return functools_partial(func, obj)


def vaguemethod(func):
    """Make a function work as both a class and instance method."""
    get = functools_partial(vagemethod_get, func)
    return type('VagueMethodDescriptor', (object,), {'__get__': get})()


def funterface_init(self, *args, **kwargs):
    """Remember args and kwargs, a bit like `functools.partial` would."""
    self.args = args
    self.kwargs = kwargs


def with_init(func, self, *args, **kwargs):
    """Call func with init args as well as called args."""
    init_args = getattr(self, 'args', ())
    init_kwargs = getattr(self, 'kwargs', {})
    return functools_partial(func, *init_args, **init_kwargs)(*args, **kwargs)


def method_decorator(method_name, func):
    """Decorate a function so it becomes a method of a new class."""
    implementation = type(
        'FakeImplementation',
        (object,),
        {
            '__init__': funterface_init,
            method_name: vaguemethod(functools_partial(with_init, func)),
        }
    )
    return implementation


def method(method_name):
    """Make a decorator that turns a function into a method on a new class."""
    return functools_partial(method_decorator, method_name)


def partial(implementation, *args, **kwargs):
    """
    Call a callable with the args given.

    On a funterface implementation this will have similar effect to
    making a partial of the original decorated function.
    """
    return implementation(*args, **kwargs)
