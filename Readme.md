# Todo
A web interface for the coolest kind of todo-list: a simple plain file!  
There's a cli: [todo-cli](https://github.com/lukasepple/todo-cli)
## Installation
Only use it for testing etc. i don't know if it's really stable.  
So:
	
	git clone https://github.com/lukasepple/todo.git
	cd todo
	virtualenv -p python3.3 .
	source bin/activate
	pip-3.3 install -r requirements.txt

Edit `app.py`, change `app.secret_key` (use something random!). Then create `salt.txt` and insert something random, too.  
Then use `hash_gen.py` to generate a salt of the passwort you want to use. Then open users.txt and insert:
	
	USERNAME HASH todofile
	
todofile means the location where the todo.txt should be stored (create this file!).  
You can add **more than one user** like that!  
Now simply do `./app.py` and your development server should run!
