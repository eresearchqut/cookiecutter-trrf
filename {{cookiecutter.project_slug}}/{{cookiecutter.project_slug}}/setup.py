import os
from setuptools import setup

package_data = {}
start_dir = os.getcwd()


def add_file_for_package(package, subdir, f):
    full_path = os.path.join(subdir, f)
    # print "%s: %s" % (package, full_path)
    return full_path


packages = [
    '{{ cookiecutter.project_slug }}',
]

for package in ['{{ cookiecutter.project_slug }}']:
    package_data[package] = []
    if "." in package:
        base_dir, package_dir = package.split(".")
        os.chdir(os.path.join(start_dir, base_dir, package_dir))
    else:
        base_dir = package
        os.chdir(os.path.join(start_dir, base_dir))

    for data_dir in (
            'templates',
            'static',
            'migrations',
            'fixtures',
            'features',
            'hooks',
            'templatetags',
            'management'):
        package_data[package].extend([add_file_for_package(package, subdir, f) for (
            subdir, dirs, files) in os.walk(data_dir) for f in files])

    os.chdir(start_dir)


setup(name='eresearchqut-{{ cookiecutter.project_slug }}',
      version="1.0.0",
      packages=packages,
      description='TRRF {{ cookiecutter.project_name }}',
      long_description='{{ cookiecutter.project_short_description }}',
      author='Queensland University of Technology - eResearch',
      package_data=package_data,
      zip_safe=False,
      )
