# Vendoring Conda packages on Cloud Foundry

To include ("vendor") Conda packages when using the official Python Cloud Foundry buildpack, 
you can include the packages in your uploaded app, and set up a local conda channel to this directory.

In this repo I have included a [simple conda package](https://github.com/ihuston/simple_conda_pkg) as a vendored dependency in the `vendor/` directory.

In my `environment.yml` file I add a new conda channel which references the local path to this directory,
*at the time that Cloud Foundry installs the package*, which is `/tmp/app/vendor`.

To try this out with your preferred CF host, 
simply clone this repo, log in to CF, and `cf push`.

*(My employer Pivotal runs a [CF installation with a free trial](http://run.pivotal.io).)* 

