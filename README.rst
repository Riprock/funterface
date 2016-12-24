Funterface
==========

funterface
    A portmanteau of *function* and *interface*. It’s also a more
    **fun** way of writing implementations of class interfaces.

Classes with one public method aren’t a good way of defining an
interface in Python. Nevertheless lots of projects do expect you to
make classes with one public method. You don’t need to write your code
with classes though, you can just write the important function.
Funterface makes this easier.

::

    @funterface.method('get_connection')
    def connection_getter(username, password, timeout):
        """Open a connection for use by some other project."""
	payload = other_project_plumbing.auth_hash(username, password)
        return other_project_plumbing.connect(payload, timeout=timeout)


    connection_implementation = connection_getter('user1', 'password')
    # other_project_plumbing.transaction calls get_connection on
    # connection_getter.
    transaction = other_project_plumbing.transaction(
        connection=connection_implementation)

Instantiating the returned class is a lot like making a
`functools.partial` of the original function. If you would prefer
something that looks more as if there were never classes you can use
`funterface.partial`.

::

    connection_implementation = funterface.partial(
        connection_getter, 'user1', 'password')
