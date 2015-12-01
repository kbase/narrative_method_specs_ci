# narrative_method_specs_ci
Narrative method specs repo for use in the -ci (or other nonproduction) environments.  It is designed to be a testing ground for new method specifications.  Method specs still must be manually added to kbase/narrative_method_specs repo to move to the production path.


[![Build Status](https://travis-ci.org/kbase/narrative_method_specs_ci.svg?branch=master)](https://travis-ci.org/kbase/narrative_method_specs_ci)


Narrative Method & App Specifications
-----------------------------------------------

This is a KBase repository for Narrative method and app specifications.  These specifications are used to 
dynamically populate the set of narrative methods and apps that are available, in terms of both method & app functionality/behavior and display.

Updates to this repository can be automatically detected by the Narrative Method Store, a service which provides
access to parsed versions of these specifications.  See https://github.com/kbase/narrative_method_store

Generally, the production Narrative Method Store (https://kbase.us/services/narrative_method_store/rpc) will
fetch from the master branch of the narrative_method_specs repository, and other staging branches will pull from other branches.  For CI development and testing, method specs on the CI deployment of NMS (https://ci.kbase.us/services/narrative_method_store/rpc) are pulled from this repo.



## Basic Repository Organization

Method specifications are organized into folders in the methods directory.  Each folder is named by the unique
method ID containing files named 'spec.json' and 'display.yaml' (see details below).  Screenshots can be
included in an optional img directory in each method folder.

Apps specifications are similarly organized into folders in the apps directory.

Categories define groups of related Methods & Apps, and also have a specification defined in folders in the
categories directory.  Methods & Apps can be in zero or more categories as defined in the Method/App
specifications.  Categories are used to organize Methods & Apps in both the Narrative interface and 
documentation pages.



## How to Add/Update Specifications

As this is a repo for specifications for CI and non-production KBase deployments, if you are developing KBase methods and apps, you can get commit privileges to this repository.  Just send an email to request access to Michael Sneddon.



## Specification Details

#### Method Specifications

Narrative methods are the discrete operations that can be performed in the Narrative interface.  The method
specifications defines:
  - The input parameters and output variables of the method
  - The input/output visualization widgets (which are deployed with the Narrative)
  - The behavior of the widget
  - The display properties of the method (method name, parameter names, etc)
  - Documentation on the method, including screenshots

The technical specifications of the parameters, output, and method behavior are defined in a [JSON](http://json.org)
file named spec.json in each method folder, and should be edited by developers who are adding the method.

The display properties of the method (e.g. the nice name, the subtitle, description, parameter names, parameter
descriptions) are defined in a [YAML](http://en.wikipedia.org/wiki/YAML) file named display.yaml in each
method folder.  The display properties should be initially populated by the original developer as best as
possible, but will likely by edited by the KBase documentation teams.

Additional technical details regarding the specific fields in spec.json and display.yaml and how they map
to Narrative behavior will be added here soon, but the best way to learn is simply to take a look at
a few examples.


#### App Specifications

Apps define an ordered set of Narrative Methods in which the output of one method can be linked to the input
of one or more following methods.  Apps will also allow users to execute all the steps together with one click.

The App specification is still in flux, and will be described in more detail soon.


#### Category Specifications 

Categories define groupings of Methods & Apps used for method and app discovery and organization.  Categories,
like methods and apps, are defined in folders named with the category ID.  Categories currently are simple objects
with a name and brief description.  Methods & Apps define the categories they should be associated with.  Methods
& Apps can be associated with zero, one, or more categories.  Categories can be nested.


## Help

Contact: Michael Sneddon (mwsneddon@lbl.gov)

