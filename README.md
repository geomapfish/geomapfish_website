# GeoMapFish website

Website management system for http://geomapfish.org

## Prerequisites

This README file was written for Windows users. The whole thing surely
works on Linux, but the commands might slightly differ.

On Windows, you should:

* Install *Python* and *virtualenv* (using *pip*)
* Install *Git*

## Installation

* Create a new local repository
* Fork this [GitHub repository](https://github.com/geomapfish/geomapfish_website)
* Initialize your local repository with your GitHub fork:

```
git init
git remote add origin https://github.com/<your_username>/geomapfish_website.git
git pull origin master
git submodule update --init
```

* Install a virtual environment, *Pelican* and *Markdown*:

```
virtualenv .
Scripts\pip install Pelican==3.7.1
Scripts\pip install markdown
```

* Create an output folder:

```
mkdir output
```

You are now ready the create and modify some content.

## Using Pelican

### Starting a local server

Open a command and type:

```
cd output
..\Scripts\python -m pelican.server
```

You can then call [localhost:8000](http://localhost:8000/) to see your local
website.

### Generating some output

Once you have written some content, you can regenerate your output HTML
file using following command:

```
Scripts\pelican content
```

## Write some content

The `content` folder contains all the pages. The pages names are numbered
as they should appear in the menu.

Pages name starting with `99_` are these which are hidden. Moreover they
should contain `status: hidden` in their metadata.

Refer the [Pelican documentation](http://docs.getpelican.com/en/stable/) for
syntax help and templating issues.

We expect people to submit modification in all three languages, or if your
knowledge in one or more language is not good enough, then **notify** it
in your pull request.

## Publication

### Making a pull request

Once you have made all the changes that you want to submit, you can make a
pull request:

```
git add -A
git commit -m "<Description of the changes>"
git push origin master
```

Then go to your GitHub fork and create a new pull request.

Somebody of the GeoMapFish community will then review your code, eventually
merge it and the update the website with your changes.

### Using the publication mechanism

You will need to have push rights on both repositories to be able to use
this mechanism. Otherwise, we recommend that you do a proper pull request
to this repository. We will more then happy to review and eventually merge
your suggestions.

If you have push rights on the [geomapfish.github.io](https://github.com/geomapfish/geomapfish.github.io/) repository, then you
use the `publish.bat` file (obviously only on Windows...).
