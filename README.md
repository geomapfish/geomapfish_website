# geomapfish_website

Website management system for http://geomapfish.org

## Prerequisites

This README file was written for Windows users. The whole thing surely
works on Linux, but the commands might silghtly differ.

On Windows, you should:

* Install Python and virtualenv (using pip)
* Install Git for Windows

## Installation

* Create a new local repository
* Fork this GitHub repositroy
* Initialize your local repository with your GitHub fork:

    git init
    git remote add origin https://github.com/your_username/.....git
    git fetch origin
    git merge origin/master
    git submodule update --init
    
* Install a virtual environnement and Pelican:
    
    virtualenv .
    Scripts\pip install Pelican==3.6.3
    
* Create an output folder:

    mkdir output

You are now ready the create and modify some content !

## Using Pelican

### Starting a local server

Either use the batch file `run_server.bat` or open a command and:

    cd output
    ..\Scripts\python -m pelican.server

### Generating some output



## Write some content

The `content` folder contains all the pages. The pages names are numbered
as the should appear in the menu.

Pages name starting with `99_` are these which are hidden. Moreover they
should contain `status: hidden` in their metadata.


Refer the Pelican documentation for syntax help and templating issues.

We expect people to submit modification in all three languages, or if your
knowledge in one or more language is not good enough, then **notify** it
in your pull request.

## Publication

### Making a pull request

If you do not have push rights on the geomapfish GitHub repositories, then
this is definitively the way to go.

Once you have made all the changes that you want to submit:

    git add -A
    git commit -m "These are the changes I want to make"
    git push origin master

Then go to your GitHub fork and create a new pull request.

Somebody of the GeoMapFish community will then review your code, eventually
merge it and the update the website with your changes.

### Using the publication mechanism

You will need to have push rights on both repositories to be able to use
this mechanism

