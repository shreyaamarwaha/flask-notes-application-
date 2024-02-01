from templates import create_app

app = create_app()

if __name__ == '__main__': #this says that we want to run the web server only when we want to run the web server
    app.run(debug=True) #app.run is gonna run our application, debug= true means that this will incorporte all the changes made to the code automatically and you won't have to re run the code manually after making some little changes every little while 
