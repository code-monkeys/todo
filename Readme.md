# Todo
A web interface for the coolest kind of todo-list: a simple plain file!  
maybe it'll change its name soon.
## Installation
Only use it for testing etc. i don't know if it's really stable.  
So:
	
	git clone https://github.com/lukasepple/todo.git
	cd todo
	virtualenv .
	source bin/activate
	pip-3.3 install -r requirements.txt

Edit `app.py`, change `salt` and `app.secret_key` (use something random!)  
Then use `gen_hash.py` to generate a salt of the passwort you want to use. Then open users.txt and insert:
	
	USERNAME HASH todofile
	
todofile means the location where the todo.txt should be stored (create this file!).  
You can add **more than one user** like that!  
Now simply do `./app.py` and your development server should run!