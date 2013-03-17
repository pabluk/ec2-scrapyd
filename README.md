ec2-scrapyd
===========

User data script to deploy scrapyd on Amazon EC2

Usage
-----

Install `boto` on a virtualenv:

    $ pip install boto

add your AWS credentials in `~/.boto` or see the [Boto Config tutorial](http://boto.readthedocs.org/en/latest/boto_config_tut.html)
edit your options in `ec2-launcher.py` and run:

    $ vim ec2-launcher.py
    $ python ec2-launcher.py
