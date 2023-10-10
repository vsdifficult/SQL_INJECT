SQL_INJECT_REQUESTS = [
    "SELECT * FROM users WHERE username = 'administrator'--' AND password = ''",  
    "UNION SELECT username, password FROM users--", 
    "SELECT * FROM v$version", 
    "SELECT * FROM information_schema.tables", 
    "/SELECT/ * FROM/ users/ WHERE /username = 'administrator'--'/ AND/ password = ''/", 
    "SELECT * FROM users WHERE username = '$administrator'--' AND password = ''",   
    "select password from users where username ='$admin'",  
    "SELECT * FROM users WHERE username = ''",  
    "UNION SELECT password FROM users ", 
    "SELECT username, password FROM userlist "
]