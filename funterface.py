"""Provide a decorator for writing one method classes as a function."""

from functools import partial as functools_partial


def funterface_init(self, *args, **kwargs):
    """Remember args and kwargs, a bit like `functools.partial` would."""
    self.args = args
    self.kwargs = kwargs


# Really wanted to make this a funterface, but can't use funterface
# until it's defined!
class VagueMethodDescriptor(object):
    """A descriptor which makes a method work as a class or instance attribute."""

    def __init__(self, func):
        """Remember the function."""
        self.func = func

    def __get__(self, obj, objtype):
        """Return the method as is or a classmethod."""
        if obj is None:
            return functools_partial(self.func, objtype)
        return functools_partial(self.func, obj)


def method(method_name):
    """Make a decorator that turns a function into a method on a new class."""
    def real_decorator(func):
        """Decorate a function so it becomes a method of a new class."""
        def init_partial(self, *args, **kwargs):
            """Call func with init args as well as called args."""
            init_args = getattr(self, 'args', ())
            init_kwargs = getattr(self, 'kwargs', {})
            with_init = functools_partial(func, *init_args, **init_kwargs)
            return with_init(*args, **kwargs)
        implementation = type(
            'FakeImplementation',
            (object,),
            {
                '__init__': funterface_init,
                method_name: VagueMethodDescriptor(init_partial),
            }
        )
        return implementation
    return real_decorator


def partial(implementation, *args, **kwargs):
    """
    Call a callable with the args given.

    On a funterface implementation this will have similar effect to
    making a partial of the original decorated function.
    """
    return implementation(*args, **kwargs)
