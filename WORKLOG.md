# Worklog

2023-05-22 13:30-14:00
* glanced at project and cleaned up files, init git repo
* created dev environment makefile pyenv setup

2023-05-23 15:30-17:30
* new db and explore code
* created unittest setup for surfers, shapers, and surfboards

2023-05-24 11:00-13:00
* created api module with rest_framework for surfers, shapers, and surfboards
* created serializers and basic unit tests with requests.get()

2023-05-25 05:00-06:30
* made new field Surfboards.shapers to be a many to many relationship allowing
  multiple shapers to be contributers to a surfboard
* migration strategy is to create the new column and populate the values with
  a single item each copying from Surfboard.shaper, then to modify the code to
  use the new Surfboard.shapers set in the application, and once it works as
  expected, to remove the old Surfboard.shaper column
* bugfix with table name Shaper.surfboard_set reverse reference many-many table

2023-05-25 09:30-11:00
* created SurfboardModel class and began migration to attach a surfboardmodel
  to each surfboard in a many-to-one relationship
* created /models/ html templates
* migration strategy is to create the new column in Surfboards.surfboard_model
  and create a SurfboardModel for each Surfboard based on who the current
  contributer/shapers are. after things work, the Surfboard.model_name
  field will be renamed to just board_name

2023-05-25 22:00-23:30
* completed data migration generating random SurfboardModel names/descriptions

2023-05-26 00:00-01:30
* created recommendation system for boards (first using random to build view)
* created recommendation strategy based off
  1. boards with the same model as ones owned by surfer
  2. boards with the same shaper as ones owned by surfer
  3. other boards owned by surfers with the same fav model
  4. other boards owned by surfers with the same fav shaper
  5. most popular shaper

2023-05-26 17:00-18:00
* finished implementing recommendations
