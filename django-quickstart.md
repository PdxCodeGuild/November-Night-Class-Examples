# How to start a Django project &nbsp;(_PDXCG Style_)

Open a terminal and go to wherever you want to create your project!

Make sure to replace **$PROJECT_NAME** with your own project name. Your project name should be named in  snake_case and contain no captial letters.

This will also require `pipenv` to be installed!

## The Steps

1. Create a directory
    * `mkdir $PROJECT_NAME`
2. Change into that directory 
    * `cd $PROJECT_NAME`
3. Install django
    * `pipenv install django`
4. Get into the environment
    * `pipenv shell`
5. Create your project in the currect directory
    * `django-admin startproject $PROJECT_NAME .`
    * **The period at the end of this command is important!** It says ignore creating a new folder and put the contents of our new project in the current directory. 

   
   
## Now you're ready to go