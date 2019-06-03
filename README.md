# TRRF template

## About

It is quite common that registry owners need customisations of their TRRF registries.

For each customised registry, we will create a separate GitHub project.
The project will include base TRRF (as a git submodule) and adds customisations like different templates, registration etc. on top.

This is a project template that can be used by Cookiecutter (https://github.com/audreyr/cookiecutter) to create customised registries as needed.

It helps with creating a custom project with minimal manual interventions by using template files and some configuration values that can be specified at creation time.

## Usage

### Install Cookiecutter

You will need to install Cookiecutter, but unfortunately Cookiecutter has a problem with copying symlinks as is, so you will have to use a fork that solves this problem.

```sh
  $ pip install --user git+https://github.com/sztamas/cookiecutter.git
```

### Create project (from template) locally

After you have ``cookiecutter`` installed you can use it to create the new project on your computer.
You can either clone this template project to your computer or just use the template directly from the GitHub repository.

You will be prompted to change the configuration values next. Usually, you can just set the project name and leave the rest as it is. Example for the ``MND`` project below.

```sh
  $ cookiecutter https://github.com/eresearchqut/cookiecutter-trrf
  project_name [Angelman]: MND
  project_slug [mnd]:
  github_repo [eresearchqut/mnd]:
  project_short_description [MND is a patient registry based on TRRF (https://github.com/eresearchqut/trrf).]:
  version [1.0.0]:
```

This will create the project in the ``mnd`` (the ``project_slug``) directory. You can inspect the contents of the directory to see what has been created.

### Create project on GitHub

You will most probably want to create the project on GitHub as well and connect it up with your local project directory you've just created.

Create an empty project on GitHub. The project will be most likely be created under the ``eresearchqut`` organisation, but it should be the repo you specified in the ``github_repo`` configuration above (``eresearchqut/mnd`` for the MND example above).

For your convenience a script has been created for you that will set up and connect your local project to the github project. To use it change into the directory you just created and run the ``setup_github.sh`` script.

```sh
  $ cd mnd
  $ ./setup_github.sh
```

This will initialise the git repository, add all your project files, set up the TRRF project as a submodule, create and switch to the ``next_release`` branch where you should do all your development.

You are all set up!

You're free to remove the ``setup_github.sh`` file if you want to.

You would most probably want to set up a CI/CD pipeline next for your newly created project and start adding the customisations to the project as needed.

