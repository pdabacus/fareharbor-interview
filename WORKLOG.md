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

2023-05-25 05:00-06:00
* made new field Surfboards.shapers to be a many to many relationship allowing
  multiple shapers to be contributers to a surfboard
* migration strategy is to create the new column and populate the values with
  a single item each copying from Surfboard.shaper, then to modify the code to
  use the new Surfboard.shapers set in the application, and once it works as
  expected, to remove the old Surfboar.shaper column

2023-05-25 06:00-07:00
*
