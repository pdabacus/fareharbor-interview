# Salty!

"Salty!" is a "web application" (very loosely; there's no actual
interactivity, just viewing of data -- the R part of a CRUD
application) for viewing information about surfboard shapers, the
surfboards they shape, and the surfers that ride them.  Yes, this is
essentially the canonical "Authors and Books" Django example, with a
little salty ocean flavor for fun.

## Take-Home

If you are doing this project partly or fully as a take-home, please keep a log of
what you did and in what order, including what assumptions you are
making, what questions came up, how you resolved them, and so on. You
can do this in a new file named `WORKLOG.md` or something similar.

Also, please make extra effort to use `git commit`, to help build a narrative.

## Getting Started

0. Clone the repository.

      $ git clone git@bitbucket.org:fareharbor/salty.git salty  
      $ cd salty  

Or if you got a tar: `tar -xzvf salty.tar.gz && cd salty`

0. Install pyenv and python 3.8.11

This step is optional but recommended. We haven't tested this project on every version of Python. Newer versions will probably work, but it's not the point of the project to troubleshoot weird python version mismatch issues.

https://github.com/pyenv/pyenv

0. Create a virtual environment.

      $ mkdir -p ~/python-environments  
      $ python -mvenv ~/python-environments/salty  
      $ source ~/python-environments/salty/bin/activate  

0. Install dependencies.

      $ pip install -r requirements.txt

0. Create and populate your database.

      $ ./new-db

0. Run the development server.

      $ ./manage.py runserver

0. Visit <http://localhost:8000> in your browser.

0. Make generaous use of `git commit`, with meaningful commit messages. This helps us understand how you think about what you're doing.

0. Don't forget to do one last `git commit` at the end!

0. When you're finished, tar the directory and send it back to us.

      $ tar -zvcf salty.tar.gz salty/

## Code Overview

As in many (most?) Django applications, the core of Salty is really the (very simple)
data model.

We have three models:

- `Surfer` represents individual surfers that might own 0 (just getting started!), 1, or many surfboards
- `Shaper` for shapers that might have made 0+ surfboards (gotta start somewhere!)
- `Surfboard` for the actual surfboards themselves

The data associated with each of these models is kinda irrelevant -- we're really more
worried about the relationships between them, and anyway I wasn't really sure
what users might actually care about, so I kinda tossed it together haphazardly.

After that we really only have views  (the routing layer is trivial), which
basically just render our templates with a bit of data.  Not a whole lot going on.

# Projects

Listed below are 4 modifications we'd like to make to the app.

Treat this as "production quality" -- we're not looking for skunkworks approaches.
For instance, in terms of code quality
and structure: Is it DRY, or are there glaring
redundancies? Or have you gone overboard on abstraction? Are things named well?
Is it "Pythonic", whatever that means? Performance is also a concern.
And of course, at the end of the day, is it correct?

It's therefore better to take a smaller or simpler approach, and nail it, than
to toss in everything and the kitchen sink in a less-than-quality way.

Also, you should feel free to change anything and everything about the data
model, views, routes, and so on...

Just remember that this is "already in production". We can't have
downtime or data loss, so make sure you can rollback any changes and
make sure none of the migrations take a long table-level lock. Have a
good migration strategy in mind, even if you don't implement it.


## Surfer API Endpoints

We would like to have 2 separate RESTful API enpoints, one for a full list of surfers
and another for each individual surfer by pk. In the response we would like
to retrieve the surfer information. If there are any other information you think
would be useful in the response then lets add them to the response as well.

## Collaboration Station

Turns out that shapers sometimes collaborate on a new shape, but our data model
only allows for one shaper per surfboard. Shit! Let's see about updating our
data model so that surfboards can be shaped by *one or more* shapers. We will also
want to update our views so that anywhere we are currently displaying the shaper
associated with a surfboard, we instead show all shapers associated with it.

## It's Not All One-Offs

Not every new surfboard is a completely unique snowflake; instead shapers often
will make a few "models" in various dimensions.  Let's say we want to update our
data model to support this usecase.  An approach would be to add a `SurfboardModel`
model, whereby shapers that previously would have several surfboards, would now
have several models, each with 1 or more surfboards associated with it.  Any
surfboards that were one-offs would nevertheless get their own surfboard model.

A surfboard model would have a `name` and a `description` at least.  After that
the important concern is again not the fields but the *relationships*. Once you've
got the data model sorted, update the views to focus attention on surfboard models.
Also, make sure you've got a view for an individual model that shows all associated
surfboards.

Finally, on the list of all models view (`/models/` perhaps?), list all associated
surfboards as well.

## This One's a Good One

Sometimes you're just a surfer looking for a new stick. Come up with a way to
determine a recommendation or set of recommendations for a surfer, and add it
to the surfer view (`/surfers/<pk>/`).  Ideally we're looking for a "good"
way to recommend a new surfboard for a surfer, so be ready to argue that your
method is at least halfway decent (`random` I'm looking at you).
