from setuptools import find_packages, setup

setup(
    name='SCMAccessControlPlugin', version='1.0',
    description = "Trac plugin for SCM access control",
    author = "Lukas Schulze",
    author_email = "info@lukas-schulze.de",
    url = "http://www.lukas-schulze.de",
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Framework :: Trac',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Python Software Foundation License',
            'Programming Language :: Python :: 2',],

    packages=find_packages(exclude=['*.tests*']),
    entry_points = """
        [trac.plugins]
        scmaccesscontrol = scm_access_control.scm_access_control
    """,
)