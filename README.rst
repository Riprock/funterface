Funterface
==========

.. image:: https://travis-ci.org/Riprock/funterface.svg?branch=master
    :target: https://travis-ci.org/Riprock/funterface

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

Application of license
----------------------

Copyright 2016 Fergal Hainey

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Contributing
------------

I will be very happy to take contributions for features, bug fixes,
documentation, or anything else via GitHub merge requests! I commit to
reviewing all merge requests received within 2 weeks. Please note that
all contributions shall fall under the same license as the project, and
that Fergal Hainey will remain the only listed copyright holder for ease
of maintenance and to make changing license easier if necessary.

Merge requests must pass the build_. To run locally the same builds as
Travis, use the `ferhai/local-travis`_ Docker image.

.. _build: https://travis-ci.org/Riprock/funterface
.. _ferhai/local-travis: https://hub.docker.com/r/ferhai/local-travis/
