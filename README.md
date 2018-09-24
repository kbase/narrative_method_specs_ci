# narrative_method_specs_ci [![Build Status](https://travis-ci.org/kbase/narrative_method_specs_ci.svg?branch=master)](https://travis-ci.org/kbase/narrative_method_specs_ci)

Narrative method specs repo for use in the -ci (or other nonproduction) environments.  It is designed to be a testing ground for type specifications.  Specs still must be manually added to kbase/narrative_method_specs repo to move to the production path.

Note that for this Repo, the 'master' branch is what is tracked in CI.

For the main narrative_method_specs repository, all changes intended for production should go through a PR to the 'develop' branch.  Those changes will then migrate to staging->next for testing, and staging->master for production release.  If you have changes that you need to test in next, but that you do not intend to go to production, you can submit PRs directly to the 'next' branch.

## Narrative Specifications

This is a KBase repository for Narrative specifications. Historically, this repo was also used to 
dynamically populate the set of narrative methods and apps that are available but this function is
now served by the catalog service (see https://github.com/kbase/catalog). Currently the primary function
of this repo is to contain specifications for Workspace types.

Updates to this repository can be automatically detected by the Narrative Method Store, a service which provides
access to parsed versions of these specifications.  See https://github.com/kbase/narrative_method_store

Generally, the production Narrative Method Store (https://kbase.us/services/narrative_method_store/rpc) will
fetch from the master branch of the narrative_method_specs repository, and other staging branches will pull from other branches.  For CI development and testing, method specs on the CI deployment of NMS (https://ci.kbase.us/services/narrative_method_store/rpc) are pulled from this repo.

#### Type Specifications

Type specifications are organized into folders in the methods directory.  Each folder is named by the unique
Workspace type and contains files named 'spec.json' and 'display.yaml' The 'spec.json' defines a number of 
parameters including `view_method_ids` which specifies which app sould be used as the viewer for this
type and `export_functions` which define methods which may be used to export they type in varies formats.
the `import_method_ids` parameter is no longer in use.

#### Category Specifications 

Categories define groupings of Methods & Apps used for method and app discovery and organization.  Categories,
like methods and apps, are defined in folders named with the category ID.  Categories currently are simple objects
with a name and brief description.  Methods & Apps define the categories they should be associated with.  Methods
& Apps can be associated with zero, one, or more categories.  Categories can be nested.

